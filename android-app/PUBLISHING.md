# Play Store Publishing Checklist

## App Identity
| Field | Value |
|---|---|
| **App name** | Elevated Radiation Map |
| **Package ID** | `de.threemills.geigermap` |
| **Version name** | 1.0 |
| **Version code** | 1 |

---

## Short Description (80 chars max)
```
Interactive map of elevated radiation locations from German monitoring sources.
```

## Full Description (4000 chars max)
```
Elevated Radiation Map displays locations with unusual or elevated radiation
readings collected from two German sources: opengeiger.de (Geiger Caching) and
Geigerzählerforum.

Features:
• Interactive map with colour-coded markers (µSv/h dose rate scale)
• Filter by source: opengeiger.de and/or Geigerzählerforum
• Tap any marker to see the location name, dose rate, notes and a direct link
  to the original source
• Open any location in Google Maps with one tap
• Show your current GPS position on the map
• Legend with full dose rate scale (Low → Extreme)

Dose rate colour scale:
🔵 Low       < 0.5 µSv/h
🟢 Elevated  0.5–1 µSv/h
🟡 High      1–3 µSv/h
🟠 Very high 3–10 µSv/h
🔴 Extreme   ≥ 10 µSv/h

Data credits:
• opengeiger.de — http://www.opengeiger.de/GeigerCaching/GeigerCaching.html
• Geigerzählerforum — https://www.geigerzaehlerforum.de/
• Map tiles: OpenStreetMap contributors / CARTO
```

---

## Store Listing Assets Needed
| Asset | Size | Notes |
|---|---|---|
| App icon (hi-res) | 512×512 px PNG | Export from `ic_launcher_foreground.xml` |
| Feature graphic | 1024×500 px PNG/JPG | Banner shown at top of store listing |
| Screenshots (phone) | 2–8 screenshots | Min 320px, max 3840px per side |
| Screenshots (tablet) | optional | 7" and/or 10" |

---

## Content Rating
- **Category:** Maps & Navigation  
- **Content rating questionnaire answers:**
  - Violence: No
  - Sexual content: No
  - User-generated content: No
  - Location sharing: Yes (device location only, not shared with others)
- **Expected rating:** Everyone (E) / PEGI 3

---

## Privacy Policy (Required for location permission)
You must host a privacy policy URL. Minimum content:
> This app requests device location solely to display your position on the map.
> No location data is transmitted to any server or third party.
> All radiation data is bundled locally and does not require an account.

Host it on GitHub Pages or any static host and paste the URL into the Play Console.

---

## Release Build Steps (Android Studio)

1. **Build → Generate Signed Bundle / APK**
2. Choose **Android App Bundle (.aab)** (required by Play Store)
3. Create a new keystore if you don't have one:
   - Store path: `e:\Projects\geiger-map-android\release.keystore`
   - Keep the keystore password and alias safe — you need them for every update
4. Build type: **release**
5. Upload the `.aab` to Play Console → Production (or Internal Testing first)

---

## Versioning (app/build.gradle)
Bump before every release:
```groovy
versionCode 2        // must always increase (integer)
versionName '1.1'   // human-readable
```
