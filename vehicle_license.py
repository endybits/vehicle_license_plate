import cv2

pth = 'vehicle_license_plate/assets/fiat.jpg'

img = cv2.imread(pth, 1)
he, wid, _ = img.shape

## Define a Region of interest
py = he//3
px = wid//4
roi = img[py: -he//10, px:-px]

roi_b = roi[:,:,0]
roi_g = roi[:,:,1]
roi_r = roi[:,:,2]
roi_yelow = cv2.subtract(roi_g, roi_b)


gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 120, 250, )
edges = cv2.dilate(edges, None, iterations=1)
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    # To know if cnt has 4 vertices
    x, y, w, h = cv2.boundingRect(cnt)
    epsilon = cv2.arcLength(cnt, True) * 0.08
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    num_vertices = len(approx)
    area = cv2.contourArea(cnt)
    if area > 3000:
        cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 1)  

cv2.imshow('IMG', img)
#cv2.imshow('GRAY', gray)  
cv2.imshow('CANNY', roi_yelow)  
cv2.waitKey(0)
cv2.destroyAllWindows()