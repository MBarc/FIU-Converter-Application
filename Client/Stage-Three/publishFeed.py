'''
Purpose: To automatically add videos to a feed on the Haivision Portal.
Author: Michael Barcelo
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #for loading time between pages

feed = 'ABC Erica - Lab Archive' # feed to put videos to

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#Logging in + navigating to page
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
chromedriver = 'C:\\Users\\mbarcelo\\AppData\\Local\\Programs\\Python\\Python36\\chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://ccfmedia.fiu.edu/login')

username_textbox = driver.find_element_by_name('username')
username_textbox.send_keys('mbarcelo')

password_textbox = driver.find_element_by_name('password')
password_textbox.send_keys('MichaelB1998!!!', Keys.ENTER)
time.sleep(3)

content_library = driver.find_element_by_id('nav-browser').click()
time.sleep(.5)

sources = driver.find_element_by_id('showing-sections').click() #showing-sections = feeds tab
time.sleep(4)

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Searching for a specific feed
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

#Navigating to feed
input_feed = driver.find_element_by_css_selector('input.search-query.advanced-mode')
input_feed.send_keys(feed, Keys.ENTER)

time.sleep(4)
driver.find_element_by_css_selector('i.site-icon-manage').click()

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Adding video to feed
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


time.sleep(4)

lines = [line.rstrip('\n') for line in open('filenames.txt')]


for i in lines:
    search_all_videos = driver.find_element_by_css_selector('input.search-query.advanced-mode')
    search_all_videos.send_keys(i, Keys.ENTER)

    time.sleep(2)

    try:
        check_box = driver.find_element_by_xpath('//*[@id="media-thumbnail-list"]/li/div/div[1]/label/span')
        check_box.click()
        time.sleep(.5)

        add_video = driver.find_element_by_css_selector('button#add-selected-to-section.btn-forward')
        add_video.click()

        time.sleep(.5)
        search_all_videos.clear()
    except Exception as e:
        print(i)
        search_all_videos.clear()
