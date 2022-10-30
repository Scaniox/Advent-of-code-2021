from pathlib import Path


def parse_packet(bits):
    version = int(bits[current_index:current_index+3])
    type_id = int(bits[current_index+3:current_index+6])
    current_index += 6

    if type_id == 4: # int literal packet
        current_index = bits.find("1", current_index)

        int_str = ""
        current_index += 5
        while bits[current_index-5] == "1":
            int_str += bits[current_index-4:current_index]
            current_index += 5
        int_str += bits[current_index-4:current_index]

        value = int(int_str)
        return

    else:
        length_t_id = int(bits[7])
        if length_t_id == 0:
            length = int(bits[8:8+15])
            end_index = current_index + length
            while current_index < end_index:
                parse_packet(bits)

        elif length_t_id == 1:
            total_packets = int(bits[8:8+11])
            for _ in range(total_packets):
                parse_packet(bits)



hex_stream = (Path(__file__).parent.parent / "16-test.txt").read_text()
bit_stream = bin(int(hex_stream, 16))[2:]

current_index = 0
