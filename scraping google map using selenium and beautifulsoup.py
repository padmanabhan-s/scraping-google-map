#Import neccesary libraries

import pandas as pd
import time
from selenium import webdriver
from bs4 import BeautifulSoup

#intiate the firefox webdriver instance

driver=webdriver.Firefox()

#enter the filename

print("Enter the filename")
filename=str(input())

#enter the link of starting google map page to scrap

print("Enter the link of google map to scrap")
url=str(input())
driver.get(url)
time.sleep(3)
record=[]
for i in range(8):
    try:
        page=driver.find_element_by_link_text(str(i+2))
        driver.set_page_load_timeout(30)
        driver.implicitly_wait(50)
        page.click()
        time.sleep(3)
        r=driver.page_source
#Beautiful soup for scraping the html source
        soup=BeautifulSoup(r,'html.parser')
        list= soup.find_all('div',{"class":"cXedhc"})
        for l in list:
            name=l.find('div').text
            detail=l.find_all('span')
            details=detail[0].text.replace('0','/0')
            record.append((name,details))
        df=pd.DataFrame(record,columns=['name','details'])
        df.to_csv(filename,index=False,encoding='utf-8')        
   
          

        
    except:
        driver.implicitly_wait(50)
        print("error at")
    
          

