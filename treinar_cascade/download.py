import os
import requests
import json

# vai criar um arquivo onde será guardado as imagens baixadas
if not os.path.exists('./amostras'):
    os.makedirs('amostras')

# nova requisição usando HTTP request (testado no postman)
# https://unsplash.com/napi/search?query=montanhas&per_page=20&plus=none
def getURL():
    array = []
    for x in range(10):
        URL = "https://unsplash.com/napi/search/photos?query=montanhas&per_page=20&page={0}&plus=none".format(x)
        data = json.loads(requests.get(URL, stream=True).content)
        
        for x in data['results']:
            array.append(x['links']['download'])
        
    return array

def getImages(array):
    for x in range(len(array)):
        with open('./amostras/img{0}.jpg'.format(x), 'wb') as handle:
            response = requests.get(array[x], stream=True)
            if not response.ok: print(response)
            for block in response.iter_content(1024):
                if not block: break
                handle.write(block)

array = getURL()
getImages(array)
# print("CRIAÇÃO DE BANCO DE IMAGENS FINALIZADO !!!")