import time
import requests

import colorama
from colorama import Fore, Style, init
init(autoreset=True)

# Define shorthand for Fore.BLUE
B = Fore.BLUE #{B}
G = Fore.GREEN #{G}
R = Fore.RED #{R}
M = Fore.MAGENTA #{M}
C = Fore.CYAN #{C}
W = Fore.WHITE #{W}
Y = Fore.YELLOW

             

print(F"""{C}██╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░╚███╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
░██╔██╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔╝╚██╗░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝{C}""")
time.sleep(1)
print(F"{G}Developed by:{G} {R}Cz3chC0d3X{R}")
print(F"{G}Version:{G} {R}1.0.0 Stable{R}")
time.sleep(0.4)
input(f" {G}[{G}{Y}+{Y}{G}]{G} {W}Press enter to start Xtool{W}")
time.sleep(0.6)
print(f"{G}..loading modules..{G}")
from main import mainopt
mainopt()
