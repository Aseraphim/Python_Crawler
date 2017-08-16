# -*- coding: UTF-8 -*-
'''
Created on Aug 7, 2017

@author: zhaxind
'''

import requests
from lxml import html
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
page = requests.get("https://ca.pcpartpicker.com/products/pricedrop/week/#dg_3", headers=headers)

tree = html.fromstring(page.text)

for x in range (0,24):
    monitor_lists = tree.xpath('//h2[@id="dg_'+str(x)+'"]/following-sibling::table/tbody/tr/*[1]/a/text()')
    mornitor_prices = tree.xpath('//h2[@id="dg_'+str(x)+'"]/following-sibling::table/tbody/tr/*[2]/text()')
    mornitor_discountpc = tree.xpath('//h2[@id="dg_'+str(x)+'"]/following-sibling::table/tbody/tr/*[6]/text()')
    
    Resolution_2k=re.compile('.*2560x1440.*')
    
    for i in monitor_lists:
        data = i +" "+mornitor_prices[(monitor_lists.index(i))] + " " +mornitor_discountpc[(monitor_lists.index(i))]
        if(re.match(Resolution_2k,i)):
            print(data)
        
