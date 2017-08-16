'''
Created on Aug 15, 2017

@author: zhaxind
'''

import requests
from lxml import html
import re
from Item.item import item


class ncixPage:
    url= "http://www.ncix.com/"  
    
    def retriveItemList(self,str):
        "this function will retrive the info of the input item name"
        queryStr= "/search/?q=" +str.replace(' ', '+')
        page = requests.get(self.url+queryStr)
        tree = html.fromstring(page.text)
        itme_name_List = tree.xpath('//tr[starts-with(@id,"tr")]/td[2]/div[1]/div[2]/span/a/text()')
        item_price_list = tree.xpath('//tr[starts-with(@id,"tr")]/td[4]/font/strong/text()')
        item_detail_URL = tree.xpath('//tr[starts-with(@id,"tr")]/td[2]/div[1]/div[2]/span/a/@href')
        item_list = list()
        for i in itme_name_List:
            retrived_item = item(i,item_price_list[itme_name_List.index(i)],item_detail_URL[itme_name_List.index(i)])
            item_list.append(retrived_item)
        return item_list
    
    def __init__(self):
        self.data = []