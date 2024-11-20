from colorama import Fore as F
import os
from halo import Halo
import json
import cfonts

os.system('clear')

print(f"""{F.CYAN}
                                                                ⣠⣤⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⣰⣿⠁⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣶⣶⣾⣿⣶⠀⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀⠀⠀⣾⣿⣤⣤⣤⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣾⡏⠀⠀⠀⠀⠉⢉⣿⠟⠁⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠙⠿⠿⣿⡿⠀⠀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣤⣤⣿⠃⣠⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⣿⢧⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠋⠀⠀
""")
logo = cfonts.render(
    text="flash-X",
    colors=[
        "white", # 
        "cyan", #
    ],
    align="center"
)
print(logo)

with open("info.json", "r") as f:
    data = json.load(f)
    version = data["version"]
    auther = data["auther"]

print(F.WHITE+'-'*60)
print(f"""
Version : {F.CYAN}{version} {F.RESET}( {F.CYAN}2024 {F.WHITE}- {F.CYAN}11 {F.WHITE}- {F.CYAN}21 {F.RESET}).
Auther  : {F.CYAN}{auther}{F.RESET}.

""")
print(F.WHITE+'-'*60)
def listMethod():

    print(f'''
{F.CYAN}1- {F.RESET}HTTP-PROXIES.
{F.CYAN}2- {F.RESET}UDP {F.CYAN}( SOON ){F.RESET}.
{F.CYAN}3- {F.RESET}SLOWLORIS {F.CYAN} ( SOON ){F.RESET}.
''')
    
    try:

        choiceMethod = int(input(f'''{F.WHITE}┌─({F.CYAN}flash-X{F.WHITE})─({F.YELLOW}~ Method{F.WHITE})
└──{F.YELLOW}~# {F.CYAN}'''))
    except ValueError:
        print(f"{F.RED} ( !!! ) Error !")
    

    if choiceMethod == 1:
        os.system('cmd /k "python3 tools/http-flood.py"' if os.name == 'nt' else 'python3 tools/http-flood.py')
    elif choiceMethod ==2:
        print('soon')
        #os.system('cmd /k "python3 tools/tsd-udp.py"' if os.name == 'nt' else 'python3 tools/tsd-udp.py')
    elif choiceMethod == 3:
        print('soon')
        #os.system('cmd /k "python3 tools/tsd-dns.py"' if os.name == 'nt' else 'python3 tools/tsd-dns.py')
    elif choiceMethod == 4:
        print('soon')
        #os.system('cmd /k "python3 tools/tsd-slowloris.py"' if os.name == 'nt' else 'python3 tools/tsd-slowloris.py')
    else:
        print(f'{F.RED}( !!! ) {F.RESET}Error! Choice {F.CYAN}1{F.RESET} or {F.CYAN}2{F.RESET} or {F.CYAN}3{F.RESET} just!!')
        exit()

listMethod()
