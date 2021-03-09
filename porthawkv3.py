#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Fazer um argumento na linha de comando. ex: -h  = help   -v  = verbose

try:
    from time import time, sleep
    import socket
    from IPy import IP
    from colorama import Fore, Style
    import os
    import traceback
    import argparse
    vm_ex, vd_ex, cy_ex, a_ex, c_end = Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTYELLOW_EX, Style.RESET_ALL
except KeyboardInterrupt:
    print(f'\n\t{a_ex}Keyboard Interrupt... Bye!{c_end}\n')
    raise SystemExit
except:
    print(f'{a_ex}[!]{c_end} {a_ex}Failed to import the dependencies...{c_end} ' +\
            f'{a_ex}Make sure to install all of the requirements{c_end} ' +\
            f'{a_ex}and try again.{c_end}')
    raise SystemExit

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='Increase output verbosity (Not implemented yet)', action='store_true')
parser.add_argument('-h', '--help', help='This is help command' )

os.system('clear') #Limpa o bash


print(f'''
{vm_ex}
github.com/RodricBr
 _____           _   _    _                _    
|  __ \         | | | |  | |              | |   
| |__) |__  _ __| |_| |__| | __ ___      _| | __
|  ___/ _ \| '__| __|  __  |/ _` \ \ /\ / / |/ /
| |  | (_) | |  | |_| |  | | (_| |\ V  V /|   < 
|_|   \___/|_|   \__|_|  |_|\__,_| \_/\_/ |_|\_\ {vd_ex}v3.0\n\t~#By: RodricBr\n\tInspiration by: Aleksa Tamburkovski{c_end}
{c_end}
''')

def scan(target):
    try:
        converted_ip = check_ip(target)
        # print(f'\n{a_ex}[!] Recommended port range:\n{c_end}1 ──› 1023 {a_ex}(May take a few minutes!){c_end}\n')
        p_start = int(input(f'{cy_ex}[P¹] Insert starting port range number:\n>>>{c_end} '))
        p_end = int(input(f'{cy_ex}[P²] Insert final port range number:\n>>>{c_end} '))
        print(f'{cy_ex}[=] Scanning Ports {p_start} to {p_end} at ──› {c_end}' + str(target))
    except KeyboardInterrupt:
        print(f'\n\t{a_ex}Keyboard Interrupt... Bye!{c_end}\n')

    for port in range(p_start, p_end + 1): #Mais comum: 80, 443, 21, 22, 110, 995, 143, 993, 25/26, 587, 3306, 2082, 2083, 2086, 3306
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

try:
    set_timeout = float(input(f'{cy_ex}[+] Insert timeout number{c_end} {a_ex}(Float nº recommended: 0.5){c_end}{cy_ex}:\n>>> {c_end}'))
    print(f'{vd_ex}[T] Timeout number set ──› {c_end}{str(set_timeout)}')
except KeyboardInterrupt:
    print(f'\n\t{a_ex}Keyboard Interrupt... Bye!{c_end}\n')
    exit()

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(set_timeout) # Timeout rapido: 0.5, normal: 2, tedioso: 10
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            try:
                print(f'{vd_ex}[+] Port {c_end}' + str(port) + f' {vd_ex}is open. Banner ──› {c_end}' + str(banner.decode().strip('\n'))) #Banner
            except KeyboardInterrupt:
                print(f'\n\t{a_ex}Keyboard Interrupt... Bye!{c_end}\n')
        except:
            try:
                print(f'{vd_ex}[+] Port {c_end}' + str(port) + f' {vd_ex}is open. Banner ──› {c_end}not found')
            except KeyboardInterrupt:
                print(f'\n\t{a_ex}Keyboard Interrupt... Bye!{c_end}\n')
    except:
        pass
        # print(f'{vm_ex}[-] Port {c_end}' + str(port) + f' {vm_ex}is closed{c_end}') Mostrar portas abertas

# port_range = int(input('[+] Set port range:\n>>> '))
try:
    targets = input(f'{cy_ex}[+] Insert the Target/s{c_end} {a_ex}(Split Targets using ","){c_end}{cy_ex}:\n>>> {c_end}')
except KeyboardInterrupt:
    print(f'\n\t{a_ex}Keyboard Interrupt... Bye!{c_end}\n')
    exit()

if ',' in targets:
    for ip_addr in targets.split(','): # Dividindo(tirando a vírgula e dividindo as duas strings)
        scan(ip_addr.strip(' ')) # Tirando(tirando o espaço)
else:
    scan(targets)
