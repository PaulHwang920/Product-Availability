import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-77464001'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    Availability = soup.find("div", {"class": "styles__StyledShipping-sc-1gn4z07-1 fGhQiy"}).get_text()
    text = "Shipping Temporarily out of stockSee similar items"

    if Availability != text:
        send_mail()
    else:
        print("Target: not in stock")


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
    print('Email has been sent')

    server.quit()

check_price()