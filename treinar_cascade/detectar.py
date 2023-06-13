import cv2

img1 = cv2.imread('teste.jpg')
img2 = cv2.imread('teste2.jpg')
img3 = cv2.imread('teste3.jpg')

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# img1 = cv2.GaussianBlur(img1, (5,5),0)
# img2 = cv2.GaussianBlur(img2, (5,5),0)
# img3 = cv2.GaussianBlur(img3, (5,5),0)

# clf1 = cv2.CascadeClassifier('./data/cascade.xml')
clf1 = cv2.CascadeClassifier('./cascadeX.xml')

detecta1 = clf1.detectMultiScale(img1, 1.3, 15)
detecta2 = clf1.detectMultiScale(img2, 1.3, 15)
detecta3 = clf1.detectMultiScale(img3, 1.3, 15)

for(x,y,w,h) in detecta1:
	img1 = cv2.rectangle(img1,(x,y),(x+w,y+h),(250,0,0),1)
	cv2.putText(img1, "Largura {0}cm".format(int(w*0.83)), (x,y-20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

for(x,y,w,h) in detecta2:
	img2 = cv2.rectangle(img2,(x,y),(x+w,y+h),(250,0,0),1)
	cv2.putText(img2, "Largura {0}cm".format(int(w*0.83)), (x,y-20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

for(x,y,w,h) in detecta3:
	img3 = cv2.rectangle(img3,(x,y),(x+w,y+h),(250,0,0),1)
	cv2.putText(img3, "Largura {0}cm".format(int(w*0.83)), (x,y-20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('imagem1',img1)
cv2.imshow('imagem2',img2)
cv2.imshow('imagem3',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()