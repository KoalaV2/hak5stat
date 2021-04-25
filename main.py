#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json

with open("products.json") as f:
    try:products = json.load(f)
    except Exception as e: print(e)

def get_pairs():
    lst_of_pairs = []
    for product in products['hak5_products']:
        pair = (product['name'],product['id'])
        lst_of_pairs.append(pair)
    return lst_of_pairs

def getstatus():
 
    for (name,id) in get_pairs():

        url = f'https://hak5.passportshipping.com/{id}'
        response = requests.get(url)  # Makes a request to the url and downloads plain html
        soup = BeautifulSoup(response.text,"html.parser")

        status_div = soup.find_all("div", {"class": "message"})[0] # Finds the div which has the status info
        delivery_div = soup.find_all("div",{"class": "date range"} )
        print(f"{name} : {delivery_div}")
        print(f"{name}: {status_div}")

def main():
    getstatus()

if __name__=="__main__":
    main()
