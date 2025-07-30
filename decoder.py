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
        raise ValueError(f"Packet count mismatch, expected {packet_count}, received {len(packets)}")

    # Calculate how many bytes are needed to represent the packet index
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
def is_complete(data: list[bytearray]):
    return
def main():
    data = decode_data([bytearray(b'\x03\x08'), bytearray(b'x\xda\x1d\xcd1\x0e\xc3 \x0c\x85\xe1\xabD\xcc=A\xd7\x1e\xa3\x00'), bytearray(b'Cd\x82IPL\x8c\x0c\x0cm\xd5\xbb\xb7\xcf\x9b\xbf_6|\x01'), bytearray(b'\xc2\x15\xeeKH\x9ci\xca\x08\xb7%T\xd8\xcav\x9a\x8a t\x02'), bytearray(b'\x84N\ts\xc4\x1ce\xf6\x03b\x97j[\x87\xae\xc6}\x90\xf9\x03'), bytearray(b'\x13\x19=\xcf\xedd35\x94\xe4\x9b\x94\xa85a\x84\x86\xd0\xf4\x04'), bytearray(b'\xda\x81\xb7\xffpX\xa9\r|\x82\x8f\xd9\x87Vp\x07wc_\x05'), bytearray(b'}9\xa8F)\xff\xdb\xef\x0fw\x056\x80\x06'), bytearray(b'__END__')], 20)
    print (data)
if __name__ == "__main__":
    main()