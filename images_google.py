import json
import os
import time
import requests
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError
 
def go(query, path):

  BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
             'v=1.0&q=' + query + '&start=%d'
 
  BASE_PATH = os.path.join(path, query)
 
  if not os.path.exists(BASE_PATH):
    os.makedirs(BASE_PATH)
 
  start = 0
  while start < 1:
    r = requests.get(BASE_URL % start)
    for image_info in json.loads(r.text)['responseData']['results']:
      url = image_info['unescapedUrl']
      try:
        image_r = requests.get(url)
      except ConnectionError, e:
        print 'could not download %s' % url
        continue

      title = image_info['titleNoFormatting'].replace('/', '').replace('\\', '')
 
      file = open(os.path.join(BASE_PATH, '%s.png') % title, 'w')
      try:
        Image.open(StringIO(image_r.content)).save(file, 'PNG')
      except IOError, e:

        print 'could not save %s' % url
        continue
      finally:
        file.close()
 
    print start
    start += 1

    time.sleep(1.5)
 
go('starcraft2', 'miCarpeta')