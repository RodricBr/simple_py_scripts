#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket, threading #Importando socket e threading
from colorama import Fore, Style #Importando cores e style
from IPy import IP
import os

vm_ex = Fore.LIGHTRED_EX
vd_ex = Fore.LIGHTGREEN_EX
cy_ex = Fore.LIGHTCYAN_EX
az_ex = Fore.LIGHTBLUE_EX
am_ex = Fore.LIGHTYELLOW_EX
c_end = Style.RESET_ALL

os.system('clear') #Limpa o bash

#AF_INET serve para especificar o tipo de conexão, no caso IPV4 do dominio ou simplesmente o nome de dominio
#SOCK_STREAM serve para especificar o tipo de conexão, no caso TCP, havendo uma handshake
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3) #Setando o timeout

print(f'''
{vm_ex}
 _____           _   _    _                _    
|  __ \         | | | |  | |              | |   
| |__) |__  _ __| |_| |__| | __ ___      _| | __
|  ___/ _ \| '__| __|  __  |/ _` \ \ /\ / / |/ /
| |  | (_) | |  | |_| |  | | (_| |\ V  V /|   < 
|_|   \___/|_|   \__|_|  |_|\__,_| \_/\_/ |_|\_\ {vd_ex}v1.2\n\t~#Por: iHawkz aka.: Hawk{c_end}
{c_end}
''')


dominio = input(f'{vd_ex}[+]{c_end} {cy_ex}Digite o IP ou Dominio:\n>>>{c_end} ')

porta = int(input(f'{vd_ex}[+]{c_end} {cy_ex}Digite a Porta:\n>>>{c_end} '))
set_timeout = sock.settimeout(float(input(f'{vd_ex}[+]{c_end} {cy_ex}Digite o Timeout:\n>>> {c_end}')))

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)
ip_convertido = check_ip(dominio)

def scanner(porta):
    try:
        sock.connect((dominio, porta))
        print(f'{vd_ex}[+]{c_end} {cy_ex}A porta ' + str(porta) + f' esta Aberta/Disponivel.{c_end}') 
    except socket.error as socket_error:     
        print(f'{vm_ex}[-]{c_end} {am_ex}A porta ' + str(porta) + f' esta Fechada/Indisponivel.{c_end}')
        print(f'\n\r{am_ex}[x]{c_end} Error: ', socket_error)
scanner(porta)

print(f'{am_ex}[x]{c_end} Finalizando...')
