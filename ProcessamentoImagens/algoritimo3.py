import cv2
import numpy as np
import math

def mostrar(img,coord):
    cordX = []
    cordY = []
    for x in coord:
        L = coord[x][0]
        C = coord[x][1]
        img[L-1,C-1] = (0,0,255)
        img[L-1,C] = (0,0,255)
        img[L-1,C+1] = (0,0,255)

        img[L,C-1] = (0,0,255)
        img[L,C] = (0,0,255)
        img[L,C+1] = (0,0,255)

        img[L+1,C-1] = (0,0,255)
        img[L+1,C] = (0,0,255)
        img[L+1,C+1] = (0,0,255)

        cv2.putText(img, (" {0}".format(x)), (C,L), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 1)
    return img

def acharPonto(coordenadas,medidas):
    coords = []

    for coord in coordenadas:
        centro_x = 0
        centro_y = 0
        vetor_x = []
        vetor_y = []

        for x in coord:
            centro_x += coord[x][0]
            centro_y += coord[x][1]

        centro_x = int(centro_x/7)
        centro_y = int(centro_y/7)

        for x in coord:
            vetor_x.append(coord[x][0] - centro_x)
            vetor_y.append(coord[x][1] - centro_y)
        
        valor_x = int(sum(vetor_x)/7)
        valor_y = int(sum(vetor_y)/7)

        coordX = centro_x+valor_x
        coordY = centro_y+valor_y
        coord['H'] = [coordX,coordY]
        coords.append(coord)
    return coords

def medidasPx(coordenadas,medidas):
    medi = []
    for i in range(len(coordenadas)):
        coord = coordenadas[i]
        #definindo tamano, em px, entre os seguimentos utilizando o teorema de pitágoras H^2 = C^2 + C^2
        ABx = coord['A'][0]-coord['B'][0]
        ABy = coord['A'][1]-coord['B'][1]
        ABx = ABx*-1 if(ABx<0) else ABx
        ABy = ABy*-1 if(ABy<0) else ABy
        ABz = math.sqrt(ABx**2 + ABy**2)
        medidas[i]['AB'][1] = round(ABz)
        medidas[i]['AB'][2] = round(medidas[i]['AB'][0]/ABz,2)

        BCx = coord['B'][0]-coord['C'][0]
        BCy = coord['B'][1]-coord['C'][1]
        BCx = BCx*-1 if(BCx<0) else BCx
        BCy = BCy*-1 if(BCy<0) else BCy
        BCz = math.sqrt(BCx**2 + BCy**2)
        medidas[i]['BC'][1] = round(BCz)
        medidas[i]['BC'][2] = round(medidas[i]['BC'][0]/BCz,2)

        CFx = coord['B'][0]-coord['C'][0]
        CFy = coord['B'][1]-coord['C'][1]
        CFx = CFx*-1 if(CFx<0) else CFx
        CFy = CFy*-1 if(CFy<0) else CFy
        CFz = math.sqrt(CFx**2 + CFy**2)
        medidas[i]['CF'][1] = round(CFz)
        medidas[i]['CF'][2] = round(medidas[i]['CF'][0]/CFz,2)

        medi.append(medidas)
    return medi

def gerarMatriz(mdd, Df):
    mtzs = []
    for medidas in mdd:
        N_px = img.shape[0]
        N_py = img.shape[1]
        u = round(N_px/2)
        v = round(N_py/2)
        ppc = medidas['AB'][2] #pixel por cm
        s_x = round(N_px/ppc) #tamanho horizontal da imagem em mm
        s_y = round(N_py/ppc) #tamanho vertical da imagem em mm

        # K = | s_x  0    u |
        #     | 0   s_y   v |
        #     | 0    0    1 |

        K = np.empty((3, 3))

        K[0,0] = s_x
        K[0,1] = 0
        K[0,2] = u

        K[1,0] = 0
        K[1,1] = s_y
        K[1,2] = v

        K[2,0] = 0
        K[2,1] = 0
        K[2,2] = 1
        mtzs.append(K)
    return mtzs

def getDots(event, C, L, flags, params):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        if(len(val) < 7):
            cv2.putText(img, ("{0} : {1}".format(L,C)), (C,L), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 0, 0), 1)
            cv2.imshow('image', img)
            val.append([L,C])
    elif event == cv2.EVENT_RBUTTONDOWN:
        val.clear()
        img = cv2.imread(x)
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', getDots)

def gerarMatrizMedia(matrizes):
    # matriz = | s_x  0   u |
    #          |  0  s_y  v |
    #          |  0   0   1 |

    mtrz = np.empty((3, 3))
    for x in matrizes:
        mtrz[0,0] += x[0,0]
        mtrz[0,1] += x[0,1]
        mtrz[0,2] += x[0,2]

        mtrz[1,0] += x[1,0]
        mtrz[1,1] += x[1,1]
        mtrz[1,2] += x[1,2]

        mtrz[2,0] += x[2,0]
        mtrz[2,1] += x[2,1]
        mtrz[2,2] += x[2,2]

    mtrz[0,0] = round(mtrz[0,0]/len(matrizes),1)
    mtrz[0,1] = round(mtrz[0,1]/len(matrizes),1)
    mtrz[0,2] = round(mtrz[0,2]/len(matrizes),1)
    mtrz[1,0] = round(mtrz[1,0]/len(matrizes),1)
    mtrz[1,1] = round(mtrz[1,1]/len(matrizes),1)
    mtrz[1,2] = round(mtrz[1,2]/len(matrizes),1)
    mtrz[2,0] = round(mtrz[2,0]/len(matrizes),1)
    mtrz[2,1] = round(mtrz[2,1]/len(matrizes),1)
    mtrz[2,2] = round(mtrz[2,2]/len(matrizes),1)

    return mtrz
    
quantidadeImagens = int(input('Quantas imagens deseja adicionar? (certifique-se que as imagens estejam com o nome referente à sua numeração EX.: 1.jpg, 2.jpg)'))
# formato = input('Qual extensão do arquivo? (png,jpg,jpeg)')
formato = 'jpg'

listaImagens = []
val = []
coordenadas = []

for item in range(0,quantidadeImagens+1):
    if(item > 0 and item <= quantidadeImagens):
        listaImagens.append("{0}.{1}".format(item,formato))

for item in listaImagens:
    img = cv2.imread(item) #carregando imagem capturada
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', getDots)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    coordenadas.append({"A":[val[0][0],val[0][1]],"B":[val[1][0],val[1][1]],"C":[val[2][0],val[2][1]],"D":[val[3][0],val[3][1]],"E":[val[4][0],val[4][1]],"F":[val[5][0],val[5][1]],"G":[val[6][0],val[6][1]]})
    val = []

Df = 15 #distancia em que a imagem foi capturada em cm

medidas = []
for x in range(quantidadeImagens):
    medidas.append({"AB":[8,0,0], "BC":[5,0,0], "CF":[13,0,0]})

newMedidas = medidasPx(coordenadas,medidas)

matrizes = gerarMatriz(medidas,Df) #gerando lista de matrizes de parâmetros intrínsecos
matrizMedia = gerarMatrizMedia(matrizes) #gerando matriz media de parâmetros intrínsecos

# print("############################ COORDENADAS #############################")

for x in coordenadas:
    print(x)
    print('\n')

print("############################ MEDIDAS #############################")

for x in medidas:
    print(x)
    print('\n')

print("############################ MATRIZES #############################")

for x in matrizes:
    print(x)
    print('\n')

print("############################ MATRIZ MEDIA #############################")

print(matrizMedia)
print('\n')

novasCoordenadas = acharPonto(coordenadas,medidas)

for x in range(len(novasCoordenadas)):
    imgMostrar = cv2.imread("{0}.{1}".format((x+1),formato))
    newImg = mostrar(imgMostrar,novasCoordenadas[x])
    cv2.imshow('imagem', newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()