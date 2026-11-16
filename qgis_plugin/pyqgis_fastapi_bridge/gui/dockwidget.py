# -*- coding: utf-8 -*-
"""
Side dock widget for the PyQGIS FastAPI Bridge plugin.
Leverages QgsTask for non-blocking asynchronous background API queries
without freezing or hanging the QGIS user interface.
Supports connecting over Tailscale or local network interfaces.
"""

import os
from PyQt5 import uic
from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import pyqtSignal

from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsWkbTypes,
    QgsCoordinateReferenceSystem,
    QgsCoordinateTransform,
    QgsTask,
    QgsApplication
)

from ..core.api_client import BackendApiClient

UI_PATH = os.path.join(os.path.dirname(__file__), "dockwidget.ui")
FORM_CLASS, _ = uic.loadUiType(UI_PATH)


class AsyncApiTask(QgsTask):
    """Background worker task (QgsTask) executing network queries without blocking the GUI."""

    def __init__(self, description, parcel_id, teryt_id, lat, lon, on_success_callback, base_url=None):
        super().__init__(description, QgsTask.CanCancel)
        self.parcel_id = parcel_id
        self.teryt_id = teryt_id
        self.lat = lat
        self.lon = lon
        self.base_url = base_url
        self.on_success = on_success_callback
        self.response_data = None
        self.error_msg = None

    def run(self):
        """Method executed on a separate worker thread."""
        try:
            self.response_data = BackendApiClient.analyze_parcel(
                parcel_id=self.parcel_id,
                teryt_id=self.teryt_id,
                lat=self.lat,
                lon=self.lon,
                base_url=self.base_url
            )
            return True
        except Exception as e:
            self.error_msg = str(e)
            return False

    def finished(self, result):
        """Method invoked on the main GUI thread upon task completion."""
        if result and self.response_data:
            self.on_success(self.response_data)


class PyQgisBridgeDockWidget(QDockWidget, FORM_CLASS):
    closingPlugin = pyqtSignal()

    def __init__(self, iface, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.iface = iface

        # Initialize API URL from environment if set (useful for Tailscale / remote teammates)
        default_api_url = os.environ.get("PYQGIS_BRIDGE_API_URL") or os.environ.get("API_BASE_URL")
        if default_api_url and hasattr(self, "txtApiUrl"):
            self.txtApiUrl.setText(default_api_url.replace("/api/v1", "").rstrip("/"))

        self.btnRefresh.clicked.connect(self.populate_layers)
        self.btnRun.clicked.connect(self.run_processing)
        self.btnClear.clicked.connect(self.txtLog.clear)

        self.populate_layers()

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def log(self, text):
        self.txtLog.append(str(text))

    def populate_layers(self):
        self.cmbLayer.clear()
        found = 0
        for layer in QgsProject.instance().mapLayers().values():
            if isinstance(layer, QgsVectorLayer) and layer.geometryType() == QgsWkbTypes.PolygonGeometry:
                self.cmbLayer.addItem(layer.name(), layer)
                found += 1

        self.log(f"Layers refreshed. Polygon layers found: {found}")

    def run_processing(self):
        layer = self.cmbLayer.currentData()
        if not layer or not layer.isValid():
            self.log("ERROR: Please select a valid vector layer!")
            return

        input_teryt = self.txtTeryt.text().strip()
        custom_api_url = self.txtApiUrl.text().strip() if hasattr(self, "txtApiUrl") else None

        self.log(f"\n==================================================")
        self.log(f" Starting async analysis (QgsTask): {layer.name()}")
        if custom_api_url:
            self.log(f" Target Server (Tailscale/Local): {custom_api_url}")
        if input_teryt:
            self.log(f" TERYT / Feature ID Filter: {input_teryt}")
        self.log(f"==================================================")

        src_crs = layer.crs()
        wgs84 = QgsCoordinateReferenceSystem("EPSG:4326")
        transform = QgsCoordinateTransform(src_crs, wgs84, QgsProject.instance())

        total = layer.featureCount()
        self.progressBar.setMaximum(max(1, total))
        self.progressBar.setValue(0)

        processed = 0
        for feature in layer.getFeatures():
            geom = feature.geometry()
            if not geom or geom.isEmpty():
                continue

            centroid = geom.centroid().asPoint()
            wgs_pt = transform.transform(centroid)
            lat, lon = wgs_pt.y(), wgs_pt.x()

            fid_str = str(feature.id())
            name_attr = feature.attribute("name") if "name" in [f.name() for f in layer.fields()] else f"Feature #{fid_str}"

            # Create async QgsTask worker with configured server endpoint
            task_desc = f"Analyzing {name_attr} ({lat:.3f}, {lon:.3f})"
            task = AsyncApiTask(
                description=task_desc,
                parcel_id=fid_str,
                teryt_id=input_teryt,
                lat=lat,
                lon=lon,
                on_success_callback=self.on_task_completed,
                base_url=custom_api_url
            )

            # Register with QGIS Task Manager (status bar in lower right of QGIS)
            QgsApplication.taskManager().addTask(task)
            processed += 1

        self.log(f"Dispatched {processed} background tasks (QgsTask). QGIS UI remains fully responsive!")

    def on_task_completed(self, data):
        """Slot receiving results from the worker thread and updating the GUI."""
        current_val = self.progressBar.value() + 1
        self.progressBar.setValue(current_val)

        pid = data.get("parcel_id", "N/A")
        status = data.get("status", "N/A")
        metrics = data.get("metrics", {})

        self.log(f"✓ Result for feature #{pid} [Status: {status}]")
        for k, v in metrics.items():
            self.log(f"   -> {k}: {v}")
