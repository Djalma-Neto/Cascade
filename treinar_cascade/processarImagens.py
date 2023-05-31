import cv2
import os

if not os.path.exists('./negativas'):
    os.makedirs('negativas')
if not os.path.exists('./objetos'):
    os.makedirs('objetos')

for x in os.listdir("amostras"):
    try:
        img = cv2.imread("./amostras/{0}".format(x),cv2.IMREAD_GRAYSCALE)
        imagem_redimensionada = cv2.resize(img, (300,300))
        cv2.imwrite("./negativas/{0}".format(x), imagem_redimensionada)
    except Exception as e:
        print(str(e))
print("IMAGENS OPTIMIZADAS!")