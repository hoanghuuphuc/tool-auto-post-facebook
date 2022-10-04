from email import message
from email.mime import image
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from os import link
from selenium import webdriver
import time
import pandas
import imghdr
import pyautogui
import shutil
excel_data_df = pandas.read_excel('fb.xlsx')
message=excel_data_df['Noidung'].tolist()
LinkGroup=excel_data_df['UID'].tolist()
# file_Anh=excel_data_df["image"].tolist()
imageFolderPath =r"D:\images\hmBlue.jpg"
time.sleep(2)
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
# driver.get("https://www.facebook.com/")
# time.sleep(2) 
driver.find_element("name","email").send_keys("trandangkhoittfb@gmail.com")
driver.find_element("name","pass").send_keys("trandangkhoi1906")
driver.find_element("name","login").click()
# time.sleep(5)

for i in range (len(LinkGroup)):
    time.sleep(2)
    driver.get(LinkGroup[i])
    time.sleep(2)
    element = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div[1]/span").click()
    time.sleep(3)
    element = driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div").send_keys(message[i])
    time.sleep(1)
    clickanh=driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/span/div/div/div[1]/div/div/div[1]/i").click()
    time.sleep(3)
    clickAnh=driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div/i").click()
    time.sleep(3)
    pyautogui.write(imageFolderPath)
    time.sleep(2)
    pyautogui.keyDown("enter")
    time.sleep(2)
    dangbai=driver.find_element("xpath","/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]").click()
    time.sleep(10)
    
    
    
   
     