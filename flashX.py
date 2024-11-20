from colorama import Fore as F
import os
from halo import Halo
import json
import cfonts

#
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

# 
logo = cfonts.render(
    text="flash-X",
    colors=["white", "cyan"],
    align="center"
)
print(logo)

# json ...
with open("info.json", "r") as f:
    data = json.load(f)
    version = data["version"]
    author = data["auther"]

# ...
print(F.RESET + '-' * 60)
print(f"""
Version : {F.CYAN}{version} {F.RESET}( {F.CYAN}2024 {F.WHITE}- {F.CYAN}11 {F.WHITE}- {F.CYAN}20 {F.RESET}).
Author  : {F.CYAN}{author}{F.RESET}.
""")
print(F.RESET + '-' * 60)

# 
def listMethod():
    print(f'''
{F.CYAN}1- {F.RESET}HTTP-PROXIES.
{F.CYAN}2- {F.RESET}UDP {F.CYAN}( SOON ){F.RESET}.
{F.CYAN}3- {F.RESET}SLOWLORIS {F.CYAN}( SOON ){F.RESET}.
''')
    try:
        choiceMethod = int(input(f'''{F.RESET}┌─({F.CYAN}flash-X{F.RESET})─({F.YELLOW}~ Method{F.RESET})
└──{F.YELLOW}~# {F.CYAN}'''))
    except ValueError:
        print(f"{F.RED}( !!! ) Error! Invalid input.")
        return

    if choiceMethod == 1:
        os.system('cmd /k "python3 tools/http-flood.py"' if os.name == 'nt' else 'python3 tools/http-flood.py')
    elif choiceMethod == 2:
        print('SOON: UDP implementation is in progress.')
    elif choiceMethod == 3:
        print('SOON: SLOWLORIS implementation is in progress.')
    else:
        print(f'{F.RED}( !!! ) {F.RESET}Error! Choose {F.CYAN}1{F.RESET}, {F.CYAN}2{F.RESET}, or {F.CYAN}3{F.RESET} only.')
        exit()

# استدعاء الوظيفة
listMethod()
