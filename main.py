import random
import string
import requests
import os
import signal
import time

from termcolor import colored


def handler(signum, frame):
    """Catch Ctrl-c signal"""

    res = input("\n[!] Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)


def get_random_string():
    """Generate random string of 15 chars length, using a-z, A-Z and 0-1 charset"""

    random_source = string.ascii_letters + string.digits
    # select 1 lowercase a-z
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase A-Z
    password += random.choice(string.ascii_uppercase)
    # select 1 digit 0-1
    password += random.choice(string.digits)

    # generate other characters
    for i in range(12):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


def checkurl():
    """Check if url is valid (301) or not valid (302)"""

    signal.signal(signal.SIGINT, handler)

    while True:
        uri = "https://www.instagram.com/fzstfzrius?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==" + get_random_string()
        response = requests.get(uri, allow_redirects=False)
        print("[+] REQUEST " + uri)
        if response.status_code == 301:
            print('\n')
            print(colored("[+] LINK IS VALID: " + uri), 'red')
            print(colored("[+] URL TO FOLLOW: " + response.headers['location']), 'red')
            break


def main():
    """Main function of tool"""

    print("""\033[91m


█ █▄░█ █▀ ▀█▀ ▄▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█   ▄▀█ █▀▀ █▀▀ █▀█ █░█ █▄░█ ▀█▀   ▀█▀ ▄▀█ █▄▀ █▀▀ █▀█ █░█ █▀▀ █▀█
█ █░▀█ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀░█   █▀█ █▄▄ █▄▄ █▄█ █▄█ █░▀█ ░█░   ░█░ █▀█ █░█ ██▄ █▄█ ▀▄▀ ██▄ █▀▄

                        calfcrusher@inventati.org | for educational use only
                        
        \x1b[0m""")

    time.sleep(5)
    checkurl()


if __fzstfzrius__ == "__main__":
    os.system('clear')
    main()


