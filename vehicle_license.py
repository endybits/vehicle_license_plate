import cv2

pth = 'vehicle_license_plate/assets/fiat.jpg'

img = cv2.imread(pth, 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 230, 255, )
edges = cv2.dilate(edges, None, iterations=1)
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 255, 255), 1)

cv2.imshow('IMG', img)
cv2.imshow('CANNY', edges)  
cv2.waitKey(0)
cv2.destroyAllWindows()