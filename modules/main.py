import time
import os
import colorama
import requests
import json
import phonenumbers
import urllib3
import namesearch
from namesearch import namesearch
from phonenumbers import geocoder, carrier, timezone
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

def phonesearch():
    try:

        User_phone = input(f"\n {W}Enter phone number target {G}Ex [+6281xxxxxxxxx] {W}: {G}")  # INPUT NUMBER PHONE
        default_region = "ID"  # DEFAULT NEGARA INDONESIA

        parsed_number = phonenumbers.parse(User_phone, default_region)  # VARIABLE PHONENUMBERS
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number = phonenumbers.is_valid_number(parsed_number)
        is_possible_number = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                     with_formatting=True)
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n {W}========== {G}SHOW INFORMATION PHONE NUMBERS {W}==========")
        print(f"\n {W}Location             :{G} {location}")
        print(f" {W}Region Code          :{G} {region_code}")
        print(f" {W}Timezone             :{G} {timezoneF}")
        print(f" {W}Operator             :{G} {jenis_provider}")
        print(f" {W}Valid number         :{G} {is_valid_number}")
        print(f" {W}Possible number      :{G} {is_possible_number}")
        print(f" {W}International format :{G} {formatted_number}")
        print(f" {W}Mobile format        :{G} {formatted_number_for_mobile}")
        print(f" {W}Original number      :{G} {parsed_number.national_number}")
        print(f" {W}E.164 format         :{G} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f" {W}Country code         :{G} {parsed_number.country_code}")
        print(f" {W}Local number         :{G} {parsed_number.national_number}")
        input(f"{G}[{G}{Y}+{Y}{G}]{G}{W} Press Enter to continue")
        from main import mainopt
        mainopt()
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f" {W}Type                 :{G} This is a mobile number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f" {W}Type                 :{G} This is a fixed-line number")
        else:
            print(f" {W}Type                 :{G} This is another type of number")

    except KeyboardInterrupt:
        print(f" {W}[{Y}!{W}] {Y}PROGRAM STOPPED...")
        
def IP_Track():  
    ip = input(f"{W}\n{G}[{G}{Y}+{Y}{G}]{G} Enter IP target : {G}") #INPUT IP ADDRESS
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
    input(f"{G}[{G}{Y}+{Y}{G}]{G}{W}Press enter to continue")
    from main import mainopt
    mainopt()



def mainopt():
    time.sleep(1.0)
    print(f"""
      {Y}--------------------------------------
      {G}[1]: {Y}IP search{Y}
      {G}[2]: {Y}Phone Search{Y}
      {G}[3]: {Y}Instagram search{Y} 
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
    selvar = input(f"{G}[{G}{Y}+{Y}{G}]{G}{W}Select option and press enter >> {W}")
    
    if selvar == '1':
        from main import IP_Track
        IP_Track()
    if selvar == '2':
        from main import phonesearch
        phonesearch()
    if selvar == '3':
        username = input(f"{W}Enter Username: ")
        results = namesearch(username)
        for site, url in results.items():
            print(f"[+] {site} : {url}")
        input(f"{G}[{G}{Y}+{Y}{G}]{G}{W}Press enter to continue")
        
    if selvar == '99': 
        os.system('cls')
        print(f"{R}Xtool terminated{R}")
        time.sleep(0.5)
        print(f"{Y}PRO TIP: Execute command {W}'bash run.sh'{W} {Y}from Xtool directory to start Xtool{Y}")
        exit(0) 
    else:
        print(f"{R}Invalid selection{R}")  
        from main import mainopt
        mainopt()  
    