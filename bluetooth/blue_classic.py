import bluetooth


# 返回地址和设备名
def scan_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    return nearby_devices


def scan_service(dev_addr):
    return bluetooth.find_service(address=dev_addr)


def connect(bd_addr):
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.AUDIO_SINK_CLASS)
    sock.connect((bd_addr, port))
    sock.send("hello!!")
    sock.close()


if __name__ == '__main__':
    mac = "F8:A7:5A:DC:72:72"
    connect(mac)

