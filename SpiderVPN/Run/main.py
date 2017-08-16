'''
Created on Aug 15, 2017

@author: zhaxind
'''

from WebsiteAnalyzers import ncix

if __name__ == '__main__':
    nicxPage = ncix.ncixPage()
    item_list = nicxPage.retriveItemList("T470")
    
    for i in item_list :
        print('--------------')
        print(i.name)
        print(i.price)
        print(i.detailed_URL)
        
    