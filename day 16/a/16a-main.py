from pathlib import Path

def parse_packet(bits):
    version = int(bits[0:3])
    type_id = int(bits[3:6])

hex_stream = (Path(__file__).parent.parent / "16-test.txt").read_text()
bit_stream = bin(int(hex_stream, 16))[2:]
