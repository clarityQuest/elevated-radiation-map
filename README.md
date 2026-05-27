# Elevated Radiation Map – Geiger Counter Measurements in Germany & Europe

**Interactive map of locations with elevated ionising radiation, measured by citizen scientists with Geiger counters across Germany and Europe.**

🗺️ **Live map:** [https://clarityquest.github.io/elevated-radiation-map/](https://clarityquest.github.io/elevated-radiation-map/)

---

## What is this?

This map visualises hundreds of real Geiger counter measurements at specific geographic locations across Germany and wider Europe.
Each measurement was recorded by a hobbyist physicist, geology enthusiast, or radiation-safety researcher, then published on one of two community platforms:

- **[opengeiger.de](http://www.opengeiger.de/GeigerCaching/GeigerCaching.html)** – Germany's largest community Geiger caching project
- **[Geigerzählerforum](https://www.geigerzaehlerforum.de/)** – German Geiger counter enthusiast forum

Measured dose rates span from normal background levels all the way to extreme hotspots, and cover a wide variety of locations: old uranium and thorium mine tailings, slag heaps, naturally radioactive rock outcrops, pottery workshops using uranium glaze, antique clocks with radium paint, and more.

---

## Dose Rate Colour Scale

| Colour | Dose rate | Classification |
|--------|-----------|---------------|
| 🔵 Blue | < 0.5 µSv/h | Low (background) |
| 🟢 Green | 0.5 – 1 µSv/h | Elevated |
| 🟠 Orange | 1 – 3 µSv/h | High |
| 🔴 Red-orange | 3 – 10 µSv/h | Very high |
| ⬛ Dark red | ≥ 10 µSv/h | Extreme |
| ⬜ Grey | — | No dose data |

Dose rate is measured in **µSv/h** (microsieverts per hour). For reference, the typical European background radiation is roughly **0.05 – 0.15 µSv/h**.

---

## Map Marker Shapes

- **Circle** — measurement from opengeiger.de
- **Triangle** — measurement from Geigerzählerforum
- **Circle + Triangle combined** — same location reported by both sources

---

## Features

- Click any marker to see the location name, reported dose rate, tier classification, notes, and a direct link to the original source entry
- **Show my position** button — uses your browser's geolocation to show your current position on the map, making it easy to see nearby elevated-radiation locations
- Toggle each data source on/off using the legend checkboxes
- **Google Maps link** for every marker — open the location in Google Maps for navigation or satellite view
- Markers resize and re-anchor dynamically as you zoom in
- At high zoom, markers from both sources that share the same physical location are automatically merged into a combined icon
- Responsive design for mobile and desktop
- Fallback tile layer (CARTO Voyager) when OpenStreetMap tiles are unavailable

---

## Data Download

The underlying measurement database is available as JSON:

📄 [database.json](database.json) — all opengeiger.de and Geigerzählerforum entries with coordinates, dose rates, and source links

---

## Frequently Asked Questions

**Where are the highest radiation locations in Germany?**  
The map includes extreme readings (≥ 10 µSv/h) at several historical uranium mining and processing sites, particularly in Saxony and Thuringia (former East Germany's Wismut uranium mining region). Old mine tailings and slag heaps from radium and uranium processing are among the highest-reading locations.

**What causes elevated radiation at these locations?**  
Sources include: naturally occurring radioactive minerals (uranium, thorium, radium), old mine tailings and slag heaps from uranium or rare-earth mining, radium-painted antique instruments, uranium-glazed pottery and tiles, monazite-rich sands, and some industrial by-products.

**Is this data official or government-sourced?**  
No — all measurements are citizen-science contributions published by hobby physicists and enthusiasts on opengeiger.de and the Geigerzählerforum. Official German radiation monitoring data is published by the BfS (Bundesamt für Strahlenschutz) at [odlinfo.bfs.de](https://odlinfo.bfs.de/).

**How accurate are the measurements?**  
Accuracy varies by instrument and technique. Measurements should be treated as indicative, not certified. Always check the original source entry for instrument type, method notes, and measurement conditions.

**What is µSv/h?**  
Microsieverts per hour — the standard unit for ambient gamma dose rate. It measures how quickly ionising radiation is delivering energy to tissue. 1 µSv/h sustained for a year equals roughly 8.76 mSv annual dose (occupational limit in most EU countries is 20 mSv/year).

**Can I contribute new locations?**  
Yes — use the **Add places / Contact** button in the map header to get in touch. New entries from opengeiger.de and the Geigerzählerforum are periodically merged into the database.

---

## Related searches

- Geiger counter map Germany
- radiation map Deutschland
- Strahlungsmessung Karte Deutschland
- elevated radiation locations Europe
- radioactivity hotspot map
- Geigerzähler Messorte Karte
- uranium mine radiation Germany
- Radioaktivität Karte Deutschland
- dose rate map Europe
- Wismut radiation sites
- naturally occurring radioactive material NORM map
- Geiger Caching opengeiger

---

## Credits & Licences

| Resource | Source | Licence |
|----------|--------|---------|
| Measurement data | [opengeiger.de](http://www.opengeiger.de/GeigerCaching/GeigerCaching.html) | © respective contributors |
| Measurement data | [Geigerzählerforum](https://www.geigerzaehlerforum.de/) | © respective contributors |
| Base map tiles | [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors | ODbL |
| Fallback tiles | [CARTO Voyager](https://carto.com/attributions) | CC BY 3.0 |
| Mapping framework | [Leaflet.js](https://leafletjs.com/) | BSD-2-Clause |

---

## Run locally

```bash
python server.py        # starts at http://localhost:8000
```

Open `http://localhost:8000` for the map or `http://localhost:8000/editor.html` for the database editor.
