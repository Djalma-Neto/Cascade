import cv2
import os

if not os.path.exists('./negativas'):
    os.makedirs('negativas')
if not os.path.exists('./positivas'):
    os.makedirs('positivas')
if not os.path.exists('./objetos'):
    os.makedirs('objetos')

for x in os.listdir("amostras"):
    try:
        img = cv2.imread("./amostras/{0}".format(x),cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (300,300))
        # img = cv2.GaussianBlur(img, (5,5),0)
        cv2.imwrite("./negativas/{0}".format(x), img)
    except Exception as e:
        print(str(e))

for x in os.listdir("objetos"):
    try:
        img = cv2.imread("./objetos/{0}".format(x), cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (300,180))
        # img = cv2.GaussianBlur(img, (5,5),0)
        cv2.imwrite("./positivas/{0}".format(x), img)
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

num = len(os.listdir("negativas"))
for x in range(len(os.listdir("positivas"))):
    try:
        img = os.listdir("positivas")[x]
        infoDir = "info/{0}/info.lst".format(x)
        comando = "opencv_createsamples -img ./positivas/{0} -bg bg.txt -info {1} -pngoutput info -bgcolor 0 -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num {2}".format(img,infoDir,num)
        os.system(comando)
    except Exception as e:
        print(str(e))

if(len(os.listdir("info")) > 1):
    for x in range(len(os.listdir("info"))):
        try:
            list = os.listdir("info")[x]
            infoDir = "info/{0}/info.lst".format(x)
            comando = "opencv_createsamples -info {0} -num {1} -w 30 -h 16 -vec vecs/positives{2}.vec".format(infoDir,num,x)
            os.system(comando)
        except Exception as e:
            print(str(e))
    comando = "py mergevec.py -v vecs -o positivas.vec"
    os.system(comando)
else:
    comando = "opencv_createsamples -info info/0/info.lst -num {0} -w 30 -h 16 -vec positivas.vec".format(num)
    os.system(comando)