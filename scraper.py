import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=sr_1_1?dchild=1&keywords=switch&qid=1587745911&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    price = float(soup2.find(id="buyNew_noncbb").get_text().strip()[1:7])

    if price < 300.00:
        send_mail()
    else:
        print("Price is above 300")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mapleplayerpaul9@gmail.com', 'Rpgstupid920@')

    subject= 'Price fell down!'
    body = URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mapleplayerpaul9@gmail.com',
        'paulsoohyunhwang@gmail.com',
        msg
    )
    print('Email has been sent')

    server.quit()

while(True):
    check_price()
    time.sleep(60)