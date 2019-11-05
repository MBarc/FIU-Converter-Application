from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #for loading time between pages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

from config import portal

from information import logger
from information import share_with

def logger(message):
    '''Logs error messages'''
    error_log = open("ERROR.txt", 'a')
    error_log.write(message)
    error_log.close()

def click_on(element, element_type):
    '''Waits, up to 10 seconds, to find element. Once it finds the element, it clicks on it.'''
    if element_type == "id":
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, element))).click()
    if element_type == "css selector":
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, element))).click()
    if element_type == "xpath":
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))).click()
        
 def search(css_selector):
    '''Waits, up to 10 seconds, to find element. Once it finds the element, it types in it.'''
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))).send_keys(feed, Keys.ENTER)
    

    
chromedriver = os.getcwd() + '\\chromedriver'
if not os.path.exists(chromedriver): #checks to see if handler has chromium installed
    logger('[Error PublishFeed]: Chrome Driver not detected! Install the latest Chrome Driver from "chromedriver.chromium.org" and place the .EXE in the same directory.')
    quit()
    
try:
   driver = webdriver.Chrome(chromedriver)
   driver.get(portal['url'])
   time.sleep(3)
    
   username_textbox = driver.find_element_by_name('username').send_keys(portal['username]')

   password_textbox = driver.find_element_by_name('password').send_keys(portal['password'], Keys.ENTER)
                                                                               
   content_library = click_on('nav-browser', "id")
                                                                               
   f = open("filenames.txt", "r")

   filenames = []
   for line in f:
      filenames.append(line) 
                                                                               
   success = []
   failed = []
   for name in filenames:
      try:
        search_bar = search('input.search-query.advanced-mode', 'css selector')
                                                                               
        vide_settings = click_on('//*[@id="large-thumbnail-list"]/li[1]/div/div[1]/ul/li[3]/i', 'xpath')
                                                                               
        share_button = click_on('//*[@id="li-showing-share"]/a', 'xpath')
      
        role_button = click_on('#default-permission-select', 'css selector')
                                                                               
        select_contributer = click_on('//*[@id="share"]/div[1]/div[2]/ul/li[4]/a', 'xpath')
                                                                               
        search_groups = search('//*[@id="search-field"]', 'xpath')
      
        select_group = click_on('//*[@id="menu-selected"]/a/i', 'xpath')
                                                                               
        save_button = click_on('//*[@id="save-all"]', 'xpath')
      
      except Exception as e:
        logger(str(e))
        clear_searchbar = driver.find_element_by_css_selector('input.search-query.advanced-mode').clear()
        failed.append(name)
driver.quit()
