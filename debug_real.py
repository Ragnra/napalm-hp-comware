from napalm_hp_comware import hp_comware
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException
import getpass
import json
import sys

cmd_menu_items = ['get_facts', 'get_interfaces', 'get_interfaces_ip', 'get_lldp_neighbors', 'get_config']
main_menu_items = ['set username/password', 'change host']

usr = ''
pwd = ''


def print_menu(menu_state,dev):
    menu_items = []
    if menu_state == 'main':
        menu_items = main_menu_items.copy()
        if dev and dev.is_alive and 'device cmd' not in ','.join(menu_items):
            menu_items.append('Device Cmd Menu')

    elif menu_state == 'dev_cmd':
        menu_items = cmd_menu_items.copy()

    for item in menu_items:
        idx = menu_items.index(item)
        print('{}. {}'.format(idx, item))
    
    if menu_state == 'main':
        print('q. quit')

    else:
        print('b. back')

def exec_cmd(cmd_idx, dev):
    try:
        idx = int(cmd_idx)
    except ValueError:
        print('Not a valid command')

    if idx >= 0 and idx < len(cmd_menu_items):
        cmd = cmd_menu_items[idx]
        print(cmd)
        cmd_to_run = getattr(dev, cmd)
        
        if not cmd_to_run:
            print('Could not find command')
            return None

        result = cmd_to_run()
        return result
    else:
        print("invalid cmd")
        return None

def set_user_pass():
    usr = input('Enter Username: ')
    pwd = getpass.getpass('Enter Password: ')
    return (usr,pwd)

def set_host(usr,pwd):
    host = input('Enter host IP:')
    dev = hp_comware.HpComwareDriver(host,usr,pwd,timeout=10)
    print('opening connection')
    try:
        dev.open()
    except NetMikoAuthenticationException:
        print('Authentication Failure')
    except NetMikoTimeoutException:
        print('Host timeout')

    return (host, dev)

def print_header(host, usr, dev):
    if not dev:
        conn = 'False'
    elif dev.is_alive:
        conn = 'True'
    else:
        conn = 'False'
    print('Host: {}@{}\t\tIs connected: {}'.format(usr,host, conn))
    print('--------------------------------------------------')

def main():
    #ipaddress = dev.get_interfaces_ip()
    menu_state = 'main'
    cmd = None
    dev = None
    usr = None
    pwd = None
    host = ''

    while cmd != 'q':
        print_header(host ,usr, dev)
        print_menu(menu_state, dev)
        cmd = input('Select Option: ').lower()
        if cmd == 'q' and menu_state == 'main':
            pass
        elif cmd == 'b' and menu_state != 'main':
            menu_state = 'main'
        else:
            if menu_state == 'dev_cmd':
                result = exec_cmd(cmd, dev)
                if result:
                    print(json.dumps(result,indent=4, sort_keys=True))
            elif menu_state == 'main':
                if cmd == '0':
                    usr, pwd = set_user_pass()
                elif cmd == '1':
                    if usr and pwd:
                        host, dev = set_host(usr,pwd)
                elif cmd == '2':
                    menu_state = 'dev_cmd'

        
    if dev:
        dev.close()

if __name__ == "__main__":
    main()