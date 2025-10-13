# Interactive Seismic Data Viewer

A high-performance web-based tool for visualizing and filtering seismic data, earthquake catalogues, and geospatial datasets.

## Live Demo

**View Live Application:** [https://azymvragakis.github.io/seismic-map-viewer/](https://azymvragakis.github.io/seismic-map-viewer/)

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [How to Use the Online Map](#how-to-use-the-online-map)
- [Adding Your Own Shapefiles](#adding-your-own-shapefiles)
- [Deployment Guide](#deployment-guide)
- [Technical Details](#technical-details)
- [Browser Compatibility](#browser-compatibility)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features

### Core Functionality
- **Multi-Layer Support**: Display and compare multiple seismic datasets simultaneously
- **Advanced Filtering**: Filter data by magnitude, depth, date, fault type, and any attribute
- **Attribute-Based Coloring**: Color-code features by properties (e.g., red for normal faults, black for reverse faults)
- **Performance Optimized**: Handles 100,000+ earthquake points with canvas rendering
- **Interactive Controls**:
  - Toggle layers on/off
  - Adjust layer opacity
  - Reorder layer stacking (z-index)
  - Customize colors and symbol sizes
  - Flash filtered features for easy identification

### Data Visualization
- Click features to view detailed information in popups
- Scrollable popups with "Show All Details" button
- Automatic zoom to clicked features
- Dimmed vs. hidden display modes for non-filtered features
- Real-time feature counting

---

## Installation

Before using or deploying this application, you need to install the required Python dependencies for shapefile processing.

### Using pip:

```bash
pip install -r requirements.txt
```

### Using conda:

```bash
conda env create -f environment.yml
conda activate seismic-viewer
```

### Required Dependencies:
- **GeoPandas** (>=0.14.0): For reading and processing shapefiles
- **Pandas** (>=2.0.0): Data manipulation
- **NumPy** (>=1.24.0): Numerical operations
- **Shapely** (>=2.0.0): Geometric operations
- **Fiona** (>=1.9.0): File I/O for geospatial data
- **PyProj** (>=3.6.0): Coordinate system transformations
- **Matplotlib** (>=3.7.0): Optional, for additional visualizations

---

## Quick Start

### Option 1: Use Online (No Installation)

Simply visit the live demo link above. No installation required!

### Option 2: Run Locally

1. **Install dependencies** (see [Installation](#installation) section above)

2. **Clone or download this repository**:
   ```bash
   git clone [your-repository-url]
   cd online_map
   ```

3. **Start the local server**:
   ```bash
   python run_server.py
   ```
   The application will open automatically at `http://localhost:8000`

4. **Or open directly**: Simply open `index.html` in your browser (no server required)

---

## How to Use the Online Map

### Basic Navigation

1. **Pan the Map**: Click and drag to move around
2. **Zoom**: Use mouse wheel, +/- buttons, or double-click
3. **Layers Panel** (left sidebar): View all available layers

### Working with Layers

#### Toggle Layer Visibility
- **Checkbox**: Click to show/hide layer on map
- **Layer Name**: Click to activate layer for filtering (highlighted in blue)

#### Adjust Layer Appearance
1. **Opacity Slider**: Control layer transparency (0-100%)
2. **Layer Order**: Use / buttons to change stacking order
3. **Color Selection**: 
   - Choose from 10 predefined colors
   - Each layer can have its own color
4. **Size Control**: 
   - Adjust point radius (1-20 pixels)
   - Affects polygon border thickness
5. Click **"Apply Style"** to update

### Filtering Data

#### Step 1: Activate a Layer
Click on the layer name in the sidebar (it will turn blue)

#### Step 2: Choose Filter Column
- Select an attribute column from the dropdown
- **Number columns**: Show number input with operators (>=, <=, =, >, <)
- **String columns**: Show dropdown with all unique values

#### Step 3: Set Filter Value
- For numbers: Enter value and select operator
- For strings: Select value from dropdown

#### Step 4: Apply Filter
- Click **"Apply"** button
- Matching features highlight in aqua
- Non-matching features become dimmed

#### Step 5: Optional Controls
- **Hide non-matching features**: Check box to completely hide non-filtered data
- **Flash Filtered Features**: Click to make filtered features pulse (helps locate them)
- **Reset**: Clear filter and show all features

### Color by Attribute

Color features based on their properties (e.g., color faults by type):

1. **Enable**: Check "Color by Attribute" box (yellow panel)
2. **Select Column**: Choose attribute to color by
3. **Set Color Mappings**: 
   - Each unique value gets a color dropdown
   - Example: `normal`  Red, `thrust`  Black, `strike-slip`  Blue
4. **Apply**: Click "Apply Attribute Colors"

**Note:** Filtered features always turn aqua (overrides attribute colors)

### Feature Information

#### View Details
- **Click any feature** on the map
- Popup shows:
  - First 5 properties (or 3 for large datasets)
  - "Show All Details" button for complete info
- **Auto-zoom**: Map zooms to clicked feature

---

## Adding Your Own Shapefiles

Follow these steps to add new seismic data or shapefiles to the viewer:

### Step 1: Prepare Your Shapefile

Your shapefile should include these files:
```
your_data.shp        Required: geometry
your_data.shx        Required: shape index
your_data.dbf        Required: attributes
your_data.prj        Required: projection
your_data.cpg        Optional: encoding
```

**Important:** 
- All files must have the same name (different extensions)
- Coordinate system should be WGS84 (EPSG:4326) or will be converted automatically

### Step 2: Convert Shapefile to GeoJSON

Place your shapefile in the `online_map` folder, then:

#### Option A: Edit convert_shapefile.py

1. Open `convert_shapefile.py`
2. Add your shapefile to the list:

```python
shapefiles = [
    ('eshm13_vanilla.shp', 'data_vanilla.geojson'),
    ('eshm13_edited.shp', 'data_edited.geojson'),
    ('catalogue.shp', 'data_catalogue.geojson'),
    ('your_data.shp', 'data_your_name.geojson'),  #  Add this line
]
```

3. Run the converter:
```powershell
python convert_shapefile.py
```

#### Option B: Manual Conversion

```python
import geopandas as gpd

# Read shapefile
gdf = gpd.read_file('your_data.shp')

# Convert to WGS84 if needed
if gdf.crs != 'EPSG:4326':
    gdf = gdf.to_crs('EPSG:4326')

# Save as GeoJSON
gdf.to_file('data_your_name.geojson', driver='GeoJSON')

print(f"Converted! Features: {len(gdf)}")
```

**Requirements:**
```powershell
# Install all dependencies
pip install -r requirements.txt

# Or install manually
pip install geopandas
```

### Step 3: Add Layer to index.html

1. Open `index.html`
2. Find the `layerConfigs` array (around line 330)
3. Add your new layer:

```javascript
const layerConfigs = [
    {
        name: 'ESHM13 Vanilla',
        file: 'data_vanilla.geojson',
        color: '#667eea',
        visible: true,
        zIndex: 1,
        size: 6
    },
    {
        name: 'ESHM13 Edited',
        file: 'data_edited.geojson',
        color: '#f093fb',
        visible: true,
        zIndex: 2,
        size: 6
    },
    {
        name: 'Catalogue',
        file: 'data_catalogue.geojson',
        color: '#ffcc00',
        visible: true,
        zIndex: 3,
        size: 6
    },
    {
        name: 'Your Layer Name',           //  Display name
        file: 'data_your_name.geojson',    //  Your GeoJSON file
        color: '#ff6b6b',                  //  Initial color (any hex)
        visible: true,                     //  Show on load
        zIndex: 4,                         //  Stack order (higher = on top)
        size: 6                            //  Point/border size
    }
];
```

### Step 4: Test Locally

```powershell
python run_server.py
# Visit: http://localhost:8000
```

Check:
-  Layer appears in sidebar
-  Features display on map
-  Clicking features shows popup
-  Filtering works
-  No console errors (F12)

### Step 5: Deploy

See [Deployment Guide](#deployment-guide) below to make your updated map public.

---

## Deployment Guide

Make your seismic viewer accessible online via a public link.

### Prerequisites

- GitHub account
- Git installed
- Your data files ready

### Recommended: Create New Public Repository

This keeps your main research private while making the viewer public.

#### 1. Create Repository on GitHub

1. Go to: https://github.com/new
2. **Repository name**: `seismic-map-viewer` (or your choice)
3. **Description**: "Interactive seismic data viewer"
4. **Visibility**:  Public
5. Click **"Create repository"**

#### 2. Copy Files to New Repository

```powershell
# Navigate to working directory
cd d:\Programms\github_repositories

# Clone new repository
git clone https://github.com/YOUR_USERNAME/seismic-map-viewer.git

# Copy files from online_map folder
cd seismic-map-viewer
Copy-Item -Path "d:\path\to\Zym_private_repo\online_map\*" -Destination "." -Recurse

# Commit and push
git add .
git commit -m "Initial commit - seismic data viewer"
git push origin main
```

#### 3. Enable GitHub Pages

1. Go to repository on GitHub
2. Click **Settings**  **Pages** (left sidebar)
3. Under **Build and deployment**:
   - Source: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/ (root)**
4. Click **Save**
5. Wait 1-2 minutes

#### 4. Access Your Live Site

Your viewer will be live at:
```
https://YOUR_USERNAME.github.io/seismic-map-viewer/
```

### Updating Your Deployed Site

After making changes locally:

```powershell
cd d:\path\to\seismic-map-viewer

# If using separate public repo, copy updated files first
Copy-Item -Path "d:\path\to\Zym_private_repo\online_map\*" -Destination "." -Recurse -Force

# Push changes
git add .
git commit -m "Update viewer with new data/features"
git push origin main

# GitHub Pages auto-updates in 1-2 minutes
```

### Troubleshooting Deployment

**404 Error?**
- Wait 5 minutes and refresh
- Verify Settings  Pages shows green success message
- Check correct branch/folder selected

**No Data Loading?**
- Ensure `.geojson` files are in same folder as `index.html`
- Check file names match exactly (case-sensitive)
- Verify files were committed: `git status`

**Large File Error (>100MB)?**
- Compress GeoJSON: Remove whitespace, reduce decimal precision
- Split large datasets into multiple layers
- Consider using external data hosting

---

## Technical Details

### Technology Stack

- **Leaflet.js 1.9.4**: Interactive mapping library
- **HTML5 Canvas**: High-performance rendering for large datasets
- **Vanilla JavaScript**: No framework dependencies
- **GeoJSON**: Standard geospatial data format
- **Python 3**: Data conversion and local server

### Architecture

```
Client-Side Only (Static Website)
├── HTML: Structure and UI
├── CSS: Styling and layout
├── JavaScript: 
│   ├── Map rendering (Leaflet)
│   ├── Data filtering logic
│   ├── Event handlers
│   └── Canvas rendering for performance
└── GeoJSON: Feature data
```

### Performance Optimizations

1. **Canvas Renderer**: Replaces DOM-based SVG rendering
   - 10-100x faster for point data
   - Handles 100,000+ features smoothly

2. **Lazy Popup Generation**: Creates popups on-demand for large datasets
   - Reduces initial load time
   - Lower memory footprint

3. **Conditional Feature Rendering**: Optional hide/show toggle
   - Filters data before rendering
   - Dramatically improves performance when filtering

4. **Simplified Geometry**: 
   - Reduced coordinate precision
   - Smaller file sizes
   - Faster parsing and rendering

### File Structure

```
online_map/
├── index.html                    # Main application
├── data_vanilla.geojson          # ESHM13 Vanilla seismic zones
├── data_edited.geojson           # ESHM13 Edited seismic zones  
├── data_catalogue.geojson        # Earthquake catalogue
├── convert_shapefile.py          # Shapefile  GeoJSON converter
├── run_server.py                 # Local development server
├── README.md                     # This file
└── LICENSE                       # CC BY-NC-ND 4.0 License

Source files (optional):
├── eshm13_vanilla.shp/shx/dbf/prj
├── eshm13_edited.shp/shx/dbf/prj
└── catalogue.shp/shx/dbf/prj
```

### Data Requirements

**Supported Formats:**
- Input: ESRI Shapefile (.shp + supporting files)
- Output: GeoJSON (RFC 7946 compliant)

**Geometry Types:**
- Points (earthquake epicenters)
- LineStrings (fault traces)
- Polygons (seismic zones)
- MultiPoint, MultiLineString, MultiPolygon

**Coordinate System:**
- WGS84 (EPSG:4326) required
- Automatic conversion from other projections via GeoPandas

### Browser Requirements

**Minimum:**
- ES6 JavaScript support
- HTML5 Canvas
- CSS3 Flexbox
- LocalStorage (optional, for future features)

---

## Browser Compatibility

### Fully Supported
-  Chrome 90+ (recommended)
-  Firefox 88+
-  Edge 90+
-  Safari 14+

### Mobile Support
-  iOS Safari 14+
-  Chrome Mobile 90+
-  Limited on small screens (best on tablet/desktop)

### Not Supported
-  Internet Explorer (any version)
-  Opera Mini
-  Very old browsers without ES6

---

## Data Sources

This viewer currently displays:

1. **ESHM13 - European Seismic Hazard Model 2013**
   - Vanilla version: Original seismic source zones
   - Edited version: Modified/updated zones
   - Source: [European Facilities for Earthquake Hazard and Risk](http://www.efehr.org/)

2. **Earthquake Catalogue**
   - 110,000+ seismic events
   - Attributes: Magnitude, depth, date, location, focal mechanisms
   - Source: [Specify your data source]

---

## Development

### Local Development Setup

```powershell
# Clone the repository
git clone https://github.com/YOUR_USERNAME/seismic-map-viewer.git
cd seismic-map-viewer

# Install all dependencies
pip install -r requirements.txt

# Or using conda
conda env create -f environment.yml
conda activate seismic-viewer

# Start local server
python run_server.py

# Open browser
start http://localhost:8000
```

### Dependencies

The project requires:
- **Python 3.8+**
- **GeoPandas**: Shapefile reading and conversion
- **Pandas**: Data manipulation
- **NumPy**: Numerical operations
- **Shapely**: Geometry operations
- **Fiona**: File I/O
- **PyProj**: Coordinate system transformations

See `requirements.txt` or `environment.yml` for specific versions.

### Making Changes

1. Edit `index.html` for UI/functionality changes
2. Test locally with `python run_server.py`
3. Add new data via `convert_shapefile.py`
4. Check browser console (F12) for errors
5. Deploy updates via Git push

### Code Structure

**Main Functions:**
- `createLayer(layerId)`: Renders GeoJSON as Leaflet layer
- `applyFilter()`: Filters features by attribute values
- `flashFilteredFeatures()`: Visual highlighting animation
- `applyColorByAttribute()`: Attribute-based styling
- `renderLayerList()`: Updates sidebar UI

---

## Known Issues & Limitations

### Current Limitations

1. **Static Data Only**: No real-time updates or database connectivity
2. **File Size Limit**: GitHub Pages has 100MB per file limit
3. **Client-Side Processing**: All filtering done in browser (may slow on very large datasets)
4. **No User Authentication**: Public site = public data

### Workarounds

- **Large Files**: Split into multiple layers or compress data
- **Real-Time Data**: Consider external API integration
- **Performance**: Use "Hide non-matching features" toggle when filtering

---

## License

**Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**

This work is licensed under the most restrictive Creative Commons license.

### You are free to:
- **Share**: Copy and redistribute the material in any medium or format

### Under the following terms:
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made
- **NonCommercial**: You may not use the material for commercial purposes
- **NoDerivatives**: If you remix, transform, or build upon the material, you may not distribute the modified material

See `LICENSE` file for full legal text.

**Copyright © 2025 [Your Name/Institution]**

This software was developed as part of [Project Name/Research] at [Institution].

---

## Acknowledgments

### Development
- Developed by: [Your Name]
- Affiliation: [Your Institution]
- Project: [Project Name/Grant Number]

### Data Sources
- ESHM13 Seismic Model: European Facilities for Earthquake Hazard and Risk (EFEHR)
- Earthquake Catalogue: [Your data source]

### Technologies
- Leaflet.js: Open-source mapping library by Vladimir Agafonkin
- OpenStreetMap: Map tiles and data contributors
- GeoPandas: Geospatial data processing library

### Supervision
- [Supervisor/Advisor Name], [Institution]

---

## Contact

For questions, issues, or collaboration inquiries:

- **Author**: [Your Name]
- **Email**: [your.email@institution.edu]
- **GitHub**: [Your GitHub Profile]
- **Institution**: [Your Institution/Department]

---

## Version History

### Version 1.0.0 (Current)
- Initial public release
- Multi-layer support with 3 seismic datasets
- Advanced filtering by any attribute
- Attribute-based coloring
- Performance optimizations for 100,000+ points
- Flash feature for filtered data
- Responsive design

---

## Future Enhancements

Potential features for future versions:

- [ ] Export filtered data as GeoJSON/CSV
- [ ] Time-series animation for temporal data
- [ ] 3D visualization for depth analysis
- [ ] Custom basemap selection
- [ ] Measurement tools (distance, area)
- [ ] Comparison mode (side-by-side maps)
- [ ] Print/export high-resolution maps
- [ ] Mobile app version
- [ ] Integration with external APIs
- [ ] User-uploaded data support

---

## Citation

If you use this tool in your research, please cite:

```bibtex
@software{seismic_viewer_2025,
  author = {Your Name},
  title = {Interactive Seismic Data Viewer},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/YOUR_USERNAME/seismic-map-viewer}
}
```

---

**Built with  for the seismology research community**
