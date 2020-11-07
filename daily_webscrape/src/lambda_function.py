import datetime
import json
import time

import boto3
import bs4
import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_wrapper import WebDriverWrapper


def lambda_handler(*args, **kwargs):
    fuel_price = get_fuel_price()
    sgd_price = get_sgd_price()
    oil_price = get_oil_price()
    date_now = str(datetime.datetime.now())
    data = {'Date':date_now, 'fuel_price':fuel_price, 'sgd_price':sgd_price, 'oil_price':oil_price}
    tablename = "fuelprice_data_table"
    #save_price_db(tablename, data)
    
    return data
    

def save_price_db(tablename, data):
  dynamodb = boto3.resource('dynamodb')   
  table = dynamodb.Table(tablename)
  table.put_item(Item=data)


def get_fuel_price():
  product_url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/pages/home.jspx'
  res = requests.get(product_url)
  soup = bs4.BeautifulSoup(res.text, features="html.parser")
  elems = soup.find_all("a", attrs={"id": "homepage:j_idt83:bestMetroPrices:0:j_idt95:1:bestMetroPrice"})
  price = float(elems[0].text)/100    # in AUD
  return str(price)[:4]               # str for dynamoDB


def get_sgd_price():
    html = None
    url = 'https://www.rba.gov.au/statistics/frequency/exchange-rates.html'
    selector = 'SGD'
    delay = 5   # sec, to wait for item to load
    price = 0   # default value

    driver = WebDriverWrapper()
    driver._driver.get(url)

    try:
        # wait until element visible
        WebDriverWait(driver._driver, delay).until(EC.presence_of_element_located((By.ID, selector)))
    except TimeoutException:
        print('Loading took too long.')
    else:
        html = driver._driver.page_source
    finally:
        driver.close()

    if html:
        soup = bs4.BeautifulSoup(html, "html.parser")
        data = soup.find(attrs={"id": selector})
        price = data.contents[3].next

    return str(price)               # str for dynamoDB


def get_oil_price():
    html = None
    url = 'https://www.tradingview.com/symbols/NYMEX-AV02%21/'
    selector = 'tv-symbol-price-quote__value js-symbol-last'
    selector1 = 'tv-symbol-price-quote__value'  # use this to check when javascript on page has loaded
    delay = 5   # sec, to wait for item to load
    price = 0   # default value

    driver = WebDriverWrapper()
    driver._driver.get(url)

    try:
        # wait until element visible
        WebDriverWait(driver._driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, selector1)))
    except TimeoutException:
        print('Loading took too long.')
    else:
        html = driver._driver.page_source
    finally:
        driver.close()

    if html:
        soup = bs4.BeautifulSoup(html, "html.parser")
        data = soup.find("div", class_=selector)
        price = data.text

    return str(price)               # str for dynamoDB