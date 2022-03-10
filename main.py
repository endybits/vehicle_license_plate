import cv2

from licence_detecting_modules import LicenceDetector

def run_detector(img):
    detector = LicenceDetector(img)    
    h, w, _ = img.shape
    roi_yelow = detector.roi(h, w)
    cooridnates = detector.get_contours(roi_yelow, drw_contours=False, show_roi_bgr=True)
    detector.draw_rect(cooridnates)
    detector.text_detecting(cooridnates, w, h)
    cv2.imshow('YELLOW', roi_yelow)

def run():
    pth = 'vehicle_license_plate/assets/fiat.jpg'
    img = cv2.imread(pth, 1)
    run_detector(img)
    
    #cv2.imshow('YELLOW', roi_yelow)
    cv2.imshow('IMG', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()