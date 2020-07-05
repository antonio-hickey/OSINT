#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 02:50:09 2020

Python script for collecting data via twitter by filtering for specific data
using Geo Locations, Keywords, and if the tweet contains media.

Using python module twint makes this proccess very easy. Visit  https://git.io/JfdTX
for more information on the twint project.

@author: Antonio Hickey
"""
import twint

# Creating Function to filter tweets by geolocation and if they have media
def Ladakh():
    c = twint.Config() # Defining  Twint Config
    c.Geo = '33.898818,78.662491,50km' # Tweets from near this geolocation
    c.Search = 'china OR india OR ww3 OR dead OR killed OR fight' # Filter for keywords
    c.Output = '/home/sratus/Desktop/OSINT/Twitter/By Locations/Ladakh/Ladakh China.csv' # Output
    c.Limit = 50 # Limit Tweets to keep it lightwieght for multiple deployments
    c.Media = True # Only include tweets with images and or videos
    twint.run.Search(c) # Deploying the search
Ladakh()

def HongKong():
    c = twint.Config()
    c.Geo = '22.324595,114.170532,50km'
    c.Search = 'breaking OR dead OR killed OR mass OR ccp OR pla'
    c.Output = '/home/sratus/Desktop/OSINT/Twitter/By Locations/Ladakh/Hong Kong.csv'
    c.Limit = 50
    c.Media = True
    twint.run.Search(c)
HongKong()

# Creating a very specific location search
def Specific_Location():
    c = twint.Config()
    c.Geo = '32.782257, -86.874614,1km' # Tweets within 1km of the Geo Location
    c.Output = '/home/sratus/Desktop/OSINT/Twitter/By Locations/Ladakh/test0.csv'
    c.Limit = 50
    c.Media = True
    twint.run.Search(c)
Specific_Location()

