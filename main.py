from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
import os


GMAIL_SMTP = "smtp.gmail.com"
YAHOO_SMTP = "smtp.mail.yahoo.com"

MY_GMAIL_EMAIL = os.environ.get("MY_GMAIL_EMAIL")
MY_GMAIL_PASSWORD = os.environ.get("MY_GMAIL_PASSWORD")

amazon_url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
    "Accept-Language": os.environ.get("ACCEPT_LANGUAGE"),
    "User-Agent": os.environ.get("USER_AGENT"),
}

response = requests.get(url=amazon_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price = float(soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString", id="priceblock_ourprice").getText().removeprefix("$"))


if price < 100:
    with SMTP(GMAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL_EMAIL, password=MY_GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_GMAIL_EMAIL,
            to_addrs=MY_GMAIL_EMAIL,
            msg=f"Subject:Super cheep!\n\nYour Instant Pot Duo Evo Plus Pressure Cooker 10 in 1,  6 Qt, 48 One Touch Programs is super cheep!!! Actual price is ${price}",
        )
