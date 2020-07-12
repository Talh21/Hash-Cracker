from utilities import *


try:
    PASSWORD_LIST_DEFAULT = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/'
                                        'master/Passwords/Common-Credentials/10k-most-common.txt').read(), "utf-8")
# If you want to use the 10 million database that in the README.md file, just change the url here

except urllib.error.URLError as err:
    print(f"Error has occurred. Please check your internet connection."
          f"\ninfo about the problem: {err}")
    quit()


def intro():
    init()
    print(f'''{Fore.RED}  
                    _         ___                   _                
  /\  /\ __ _  ___ | |__     / __\_ __  __ _   ___ | | __ ___  _ __  
 / /_/ // _` |/ __|| '_ \   / /  | '__|/ _` | / __|| |/ // _ \| '__| 
/ __  /| (_| |\__ \| | | | / /___| |  | (_| || (__ |   <|  __/| |    
\/ /_/  \__,_||___/|_| |_| \____/|_|   \__,_| \___||_|\_\\___||_|    

                                               {Style.RESET_ALL}[@Made by Tal Hasson]\n\n''')


def user_prompt():
    print('''Choose hash type from the following options:
1.MD5
2.SHA-1
3.SHA-256
4.SHA-384
5.SHA-512''')

    hash_option = input("\n[*] Choose the hash type: ").lower()
    while check_if_option_is_valid(hash_option) is False:
        hash_option = input(f"The option: '{hash_option}' is not in the list of the hash types above."
                            "\nTry again or press 'Q' to Exit: ")
    if hash_option == "q":
        print("----------------------------------")
        print("\nThank you for using this program (:\nHope to see you soon!")
        quit()

    return hash_option


def is_user_wants_to_load_passwords():
    user_choice = input("\n[~] Do you want to load passwords from a file? [YES/NO]\nType your answer: ").lower()
    while check_if_yes_or_no(user_choice) is False:
        user_choice = input("[-] You can choose only [YES/NO]\nTry again: ")
    if user_choice == "q":
        print("----------------------------------")
        print("\nThank you for using this program (:\nHope to see you soon!")
        quit()

    return user_choice


def md5():
    if user_answer == "no":
        for guess in PASSWORD_LIST_DEFAULT.split("\n"):
            password_converted_to_hash = hashlib.md5(bytes(f"{guess}", "utf-8")).hexdigest()
            if password_converted_to_hash == hash_pass:
                print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {guess}")
                quit()
        print("\r[-] Sorry, Could not find the password in the database.")
        quit()

    pass_list = is_file_empty()
    for password in pass_list:
        password_converted_to_hash = hashlib.md5(bytes(f"{password}", "utf-8")).hexdigest()
        if password_converted_to_hash == hash_pass:
            print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {password}")
            quit()
    print("\r[-] Sorry, Could not find the password in the database.")
    quit()


def sha1():
    if user_answer == "no":
        for guess in PASSWORD_LIST_DEFAULT.split("\n"):
            password_converted_to_hash = hashlib.sha1(bytes(f"{guess}", "utf-8")).hexdigest()
            if password_converted_to_hash == hash_pass:
                print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {guess}")
                quit()
        print("\r[-] Sorry, Could not find the password in the database.")
        quit()

    pass_list = is_file_empty()
    for password in pass_list:
        password_converted_to_hash = hashlib.sha1(bytes(f"{password}", "utf-8")).hexdigest()
        if password_converted_to_hash == hash_pass:
            print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {password}")
            quit()
    print("\r[-] Sorry, Could not find the password in the database.")
    quit()


def sha256():
    if user_answer == "no":
        for guess in PASSWORD_LIST_DEFAULT.split("\n"):
            password_converted_to_hash = hashlib.sha256(bytes(f"{guess}", "utf-8")).hexdigest()
            if password_converted_to_hash == hash_pass:
                print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {guess}")
                quit()
        print("\r[-] Sorry, Could not find the password in the database.")
        quit()

    pass_list = is_file_empty()
    for password in pass_list:
        password_converted_to_hash = hashlib.sha256(bytes(f"{password}", "utf-8")).hexdigest()
        if password_converted_to_hash == hash_pass:
            print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {password}")
            quit()
    print("\r[-] Sorry, Could not find the password in the database.")
    quit()


def sha384():
    if user_answer == "no":
        for guess in PASSWORD_LIST_DEFAULT.split("\n"):
            password_converted_to_hash = hashlib.sha384(bytes(f"{guess}", "utf-8")).hexdigest()
            if password_converted_to_hash == hash_pass:
                print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {guess}")
                quit()
        print("\r[-] Sorry, Could not find the password in the database.")
        quit()

    pass_list = is_file_empty()
    for password in pass_list:
        password_converted_to_hash = hashlib.sha384(bytes(f"{password}", "utf-8")).hexdigest()
        if password_converted_to_hash == hash_pass:
            print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {password}")
            quit()
    print("\r[-] Sorry, Could not find the password in the database.")
    quit()


def sha512():
    if user_answer == "no":
        for guess in PASSWORD_LIST_DEFAULT.split("\n"):
            password_converted_to_hash = hashlib.sha512(bytes(f"{guess}", "utf-8")).hexdigest()
            if password_converted_to_hash == hash_pass:
                print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {guess}")
                quit()
        print("\r[-] Sorry, Could not find the password in the database.")
        quit()

    pass_list = is_file_empty()
    for password in pass_list:
        password_converted_to_hash = hashlib.sha512(bytes(f"{password}", "utf-8")).hexdigest()
        if password_converted_to_hash == hash_pass:
            print(f"{Fore.GREEN}Password is:{Style.RESET_ALL} {password}")
            quit()
    print("\r[-] Sorry, Could not find the password in the database.")
    quit()


if __name__ == '__main__':
    intro()
    time.sleep(2)
    hash_type = user_prompt()
    user_answer = is_user_wants_to_load_passwords()
    hash_pass = input("\n[*] Please enter the hash: ")
    while hash_pass.lower() != "q":
        if hash_type == "1":
            md5()
        elif hash_type == "2":
            sha1()
        elif hash_type == "3":
            sha256()
        elif hash_type == "4":
            sha384()
        elif hash_type == "5":
            sha512()

    print("----------------------------------")
    print("\nThank you for using this program (:\nHope to see you soon!")
    quit()
