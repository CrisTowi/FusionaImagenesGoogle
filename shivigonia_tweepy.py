## import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

## CONSUMER_KEY = 'pQtGAqxQliLOdnGKsU0qzrjbX'
## CONSUMER_SECRET = 'sTYvYJICAaPOHYpMoCXJmwM8ocaKKn0WDXOomdyhgGCm1tkub9'
## OAUTH_TOKEN = '143325223-CFTV9dSrKZ2IKDiWFStEDd9OEFApFKxHc6PjuggQ'
## OAUTH_TOKEN_SECRET = 'Mef73sLDKCVOlb6QJEkMd6sH36CSCWDku8FMxJsPjunuG'

#auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
##                           CONSUMER_KEY, CONSUMER_SECRET)

##twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

## print twitter_api


from __future__ import absolute_import, print_function

import tweepy


# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="pQtGAqxQliLOdnGKsU0qzrjbX"
consumer_secret="sTYvYJICAaPOHYpMoCXJmwM8ocaKKn0WDXOomdyhgGCm1tkub9"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="143325223-CFTV9dSrKZ2IKDiWFStEDd9OEFApFKxHc6PjuggQ"
access_token_secret="Mef73sLDKCVOlb6QJEkMd6sH36CSCWDku8FMxJsPjunuG"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps





# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

##WORLD_WOE_ID = 1
##MX_WOE_ID = 23424900

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

##world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
##mx_trends = twitter_api.trends.place(_id=MX_WOE_ID)

##print world_trends
##print
##print mx_trends

##import json

##print json.dumps(world_trends, indent=1)
##print
##print json.dumps(mx_trends, indent=1)


