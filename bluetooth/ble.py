from bluepy.btle import Scanner, DefaultDelegate, Peripheral


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)


def scan_devices():
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.scan(10.0)
    for dev in devices:
        print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
        for (adtype, desc, value) in dev.getScanData():
            print("  %s = %s" % (desc, value))


if __name__ == '__main__':
    p = Peripheral("b4:99:4c:60:94:42")
    services = p.getServices()

    # displays all services
    for service in services:
        print(service)
