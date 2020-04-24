import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.bestbuy.com/site/animal-crossing-new-horizons-nintendo-switch/5723316.p?skuId=5723316'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    Availability = soup.find(text="Add to Cart")
    text = "Add to Cart"

    if Availability == text:
        send_mail()
    else:
        print("not in stock")


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

while(True):
    check_price()
    time.sleep(60)