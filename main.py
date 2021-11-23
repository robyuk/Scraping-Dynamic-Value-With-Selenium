from selenium import webdriver
import time

rywebpage='http://automated.pythonanywhere.com/'
ryxpath='/html/body/div[1]/div/h1[2]'
ryfullxpath='/html/body/div[1]/div/h1[2]/text()'

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
  """ Extract only the temperature from the text string """
  temp=float(text.split(": ")[1])
  return temp

def main(rywebpage,ryxpath):
  """ gets a dynamic value from a web page """
  driver=getdriver(rywebpage)
  driver.get(rywebpage)
  time.sleep(2)
  element=driver.find_element(by='xpath', value=ryxpath)
  return gettemp(element.text)

print(main(rywebpage,ryxpath))