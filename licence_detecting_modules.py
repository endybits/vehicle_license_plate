import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

class LicenceDetector():
    def __init__(self, img):
        self.img = img

    
    def __show_img__(self, show_roi):
        #cv2.imshow('IMG', self.img)
        if show_roi:
            cv2.imshow('ROI', self.roi)

    
    def roi(self, h, w):
        '''
            Defining a Region of interest
            Subtracting the array blue of array green, its result is the yellow array on RGB 
            (The same color of license plates)
            @return np.array[][]
        '''
        py = h//3
        px = w//4
        self.roi = self.img[py: -h//10, px:-px]

        roi_b = self.roi[:,:,0]
        roi_g = self.roi[:,:,1]
        #roi_r = roi[:,:,2]
        roi_yelow = cv2.subtract(roi_g, roi_b)
        return roi_yelow


    def get_contours(self, roi_yelow, drw_contours = False, show_roi_bgr = True):
        _, thres = cv2.threshold(roi_yelow, 100, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                
                x, y, w, h = cv2.boundingRect(cnt)
                x1, y1 = x - 5, y - 5
                x2 = x + 9 + w
                y2 = y + 3 + h
                if drw_contours:
                    cv2.drawContours(self.roi, [cnt], -1, (0, 255, 0), 1)
                if show_roi_bgr:
                    self.__show_img__(show_roi_bgr)
                return(x1, y1, x2, y2)


    def draw_rect(self, coords):
        cv2.rectangle(self.roi, coords[:2], coords[2:], (0, 255, 0), 2)


    def text_detecting(self, coodrs, w, h):
        x1, y1, x2, y2 = coodrs[0], coodrs[1], coodrs[2], coodrs[3]
        
        # Resizing the ROI to license region of interest
        roi_bgr = self.roi[y1:y2, x1:x2,:]
        license_roi_rgb = cv2.cvtColor(roi_bgr, cv2.COLOR_BGR2RGB)
        
        # Extracting text from license region of interest
        txt = pytesseract.image_to_string(license_roi_rgb)
        print(txt)
        cv2.rectangle(self.img, (w//4, h - h//10), (w - w//4, h), (0), -1)
        cv2.putText(self.img, txt, (w//4 + 35, h - h//10 + 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2 )