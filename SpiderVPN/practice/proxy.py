# -*- coding: UTF-8 -*-

import requests
import re
from bs4 import BeautifulSoup
from lxml import html

url = "https://www.iplocation.net/find-ip-address"

proxies = {
  "https": "https://86.109.100.80:8080",
}
headers = requests.utils.default_headers()
page = requests.get(url,headers=headers,proxies=proxies)
tree = html.fromstring(page.text)
ipaddress = tree.xpath("//table[@class='iptable']/tr[1]/td[1]/span/text()")[0]
Location = tree.xpath("//table[@class='iptable']/tr[2]/td[1]/text()")[0]
#print(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', page.text)[0])
print("Respond from: " + page.url)
print("ip address: " + ipaddress)
print("location: "+ Location)
#print(page.text)

print('-------------------------------------')

url = "https://www.iptrackeronline.com/"

headers = requests.utils.default_headers()
page = requests.get(url,headers=headers,proxies=proxies)
tree = html.fromstring(page.text)
IPAddress = tree.xpath("//table[@class='forumline' and @style='display:none;']/tr[2]/td[1]/input[1]/@value")[0]
# print(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', page.text)[0])
Country = tree.xpath("//table[@class='forumline' and @style='display:none;']/tr[2]/td[2]/input[1]/@value")[0]
Region = tree.xpath("//table[@class='forumline' and @style='display:none;']/tr[3]/td[2]/input[1]/@value")[0]
City = tree.xpath("//table[@class='forumline' and @style='display:none;']/tr[4]/td[2]/input[1]/@value")[0]
print("Respond from: " + page.url)
print("ip address: " + IPAddress)
print("Country: " + Country)
print("Region: " + Region) 
print("City: " + City)


