import struct


def create_magic_packet0(mac):
    data = b'FF' * 6 + (mac * 16).encode()
    print(data)

    print(type(data))
    send_data = b''
    for i in range(0, len(data), 2):
        send_data = send_data + struct.pack(b'B', int(data[i: i + 2], 16))  # int(data[i: i+2], 16) 把16进制转换成整数
    print(type(send_data))
    return send_data
