import cv2


# histogram esitleme
# goruntuyu gray uygulayarak acar
img = cv2.imread('spine.bmp', 0)
equ = cv2.equalizeHist(img)

# goruntuyu projeye kaydetmek icin gerekli fonksiyon
cv2.imwrite('soru1-sonuc.jpg', equ)

# goruntuyu projeyi ekranda gostermsi icin gerekli fonksiyon
cv2.imshow("orjinal", img)
cv2.imshow("histogram esitleme ", equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
