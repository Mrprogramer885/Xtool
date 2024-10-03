echo ---------------------------------------------------------------------
echo ---------------------------------------------------------------------
echo By continuing you agree to this:
echo Author of Xtool is not responsible for any damage you have done by using this tool.
echo This tool is made only for educational purposes, any illegal action done with this this tool is your problem, Not Mine.
echo This was made by Petrvrba03 and it is the only developer of this tool, anyone other is not.
echo note that if you downloaded this tool from anywhere else than github or purchased it, it may be infected and not safe. delete it immediately.
echo This tool does not allows you to hack, stalk, or destroy online things such as emails, electronic devices or anything else.
echo ---------------------------------------------------------------------
echo ---------------------------------------------------------------------
echo by continuing you are accepting everything above and that i am not responsible for anything that you did or happened to your device by using my tool
read
echo installing packages...
pip install phonenumbers
echo phonenumbers lookup database downloaded
pip install instaloader
echo instagram lookup API installed.
pip install requests
echo requests package downloaded
pip install colorama
echo colored terminal text module installed
echo installing all secondary required packages
pip install -r requirements.txt
echo all secondary required packages installed
echo instalation completed, press enter to start Xtool
read
python3 modules/start.py
