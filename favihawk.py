try:
    import mmh3
    import requests
    import codecs
    from colorama import Fore, Style

    c_end, c_verd, c_cyan, c_ama = Style.RESET_ALL, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTYELLOW_EX
except KeyboardInterrupt:
    print(f'\n\t{a_ex}Keyboard Interrupt... Bye!{c_end}\n')
    raise SystemExit
except:
    print(f'{a_ex}[!]{c_end} {a_ex}Failed to import the dependencies...{c_end} ' +\
            f'{a_ex}Make sure to install all of the requirements{c_end} ' +\
            f'{a_ex}and try again.{c_end}')
    raise SystemExit

print(f'''{c_cyan}
\t ________________________________
\t|         -> FavHawk <-          |
\t| Web-Recon Favicon Hashing Tool |
\t|       github.com/RodricBr      |
\t|________________________________|
{c_end}''')

#Shodan Filter ex: http.favicon.hash:'hash number'
response = requests.get(input(f'{c_verd}[+] Insert Favicon URL{c_ama}(Ex: https://exemple.com/img/favicon.ico){c_verd}:\n>>>{c_end} '))
favicon = codecs.encode(response.content, 'base64')
hash = mmh3.hash(favicon)
print(f'{c_verd}[+] Favicon Hash:{c_end} {hash}')
