import time
import os
import colorama
import requests
import json
import phonenumbers
import urllib3
import instaloader
from namesearch import namesearch
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style, init
init(autoreset=True)



B = Fore.BLUE #{B}
G = Fore.GREEN #{G}
R = Fore.RED #{R}
M = Fore.MAGENTA #{M}
C = Fore.CYAN #{C}
W = Fore.WHITE #{W}
Y = Fore.YELLOW #{Y}

def XtInfo(json_file_path):
    """
    Reads a JSON file and prints information about the Xtool.

    :param json_file_path: Path to the JSON file.
    """
    # Open the JSON file and load the data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Extract information from the JSON structure
    xtool_info = data.get("Xtool", {})

    # Print information about Xtool
    print(f"Name: {xtool_info.get('name', '')}")
    print(f"Program Size: {xtool_info.get('ProgramSize', '')}")
    print(f"Installed Size: {xtool_info.get('installedSize', '')}")
    print(f"Creator: {xtool_info.get('creator', '')}")
    print(f"Latest Version: {xtool_info.get('latestVersion', '')}")
    print(f"Website: {xtool_info.get('website', '')}")

    print("\nPackages:")
    packages = xtool_info.get('packages', {})
    for package_name, package_version in packages.items():
        print(f"{package_name}: {package_version}")

def IgAccInfo():
    # Get target username from user input
    target_username = input("Enter the Instagram username: ")
    L = instaloader.Instaloader()

    # Load login credentials from file using the target username
    try:
        profile = instaloader.Profile.from_username(L.context, target_username)
        
        print(f"Username: {profile.username}")
        print(f"User ID: {profile.userid}")
        print(f"Number of Followers: {profile.followers}")
        print(f"Number of Following: {profile.followees}")
        print(f"Number of Posts: {profile.mediacount}")
        print(f"Full Name: {profile.full_name}")
        print(f"Biography: {profile.biography}")
        print(f"Profile Picture URL: {profile.profile_pic_url}")
        print(f"External URL: {profile.external_url}")
        print(f"Is Private: {profile.is_private}")
        print(f"Is Verified: {profile.is_verified}")
        print(f"Business Account: {profile.is_business_account}")
        print(f"Business Category: {profile.business_category_name}")
        input(f"{G}[{G}{Y}+{Y}{G}]{G}{W}Press Enter to continue")
        from main import mainopt
        mainopt()
        

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Error: {e}")

def phonesearch():
    try:

        User_phone = input(f"\n {G}[{G}{Y}+{Y}{G}]{G}{W}Enter phone number target {G}Ex [+6281xxxxxxxxx] {W}: {G}")  
        default_region = "ID"  

        parsed_number = phonenumbers.parse(User_phone, default_region)  
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
        print(f"")
        
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

def chkver():
    raw_url = 'https://raw.githubusercontent.com/Mrprogramer885/source/main/versioninfo.txt'

    try:   
        response = requests.get(raw_url)
        response.raise_for_status()  

        file_content = response.text
        version_lines = [line.strip() for line in file_content.split('\n') if line.strip().startswith('Version:')]
        if version_lines:
            version_line = version_lines[0]
            _, version_str = version_line.split(':', 1)
            version_str = version_str.strip()
            if version_str > '1.1.0':
                print(f"{G}[{G}{Y}+{Y}{G}]{G}{G}New update available.{G}")
                input()
                from main import mainopt
                mainopt()
            else:
                print(f"{G}[{G}{Y}+{Y}{G}]{G}{G}No updates available.{G}")
                input()
                from main import mainopt
                mainopt()
        else:
            print(f"{G}[{G}{Y}+{Y}{G}]{G}{G}Version information not found in the file.{G}")
            input()
            from main import mainopt
            mainopt()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def mainopt():
    time.sleep(1.0)
    print(f"""
      {Y}--------------------------------------
      {G}[1]: {Y}IP search{Y} {G}(Available)
      {G}[2]: {Y}Phone Search{Y} {G}(Available)
      {G}[3]: {Y}Instagram search{Y} {G}(Available)
      {G}[4]: {Y}Google dorks{Y} {R}(WIP)
      {G}[5]: {Y}Email search{Y} {R}(WIP)
      {G}[6]: {Y}username osint{Y} {G}(Available)
      {G}[7]: {Y}Social media search{Y} {R}(WIP)
      {G}[8]: {Y}Github search{Y} {R}(WIP)
      {G}[9]: {Y}Port scan{Y} {R}(WIP)
      {G}[10]: {Y}Check for updates{Y} {G}(Available)
      {G}[11]: {Y}Changelog{Y} {G}(Available)
      {G}[12]: {Y}Xtool info{Y} {R}(WIP)
      {G}[13]: {Y}Delete all Xtool data{Y} {R}(WIP)
      {G}[14]: {Y}Uninstall{Y} {R}(WIP)
      {Y} additional CLI commands (not used as arguments)
      -help -exit -info
      
      {R}[99]: Exit Xtool{R}
      
      {Y}---------------------------------------- 
      """)
    selvar = input(f"{G}[{G}{Y}+{Y}{G}]{G}{W}Select option or command and press enter >> {W}")
    
    if selvar == '1':
        from main import IP_Track
        IP_Track()
    if selvar == '2':
        from main import phonesearch
        phonesearch()
    if selvar == '3':
        from main import IgAccInfo
        IgAccInfo()
    if selvar == '6':
        username = input(f"{G}[{G}{Y}+{Y}{G}]{G}{W}Enter Username: ")
        results = namesearch(username)
        for site, url in results.items():
            print(f"[+] {site} : {url}")
        input(f"{G}[{G}{Y}+{Y}{G}]{G}{W}Press enter to continue")
    if selvar == '10':
        print(f"{G}[{G}{Y}+{Y}{G}]{G}Fetching github data...")
        from main import chkver
        chkver()
        input(f"{G}[{G}{Y}+{Y}{G}]{G}{W} Press enter to continue")
        from main import mainopt
        mainopt()       
    if selvar == '11':
        with open('changelog.txt', 'r') as file:
            content = file.read()
            print(content)
            input(f"{G}[{G}{Y}+{Y}{G}]{G}{W} Press enter to continue")
            from main import mainopt
            mainopt()
    if selvar == '12':
        XtInfo('Xtool.json')  
        input(f"{G}[{G}{Y}+{Y}{G}]{G}{W} Press enter to continue")
        from main import mainopt          
    if selvar == '99': 
        os.system('cls')
        print(f"{R}Xtool terminated{R}")
        time.sleep(0.5)
        print(f"{Y}PRO TIP: Execute command {W}'bash run.sh'{W} {Y}from Xtool directory to start Xtool{Y}")
        exit(0)
    if selvar == '-h':
        with open('help.txt', 'r') as file:
            content = file.read()
            print(content)
            input(f"{G}[{G}{Y}+{Y}{G}]{G}{W} Press enter to continue")
            from main import mainopt 
    if selvar == '-help':
        with open('help.txt', 'r') as file:
            content = file.read()
            print(content)
            input(f"{G}[{G}{Y}+{Y}{G}]{G}{W} Press enter to continue")
            from main import mainopt   
    if selvar == '-exit': 
        os.system('cls')
        print(f"{R}Xtool terminated{R}")
        time.sleep(0.5)
        print(f"{W}Thanks for using Xtool{W}")
        print(f"{Y}PRO TIP: Execute command {W}'bash run.sh'{W} {Y}from Xtool directory to start Xtool{Y}")
        exit(0)         
    if selvar == '-info':
        XtInfo('Xtool.json')  
        input(f"{G}[{G}{Y}+{Y}{G}]{G}{W} Press enter to continue")
        from main import mainopt
        mainopt()      
    else:
        print(f"{G}[{G}{Y}+{Y}{G}]{G}{R}Invalid selection{R}")  
        from main import mainopt
        mainopt()  
    