from colorama import Style, Fore, init
from urllib.request import urlopen
import urllib.error
import hashlib
import time


PASSWORDS_FILE = 'passwords.txt'


def check_if_option_is_valid(chosen_option):
    if chosen_option != "1" and chosen_option != "2" and \
            chosen_option != "3" and chosen_option != "4" and chosen_option != "5" and chosen_option != "q":
        return False


def check_if_yes_or_no(user_answer):
    if user_answer.lower() == "yes" or user_answer.lower() == "no" or user_answer == "q":
        return True
    else:
        return False


def is_file_empty():
    passwords = []
    try:
        with open(PASSWORDS_FILE, 'r') as pass_list:
            for line in pass_list:
                line = line.strip()
                if line:
                    passwords.append(line)
            if len(passwords) == 0:
                print(f"\n[-] {Fore.RED}Pay attention!{Style.RESET_ALL} your file is empty...\nQuiting!!!")
                quit()
    except FileNotFoundError:
        print(f"\n[-] {Fore.RED}Error:{Style.RESET_ALL} File was`nt found... Quitting!!! ")
        quit()
    return passwords
