import os

numNeg = len(os.listdir('negativas'))
cont = 1

#criar os arquivos de vetores
for vect in os.listdir('infos'):
    vecDir = 'infos/{0}/info.lst'.format(vect)
    infosDir = 'vetores/positives{0}.vec'.format(cont)
    comando = ('opencv_createsamples -info {0} -num {1} -w 20 -h 20 -vec {2}'.format(vecDir, numNeg, infosDir))
    os.system(comando)
    cont += 1

os.system('python3  mergevec.py -v vetores -o positives.vec')

print("VETORES CRIADOS !!!")
