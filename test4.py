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

#

#Days

days = list(soup.find_all(class_='list-card-variable-text list-card-img-overlay', text=False))
dls = list()

for i in days:
        days1=str(i.text).split(' ',1)
        days2=days1[0]

        if days2.isnumeric():days1=i.text
        else:days1='No Days on Zillow'

        dls.append(days1)


#df = pd.DataFrame(bls)
#print(df)