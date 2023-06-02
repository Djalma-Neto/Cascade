import cv2

img = cv2.imread('teste.jpg')
# img = cv2.imread('teste2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.GaussianBlur(img, (5,5),0)

clf1 = cv2.CascadeClassifier('./data/cascade.xml')
detecta = clf1.detectMultiScale(img, 1.3, 15)

detecta2 = clf1.detectMultiScale(img2, 1.3, 15)

for(x,y,w,h) in detecta:
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),1)
	cv2.putText(img, "local".format(), (x,y-20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

for(x,y,w,h) in detecta2:
	img2 = cv2.rectangle(img2,(x,y),(x+w,y+h),(250,0,0),1)
	cv2.putText(img2, "local".format(), (x,y-20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('imagem',img)
cv2.imshow('imagemBlur',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()