import cv2
import numpy as np

def escalaCinza(imagem):
	L = imagem.shape[0]
	C = imagem.shape[1]
	newImage = np.zeros((L,C), dtype=np.uint8)

	for l in range (L):
		for c in range(C):
			(b,g,r) = imagem[l,c]
			
			r = r*0.8
			g = g*0.8
			b = b*0.8
			gray = (b+g+r)/3

			# newImage[l,c] = (b,g,r)
			newImage[l,c] = gray
	return newImage

def blurred(imagem):
    maior = 0
    menor = 0
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
                    maior = newVal if(newVal>maior)else maior
                    menor = newVal if(newVal<menor)else menor
            newVal = int(newVal)
            newVal = 255 if(newVal>255) else newVal #limitando para não ultrapassar o valor de 255
            newImage[l,c] = newVal
    return newImage, maior, menor

def densidade(img, intencidade):
    L = img.shape[0]
    C = img.shape[1]

    # descobrindo a densidade de pixel
    objLengt = 6 #na imagem a borracha tem 6cm
    correcao = 3
    totalCount = 0
    for l in range(0,L):
        count = 0
        for c in range(0,C):
            cor = img[l,c]
            if((cor > intencidade+correcao)):
                img[l,c] = 0
            else:
                img[l,c] = 255
                count += 1

            totalCount = count if count>totalCount else totalCount
    return img, round(totalCount/objLengt), totalCount

def descobrirPontos(img,img2, PPC, distancia):
    L = img.shape[0]
    C = img.shape[1]
    Cor = (0,0,255)
    pontos = []

    for l in range(50,L,25):
         for c in range(C-100,C,25):
              pontos.append([l,c])
    for p in pontos: 
        img[p[0], p[1]-1] = Cor
        img[p[0]-1, p[1]] = Cor
        img[p[0]-1, p[1]+1] = Cor
        img[p[0], p[1]-1] = Cor
        img[p[0], p[1]] = Cor ####  (Ponto específico)
        img[p[0], p[1]+1] = Cor
        img[p[0]+1, p[1]-1] = Cor
        img[p[0]+1, p[1]] = Cor
        img[p[0]+1, p[1]+1] = Cor

        desloc = int(p[1]-(distancia*PPC)) if int(p[1]-(distancia*PPC))>0 else 0
        p2 = [p[0], desloc] #deslocando o ponto para a esquerda
        
        img2[p2[0]-1, p2[1]-1] = Cor
        img2[p2[0]-1, p2[1]] = Cor
        img2[p2[0]-1, p2[1]+1] = Cor
        img2[p2[0], p2[1]-1] = Cor
        img2[p2[0], p2[1]] = Cor ####  (Ponto específico)
        img2[p2[0], p2[1]+1] = Cor
        img2[p2[0]+1, p2[1]-1] = Cor
        img2[p2[0]+1, p2[1]] = Cor
        img2[p2[0]+1, p2[1]+1] = Cor
    
    return img,img2


imagem = cv2.imread('Imagem1.jpg')
imagemS = cv2.imread('Imagem2.jpg')
imagemC = escalaCinza(imagem)
imagemB, maior, menor = blurred(imagemC)
valorTonalidadeMedia = round((menor+maior)/2)
# cv2.imshow('imagemB', imagemB)

# apos executar essa etapa, sabemos que o objeto na imagem é composta por 113 pixeis na horizontal logo
# temos que 113/6 = 18,8 => 19, logo temos 19 pixel por cm na imagem
(imagem2, PPC, totalCount) = densidade(imagemB,valorTonalidadeMedia) #PPC (Pontos por Centimetro)
# cv2.imshow('Imagem Original', imagem2)
img1,img2 = descobrirPontos(imagem,imagemS, PPC,10) #O deslocamento foi de 10cm
cv2.imshow('Imagem Original', img1)
cv2.imshow('Imagem Movimentada a Direita', img2)
# print(PPC)
# print(totalCount)
# print(totalCount)
# print('o Objeto tem: {0} de comprimento'.format(round(totalCount/PPC,2)))
cv2.waitKey(0)