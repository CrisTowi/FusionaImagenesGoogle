import json
import os
import time
import requests
from PIL import Image
from StringIO import StringIO
from requests.exceptions import ConnectionError
import twitter

def go(query):
    
    path = 'MiNuevaCarpeta'
    
    BASE_URL = 'https://ajax.googleapis.com/ajax/services/search/images?'\
             'v=1.0&q=' + query + '&start=%d&tbs=isz:m'
    BASE_PATH = os.path.join(path, '')

    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)
    start = 0
    while start < 1:
        r = requests.get(BASE_URL % start)
        image_info = json.loads(r.text)['responseData']['results'][0]
        url = image_info['unescapedUrl']
        try:
            image_r = requests.get(url)
        except ConnectionError, e:
            print 'could not download %s' % url
            continue

        title = image_info['titleNoFormatting'].replace('/', '').replace('\\', '')

        file = open(os.path.join(BASE_PATH, '%s.jpg') % title, 'w')
        try:
            Image.open(StringIO(image_r.content)).save(file, 'JPGE')
        except IOError, e:

            print 'could not save %s' % url
            continue
        finally:
            file.close()
        start += 1

        time.sleep(1.5)

def cambia_imagen():
    im = Image.open("imagen.jpg") #Can be many different formats.
    pix = im.load()
    print pix
    print im.size #Get the width and hight of the image for iterating over

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pix[i,j] = (pix[i,j][0] + 150, pix[i,j][1] + 150, pix[i,j][2] + 150)

    im.save('salida.jpg')

    im2 = Image()
    print im2

def crea_imagen_blanca(x_tam, y_tam, nombre):
    white = (255,255,255)
    img = Image.new("RGB", [x_tam,y_tam], white)
    img.save(nombre)


def get_tt():
    #Credenciales del API de twitter
    CONSUMER_KEY = 'pQtGAqxQliLOdnGKsU0qzrjbX'
    CONSUMER_SECRET = 'sTYvYJICAaPOHYpMoCXJmwM8ocaKKn0WDXOomdyhgGCm1tkub9'
    OAUTH_TOKEN = '143325223-CFTV9dSrKZ2IKDiWFStEDd9OEFApFKxHc6PjuggQ'
    OAUTH_TOKEN_SECRET = 'Mef73sLDKCVOlb6QJEkMd6sH36CSCWDku8FMxJsPjunuG'

    #Autenticacion para tener acceso al API
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    #Obtiene el objeto API mandandole como parametro el token de autenticacion
    twitter_api = twitter.Twitter(auth=auth)

    #WORLD_WOE_ID = 1
    MX_WOE_ID = 23424900

    #Obtienes los TT de Mexico
    mx_trends = twitter_api.trends.place(_id=MX_WOE_ID)

    trends = mx_trends[0]

    arreglo = []

    for trend in trends['trends']:
        arreglo.append(trend['name'])

    return arreglo

arreglo = get_tt()

for palabra in arreglo:
    palabra=palabra.replace('#','')
    print palabra
    go(palabra)


