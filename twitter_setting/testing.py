import tweepy

auth = tweepy.OAuthHandler(370KZlaxktnVE8J4vCDti1yti,vCUR4w0BDcsvQpagrKYzo0UVTqt5MIBAJL0kqrJTvNo7uIhLMW)
auth.set_access_token(353981251-U5cdsiVYurRRn3PsHsv4KGfcz4U6OKGUCxTqLWtr, OIwdiDLR7OTtdt3dfRfEtMScWaHg0N7ztSTnVAeu4cmOG)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text