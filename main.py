from selenium import webdriver
import yagmail
import os
import time

# Does not work because of Amazon bot check!!

rywebpage='https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M/'
ryxpath='//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[1]'
ryfullxpath='/html/body/div[1]/div[2]/div[9]/div[6]/div[4]/div[9]/div[2]/div/table/tbody/tr/td[2]/span[1]/span[1]'


def sendEmail(price,oldprice):
  sender=os.getenv('automailsender')
  # you can obtain a disposable receiver email address from 
  # https://dropmail.me/
  receiver='lrajcuxyb@laste.ml'
  subject=f'PF0989 Price has changed to ${price}'
  content=f,"""
Price has changed!
PF WaterWorks PF0989 Garbage Disposal Installation Kit, White
  Current price=${price}
  Previous price=${oldprice}
"""
  yag=yagmail.SMTP(user=sender, password=os.getenv('automailpw'))
  yag.send(to=receiver, subject=subject, contents=content+str(drop)+"%")
  print("Email sent")
  

def getdriver(rywebpath):
  #Set options to make web browsing easier
  options=webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_argument('disable-blink-features=AutomationControlled')
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  
  driver=webdriver.Chrome(options=options)
  return driver

def gettemp(text):
  """ Extract only the number from the text string """
  temp=float(text.split(" ")[0])
  return temp

def scrape(rywebpage,ryxpath):
  """ gets a dynamic value from a web page """
  driver=getdriver(rywebpage)
  driver.get(rywebpage)
  time.sleep(2)
  element=driver.find_element(by='xpath', value=ryxpath)
  return gettemp(element.text)


oldprice=scrape(rywebpage,ryxpath)

#uncomment next line for testing
oldprice=0

while True:
  time.sleep(36)
  currentprice=scrape(rywebpage,ryxpath)
  if not currentprice == oldprice:
    sendEmail(currentprice)
    oldprice=currentprice
