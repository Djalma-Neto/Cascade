import os

numEst = ''
numPos = len(os.listdir('positivas'))
numNeg = len(os.listdir('negativas'))

for x in range(10):
    print(".")

print('////////////////////////////////')
print('numPos: ',int(numPos))
print('numNeg: ',int(numNeg))
print('////////////////////////////////')

try:
    numEst = int(input('Estagios(minimo 10): '))
except:
    pass

numEst = numEst if numEst else 10

comando = 'opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos {0} -numNeg {1} -numStages {2} -w 20 -h 20'.format(numPos, numNeg, numEst)
os.system(comando)

print("TREINAMENTO FINALIZADO !!!")