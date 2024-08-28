import requests
import itertools
import random
import string
from colorama import init, Fore, Style
from pyfiglet import Figlet


init()

def print_colored(message, color):
    print(f"{color}{message}{Style.RESET_ALL}\n", end='')


def pyfiglet():
    init()
    f = Figlet(font='small')
    oso = f.renderText('GitHub  @   Checker')
    print_colored(f"{oso}", Fore.LIGHTMAGENTA_EX)


def print_center(message, color):
    total_width = 80 
    padding = (total_width - len(message)) // 2
    print(f"{' ' * padding}{color}{message}{Style.RESET_ALL}")

    ####################################################################################################

def generate_usernames():
    letters = string.ascii_lowercase
   # numbers = string.digits
    #all_characters = letters + numbers
    while True:
        username = ''.join(random.choice(letters) for _ in range(4))
        yield username

def check_github_username(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 404:
        print(f"{Fore.GREEN}The username '{username}' is available.{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}The username '{username}' is not available.{Style.RESET_ALL}")
        return False

def main():
    pyfiglet()
    print_center(f"MADE BY @0so", Fore.LIGHTCYAN_EX)
    with open("available_usernames.log", "w") as f:
        for username in generate_usernames():
            if check_github_username(username):
                f.write(username + "\n")
                f.flush()  
if __name__ == "__main__":
    main()