import struct
import socket
import re


def format_mac(mac):
    mac_re = re.compile(r'''
                      (^([0-9A-F]{1,2}[-]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[:]){5}([0-9A-F]{1,2})$
                      |^([0-9A-F]{1,2}[.]){5}([0-9A-F]{1,2})$
                      )''', re.VERBOSE | re.IGNORECASE)
    # print(re.match(mac_re, mac))
    if re.match(mac_re, mac):
        if mac.count(':') == 5 or mac.count('-') == 5 or mac.count('.'):
            sep = mac[2]
            mac_fm = mac.replace(sep, '')
            return mac_fm
    else:
        raise ValueError('Incorrect MAC format')


def create_magic_packet0(mac):
    data = b'FF' * 6 + (mac * 16).encode()
    print(data)

    print(type(data))
    send_data = b''
    for i in range(0, len(data), 2):
        send_data = send_data + struct.pack(b'B', int(data[i: i + 2], 16))  # int(data[i: i+2], 16) 把16进制转换成整数
    print(type(send_data))
    return send_data


def send_magic_packet(send_data):
    # broadcast_address = '192.168.255.255'
    broadcast_address = '255.255.255.255'
    port = 9
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(send_data, (broadcast_address, port))
