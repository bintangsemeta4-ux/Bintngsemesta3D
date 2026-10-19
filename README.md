# Bintang Semesta 3D Designer V3 (Android WebView project)

V3 improves placement controls for doors and windows: choose position (left/center/right/far left/far right) and building side (front/back/left/right). Columns and ceiling visuals are guarded against accidental duplicates. Includes project cost estimates and JSON/CSV/PDF actions from V2.

## Build APK
Upload the full project contents to your GitHub repository, keeping `.github/workflows/build-apk.yml`. Commit changes, then open Actions and run **Build Bintang Semesta APK**. On a successful run, download the artifact ZIP and install the APK inside it.

The app loads Three.js from a CDN, so an internet connection is required for the 3D renderer. This is a conceptual visualizer, not a construction drawing/CAD tool; wall openings are not yet Boolean cut-outs.
