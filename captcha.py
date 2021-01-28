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
#   content_l = s.get(url, headers=req_headers)
#   content_d = s.get(url, headers=req_headers)
#   content_p = s.get(url, headers=req_headers)
#   content_bd = s.get(url, headers=req_headers)
#   content_ba = s.get(url, headers=req_headers)
#   content_s = s.get(url, headers=req_headers)
#   content_t = s.get(url, headers=req_headers)
#   content_a = s.get(url, headers=req_headers)
#   content_cb = s.get(url, headers=req_headers)

bcontent1 = BeautifulSoup(content1.content, 'html.parser')
#bcontent_l = BeautifulSoup(content_l.content, 'html.parser')
#bcontent_d = BeautifulSoup(content_d.content, 'html.parser')
#bcontent_p = BeautifulSoup(content_p.content, 'html.parser')
#bcontent_bd = BeautifulSoup(content_bd.content, 'html.parser')
#bcontent_ba = BeautifulSoup(content_ba.content, 'html.parser')
#bcontent_s = BeautifulSoup(content_s.content, 'html.parser')
#bcontent_t = BeautifulSoup(content_t.content, 'html.parser')
#bcontent_a = BeautifulSoup(content_a.content, 'html.parser')
#bcontent_cb = BeautifulSoup(content_cb.content, 'html.parser')


#print(bcontent1)

# create the first two dataframes
df = pd.DataFrame()
df1 = pd.DataFrame()
# all for loops are pulling the specified variable using beautiful soup and inserting into said variable
for i in bcontent1:
    link = bcontent1.find_all(class_='list-card-link')
    days = list(bcontent1.find_all(class_='list-card-variable-text list-card-img-overlay', text=True))
    price = list(bcontent1.find_all(class_='list-card-price'))
    bbs = list(bcontent1.find_all("ul", class_="list-card-details"))
    home_type = bcontent1.find_all('div', {'class': 'list-card-footer'})
    type1 = bcontent1.find_all('div', {'class': 'list-card-statusText'})
    address = bcontent1.find_all(class_='list-card-addr')
    brokerage = list(bcontent1.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))



    # create dataframe columns out of variables
    df['price'] = price
    df['address'] = address
    df['beds'] = bbs
# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in bcontent1.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df['links'] = urls
df['links'] = df['links'].astype('str')
# remove html tags
df['links'] = df['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df['links'] = df['links'].replace('" tabindex="0"></a>', ' ', regex=True)

print(df)
#for i in soup