#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:58:28 2020

@author: Antonio Hickey
"""
import twint
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Users
def Yusuf_Bot():
    # Configure
    c = twint.Config()
    c.Username = "YusufDFI"
    c.Output = '/home/testing/7-07-20/Yusuf.csv'
    c.Limit = 50
    c.Lang = "en"
    c.Translate = True
    c.TranslateDest = "it"
    c.Media = True
    # Run
    twint.run.Search(c)
Yusuf_Bot()
def SuperPowerChina():
    # Configure
    c = twint.Config()
    c.Username = "SuperPowerChina"
    c.Output = '/home/testing/7-07-20/SPC-China.csv'
    c.Limit = 50
    c.Lang = "en"
    c.Translate = True
    c.TranslateDest = "it"
    c.Media = True
    # Run
    twint.run.Search(c)
SuperPowerChina()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# By Location
def Ladakh():
    c = twint.Config()
    c.Geo = '33.898818,78.662491,50km' 
    c.Search = 'china OR india OR ww3 OR dead OR killed OR fight' 
    c.Output = '/home/testing/7-07-20/Ladakh China.csv' 
    c.Limit = 50 
    c.Media = True 
    twint.run.Search(c) 
Ladakh()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# By Hashtag
def Ladakh2():
    # Configure
    c = twint.Config()
    c.Search = "#Ladakh"
    c.Output = '/home/testing/7-07-20/Ladakh.csv'
    c.Limit = 50
    c.Media = True
    # Run
    twint.run.Search(c)
Ladakh2()    
def IndiaChina():
    # Configure
    c = twint.Config()
    c.Search = "#IndiaChina"
    c.Output = '/home/testing/7-07-20/Twitter Hashtags By Region/India-China/IndiaChina.csv'
    c.Limit = 50
    c.Media = True
    # Run
    twint.run.Search(c)
IndiaChina()    
def IndianArmy():
    # Configure
    c = twint.Config()
    c.Search = "#IndianArmy"
    c.Output = '/home/testing/7-07-20/IndianArmy.csv'
    c.Limit = 50
    c.Lang = "en"
    c.Media = True
    # Run
    twint.run.Search(c)
IndianArmy()
def Galwan():
    # Configure
    c = twint.Config()
    c.Search = "#Galwan"
    c.Output = '/home/testing/7-07-20//Galwan.csv'
    c.Limit = 50
    c.Media = True
    # Run
    twint.run.Search(c)
Galwan()
def Sikkim():
    # Configure
    c = twint.Config()
    c.Search = "#Sikkim"
    c.Output = '/home/testing/7-07-20/Sikkim.csv'
    c.Limit = 50
    c.Media = True
    # Run
    twint.run.Search(c)    
Sikkim()
#-------------------------------------------------------------------------------------------------------------------------

