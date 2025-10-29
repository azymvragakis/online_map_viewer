# KMZ Folder Loading Instructions

## Overview
The map viewer now automatically loads KMZ files from the `kmz` folder when the page loads. This replaces the interactive upload interface.

## Setup Instructions

1. **KMZ Folder**: Place your KMZ files in the `/kmz` folder (already created)

2. **File Structure**:
   ```
   online_map_viewer/
   ├── kmz/
   │   ├── your_file1.kmz
   │   ├── your_file2.kmz
   │   └── any_other_files.kmz
   ├── index.html
   └── ... (other files)
   ```

3. **File Requirements**:
   - Files must be in KMZ format (KML files zipped)
   - Original symbology and styling will be preserved
   - Files are loaded automatically when the page opens

## Features

- **Automatic Loading**: All KMZ files in the folder are loaded on page startup
- **Symbology Preservation**: Original colors, icons, and styling are maintained
- **Layer Integration**: KMZ layers integrate with existing layer controls
- **Filtering Support**: Works with the existing filter system
- **Opacity Control**: Opacity can be adjusted like other layers

## Technical Details

- KMZ files are processed using JSZip for extraction
- KML content is converted to GeoJSON using toGeoJSON library
- Styling information is preserved from the original KML
- Layers are added to the map with the filename as the layer name

## Usage

1. Copy your KMZ files to the `kmz` folder
2. Refresh the browser page
3. Your KMZ layers will appear in the layer control panel
4. Use the layer controls to toggle visibility, adjust opacity, etc.

## Troubleshooting

- Ensure KMZ files are valid and not corrupted
- Check browser console for any loading errors
- Make sure the kmz folder is accessible by the web server
- Large KMZ files may take longer to load
