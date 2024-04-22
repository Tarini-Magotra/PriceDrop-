import requests
import smtplib
import lxml
from bs4 import BeautifulSoup
import smtplib

headers={
 "Accept-Language" :"en-GB,en-US;q=0.9,en;q=0.8",
 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
 "sec-ch-ua-platform":"Windows",
 "Accept-Encoding":"gzip, deflate, br"
}

response=requests.get("https://amzn.eu/d/5FwLXjC",headers=headers)
web_page=(response.text)
soup=BeautifulSoup(web_page,"lxml")
tag=soup.find(class_="a-price-whole")

#when text < 3000 get a notification

print(tag)






