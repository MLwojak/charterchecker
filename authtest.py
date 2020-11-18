# This file is used to verify the ability to authenticate against the API. Replace the strings with your API and access token keys.

import tweepy

auth = tweepy.OAuthHandler("API KEYS","API KEYS")
auth.set_access_token("ACCESS TOKENS", "ACCESS TOKENS")
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
