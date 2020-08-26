import bs4
import requests
import datetime

def get_price():
    product_url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/pages/home.jspx'
    res = requests.get(product_url)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    elems = soup.find_all("a", attrs={"id": "homepage:j_idt84:bestMetroPrices:0:j_idt96:1:bestMetroPrice"})
    price = float(elems[0].text)/100    # in AUD
    return {'date': str(datetime.datetime.now()), 'price': price}