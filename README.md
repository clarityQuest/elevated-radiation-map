# opengeiger-map

Interactive map of the opengeiger.de "Interesting excursions" locations with measured dose rates.

Live webpage (GitHub Pages):
https://clarityQuest.github.io/opengeiger-map/

If the page still shows 404, GitHub Pages deployment is still in progress. You can also open the map directly from the repository file:
https://github.com/clarityQuest/opengeiger-map/blob/main/index.html

This project renders known Geiger Caching spots as clickable markers on a Leaflet map. Marker color and size reflect the dose rate category, and selecting a marker opens a detail panel with location notes and a direct link back to the original opengeiger.de entry.

The page is a static HTML implementation and can be hosted directly with GitHub Pages.

## Sources

- opengeiger.de Geiger Caching page (location names, notes, dose rates): http://www.opengeiger.de/GeigerCaching/GeigerCaching.html
- OpenStreetMap tiles and map data attribution: https://www.openstreetmap.org/copyright
- Leaflet mapping library: https://leafletjs.com/
