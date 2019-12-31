from bluepy.btle import Scanner, UUID, Peripheral
import struct

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
        print("  0x" + format(characteristic.getHandle(), '02X') + "   " + str(
            characteristic.uuid) + " " + characteristic.propertiesToString())
        if characteristic.supportsRead():
            val = characteristic.read()
            print(val)
        if str(characteristic.uuid) == "0000fff1-0000-1000-8000-00805f9b34fb":
            characteristic.write(struct.pack('<B', 3))
    print("--------------------------------------------------------")


if __name__ == '__main__':
    light = scan_devices()
    get_services(light)
