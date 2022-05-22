import requests
from bs4 import BeautifulSoup as bs
from smtplib import SMTP

###################### LOGIN DETAILS ###########################
my_email = SENDER'S EMAIL
password = EMAIL'S PASSWORD
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/101.0.4951.67 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
#################### URL OF ITEM OF CHOICE ##############################
amazon_url = "https://www.amazon.com/Hamilton-Beach-Enamel-Dishwasher-Kitchen/dp/B09LMPJCB4/ref=sr_1_6?crid=1AKSXFMYV8" \
             "7GO&keywords=cookware+sets&nav_sdd=aps&qid=1653251123&refinements=p_n_feature_four_browse-bin%3A224204901" \
             "1&rnid=2242047011&s=kitchen&sprefix=cookw&sr=1-6"
#################### TARGET PRICE FOR ITEM ######################
target_price = 200

response = requests.get(url=amazon_url, headers=headers)
response.raise_for_status()
content = response.text

soup = bs(content, "lxml")
price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
print(price)

#################### COMPARE PRICE AND SEND EMAIL ######################
if price <= target price:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=RECIPIENT'S EMAIL,
            msg=f"Your product is below ${target_price} today. Please purchase now."
        )
