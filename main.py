#!/usr/bin/env python3

import json
import requests
from bs4 import BeautifulSoup

def get_pairs(productsInput):
    return [(p['name'],p['id']) for p in productsInput['hak5_products']]

def getstatus(productsInput):
    toReturn = []
    for (product_name, product_id) in get_pairs(productsInput):
        me = {
            'name':product_name,
            'id':product_id,
            'delivery_status':None,
            'estimated_delivery':None
        }

        r = requests.get(f'https://hak5.passportshipping.com/{product_id}') # Makes a request to the url and downloads plain html
        soup = BeautifulSoup(r.text, "html.parser") # Formats with Soup

        try: # Gets the "Status update" part and formats it
            me['delivery_status'] = soup.find("div", {"class": "message"}).text.split("\n")[2].lstrip(' ')
        except:pass

        try: # Grabs the estimated time (which is 2 parts) and then gets the data and formats it
            me['estimated_delivery'] = " - ".join([x.text.split("\n")[1].lstrip(' ') for x in soup.find_all("div", {"class": "date range"})])
            if me['estimated_delivery'] == "":
                me['estimated_delivery'] = None
        except:pass

        toReturn.append(me)
    return toReturn

if __name__=="__main__":
    # Loads JSON file with the products
    with open("products.json") as f:
        products = json.load(f)

    print("[*] Loading products...")

    for x in getstatus(products):
        print(f'\n"{x["name"]}" (ID: {x["id"]}):')

        if x["delivery_status"] == None:
            print("Delivery status not found")
        else:
            print(f'Delivery status: {x["delivery_status"]}')

        if x["estimated_delivery"] == None:
            print("Estimated delivery not found")
        else:
            print(f'Estimated delivery: {x["estimated_delivery"]}')
