'''
Purpose: To automatically add videos to a feed on the Haivision Portal.
Author: Michael Barcelo
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #for loading time between pages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os

from config import portal #same directory ; imports URL, username, and password

from infomration import logger
from information import feed

feed = 'ABC Erica - Lab Archive' # feed to put videos to

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

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#Logging in + navigating to page
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
driver.get('https://ccfmedia.fiu.edu/login')
time.sleep(3)

chromedriver = os.cwd() + '\\chromedriver'
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
                                    
    feeds_tab = click_on('showing-sections', "id")

    search_for_feed = search('input.search-query.advanced-mode')

    feed_thumbnail = click_on('i.site-icon-manage', "css selector")

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Adding videos to feed
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
lines = [line.rstrip('\n') for line in open('filenames.txt')]

successful = []
failed = []
for name in lines:

    search_all_videos = search('input.search-query.advanced-mode').send_keys(name, Keys.ENTER)

    try:

        check_box = click_on('//*[@id="media-thumbnail-list"]/li/div/div[1]/label/span', 'xpath')

        add_video = click_on('button#add-selected-to-section.btn-forward', 'css selector')

        search_bar = driver.find_element_by_css_selector('input.search-query.advanced-mode').clear()

        successful.append(name)

    except Exception as e:

        failed.append(name)

        logger(str(e))
        
        search_bar = driver.find_element_by_css_selector('input.search-query.advanced-mode').clear()

driver.quit() #deallocating resources
