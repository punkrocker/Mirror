from bluepy.btle import Scanner, DefaultDelegate, Peripheral

yeelight_name = "Yeelight Blue II"


def scan_devices():
    scanner = Scanner()
    devices = scanner.scan(10.0)
    for dev in devices:
        name = dev.getValueText(0x09)
        if name == yeelight_name:
            print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
            return dev


def get_services(mac):
    p = Peripheral(mac)
    services = p.getServices()
    # displays all services
    for service in services:
        print(service)
    characteristics = p.getCharacteristics()
    print("Handle   UUID                                Properties")
    print("-------------------------------------------------------")
    for ch in characteristics:
        print("  0x" + format(ch.getHandle(), '02X') + "   " + str(ch.uuid) + " " + ch.propertiesToString())


if __name__ == '__main__':
    light = scan_devices()
    get_services(light.addr)
