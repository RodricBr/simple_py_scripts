#!/usr/bin/python3
# -*- coding: utf-8 -*-
try:
    import urllib.request #Faz request para um URL
    import io
    import sys
    from colorama import Fore, Style
    vd, cy, c_end, rd, a_ex, rx = Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Style.RESET_ALL, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX
except KeyboardInterrupt:
    print(f'\n\t{a_ex}Keyboard Interrupt... Bye!{c_end}\n')
    raise SystemExit
except:
    print(f'{a_ex}[!]{c_end} {a_ex}Failed to import the dependencies...{c_end} ' +\
            f'{a_ex}Make sure to install all of the requirements{c_end} ' +\
            f'{a_ex}and try again.{c_end}')
    raise SystemExit

print(f'''{rx}
\t ______________________________
\t|   Vulnerable repo. scanner   |
\t|            v1.0              |
\t| Made by: github.com/RodricBr |
\t|______________________________|
{c_end}{cy}
\tNote:\n\tThis is a project program\n\tand will be upgraded in the future                 
\t[!] Current erros to be later solved:
\t> .git repo not showing in most sites
\t> robots.txt getting blocked by most WAFs
{c_end}''')


def robots_txt(url):
    try:
        if url.endswith('/'): #Se termina com /, usa o URL
            path = url
        else:
            path = url + '/' #Senão o / é adicionado ao final da URL
        try:
            request = urllib.request.urlopen(path + 'robots.txt/', data=None)
        except urllib.error.HTTPError as erro:
            print(f'{rd}HTTPError:{c_end} {erro.code}\n{rd}The URL requested is unavailable or was blocked by a WAF!{c_end}')
            exit()
        except urllib.error.URLError as erro:
            print(f'{rd}URLError:{c_end} {erro.reason}\n{rd}Certificate does not match the website requested!{c_end}')
            exit()
        data = io.TextIOWrapper(request, encoding='utf-8')
        return data.read()
    except TypeError:
        print(f'{rd}"robots.txt" directory was not found or is not available{c_end}')


def dot_git(url):
    try:
        if url.endswith('/'):
            path = url
        else:
            path = url + '/'
        try:
            request = urllib.request.urlopen(open + '.git/', data=None)
        except urllib.error.HTTPError as erro:
            print(f'{rd}HTTPError:{c_end} {erro.code}\n{rd}The URL requested is unavailable or was blocked by a WAF!{c_end}')
            exit()
        except urllib.error.URLError as erro:
            print(f'{rd}URLError:{c_end} {erro.reason}\n{rd}Certificate does not match for the website requested!{c_end}')
            exit()
        data = io.TextIOWrapper(request, encoding='utf-8')
        return data.read()
    except TypeError:
        print(f'{rd}No ".git" directory was found or is available{c_end}')

domain = str(input(f'{vd}[+] Type the URL:\n>>>{c_end} '))

try:
    is_https = str(input(f'{vd}[+] Type if its "HTTP" or "HTTPS":\n>>>{c_end} ')).lower().strip(' ')
except:
    if is_https != 'http' and 'https':
        print(f'\n\t{rd}You typed something wrong or the site is unavailable!\n\tQuitting...{c_end}')
        quit()
    else:
        pass

print(f'{cy}[=] Scanning robots.txt at ──›{c_end} http(s)://{domain}')
print(f'{cy}[=] Scanning .git at       ──›{c_end} http(s)://{domain}\n')
print('=' * 35 + '>>> robots.txt\n')
print(robots_txt(is_https + '://' + domain))
print('=' * 35 + '>>> .git\n')
print(dot_git(is_https + '://' + domain))

# google dorking for .git repo: site:.gov.br inurl:.git
# PROBLEMA!!
# O .git NÃO ESTÁ SENDO DIGITADO NA URL
# SÓ SEI QUE NESSE SITE: www.fetems.org.br/.git/ QUE É UM EXEMPLO DE SITE
# QUE TEM UM .git VAZADO, NÃO ESTÁ PRINTANDO E DETECTANDO NADA!
