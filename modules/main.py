import time
import os
import colorama
import iposint
import requests
import json
from colorama import Fore, Style, init
init(autoreset=True)

# Define shorthand for Fore.BLUE
B = Fore.BLUE #{B}
G = Fore.GREEN #{G}
R = Fore.RED #{R}
M = Fore.MAGENTA #{M}
C = Fore.CYAN #{C}
W = Fore.WHITE #{W}
Y = Fore.YELLOW #{Y}


def IP_Track():
    ip = input(f"{W}\n Enter IP target : {G}") #INPUT IP ADDRESS
    print()
    print(f' {W}============= {G}SHOW INFORMATION IP ADDRESS {W}=============')
    req_api = requests.get(f"http://ipwho.is/{ip}") #API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    print(f"{W}\n IP target       :{G}", ip)
    print(f"{W} Type IP         :{G}", ip_data["type"])
    print(f"{W} Country         :{G}", ip_data["country"])
    print(f"{W} Country Code    :{G}", ip_data["country_code"])
    print(f"{W} City            :{G}", ip_data["city"])
    print(f"{W} Continent       :{G}", ip_data["continent"])
    print(f"{W} Continent Code  :{G}", ip_data["continent_code"])
    print(f"{W} Region          :{G}", ip_data["region"])
    print(f"{W} Region Code     :{G}", ip_data["region_code"])
    print(f"{W} Latitude        :{G}", ip_data["latitude"])
    print(f"{W} Longitude       :{G}", ip_data["longitude"])
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{W} Maps            :{G}",f"https://www.google.com/maps/@{lat},{lon},8z")
    print(f"{W} EU              :{G}", ip_data["is_eu"])
    print(f"{W} Postal          :{G}", ip_data["postal"])
    print(f"{W} Calling Code    :{G}", ip_data["calling_code"])
    print(f"{W} Capital         :{G}", ip_data["capital"])
    print(f"{W} Borders         :{G}", ip_data["borders"])
    print(f"{W} Country Flag    :{G}", ip_data["flag"]["emoji"])
    print(f"{W} ASN             :{G}", ip_data["connection"]["asn"])
    print(f"{W} ORG             :{G}", ip_data["connection"]["org"])
    print(f"{W} ISP             :{G}", ip_data["connection"]["isp"])
    print(f"{W} Domain          :{G}", ip_data["connection"]["domain"])
    print(f"{W} ID              :{G}", ip_data["timezone"]["id"])
    print(f"{W} ABBR            :{G}", ip_data["timezone"]["abbr"])
    print(f"{W} DST             :{G}", ip_data["timezone"]["is_dst"])
    print(f"{W} Offset          :{G}", ip_data["timezone"]["offset"])
    print(f"{W} UTC             :{G}", ip_data["timezone"]["utc"])
    print(f"{W} Current Time    :{G}", ip_data["timezone"]["current_time"])
    input("Press enter to continue")
    from main import mainopt
    mainopt()


def mainopt():
    print(f"""
      {Y}--------------------------------------
      {G}[1]: {Y}IP search{Y}
      {G}[2]: {Y}Phone Search{Y}
      {G}[3]: {Y}Instagram search{Y} {R}(WIP)
      {G}[4]: {Y}Google dorks{Y} {R}(WIP)
      {G}[5]: {Y}Email search{Y} {R}(WIP)
      {G}[6]: {Y}username osint{Y} {R}(WIP)
      {G}[7]: {Y}Social media search{Y} {R}(WIP)
      {G}[8]: {Y}Github search{Y} {R}(WIP)
      {G}[9]: {Y}Port scan{Y} {R}(TCP)
      {G}[10]: {Y}Check for updates{Y} {R}(WIP)
      {G}[11]: {Y}Changelog{Y} {R}(WIP)
      {G}[12]: {Y}Delete Cache{Y} {R}(WIP)
      {G}[13]: {Y}Delete all Xtool data{Y} {R}(WIP)
      {G}[14]: {Y}Uninstall{Y} {R}(WIP)
      
      {R}[99]: Exit Xtool{R}
      {Y}---------------------------------------- 
      """)
    selvar = input(f"{G}[{G}{C}*{C}{G}]{G}{W}Select option and press enter >> {W}")
    
    if selvar == '1':
        from main import IP_Track
        IP_Track()
    