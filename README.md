# denali_mlss

This project documents the evaluation process for camera-based object detection using the SightLine Development Kit as part of the MLSS action plan.

## Project Overview

- Platform: SightLine video processing dev kit
- Objective: Evaluate camera-based object detection for DENALI using SightLine SDK
- Status: Operated in demo mode (no live testing)
- Data: Pre-recorded video, telemetry, and metadata
- For latest updates, see: `Moving Target Indicator` folder

---

## Output File Types

### KLV (Key-Length-Value) Metadata
- Encoded telemetry metadata in compliance with STANAG 4609 / MISB standards
- Best visualized via video playback with overlay or as temporal plots
- Example output:

Key: 060e2b34020b01010e01030101000000
Length: 97
Value (hex): 0208000606918c61dc5f050200000602…


### KML (Keyhole Markup Language)
#### Single KML
- XML-based format containing a single geospatial point
- Easy to visualize in Google Earth or GIS software
- Example: [1_0222.kml](acquisition_test/1_0222.kml)

#### Multiple KML
- Folder of KML files or one KML with multiple placemarks
- Splits data into modular layers or individual missions/events
- Example output: [_1.kml](acquisition_test/_1.kml)

### NITF (National Imagery Transmission Format)
- Used for packaging imagery and associated metadata
- Standard format for military/ISR transmission
- Contains multiple bands of image data and embedded metadata
- Supported by GIS tools such as ArcGIS Pro
- Example output using Python `rasterio`:

File opened successfully!
Width: 1920
Height: 1080
Number of bands: 3
CRS: None
Band data shape: (1080, 1920)


---

## Video Format

- IP Stream: H.264 or H.265 encoded video via UDP
- Frame Buffer: Raw RGB/YUV frames
- Telemetry: Object bounding boxes, tracking vectors, KLV metadata via UDP/TCP
- Recording: Snapshots or video on SD card, SSDs

---

## Limitations

### Built-in Algorithms
- Cannot modify built-in tracking, stabilization, or detection algorithms
- Only tunable via SLA GUI or IP telemetry commands
- Custom computer vision/ML models require external hardware integration

---

## Challenges Encountered

- Difficulty extracting full NITF metadata
- Basic metadata extraction succeeded with `rasterio`
- Trouble pip installing `gdal` python library; `osgeo4w` driver took a long time and didn't finish installing

---

## File References

- **KLV Metadata File**: [1_0000.klv](acquisition_test/1_0000.klv)
- **Single KML File**: [1_0222.kml](acquisition_test/1_0222.kml)
- **Multiple KML File**: [_1.kml](acquisition_test/_1.kml)
- **NITF File**: [1_0386.NTF](acquisition_test/1_0386.NTF)

---

## Documentation and Resources

- [SightLine API Documentation](https://sightlineapplications.com/releases/latest/IDD-SLA-Protocol_3_9.pdf)
- [SightLine Startup Guide](https://sightlineapplications.com/wp-content/uploads/EAN-Startup-Guide-4100-OEM.pdf)
- [EAN-File-Recording.pdf](https://sightlineapplications.com/wp-content/uploads/EAN-File-Recording.pdf)
- [NITF Data Intro (ArcGIS)](https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/introduction-to-nitf-data.htm)
- [MIL-STD-2500C – NITF Format Specification](https://everyspec.com/MIL-STD/MIL-STD-2000-2999/MIL-STD-2500C_34661/)

---


## Getting Started

1. Open one of the two python scripts to extract metadata accordingly.
2. Modify file name as needed.

---

## GitHub Repository

- Repository: [vattanary-tevy/denali_mlss](https://github.com/vattanary-tevy/denali_mlss)