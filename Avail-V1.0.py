import sys
import smtplib
import datetime
import requests
from time import localtime, strftime, sleep
from bs4 import BeautifulSoup
from playsound import playsound
from win10toast import ToastNotifier
from colorama import init, Fore, Back, Style

init()

# founders edition url
fe_url = "WEBSITE URL HERE"
headers = {"User-Agent": 'USER AGENT HERE'}
fe_page = requests.get(fe_url, headers = headers)
soup = BeautifulSoup(fe_page.content, 'html.parser')

# login for sms and email
username = "GMAIL HERE"
vtext = "PHONE # ASSOCIATED WITH EMAIL HERE"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo
server.login(username, 'GMAIL APP LOGIN PASSWORD HERE')


# sms messaging
def sms():
    subject = ""
    body = "The Nvidia Rtx 3080 FE is now available at:"
    txtmsg = f"subject: {subject}\n\n{body}"

    tsubject = ""
    tbody = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
    msg = f"subject: {tsubject}\n\n{tbody}"

    server.sendmail(username, vtext, txtmsg)
    server.sendmail(username, vtext, msg)

def sms2():
    subject = ""
    body = "ERROR: Unkown STR"
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(username, vtext, msg)

# email
def send_mail():

    subject = "Nvidia Rtx 3080 FE is Now Available!"
    body = "The Nvidia Rtx 3080 FE is Now Available! is now available at: \n https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
    username,
    username,
    msg
    )

# should prob make the prints into variables
# availability checker
def fe_checker():
    while True:
        cur_time = strftime("%H:%M:%S", localtime())
        fe_avail = soup.find(style = "padding:0 8px").text
        if fe_avail == str("Sold Out"):
            print(cur_time, Fore.WHITE + "::", Fore.BLUE + "[Best-Buy(US)]", Style.RESET_ALL, 
                Fore.CYAN + "Nvidia RTX 3080 FE", Fore.WHITE + "::", Fore.RED + "Sold-Out")
            print(Fore.WHITE + "-------------------------------------------------------------")
            print(Style.RESET_ALL)
            sleep(5)
        elif fe_avail == str("Add to Cart"):
            print(cur_time, Fore.WHITE + "::", Fore.BLUE + "[Best-Buy(US)]", Style.RESET_ALL,
                Fore.CYAN + "Nvidia RTX 3080 FE", Fore.WHITE + "::", Fore.GREEN + "Available")
            print(Fore.WHITE + "-------------------------------------------------------------")
            print(Style.RESET_ALL)
            send_mail()
            sms()
            print(Fore.GREEN + "Sent!")
            ToastNotifier().show_toast("Nvidia Rtx 3080 FE", "The Rtx 3080 is now available") 
            playsound("Alert.mp3")
            sleep(2)
        elif fe_avail != str("Sold Out") or str("Add to Cart"):
            print(Fore.RED + "ERROR: Unkown STR")
            sms2()
            sys.exit() 

# may not implement
def autoBuy():
    pass


fe_checker()
            
