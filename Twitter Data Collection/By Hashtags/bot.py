#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 02:13:03 2020

@author: Antonio Hickey
"""
import twint

def SouthChinaSea():
    c = twint.Config()
    c.Search = '#SouthChinaSea'
    c.Output = '/home/sratus/Desktop/OSINT/Twitter/Twitter Hashtags By Region/SouthChinaSea/SouthChinaSea.csv'
    c.Limit = 50
    c.Media = True
    twint.run.Search(c)
SouthChinaSea()

def ChinaNavy():
    c = twint.Config()
    c.Search = '#China AND #PLAN'
    c.Output = '/home/sratus/Desktop/OSINT/Twitter/Twitter Hashtags By Region/SouthChinaSea/ChineseNavy.csv'
    c.Limit = 50
    c.Media = True
    twint.run.Search(c)    
ChinaNavy()

def USNavy7():
    c = twint.Config()
    c.Search = '#USNavy AND #US7thFlt'
    c.Output = '/home/sratus/Desktop/OSINT/Twitter/Twitter Hashtags By Region/SouthChinaSea/USNavy7.csv'
    c.Limit = 50
    c.Media = True
    twint.run.Search(c)  
USNavy7()    