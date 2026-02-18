"""
Convert multiple shapefiles to GeoJSON for web mapping
"""
import geopandas as gpd
import json

# List of shapefiles to convert
shapefiles = [
    {'input': r'shape_files\EqCatM4.shp', 'output': 'EqCatM4.geojson', 'name': 'EqCatM4'}
    # {'input': r'shape_files\WCS_reverse_planes.shp', 'output': 'WCS_reverse_planes.geojson', 'name': 'WCS_Reverse_Planes'},    
    # {'input': r'shape_files\WCS_polylines.shp', 'output': 'WCS_polylines.geojson', 'name': 'WCS_polylines'}
    # {'input': r'shape_files\rcs_strike_slip.shp', 'output': 'rcs_strike_slip.geojson', 'name': 'RCS_Strike_Slip_Faults'},
    
    # {'input': r'shape_files\wcs_normal.shp', 'output': 'wcs_normal.geojson', 'name': 'WCS_Normal_Faults'},
    # {'input': r'shape_files\wcs_strike_slip.shp', 'output': 'wcs_strike_slip.geojson', 'name': 'WCS_Strike_Slip_Faults'}
    ]

for shapefile in shapefiles:
    print(f"\n{'='*60}")
    print(f"Processing: {shapefile['name']}")
    print('='*60)
    
    try:
        # Read the shapefile
        print(f"Reading {shapefile['input']}...")
        gdf = gpd.read_file(shapefile['input'])
        
        # Show basic info
        print(f"\nTotal features: {len(gdf)}")
        print(f"\nColumn names and types:")
        print(gdf.dtypes)
        print(f"\nFirst few rows:")
        print(gdf.head())
        
        # Check coordinate system
        print(f"\nCoordinate Reference System: {gdf.crs}")
        
        # Convert to WGS84 (EPSG:4326) for web mapping if needed
        if gdf.crs and gdf.crs.to_epsg() != 4326:
            print("\nConverting to WGS84 (EPSG:4326)...")
            gdf = gdf.to_crs(epsg=4326)
        
        # Convert to GeoJSON
        print(f"\nConverting to GeoJSON...")
        gdf.to_file(shapefile['output'], driver='GeoJSON')
        print(f"✓ Saved as '{shapefile['output']}'")
        
        # Show some statistics if there are numeric columns
        print("\nNumeric column statistics:")
        numeric_cols = gdf.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            if col != 'geometry':
                print(f"\n{col}:")
                print(f"  Min: {gdf[col].min()}")
                print(f"  Max: {gdf[col].max()}")
                print(f"  Mean: {gdf[col].mean():.2f}")
    
    except Exception as e:
        print(f"❌ Error processing {shapefile['name']}: {e}")

print(f"\n{'='*60}")
print("✓ All conversions complete!")
print('='*60)
