#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup



url="https://dnsleaktest.com"
req=requests.get(url)
soup=BeautifulSoup(req.content,"html.parser")

#searching for the juicy data to filter
#print(soup.prettify())

result=soup.find_all("p")
print(result[0].text)
print(result[1].text)
