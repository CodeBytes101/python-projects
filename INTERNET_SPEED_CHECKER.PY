# Download the speedtest-cli module with command "pip install speedtest-cli"
# Similarly colorama module with 'pip install colorama' 

import speedtest
import colorama
import sys
from time import sleep

# type function fro typing effect

def type(words:str):
    for char in words:
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

while True:
    colorama.init(autoreset=True)

    #intializing speedtest module

    test = speedtest.Speedtest()

    type('Getting Servers...')
    test.get_servers()

    type('Getting Best Servers...')
    best = test.get_best_server()

    # Fetching host and address of the host

    host =  best['sponsor']
    host = (colorama.Fore.GREEN + f'{host}')
    country  = best['country']
    country = (colorama.Fore.GREEN + f'{country}')
    city = best['name']
    city = (colorama.Fore.GREEN + f"{city}")

    type('[*] Server Found')
    print(f'ISP: {host}, {city}, {country}')
    print()

    type('calculating Download Speed....')

    # Download Speed !
    down_speed = test.download()

    print()
    type(f'Download Speed: {down_speed / 1024 /1024: .2f} mb/ps OR {down_speed / 1024 /1024 /8: .2f} MB/ps')
    print()

    type('calculating Upload Speed....')

    #Upload Speed !
    up_speed =  test.upload()
    print()
    type(f'Upload Speed: {up_speed /1024 /1024: .2f} mb/ps OR {up_speed /1024 /1024 /8: .2f} MB/ps')
    print()

    choice = input('Do you want to Try again [Y/N]: ')
    if choice.lower() == 'y':
        continue
    elif choice.lower() == 'n':
        break
    else:
        type('[*] Invalid Input !')
        break
