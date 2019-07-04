import wake_up

mac = '98:90:96:C1:FE:CB'


def boot_computer(mac):
    try:
        print('正在向 ', mac, ' 发送魔法唤醒包！')
        mac = wake_up.format_mac(mac)
        send_data = wake_up.create_magic_packet(mac)

        wake_up.send_magic_packet(send_data)
        return '成功向' + mac + '发送唤醒包！'
    except ValueError:
        print('未收到传入的参数\n获取帮助：python3 main_boot_computer.py -h')


if __name__ == '__main__':
    boot_computer(mac)
