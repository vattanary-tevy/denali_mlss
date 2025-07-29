import rasterio

# Open the NITF file
file_path = "1_0386.NTF"
with rasterio.open(file_path) as src:
    print("File opened successfully!")
    print("Width:", src.width)
    print("Height:", src.height)
    print("Number of bands:", src.count)
    print("CRS:", src.crs)

    # Read the firyes, writest band (example)
    band1 = src.read(1)
    print("Band data shape:", band1.shape)