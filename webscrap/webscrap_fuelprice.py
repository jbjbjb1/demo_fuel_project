import bs4
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_price(product_url):
    res = requests.get(product_url)
    soup = bs4.BeautifulSoup(res.text, features="html.parser")
    elems = soup.find_all("a", attrs={"id": "homepage:j_idt84:bestMetroPrices:0:j_idt96:1:bestMetroPrice"})
    return elems[0].text

url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/pages/home.jspx'
price = get_price(url)
print('The price today for fuel is', price)