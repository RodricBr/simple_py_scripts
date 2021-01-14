#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
from IPy import IP
from colorama import Fore, Style
import os


vm_ex = Fore.LIGHTRED_EX
vd_ex = Fore.LIGHTGREEN_EX
cy_ex = Fore.LIGHTCYAN_EX
a_ex = Fore.LIGHTYELLOW_EX
c_end = Style.RESET_ALL

os.system('clear') #Limpa o bash

print(f'''
{vm_ex}
github.com/RodricBr
 _____           _   _    _                _    
|  __ \         | | | |  | |              | |   
| |__) |__  _ __| |_| |__| | __ ___      _| | __
|  ___/ _ \| '__| __|  __  |/ _` \ \ /\ / / |/ /
| |  | (_) | |  | |_| |  | | (_| |\ V  V /|   < 
|_|   \___/|_|   \__|_|  |_|\__,_| \_/\_/ |_|\_\ {vd_ex}v2.0\n\t~#By: iHawkz/Rodric\n\tInspiration by: Aleksa Tamburkovski{c_end}
{c_end}
''')

def scan(target):
    converted_ip = check_ip(target)
    print(f'{cy_ex}[=] Scanning Ports 1 to 443 at ──› {c_end}' + str(target))
    for port in range(1, 444):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

set_timeout = float(input(f'{cy_ex}[+] Insert timeout number{c_end} {a_ex}(Float nº recommended: 0.5){c_end}{cy_ex}:\n>>> {c_end}'))
print(f'{vd_ex}[T] Timeout number set ──› {c_end}{str(set_timeout)}')

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(set_timeout) # Timeout rapido: 0.5, normal: 2, tedioso: 10
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print(f'{vd_ex}[+] Port {c_end}' + str(port) + f' {vd_ex}is open at ──› {c_end}' + str(banner.decode().strip('\n')))
        except:
            print(f'{vd_ex}[+] Port {c_end}' + str(port) + f' {vd_ex}is open{c_end}')
    except:
        pass
        # print(f'{vm_ex}[-] Port {c_end}' + str(port) + f' {vm_ex}is closed{c_end}') Mostrar portas abertas


targets = input(f'{cy_ex}[+] Insert the Target/s{c_end} {a_ex}(Split Targets using ","){c_end}{cy_ex}:\n>>> {c_end}')
if ',' in targets:
    for ip_addr in targets.split(','): # Dividindo(tirando a vírgula e dividindo as duas strings)
        scan(ip_addr.strip(' ')) # Tirando(tirando o espaço)
else:
    scan(targets)
