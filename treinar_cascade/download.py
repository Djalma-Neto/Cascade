import urllib
import numpy as np
import cv2
import os

if not os.path.exists('infos'):
    os.makedirs('infos')

if not os.path.exists('vetores'):
    os.makedirs('vetores')
    
if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.exists('positivas'):
    os.makedirs('positivas')

if not os.path.exists('feias'):
    os.makedirs('feias')

if not os.path.exists('negativas'):
    os.makedirs('negativas')

    link_imagens_negativas = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    urls_imagens_negativas = urllib.urlopen(link_imagens_negativas).read().decode()

    numero_imagem = 1

    for i in urls_imagens_negativas.splitlines():
        try:
            print(i)
            urllib.urlretrieve(i, "negativas/"+str(numero_imagem)+".jpg")
            img = cv2.imread("negativas/"+str(numero_imagem)+".jpg",cv2.IMREAD_GRAYSCALE)
            imagem_redimensionada = cv2.resize(img, (100,100))
            cv2.imwrite("negativas/"+str(numero_imagem)+".jpg",imagem_redimensionada)
            numero_imagem += 1
        except Exception as e:
            print(str(e))
print("DOWNLOAD FINALIZADO !!!")