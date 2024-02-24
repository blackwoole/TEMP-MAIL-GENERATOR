import tls_client;from utils.console import *;import os;s = tls_client.Session(client_identifier="chrome_112",random_tls_extension_order=True); import datetime;os.system('cls')
def format_current_time():
    current_time = datetime.datetime.now();formatted_time = current_time.strftime("%H:%M:%S");return formatted_time
def GenerateMail():
  respAPI = s.get('https://api.tempmail.lol/generate');email=respAPI.json()["address"];token=respAPI.json()["token"];return ''.join(str(email) + ':' + str(token))
def mailInf(token):
    try:APIAuth = s.get(f'https://api.tempmail.lol/auth/{token}').json();subject = APIAuth["email"][0]["subject"];return subject
    except IndexError:return 'No mails found.'
def run():
  xa = input(f"{Fore.LIGHTBLACK_EX}<{format_current_time()}>   {Fore.LIGHTBLUE_EX}<INP>   {Fore.LIGHTBLACK_EX}REFRESH MAILS [Y/N] : {Fore.RESET}");return xa
x = input(f"{Fore.LIGHTBLACK_EX}<{format_current_time()}>   {Fore.LIGHTBLUE_EX}<INP>   {Fore.LIGHTBLACK_EX}PRESS 'Y' TO GENERATE A TEMP MAIL : {Fore.RESET}")
if str(x).lower() == 'y':
  initial = GenerateMail(); splittedmail, splittedtoken = initial.split(':');Sprint(f"GENERATED TEMP MAIL -> {splittedmail}, TOKEN: {splittedtoken[:16]}..")
  while True:
    rocket = run()
    if str(rocket).lower() == 'y':
      mails=mailInf(splittedtoken)
      if mails == 'No mails found.':Wprint("NO MAILS FOUND.")
      else:Sprint(f"SCRAPED MAIL ->\n     SUBJECT : {mailInf(splittedtoken)}")
    else:exit()
else:exit()