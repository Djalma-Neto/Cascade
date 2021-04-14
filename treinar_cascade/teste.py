numEst  = 

try:
    numEst = int(input('valor'))
except:
    pass

numEst = numEst if numEst else 10
print(numEst)