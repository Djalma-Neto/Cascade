import os
import cv2

for x in range(len(os.listdir("positivas"))):
    try:
        img = os.listdir("positivas")[x]
        infoDir = "info/{0}/info.lst".format(x)
        comando = "opencv_createsamples -img .positivas/{0} -bg bg.txt -info {1} -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 200".format(img,infoDir)
        os.system(comando)
    except Exception as e:
        print(str(e))