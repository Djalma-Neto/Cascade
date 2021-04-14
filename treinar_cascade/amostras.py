import os

cont = 1
positivas = 0

num = 0
for x in os.listdir('negativas'):
    num += 1

#criar varias amostras com as imagens positivas
for img in os.listdir('positivas'):
    imgDir = 'positivas/'+img
    infosDir = 'infos/info{0}/info.lst'.format(cont)
    comando = ('opencv_createsamples -img {0} -bg bg.txt -info {1} -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num {2}'.format(imgDir, infosDir, num))
    os.system(comando)
    cont +=1

print("AMOSTRAS FINALIZADAS !!!")
