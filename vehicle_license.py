import cv2

pth = 'vehicle_license_plate/assets/fiat.jpg'

img = cv2.imread(pth, 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



cv2.imshow('IMG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()