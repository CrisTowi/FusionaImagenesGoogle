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

    r = requests.get(BASE_URL % start)
    image_info = json.loads(r.text)['responseData']['results'][0]
    url = image_info['unescapedUrl']
    try:
        image_r = requests.get(url)
    except ConnectionError, e:
        print 'could not download %s' % url

    title = query

    file = open(os.path.join(BASE_PATH, '%s.png') % title, 'w')
    try:
        Image.open(StringIO(image_r.content)).save(file, 'PNG')
    except IOError, e:

        print 'could not save %s' % url
    finally:
        file.close()

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

def get_lista_imagenes():
    lista_imagenes_string = []
    lista_imagenes = []
    for file in os.listdir("MiNuevaCarpeta"):
        if file.endswith(".png"):
            lista_imagenes_string.append(str(file))

    for string_imagen in lista_imagenes_string:
        im = Image.open('MiNuevaCarpeta/' + string_imagen)
        print im

        lista_imagenes.append(im)

    return lista_imagenes

def junta_imagenes():
    lista_matrices = []
    lista_imagenes = get_lista_imagenes()

    for imagen_obj in lista_imagenes:
        lista_matrices.append(imagen_obj.load())

    imagen_blanca = Image.open('imagen_blanca.png')
    pix = imagen_blanca.load()
    imagen_actual = 0

    for i in range(imagen_blanca.size[0]):
        for j in range(imagen_blanca.size[1]):

            if i >= lista_imagenes[imagen_actual].size[0]:
                break;
            elif j >= lista_imagenes[imagen_actual].size[1]:
                break;
            else:
                pix[i,j] = lista_matrices[imagen_actual][i,j]
        
        if i % 50 == 0:
            imagen_actual = imagen_actual + 1
            if imagen_actual == len(lista_imagenes) - 1:
                imagen_actual = 0

    imagen_blanca.save('salida.jpg')


arreglo_tts = get_tt()

for palabra in arreglo_tts:
    palabra=palabra.replace('#','')
    palabra=palabra.replace(' ','')
    print palabra
    go(palabra)

crea_imagen_blanca(1600,1600,'imagen_blanca.png')
junta_imagenes()