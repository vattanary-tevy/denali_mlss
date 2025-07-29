# denali_mlss

Based on the Sightline dev kit, this repo includes samples of recorded data in multiple file formats:
- single kml file
- multiple kml file
- klv file
- nitf file

'1_klv_acq.py' extracts the included .klv file, and outputs the "key, length, and value (in hex)" of the image.

'2_ntf_acq.py' extracts limited features of the metadata. 

## Key Libraries

- rasterio

## Getting Started

1. Open one of the two python scripts to extract metadata accordingly.
2. Modify file name as needed.