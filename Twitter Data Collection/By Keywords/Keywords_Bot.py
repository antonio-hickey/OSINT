import twint

def test(): # Creating Function
    c = twint.Config() # Defining Configure
    c.Search = 'test' # Keyword to search for
    c.Output = '/home/sratus/Desktop/OSINT/Twitter/Twitter Keywords By Region/test.csv' # Output
    c.Limit = 50 # Limit amount of tweets collected
    twint.run.Search(c) # Running the data collection
test() # Running the function

def test1():
    c = twint.Config()
    c.Search = 'breaking AND news' # Filter Tweets with both Keywords 
    c.Output = '/home/sratus/Desktop/OSINT/Twitter/Twitter Keywords By Region/test1.csv'
    c.Limit = 50
    twint.run.Search(c)
test1()

def test2():
    c = twint.Config()
    c.Search = 'breaking OR just in' # Filter tweets with one or both Keywords
    c.Output = '/home/sratus/Desktop/OSINT/Twitter/Twitter Keywords By Region/test2.csv'
    c.Limit = 50
    twint.run.Search(c)
test2()