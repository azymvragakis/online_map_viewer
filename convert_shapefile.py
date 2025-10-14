"""
Convert multiple shapefiles to GeoJSON for web mapping
"""
import geopandas as gpd
import json

# List of shapefiles to convert
shapefiles = [
    {'input': r'shape_files\eshm13_edited.shp', 'output': 'eshm13_edited.geojson', 'name': 'ESHM13_edited'},
    {'input': r'shape_files\eshm20_edited.shp', 'output': 'eshm20_edited.geojson', 'name': 'ESHM20_edited'},
    {'input': r'shape_files\vam16_edited.shp', 'output': 'vam16_edited.geojson', 'name': 'VAM16_edited'},
    {'input': r'shape_files\eshm13_vanilla.shp', 'output': 'eshm13_vanilla.geojson', 'name': 'ESHM13_vanilla'},
    {'input': r'shape_files\eshm20_vanilla.shp', 'output': 'eshm20_vanilla.geojson', 'name': 'ESHM20_vanilla'},
    {'input': r'shape_files\vam16_vanilla.shp', 'output': 'vam16_vanilla.geojson', 'name': 'VAM16_vanilla'}
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
