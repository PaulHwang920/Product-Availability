import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255&irclickid=2-HVx9URLxyOUGR0MdV3iVCmUki2tzyBUVyxUA0&irgwc=1&ref=198&loc=2-HVx9URLxyOUGR0MdV3iVCmUki2tzyBUVyxUA0&acampID=614286&mpid=10078'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    Availability = soup.find(text="Add to Cart")
    text = "Add to Cart"

    if Availability == text:
        send_mail()
    else:
        print("BestBuy: not in stock")


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