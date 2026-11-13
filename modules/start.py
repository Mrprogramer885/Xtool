import time
import requests
from colorama import Fore, init

init(autoreset=True)

C = Fore.CYAN
G = Fore.GREEN
R = Fore.RED
Y = Fore.YELLOW
W = Fore.WHITE

def netchk():
    try:
        response = requests.get("https://www.google.com", timeout=3)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False

def get_dev_msg():
    url = "https://raw.githubusercontent.com/Mrprogramer885/source/refs/heads/main/devmsg.txt"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print(response.text.strip())
    except requests.RequestException:
        print(f"{Y}[!] Could not fetch developer message.{Y}")

def start():
    get_dev_msg()
    print(f"""{C}
██╗░░██╗████████╗░█████╗░░█████╗░██╗░░░░░
╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░╚███╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░
░██╔██╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░
██╔╝╚██╗░░░██║░░░╚█████╔╝╚█████╔╝███████╗
╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝{C}""")
    time.sleep(1)
    print(f"{G}Developed by:{G} {R}theczechceo{R}")
    print(f"{G}Version:{G} {R}1.2.5 Beta{R}")
    time.sleep(0.4)
    input(f" {G}[+]{G} {W}Press enter to start Xtool{W}")
    time.sleep(0.6)
    print(f"{G}..loading modules..{G}")
    
    from main import mainopt
    mainopt()

if __name__ == "__main__":
    if netchk():
        print(f"{G}Internet is available.{G}")
        start()
    else:
        print(f"{R}No internet connection.{R}")
        time.sleep(0.9)
        print(f"{Y}Xtool cannot work without valid internet connection. Make sure you are connected to internet or use mobile data.{Y}")
        exit(1)