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
   r = s.get(url, headers=req_headers)
   r2 = s.get(url, headers=req_headers)
   r3 = s.get(url, headers=req_headers)
   r4 = s.get(url, headers=req_headers)
   r5 = s.get(url, headers=req_headers)
   r6 = s.get(url, headers=req_headers)
   r7 = s.get(url, headers=req_headers)
   r8 = s.get(url, headers=req_headers)
   r9 = s.get(url, headers=req_headers)
   r10 = s.get(url, headers=req_headers)

soup = BeautifulSoup(r.content, 'html.parser')
soup1 = BeautifulSoup(r2.content, 'html.parser')
soup2 = BeautifulSoup(r3.content, 'html.parser')
soup3 = BeautifulSoup(r4.content, 'html.parser')
soup4 = BeautifulSoup(r5.content, 'html.parser')
soup5 = BeautifulSoup(r6.content, 'html.parser')
soup6 = BeautifulSoup(r7.content, 'html.parser')
soup7 = BeautifulSoup(r8.content, 'html.parser')
soup8 = BeautifulSoup(r9.content, 'html.parser')
soup9 = BeautifulSoup(r10.content, 'html.parser')

# create the first two dataframes
df = pd.DataFrame()
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
df7 = pd.DataFrame()
df8 = pd.DataFrame()
df9 = pd.DataFrame()

# all for loops are pulling the specified variable using beautiful soup and inserting into said variable
for i in soup:
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    days = list(soup.find_all(class_='list-card-variable-text list-card-img-overlay', text=True))
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    type1 = soup.find_all('div', {'class': 'list-card-statusText'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')


df['address'] = address
df['prices'] = price
df['beds'] = beds
df['home_type'] = home_type



df = df.append(df2, ignore_index = True)
df = df.append(df3, ignore_index = True)
df = df.append(df4, ignore_index = True)
df = df.append(df5, ignore_index = True)
df = df.append(df6, ignore_index = True)
df = df.append(df7, ignore_index = True)
df = df.append(df8, ignore_index = True)
df = df.append(df9, ignore_index = True)

print(df)
df.to_csv('Clasificacion.txt', index=False)


#for i in soup