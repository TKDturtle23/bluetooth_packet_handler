import zlib


def decompress_data(data: bytearray):
    # Decompress using zlib
    return bytearray(zlib.decompress(bytes(data)))

def decode_data(packets: list[bytearray], max_packet_size: int):
    if not packets or len(packets[0]) < 2:
        raise ValueError("Invalid packets format")

    compression_level = packets[0][0]
    packet_count = packets[0][1]

    if packet_count != len(packets) - 1:
        raise ValueError("Packet count mismatch")

    # Calculate how many bytes are needed to represent the packet index
    # Use the first packet to estimate index_bytes
    first_packet = packets[1]
    index_bytes = 1
    payload_size = max_packet_size - index_bytes
    while len(first_packet) > max_packet_size:
        index_bytes += 1
        payload_size = max_packet_size - index_bytes

    data = bytearray()
    for packet in packets[1:]:
        payload = packet[:-index_bytes]
        data.extend(payload)

    # Decompress based on compression_level
    if compression_level > 0:
        data = decompress_data(data)

    return data
def main():
    data = decode_data([bytearray(b'\x01\x03'), bytearray(b'x\x01\x15\xc8\xb1\r\x800\x10\x03\xc0\xc1\x98&\xc8X\xca\xdb!\x00'), bytearray(b'\x85\x15!\xb6\x874W\\\x0b\x0eS\xd5b\x81\xe5\x08\xc5\xd9\x9f\x01'), bytearray(b'uQ\xf7\x08\xcc3su\xbc\x7f\xa6@k\xfb\x01`\xb8\x16X\x02')], 20)
    print (data)
if __name__ == "__main__":
    main()