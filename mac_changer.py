import subprocess


def change_mac(interface: str, new_mac: str):
    print(f'[+] Changing MAC address for {interface} to {new_mac}')
    subprocess.call(f'ifconfig {interface} down', shell=True)
    subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
    subprocess.call(f'ifconfig {interface} up', shell=True)
    subprocess.call('ifconfig', shell=True)


if __name__ == '__main__':
    change_mac(interface='eth0', new_mac='00:11:22:33:44:66')
