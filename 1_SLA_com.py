import socket
import struct

def build_get_version_cmd():
    header = b'\x51\xAC'             # SLA command header
    msg_id = struct.pack('<H', 0x0100)  # Message ID: GetVersion
    length = struct.pack('<H', 0)       # No payload
    crc = struct.pack('<H', 0)          # SightLine ignores CRC if set to 0
    return header + msg_id + length + crc

UDP_IP = "192.168.0.35"  # SLA board IP
UDP_PORT = 14001          # Command port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)  # 2-second timeout

packet = build_get_version_cmd()
sock.sendto(packet, (UDP_IP, UDP_PORT))

try:
    data, addr = sock.recvfrom(1024)
    print("Received:", data)
except socket.timeout:
    print("No response — check IP, port, and SLA config")
