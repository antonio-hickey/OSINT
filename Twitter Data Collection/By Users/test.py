"""
Created on Mon Jun 29 01:58:28 2020

This is how we use twint(https://git.io/JfdTX), to collect twitter data filtered by usernames.

- Function to collect twitter data from Donald Trump
- Function to collect twitter data from Joe Biden

@author: Antonio Hickey
"""

import twint

def trump():
    #Config
    c = twint.Config()
    c.Username = 'realDonaldTrump'
    c.Limit = 50
    c.Output = 'test_t.csv'
    # Run
    twint.run.Search(c)
trump()
def biden():
    #Config
    c = twint.Config()
    c.Username = 'JoeBiden'
    c.Output = 'test_b.csv'
    c.Limit = 50
    # Run
    twint.run.Search(c)
biden()
print('Collected Data outputed to test_t.csv and test_b.csv')
