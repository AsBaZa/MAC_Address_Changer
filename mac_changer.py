import subprocess


def change_mac(new_mac: str):
    subprocess.call('ifconfig eth0 down', shell=True)
    subprocess.call(f'ifconfig eth0 hw ether {new_mac}', shell=True)
    subprocess.call('ifconfig eth0 up', shell=True)
    subprocess.call('ifconfig', shell=True)


if __name__ == '__main__':
    change_mac(new_mac='00:11:22:33:44:66')
