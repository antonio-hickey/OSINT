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