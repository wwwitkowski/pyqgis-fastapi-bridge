# -*- coding: utf-8 -*-
"""
Unit tests for QGIS plugin components that do not require a live QGIS GUI environment.
"""

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import unittest
import configparser
from qgis_plugin.pyqgis_fastapi_bridge.core.api_client import BackendApiClient

class TestQgisPluginInfrastructure(unittest.TestCase):
    def setUp(self):
        self.plugin_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "qgis_plugin",
            "pyqgis_fastapi_bridge"
        )

    def test_metadata_file_validity(self):
        metadata_path = os.path.join(self.plugin_dir, "metadata.txt")
        self.assertTrue(os.path.exists(metadata_path), "metadata.txt must exist in plugin directory")

        config = configparser.ConfigParser()
        config.read(metadata_path, encoding="utf-8")
        self.assertIn("general", config.sections(), "metadata.txt must contain a [general] section")

        general = config["general"]
        required_keys = ["name", "qgisminimumversion", "description", "version", "author", "email", "about"]
        for key in required_keys:
            self.assertIn(key, general, f"Missing required key in metadata.txt: {key}")
            self.assertTrue(len(general[key]) > 0, f"Key {key} must not be empty")

    def test_api_client_fallback_mode(self):
        # Test client invocation with deliberately inactive port to verify graceful offline fallback
        res = BackendApiClient.analyze_parcel(parcel_id="MOCK-001", lat=52.0, lon=21.0)
        self.assertIsInstance(res, dict)
        self.assertIn("status", res)
        self.assertIn("metrics", res)

if __name__ == "__main__":
    unittest.main()
