from bluepy.btle import Scanner, UUID, Peripheral

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
    for characteristic in characteristics:
        if characteristic.supportsRead():
            print(str(characteristic))
            print(characteristic.uuid)
            print(UUID(characteristic.uuid).getCommonName())
            # val = characteristic.read()
            # if UUID(characteristic.uuid).getCommonName() == "Battery Level":
            #     print("battery level is " + str(ord(val)))
            # else:
            #     print(val)
            print(str(characteristic.properties) + "\n")
        print("========End of characters=========\n")
    print("--------------------------------------------------------")


if __name__ == '__main__':
    light = scan_devices()
    get_services(light.addr)
