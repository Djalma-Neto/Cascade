import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def equalizar(img):
    L = img.shape[0]
    C = img.shape[1]
    totalPixel = L*C
    values = []
    for l in range(0,L):
        for c in range(0,C):
            values.append(img[l,c])
    probabilidade = {}
    probaCum = {}
    sumProb = 0
    newImage =np.zeros((L,C), dtype=np.uint8)

   # calculando probabilidade
    for x in range(0,256):
        prob = values.count(x)/totalPixel
        probabilidade[str(x)] = prob

    # calculando probabilidade cumulativa
    for x in range(0,256):
        if(x>0):
            sumProb += probabilidade[str(x)]
        probaCum[str(x)] = sumProb

    # cirando as novas intencidades
    for l in range(0,L):
        for c in range(0,C):
             newImage[l,c] = probaCum[str(img[l,c])]*255
    return newImage

def graficoHistogramaCumulativo(img, titulo='Histograma Cumulativo'):
    L = img.shape[0]
    C = img.shape[1]
    totalPixel = L*C
    values = []
    for l in range(0,L):
        for c in range(0,C):
            values.append(img[l,c])

    # newValues = []
    newValues = np.arange(256)
    probabilidade = {}
    probaCum = []
    sumProb = 0
    
    # calculando probabilidade
    for x in range(0,256):
        prob = values.count(x)/totalPixel
        probabilidade[str(x)] = prob

    # calculando probabilidade cumulativa
    for x in range(0,256):
        if(x>0):
            sumProb += probabilidade[str(x-1)]
        probaCum.append(sumProb+probabilidade[str(x)])

    figure = plt.figure(figsize=(10,5)).add_subplot(111)
    # figure.set_ylim(0,300)
    figure.set_xlim(0,300)
    
    plt.title(titulo)
    plt.xlabel('Intencidade')
    plt.ylabel('Frequência Cumulativa')
    
    plt.plot(newValues,probaCum,color = '#adadad') # type: ignore
    plt.show()

def equalizarTranslacao(img,titulo='Histograma Translação'):
    L = img.shape[0]
    C = img.shape[1]
    newImage = np.zeros((L,C), dtype=np.uint8)
    values = []
    for l in range(0,L):
        for c in range(0,C):
            values.append(img[l,c])

    valueMin = min(values)
    valueMax = max(values)-valueMin
    value = (((255-valueMax)*100)/valueMax)/100
    
    # translata a intencidade da imagem de forma que comece em 0
    for l in range(0,L):
        for c in range(0,C):
            val = img[l,c]-valueMin
            val = math.ceil(val+(val*value))
            newImage[l,c] = 255 if(val>255) else 0 if(val<0) else val
    return newImage

def graficoHistograma(img, titulo='Histograma'):
    L = img.shape[0]
    C = img.shape[1]
    values = []
    for l in range(0,L):
        for c in range(0,C):
            values.append(img[l,c])

    newValues = list(set(values))
    frequencias = []
    
    for x in newValues:
        frequencias.append(values.count(x))

    figure = plt.figure(figsize=(10,5)).add_subplot(111)
    # figure.set_ylim(0,300)
    figure.set_xlim(0,300)
    
    plt.title(titulo)
    plt.xlabel('Frequencia')
    plt.ylabel('Intencidade')
    
    # plt.scatter(frequencias,newValues, color = '#adadad', marker = '.', s = 30) # type: ignore
    # plt.bar(newValues,frequencias,color = '#adadad',width=width) # type: ignore
    plt.plot(newValues,frequencias,color = '#adadad') # type: ignore
    
    plt.show()
    return frequencias, newValues

def redimencionar(imagem):
	L = imagem.shape[0]
	C = imagem.shape[1]
	C = C if C%2==0 else C-1
	L = L if L%2==0 else L-1

	reducao = 50 # valor em %

	print('Altura {0}'.format(L))
	print('Largura {0}'.format(C))

	newL = int(L*(reducao/100))
	newC = int(C*(reducao/100))

	newImage = np.zeros((newL,newC), dtype=np.uint8)
	newL = newImage.shape[0]
	newC = newImage.shape[1]

	print('Nova Altura {0}'.format(newL))
	print('Nova Largura {0}'.format(newC))

	countL = 0
	countC = 0
	media = 0

	for l in range(0,L,2):
		for c in range(0,C,2):
			coordenadas = [
				[l-1,c-1],[l-1,c],[l-1,c+1],[l+1,c-1],[l+1,c],[l+1,c+1],[l,c-1],[l,c+1],[l,c]
			]
			cord = []

			for x in range(len(coordenadas)):
				cord = coordenadas[x]
				if(cord[0]>=0 and cord[1]>=0 or cord[0]<=L and cord[1]<=C):
					media = media+int(imagem[cord[0],cord[1]])
			media = media/9
			newImage[countL-1,countC-1] = int(media)
			media = 0
			countC = countC+1
		countC = 0
		countL = countL+1

	# print(media)
	return newImage

def escalaCinza(imagem):
	L = imagem.shape[0]
	C = imagem.shape[1]
	newImage = np.zeros((L,C), dtype=np.uint8)

	for l in range (L):
		for c in range(C):
			(b,g,r) = imagem[l,c]
			
			r = r*0.7
			g = g*0.7
			b = b*0.7
			gray = (b+g+r)/3

			# newImage[l,c] = (b,g,r)
			newImage[l,c] = gray
	return newImage

def blurred(imagem):
    L = imagem.shape[0]
    C = imagem.shape[1]
    newImage = np.zeros((L,C), dtype=np.uint8)
    for l in range(0,L):
        for c in range(0,C):
            newVal = 0
            coordenadas = [
                [l-2,c-2],[l-2,c-1],[l-2,c],[l-2,c+1],[l-2,c+2],
                [l-1,c-2],[l-1,c-1],[l-1,c],[l-1,c+1],[l-1,c+2],
                [l,c-2],[l,c-1],[l,c],[l,c+1],[l,c+2],
                [l+1,c-2],[l+1,c-1],[l+1,c],[l+1,c+1],[l+1,c+2],
                [l+2,c-2],[l+2,c-1],[l+2,c],[l+2,c+1],[l+2,c+2],
            ]
            pesos = [2,4,5,4,2,
                       4,9,12,9,4,
                       5,12,15,2,5,
                        4,9,12,9,4,
                        2,4,5,4,2]
            for x in range(len(coordenadas)):
                val = coordenadas[x]
                if(val[0]>=0 and val[1]>=0 and val[0]<L and val[1]<C):
                    newVal += imagem[val[0],val[1]]*(pesos[x]/100)
            newVal = int(newVal)
            newVal = 255 if(newVal>255) else newVal #limitando para não ultrapassar o valor de 255
            newImage[l,c] = newVal
    return newImage

def gerEdges(img):
    L = imagem.shape[0]
    C = imagem.shape[1]
    newImage = np.zeros((L,C), dtype=np.uint8)
    fp = 23
    for l in range(1,L-1):
        for c in range(1,C-1):
            coordenadas = [[l,c-1],[l-1,c]]
            for cord in coordenadas:
                lin = cord[0]
                col = cord[1]
                if(img[lin,col] >= img[l,c]-fp and img[lin,col] <= img[l,c]+fp):
                    newImage[l,c] = newImage[l,c]
                else:
                     newImage[l,c] = 255
    return newImage
# ================================================= Dimensão ===========================================

# imagem = cv2.imread('caneca.jpg')
# imagem = cv2.imread('canecaM.jpg')
# imagem1 = escalaCinza(imagem)
# imagem2 = redimencionar(imagem1)
# imagem3 = redimencionar(imagem2)

# cv2.imshow('Original', imagem1)
# cv2.imshow('Modificada 50%', imagem2)
# cv2.imshow('Modificada 25%', imagem3)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ========================================== Equalização Translação ======================================
# imagem = cv2.imread('canecaM.jpg')
# imagem = escalaCinza(imagem)

# imagem2 = equalizarTranslacao(imagem)

# cv2.imshow('Original',imagem)
# cv2.imshow('Equalizada',imagem2)
# graficoHistograma(imagem, 'Imagem Original Histograma')
# graficoHistograma(imagem2, 'Imagem Equalizada Histograma')


#================================================ Equalização =============================================

# imagem = cv2.imread('paisagem.jpeg')
# imagem = cv2.imread('canecaM.jpg')
# imagem = escalaCinza(imagem)

# cv2.imshow('Escala de cinza',imagem)
# graficoHistograma(imagem, 'Imagem Original Histograma')
# graficoHistogramaCumulativo(imagem, 'Imagem Original Histograma Cumulativo')
# cv2.destroyAllWindows()

# imagem2 = equalizar(imagem)
# cv2.imshow('Equalizada',imagem2)
# graficoHistograma(imagem2, 'Imagem Equalizada Histograma')
# graficoHistogramaCumulativo(imagem2, 'Imagem Equalizada Histograma Cumulativo')

# cv2.imshow('Escala de cinza',imagem)
# cv2.imshow('Imagem Equalizada',imagem2)

# ==================================================== Bordas ===============================================
# imagem = cv2.imread('paisagem.jpeg')
# imagem = cv2.imread('canecaM.jpg')
imagem = cv2.imread('estrada.jpg')
imagem = escalaCinza(imagem)
imagem2 = equalizar(imagem)
imagem3 = blurred(imagem2)
imagem4 = gerEdges(imagem3)
cv2.imshow('Escala de cinza',imagem)
cv2.imshow('Escala de cinza equalizada',imagem2)
cv2.imshow('Blurred',imagem3)
cv2.imshow('Edges',imagem4)

# ============================================================================================================

cv2.waitKey(0)
cv2.destroyAllWindows()