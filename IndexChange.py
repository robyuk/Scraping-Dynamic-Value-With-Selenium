from selenium import webdriver
import yagmail
import os
import time

rywebpage='https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6'
ryxpath='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]'
ryfullxpath='/html/body/div[1]/div/section[1]/div/div/div[2]/span[2]'


def sendEmail(drop):
  sender=os.getenv('automailsender')
  # you can obtain a disposable receiver email address from 
  # https://dropmail.me/
  receiver='cxpvzdnvb@netmail.tk'
  subject=f'CBX has changed {drop}%'
  content="""
CBX has changed!

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

changePercent=scrape(rywebpage,ryxpath)
if changePercent < 0.1:
  sendEmail(changePercent)
