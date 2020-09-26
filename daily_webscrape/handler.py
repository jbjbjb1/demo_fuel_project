import boto3
import bs4
import json
import requests
import datetime

def scrape(event, context):
  fuel_price = get_fuel_price()
  #oil_price = get_oil_price()
  sgd_price = get_sgd_price()
  date_now = str(datetime.datetime.now())
  data = {'Date':date_now, 'fuel_price':fuel_price, 'sgd_price':sgd_price}
  tablename = "fuel_price_south"
  save_price_db(tablename, data)


def get_fuel_price():
  product_url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/pages/home.jspx'
  res = requests.get(product_url)
  soup = bs4.BeautifulSoup(res.text, features="html.parser")
  elems = soup.find_all("a", attrs={"id": "homepage:j_idt84:bestMetroPrices:0:j_idt96:1:bestMetroPrice"})
  price = float(elems[0].text)/100    # in AUD
  return str(price)                   # str for dynamoDB


def get_sgd_price():
  product_url = 'https://www.rba.gov.au/statistics/frequency/exchange-rates.html'
  res = requests.get(product_url)
  soup = bs4.BeautifulSoup(res.text, features="html.parser")
  elems = soup.find(attrs={"id": "SGD"})
  price = elems.contents[3].next
  return str(price)                   # str for dynamoDB


def save_price_db(tablename, data):
  dynamodb = boto3.resource('dynamodb')   
  table = dynamodb.Table(tablename)
  table.put_item(Item=data)