# opengeiger-map

Interactive map of the opengeiger.de "Interesting excursions" locations with measured dose rates.

Live webpage:
https://clarityQuest.github.io/opengeiger-map/

This project renders known Geiger Caching spots as clickable markers on a Leaflet map. Marker color and size reflect the dose rate category, and selecting a marker opens a detail panel with location notes and a direct link back to the original opengeiger.de entry.

The page is a static HTML implementation and can be hosted directly with GitHub Pages.

## Sources

- opengeiger.de Geiger Caching page (location names, notes, dose rates): http://www.opengeiger.de/GeigerCaching/GeigerCaching.html
- OpenStreetMap tiles and map data attribution: https://www.openstreetmap.org/copyright
- Leaflet mapping library: https://leafletjs.com/
