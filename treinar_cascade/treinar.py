import os

if not os.path.exists('./data'):
    os.makedirs('data')

numPos = round((len(os.listdir("negativas"))*len(os.listdir("positivas")))-200)
numNeg = round(len(os.listdir("negativas"))/2)

comando = "opencv_traincascade -data data -vec positivas.vec -bg bg.txt -numPos {0} -numNeg {1} -numStages 9 -w 20 -h 20".format(numPos,numNeg)
os.system(comando)

os.system("py detectar.py")