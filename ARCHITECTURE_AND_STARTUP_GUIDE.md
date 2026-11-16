# 🧭 Architektura i Przewodnik Projektu: Co, Gdzie i Jak?

> **PyQGIS FastAPI Bridge** — asynchroniczny szkielet łączący środowisko analityczne **Python / FastAPI**, stację roboczą **QGIS** oraz interaktywny podgląd **Web (MapLibre GL JS)**.

---

## ⚡ 1. Jak Uruchomić Wszystko w 1 Kliknięcie?

* **Windows:** Uruchom dwuklikiem plik **`start_all.bat`**.
* **Linux / macOS:** Wykonaj w terminalu `./start_all.sh`.

### Co robi skrypt `start_all`?
1. Sprawdza środowisko Pythona i uruchamia 16 testów jednostkowych.
2. Automatycznie linkuje wtyczkę do aktywnego profilu QGIS (`link_plugin.bat`).
3. Sprawdza, czy Docker Desktop działa – jeśli tak, startuje bazę PostGIS i TiTiler (`docker-compose.yml`).
4. Uruchamia serwer FastAPI na `0.0.0.0:8000` i automatycznie otwiera aplikację mapową w przeglądarce pod adresem **`http://127.0.0.1:8000`**.

---

## 🗺️ 2. Co Gdzie Jest? (Struktura Repozytorium)

```text
pyqgis-fastapi-bridge/
│
├── 🚀 start_all.bat / .sh          # 1-kliknięciowy starter całego środowiska
├── 🔗 link_plugin.bat / .sh        # Linkuje wtyczkę bezpośrednio do folderu wtyczek QGIS
├── 🧪 run_tests.bat / .sh          # Uruchamia pełny pakiet 16 testów jednostkowych
├── 🎨 open_designer.bat           # Odpala Qt Designera ze specjalnymi kontrolkami QGIS
├── 📦 pyproject.toml               # Standard instalacyjny pakietu Python (pip install -e .)
│
├── 🧠 backend/                     # MÓZG ANILITYCZNY (FastAPI)
│   ├── run_backend.py              # Główny punkt startowy serwera (port 8000)
│   ├── app/main.py                 # Konfiguracja FastAPI, CORS, routing i serwowanie frontendu
│   ├── app/api/v1/router.py        # Centralny routing API (/api/v1)
│   ├── app/api/v1/endpoints/       # Endpointy: /analysis, /cadastre (ULDK)
│   └── app/ingestion/              # Integracje z otwartymi API: GUGiK ULDK (działki), IMGW (pogoda)
│
├── 🖥️ qgis_plugin/                 # WTYCZKA DO QGIS (PyQGIS)
│   └── pyqgis_fastapi_bridge/
│       ├── plugin.py               # Cykl życia wtyczki, menu i pasek narzędzi w QGIS
│       ├── metadata.txt            # Metadane wtyczki dla QGIS 3.44.15 LTR
│       ├── gui/dockwidget.ui       # Wygląd panelu bocznego (edytowalny w Qt Designerze)
│       ├── gui/dockwidget.py       # Obsługa zdarzeń i wielowątkowości QgsTask (zero zacinania QGIS)
│       └── core/api_client.py      # Klient HTTP komunikujący się z FastAPI (z trybem offline fallback)
│
├── 📐 sample_project/              # GOTOWY PROJEKT TESTOWY DO QGIS
│   ├── sample_project.qgz / .qgs   # Projekt QGIS z natywnym układem EPSG:2180 i podkładem OSM
│   └── sample_polygons.geojson     # Poligony testowe w okolicach wsi Moszna (WGS84 / EPSG:4326)
│
├── 🌐 web/                         # INTERAKTYWNY PODGLĄD W PRZEGLĄDARCE
│   └── index.html                  # Aplikacja mapowa MapLibre GL JS + OpenStreetMap (serwowana z FastAPI)
│
├── 🔄 shared/                      # WSPÓLNE KONTRAKTY DANYCH (Single Source of Truth)
│   ├── schemas/geo_models.py       # Pydantic: GeoFeatureRequest, SpatialMetric, GeoAnalysisResponse
│   └── constants/poland_crs.py     # Stałe układów współrzędnych: EPSG:2180, EPSG:4326, EPSG:3857
│
├── 🐳 docker/                      # POMOCNICZE USŁUGI KONTENEROWE
│   └── docker-compose.yml          # Baza PostGIS (5432) oraz serwer kafelków rastrów TiTiler (8080)
│
├── 📚 docs/                        # REJESTRY I BAZA WIEDZY GIS
│   ├── polish_public_gis_registries.md   # Kompendium 46 państwowych i unijnych usług GIS (WMS/WFS/REST)
│   └── polish_public_gis_registries.csv  # Maszynowy rejestr usług z adresami endpointów
│
└── 🤖 AGENTS.md / CONTRIBUTING.md  # Zasady Human-First AI, Issue-Driven Development i standardy kodu
```

---

## 🔄 3. Jak Przepływają Dane w Systemie? (Data Flow)

```text
1. Rolnik / Analityk klika w QGIS w działkę lub wpisuje numer TERYT
                          │
                          ▼
2. QGIS Plugin (PyQGIS) uruchamia zadanie w tle (QgsTask)
   [Interfejs QGIS ani na moment się nie zacina!]
                          │
                          ▼  (Zapytanie HTTP / JSON przez sieć lokalną lub Tailscale)
3. FastAPI Backend odbiera żądanie
   ├── Odpytuje GUGiK ULDK (pobiera oficjalną geometrię działki ewidencyjnej w EPSG:2180)
   ├── Odpytuje IMGW (pobiera aktualną temperaturę, opady i wiatr z najbliższej stacji)
   └── Wylicza pole powierzchni w ha/m², obwód i wskaźniki ryzyka
                          │
                          ▼  (Zwraca GeoAnalysisResponse wg kontraktu Pydantic)
4. Wyniki trafiają jednocześnie na 2 EKRANY:
   ├── Do QGIS: wtyczka koloruje działkę na mapie i wypisuje raport w oknie logów
   └── Do Przeglądarki (Web): http://127.0.0.1:8000 rysuje poligon na podkładzie OpenStreetMap
```

---

## 🌍 4. Kluczowe Zasady Geoprzestrzenne (CRS)

* **Układ analityczny i projektowy: `EPSG:2180 (PUWG 1992)`**  
  Oficjalny państwowy układ metryczny w Polsce. W nim liczymy powierzchnie w hektarach/m² i z niego korzystają polskie geoportale.
* **Układ wymiany danych: `EPSG:4326 (WGS 84 Lon/Lat)`**  
  Wszystkie pliki `.geojson` oraz odpowiedzi REST API posługują się stopniami `[długość, szerokość]`.
* **Kafelki Webowe: `EPSG:3857 (Web Mercator)`**  
  Standardowy układ kafelek OpenStreetMap i MapLibre GL JS w przeglądarce. QGIS transformuje go w locie do EPSG:2180.

---

## 👥 5. Praca Zespołowa przez Tailscale (P2P)

Nie musicie wdrażać backendu na publiczne serwery w chmurze, aby wspólnie pracować:
1. Zainstalujcie **Tailscale** na swoich komputerach.
2. Osoba hostująca backend uruchamia `start_all.bat`.
3. Pozostali członkowie zespołu wpisują jej adres Tailscale (np. `http://100.85.12.34:8000`) w panelu wtyczki w QGIS lub w przeglądarce.
4. Cały zespół korzysta na żywo ze wspólnego silnika analitycznego!
