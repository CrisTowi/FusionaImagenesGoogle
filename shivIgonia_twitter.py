import twitter

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

CONSUMER_KEY = 'pQtGAqxQliLOdnGKsU0qzrjbX'
CONSUMER_SECRET = 'sTYvYJICAaPOHYpMoCXJmwM8ocaKKn0WDXOomdyhgGCm1tkub9'
OAUTH_TOKEN = '143325223-CFTV9dSrKZ2IKDiWFStEDd9OEFApFKxHc6PjuggQ'
OAUTH_TOKEN_SECRET = 'Mef73sLDKCVOlb6QJEkMd6sH36CSCWDku8FMxJsPjunuG'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print twitter_api


# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
MX_WOE_ID = 23424900

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
mx_trends = twitter_api.trends.place(_id=MX_WOE_ID)

print world_trends
print
print mx_trends

import json

print json.dumps(world_trends, indent=1)
print
print json.dumps(mx_trends, indent=1)

