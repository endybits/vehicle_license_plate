import cv2

pth = 'vehicle_license_plate/assets/fiat.jpg'

img = cv2.imread(pth, 1)
he, wid, _ = img.shape

## Defining a Region of interest
## Subtracting the array blue of array green, its result is the yellow array on RGB 
## (The same color of license plates)
py = he//3
px = wid//4
roi = img[py: -he//10, px:-px]

roi_b = roi[:,:,0]
roi_g = roi[:,:,1]
roi_r = roi[:,:,2]
roi_yelow = cv2.subtract(roi_g, roi_b)

_, thres = cv2.threshold(roi_yelow, 100, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(roi, contours, -1, (0, 255, 0), 1)  

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(cnt)
        x1, y1 = x - 5, y - 5
        x2 = x + 9 + w
        y2 = y + 3 + h
        #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 1)  
        cv2.rectangle(roi, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('IMG', img)
cv2.imshow('ROI', roi)  
cv2.imshow('Thresh', thres)
cv2.waitKey(0)
cv2.destroyAllWindows()