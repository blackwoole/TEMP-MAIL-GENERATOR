from colorama import Fore; import datetime
def format_current_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    return formatted_time
def Sprint(content: str):
    print(f"{Fore.LIGHTBLACK_EX}<{format_current_time()}>   {Fore.LIGHTGREEN_EX}<HIT>   {Fore.LIGHTBLACK_EX}{content}{Fore.RESET}")
def Eprint(content: str):
    print(f"{Fore.LIGHTBLACK_EX}<{format_current_time()}>   {Fore.LIGHTRED_EX}<ERR>   {Fore.LIGHTBLACK_EX}{content}{Fore.RESET}")
def Wprint(content: str):
    print(f"{Fore.LIGHTBLACK_EX}<{format_current_time()}>   {Fore.LIGHTYELLOW_EX}<WRN>   {Fore.LIGHTBLACK_EX}{content}{Fore.RESET}")
def Cprint(color, tag, content: str):
    print(f"{Fore.LIGHTBLACK_EX}<{format_current_time()}>   {color}<{tag}>   {Fore.LIGHTBLACK_EX}{content}{Fore.RESET}")