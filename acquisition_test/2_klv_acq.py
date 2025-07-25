def read_klv_file(filename):
    with open(filename, 'rb') as f:
        while True:
            key = f.read(16)
            if not key:
                break
            length = int.from_bytes(f.read(1), 'big')
            value = f.read(length)
            print(f"Key: {key.hex()} | Length: {length} | Value (hex): {value.hex()[:32]}...")

read_klv_file("C:/Users/VattanaryTevy/OneDrive - PowerLight Technologies/Desktop/denali_mlss/acquisition_test/1_0000.klv")
