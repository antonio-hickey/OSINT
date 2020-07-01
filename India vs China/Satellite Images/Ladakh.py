#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:47:15 2020

This bot is using https://earthexplorer.usgs.gov to take screenshots of specific geolocations.
the bot requests the website, clicks add coordinates, it then types the pre defined coordinates (Lat_x, Lon_x)
clicks to save coordinate, and then repeats this process except for requesting the site, so we save our first 
coordinate and now this new 2nd point. The bot then clicks the zoom out button 1 time for a perfect screenshot.
the bot saves our screenshot with todays date. We can then use crontab to schedule this script to be ran every 24
hours to collect daily Satellite Images from specific geolocations.

@author: Antonio Hickey
"""
#---------------------------------------------------------------------------------------------------------------------------
# Importing Python Modules
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as wd
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import ast
import datetime
import sys
from sys import argv, exit
import time
#-----------------------------------------------------------------------------------------------------------------------------------
# Browser Path
PATH = "/home/sratus/Desktop/API/chromedriver"
# Browser Config
options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument('headless') # For Production Use
options.add_argument('window-size=1200x600') # For Production Use
# driver = webdriver.Chrome(chrome_options=options) # For dev use with IDE
driver = webdriver.Chrome(ChromeDriverManager().install()) # For Production use
#-----------------------------------------------------------------------------------------------------------------------------------
# Defining Function
def Indian_Base():
    # Actions 
    actionChains = wd(driver)
    # Requesting Twitter
    driver.get('https://earthexplorer.usgs.gov/')
    # Opening Coordinates Panel
    Coord1_Panel = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div[2]/div[1]/div[4]/div[1]/div[3]/input[2]")
    Coord1_Panel.click()
    # Point 1
    ###1. Latitude
    Lat_1a = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[1]/input")
    Lat_1a.send_keys("33")
    Lat_1b = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[2]/input")
    Lat_1b.send_keys("44")
    Lat_1c = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[3]/input")
    Lat_1c.send_keys("25")
    ###1. Longitude
    Lon_1a = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[1]/input")
    Lon_1a.send_keys("078")
    Lon_1b = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[2]/input")
    Lon_1b.send_keys("44")
    Lon_1c = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[3]/input")
    Lon_1c.send_keys("46")
    Lon_1d = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/select")
    Lon_1d.click()
    Lon_1e = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/select/option[2]")
    Lon_1e.click()
    # Adding Coordinate
    Add_1 = driver.find_element_by_xpath("/html/body/div[10]/div[3]/div/button[1]")
    Add_1.click()
    
    # Opening Coordinates Panel
    Coord2_Panel = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div[2]/div[1]/div[4]/div[1]/div[3]/input[2]")
    Coord2_Panel.click()
    
    # Point 2
    ###2. Latitude
    Lat_2a = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[1]/input")
    Lat_2a.send_keys("33")
    Lat_2b = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[2]/input")
    Lat_2b.send_keys("44")
    Lat_2c = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[3]/input")
    Lat_2c.send_keys("26")
    ###1. Longitude
    Lon_2a = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[1]/input")
    Lon_2a.send_keys("078")
    Lon_2b = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[2]/input")
    Lon_2b.send_keys("45")
    Lon_2c = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[3]/input")
    Lon_2c.send_keys("03")
    Lon_2d = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/select")
    Lon_2d.click()
    Lon_2e = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/select/option[2]")
    Lon_2e.click()
    # Adding Coordinate
    Add_2 = driver.find_element_by_xpath("/html/body/div[10]/div[3]/div/button[1]")
    Add_2.click()
    
    # Zoom out for Screenshot
    zoom_out = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/a[2]")
    zoom_out.click()
    
    # Define x Date
    date_string = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Take Screenshot
    time.sleep(2)
    driver.save_screenshot('/home/sratus/Desktop/OSINT/Satellite Images By Region/India' + date_string + '.png')
#-----------------------------------------------------------------------------------------------------------------------------------
def China_Base():
    # Actions 
    actionChains = wd(driver)
    # Requesting Twitter
    driver.get('https://earthexplorer.usgs.gov/')
    # Opening Coordinates Panel
    Coord1_Panel = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div[2]/div[1]/div[4]/div[1]/div[3]/input[2]")
    Coord1_Panel.click()
    # 1
    ###1. Latitude
    Lat_1a = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[1]/input")
    Lat_1a.send_keys("33")
    Lat_1b = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[2]/input")
    Lat_1b.send_keys("44")
    Lat_1c = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[3]/input")
    Lat_1c.send_keys("25")
    ###1. Longitude
    Lon_1a = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[1]/input")
    Lon_1a.send_keys("078")
    Lon_1b = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[2]/input")
    Lon_1b.send_keys("52")
    Lon_1c = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[3]/input")
    Lon_1c.send_keys("35")
    Lon_1d = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/select")
    Lon_1d.click()
    Lon_1e = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/select/option[2]")
    Lon_1e.click()
    # Adding Coordinate
    Add_1 = driver.find_element_by_xpath("/html/body/div[10]/div[3]/div/button[1]")
    Add_1.click()
    
    # 2
    ###2. Opening Coordinates Panel
    Coord2_Panel = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div[2]/div[1]/div[4]/div[1]/div[3]/input[2]")
    Coord2_Panel.click()
    ###2. Latitude
    Lat_2a = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[1]/input")
    Lat_2a.send_keys("33")
    Lat_2b = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[2]/input")
    Lat_2b.send_keys("44")
    Lat_2c = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/label[3]/input")
    Lat_2c.send_keys("25")
    ###2. Longitude
    Lon_2a = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[1]/input")
    Lon_2a.send_keys("078")
    Lon_2b = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[2]/input")
    Lon_2b.send_keys("52")
    Lon_2c = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/label[3]/input")
    Lon_2c.send_keys("36")
    Lon_2d = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/select")
    Lon_2d.click()
    Lon_2e = driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[5]/select/option[2]")
    Lon_2e.click()
    # Adding Coordinate
    Add_2 = driver.find_element_by_xpath("/html/body/div[10]/div[3]/div/button[1]")
    Add_2.click()
    
    # Zoom out for Screenshot
    zoom_out = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/a[2]")
    zoom_out.click()
    
    # Define x Date
    date_string = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Take Screenshot
    time.sleep(2)
    driver.save_screenshot('/home/sratus/Desktop/OSINT/Satellite Images By Region/China-' + date_string + '.png')
#-----------------------------------------------------------------------------------------------------------------------------------
# Running The Functions
Indian_Base()
time.sleep(1) # Use this to give a small pause interval
China_Base()

