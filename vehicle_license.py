import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
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
        # Resizing the ROI to license region of interest
        roi_bgr = roi[y1:y2, x1:x2,:]
        license_roi_rgb = cv2.cvtColor(roi_bgr, cv2.COLOR_BGR2RGB)
        # Extracting text from license region of interest
        txt = pytesseract.image_to_string(license_roi_rgb)
        print(txt)
        cv2.rectangle(img, (wid//4, he - he//10), (wid - wid//4, he), (0), -1)
        cv2.putText(img, txt, (wid//4 + 35, he - he//10 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2 )

cv2.imshow('IMG', img)
#cv2.imshow('ROI', license_roi_rgb)  
cv2.imshow('Thresh', thres)
cv2.waitKey(0)
cv2.destroyAllWindows()