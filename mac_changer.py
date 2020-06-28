#!/usr/bin/env python
import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')

    options, arguments = parser.parse_args()

    if not options.interface:
        parser.error('[-] Please specify an interface, use --help for more info\n')
    elif not options.new_mac:
        parser.error('[-] Please specify a new mac, use --help for more info\n')

    return options


def change_mac(interface: str, new_mac: str):
    print(f'[+] Changing MAC address for {interface} to {new_mac}')
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


def get_current_mac(interface: str):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    mac_address_search_result = re.search(pattern=r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',
                                          string=ifconfig_result.decode('utf-8'))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read the MAC address.')


if __name__ == '__main__':
    OPTIONS = get_arguments()

    current_mac = get_current_mac(interface=OPTIONS.interface)
    print(f'Current MAC: {current_mac}')
    change_mac(interface=OPTIONS.interface, new_mac=OPTIONS.new_mac)
    current_mac = get_current_mac(interface=OPTIONS.interface)

    if current_mac == OPTIONS.new_mac:
        print(f'[+] MAC address was successfully changed to {current_mac}')
    else:
        print('[-] MAC address did not get changed.')
