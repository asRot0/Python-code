import requests
import sys
import time
import datetime


def line(line):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        time.sleep(0.05)
    print()


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def prYellow(skk): print("\033[93m {}\033[00m".format(skk))
def prCyan(skk): print("\033[96m {}\033[00m".format(skk))
def prGreen(skk): print("\033[92m {}\033[00m".format(skk))
def prRed(skk): print("\033[91m {}\033[00m".format(skk))


line_1 = '█████████████████████████████████████'
line_2 = '███████████ip-information████████████'
line(line_1)
line(line_2)
print(line_1)

prGreen(" SELECT NO 1 TO GET DETAILS ABOUT YOUR IP  ")
prGreen(" SELECT NO 2 TO TRACK AND GET DETAILS ABOUT IP  ")
prGreen(" SELECT ANY KEY TO EXIT THE SCRIPT  ")

now = datetime.datetime.now()
input_prompt = f'''┌─[ IP Tracker ]─[{now.strftime("%Y-%m-%d %H:%M:%S")}]─[```]\n└──╼ # '''

option = input(input_prompt)

while True:
    if option == '1':
        ip_address = get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        for key, value in response.items():
            prYellow(f'{key}: {value}')
        sys.exit()
    elif option == '2':
        prCyan("███enter your ip here███")
        ip = input(' █IP█ ')
        response = requests.get(f'https://ipapi.co/{ip}/json/').json()
        for key, value in response.items():
            prYellow(f'{key}: {value}')
        sys.exit()
    else:
        prRed("IP Tracker is going to sleep now. See you next time!")
        prRed("Sweet dreams! 💤")
        sys.exit()
