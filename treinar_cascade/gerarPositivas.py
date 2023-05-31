import cv2
import os

if not os.path.exists('./positivas'):
    os.makedirs('positivas')

for x in os.listdir("objetos"):
    try:
        img = cv2.imread("./objetos/{0}".format(x),cv2.IMREAD_GRAYSCALE)
        imagem_redimensionada = cv2.resize(img, (100,55))
        cv2.imwrite("./positivas/{0}".format(x), imagem_redimensionada)
    except Exception as e:
        print(str(e))

# cria lista em txt com o endereço das imagens
for file_type in ["negativas"]:
    for x in os.listdir(file_type):
        try:
            line = "./{0}/{1}\n".format(file_type,x)

            with open('bg.txt','a') as f:
                f.write(line)

        except Exception as e:
            print(str(e))
print("IMAGENS POSITIVAS GERADAS!")