import fiona

# Path to your .NTF file
ntf_file_path = 'path/to/your/file.ntf'

# Open and read the .NTF file
with fiona.open(ntf_file_path) as src:
    print(f"CRS: {src.crs}")
    print(f"Number of features: {len(src)}")
    
    for feature in src:
        print("Feature ID:", feature['id'])
        print("Geometry Type:", feature['geometry']['type'])
        print("Properties:", feature['properties'])
        print("Geometry Coordinates:", feature['geometry']['coordinates'])
        print("-" * 40)
