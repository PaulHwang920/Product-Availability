import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.walmart.com/ip/Nintendo-Switch-Console-with-Neon-Blue-Red-Joy-Con/709776123?selectedSellerId=0&u1=&oid=223073.1&wmlspartner=MfQy8kfx*Gk&sourceid=17962092231599100009&affillinktype=10&veh=aff'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

f=open("Log.txt", "a+")

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    Availability = soup.find(text="Out of stock")
    text = "Out of stock"

    if Availability != text:
        send_mail()
    else:
        f.write("Walmart: not in stock")
        f.write("\n")


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mapleplayerpaul9@gmail.com', 'Rpgstupid920@')

    subject= 'SWITCH AVAILABLE'
    body = URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mapleplayerpaul9@gmail.com',
        'paulsoohyunhwang@gmail.com',
        msg
    )
    f.write('Email has been sent')
    f.write("\n")

    server.quit()

check_price()
f.close()