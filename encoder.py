import zlib

def compress_level_1(data: bytearray):
    # Apply minimal zlib compression (level 1)
    compressed = zlib.compress(bytes(data), level=1)
    return bytearray(compressed)

def compress_level_2(data: bytearray):
    # Moderate zlib compression (level 5)
    compressed = zlib.compress(bytes(data), level=5)
    return bytearray(compressed)

def compress_level_3(data: bytearray):
    # Strongest zlib compression (level 9)
    compressed = zlib.compress(bytes(data), level=9)
    return bytearray(compressed)



def encode_data(data: bytearray, max_packet_size: int, compression_level=0):
    if compression_level == 1:
        data = compress_level_1(data)
    elif compression_level == 2:
        data = compress_level_2(data)
    elif compression_level == 3:
        data = compress_level_3(data)

    packets: list[bytearray] = []
    index = 0

    # Calculate how many bytes are needed to represent the packet index
    max_index = (len(data) + max_packet_size - 1) // (max_packet_size - 1)
    index_bytes = 1
    while max_index > (1 << (8 * index_bytes)) - 1:
        index_bytes += 1

    payload_size = max_packet_size - index_bytes
    for i in range(0, len(data), payload_size):
        packet = data[i:i + payload_size]
        # Append index as big-endian
        for b in reversed(range(index_bytes)):
            packet.append((index >> (8 * b)) & 0xFF)
        index += 1
        packets.append(packet)
    # Prepend the amount of packets to the start of packets
    packet_count = len(packets)
    packets.insert(0, bytearray([compression_level & 0xFF, packet_count & 0xFF]))

    return packets

def main():
    data = encode_data(bytearray("asd;lfkjaslkdfjlskdjfoiwuefknmsdlfbsouidyfoisjdflksjdf", "utf-8"), 20, 3)
    print (data)
if __name__ == "__main__":
    main()