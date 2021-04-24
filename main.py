#!/usr/bin/env python3
import requests
import urllib3.request
from bs4 import BeautifulSoup
import json

with open("products.json") as f:
    try:products = json.load(f)
    except:products = {}

def getproductid():
    for i in products['hak5_products']:
        productid = i["id"]
        print(productid)

def pineapple():
    url = 'https://hak5.passportshipping.com/'
    response = requests.get(url)  # Makes a request to the url and downloads plain html
    soup = BeautifulSoup(response.text,"html.parser")
    status_div = soup.find_all("div", {"class": "message"})[0] # Finds the div which has the status info
    delivery_div = soup.find_all("div",{"class": "date range"} )
    print(delivery_div)
    print(f"Pineapple: {status_div}")

def main():
    getproductid()

if __name__=="__main__":
    main()
