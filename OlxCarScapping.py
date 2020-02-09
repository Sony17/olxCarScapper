import requests , re 
from bs4 import BeautifulSoup
from selenium import webdriver 
import pandas

#get the website pages
#min = input('minimum range :')
#max = input('maximum range :')
min='70000'
max='150000'
url ='https://www.olx.in/delhi_g4058659/cars_c84?filter=price_between_'+min+'_to_'+max
#browser = webdriver.Chrome('chromedriver') 
#browser.get(url)
resposeData=requests.get(url)
CarData= resposeData.content
#print(resposeData.raise_for_status())
soup = BeautifulSoup(CarData,"html.parser")
#print(soup)
CarList = soup.find_all("li",{"class":"EIR5N"})

l=[]

for car in CarList:
   d={}
   try:
     d["itemPrice"]=car.find("span",{"data-aut-id":"itemPrice"}).text
   except AttributeError:
     d["itemPrice"] = None
     
   try:
     d["itemDetails"]=car.find("span",{"data-aut-id":"itemDetails"}).text
   except AttributeError:
     d["itemDetails"] = None
     
   try:
     d["itemTitle"]=car.find("span",{"data-aut-id":"itemTitle"}).text
   except AttributeError:
     d["itemTitle"] = None

   try: 
     d["date"]=car.find("span",{"class":"zLvFQ"}).text
   except AttributeError:
     d["itemTitle"] = None

   try:
     d["item-location"]=car.find("span",{"data-aut-id":"item-location"}).text
   except AttributeError:
     d["itemTitle"] = None

   try:
     link =car.find('a', attrs={'href': re.compile("^/item\/")})
     partUrl=link.get('href')
     olxUrl ='https://www.olx.in'
     url = olxUrl+partUrl
     d["PhoneUrl"]=url
   except AttributeError:
     d["itemTitle"] = None

   l.append(d)
     


        
    
        #NumResp = requests.get(url)
        #CarOwnerData= NumResp.content
        #CarOwnersoup = BeautifulSoup(CarOwnerData,"html.parser")
        #print(CarOwnersoup)
        #d["itemTitle"]=url



df =pandas.DataFrame(l)
df.to_csv("CarDataOlx2_9.csv")
    


  
