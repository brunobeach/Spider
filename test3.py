import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re
import requests
import lxml
from lxml.html.soupparser import fromstring
import prettify
import numbers
import htmltext


req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
with requests.Session() as s:
   url = 'https://www.zillow.com/new-york-ny/'
   content1 = s.get(url, headers=req_headers)

soup = BeautifulSoup(content1.content, 'html.parser')
prop=0
propa=0

#Addres
address = soup.find_all(class_='list-card-addr')
adls = list()

for i in address:
        adls.append(i.text)
        prop +=1

#Price
price = list(soup.find_all(class_='list-card-price'))
prls = list()
pricetotal=0
for i in price:
        prls.append(i.text)
        pricetotal= int((str(i.text).replace('$', '')).replace(',','')) + pricetotal



#rooms

rooms = list(soup.find_all("ul", class_="list-card-details"))
rols = list()

for i in rooms:
        cad=(str(i.text).split(','))
        beds=cad[0]
        beds2=beds.split(' ')
        beds=beds2[0]
        rols.append(beds)

#bath

bani = list(soup.find_all("ul", class_="list-card-details"))
bals = list()

for i in bani:
        cad=(str(i.text).split(','))
        bath = cad[1]
        bath2=bath.split(' ',1)
        bath=bath2[0]
        bals.append(bath)


#Square

sqr = list(soup.find_all("ul", class_="list-card-details"))
sqls = list()
sq2=0
for i in sqr:
        cad=(str(i.text).split(','))
        if cad[2].isnumeric():square = cad[3]
        else:square = cad[2]
        squareline=(str(square).split(' ',1))
        square1=squareline[0]
        if square1.isnumeric():square=square1
        else:square=0
        sq2=int(square)+sq2
        sqls.append(square)

#Days

days = list(soup.find_all(class_='list-card-variable-text list-card-img-overlay', text=False))
dls = list()

for i in days:
        dls.append(i.text)

#broker

broker = list(soup.find_all(class_='list-card-footer',text=False))
brls = list()
for i in broker:
        brls.append(str(i.text).replace('Listing by: ',''))
        if str(i.text).replace('Listing by: ','') == '':propa=prop-1

df = pd.DataFrame(brls)

#type
tp = list(soup.find_all(class_="list-card-statusText"))
tpls = list()
convar=0
mulvar=0
houvar=0
ownvar=0

for i in tp:
        tpls.append(str(i.text).replace('- ',''))
        if str(i.text).replace('- ','') =='Condo for sale': convar +=1
        if str(i.text).replace('- ', '') == 'Multi-family home for sale': mulvar += 1
        if str(i.text).replace('- ', '') == 'House for sale': houvar += 1
        if str(i.text).replace('- ', '') == 'For sale by owner': ownvar += 1

df = pd.DataFrame({'Days':dls,'prices': prls, 'Beds':rols, 'Baths':bals,'Squares':sqls,'Type':tpls, 'Address': adls,'Broker':brls })

#Link
urls = []
for link in soup.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
#    This is not mandatory necessary, but in Mac the regular removing tags doesn't work well
#    print(((((str(href)).replace('<a class="',' ')).replace('list-card-link list-card-link-top-margin"','')).replace('href="','')).replace('" tabindex="0"></a>',''))
    urls.append(((((str(href)).replace('<a class="',' ')).replace('list-card-link list-card-link-top-margin"','')).replace('href="','')).replace('" tabindex="0"></a>',''))

df['links'] = urls
df['links'] = df['links'].astype('str')

print(df)


df.to_csv('final.csv', index=False)

#Report

print('Property Quantity: ' + str(prop))
print('Average Price $' + str(round(pricetotal/prop)) + '; and $' + str(round(pricetotal/sq2,2)) + ' for Square')
if ownvar != 0:print('Number of Condo: ' + str(convar))
if ownvar != 0:print('Number of Multi Family Home: ' + str(mulvar))
if ownvar != 0:print('Number of House: ' + str(houvar))
if ownvar != 0:print('Number of Owner: ' + str(ownvar))
print('Number of properties per broker: ' + str(propa))