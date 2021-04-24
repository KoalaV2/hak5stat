#!/usr/bin/env python3
import requests
import urllib3.request
from bs4 import BeautifulSoup
import json

with open("products.json") as f:
    try:products = json.load(f)
    except Exception as e: print(e)

def getproductid():
    productid = []
    for i in products['hak5_products']:
        productid.append(i["id"])
    return(productid)

def getproductname():
    productname = []
    for i in products['hak5_products']:
        productname.append(i["name"])
    return(productname)

def pineapple():
    productlist = getproductid()
    productname = getproductname()

    for i in productlist:
        url = f'https://hak5.passportshipping.com/{i}'

        response = requests.get(url)  # Makes a request to the url and downloads plain html
        soup = BeautifulSoup(response.text,"html.parser")
        status_div = soup.find_all("div", {"class": "message"})[0] # Finds the div which has the status info
        delivery_div = soup.find_all("div",{"class": "date range"} )
        print(delivery_div)
        print(f"{productname}: {status_div}")

def main():
    #getproductid()
    pineapple()

if __name__=="__main__":
    main()
