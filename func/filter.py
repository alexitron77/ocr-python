
import cv2

def get_grayscale(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    show("greyscale", img)

def thresholding(image):
    img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    show("thresholding", img)
  
def show(desc, img):
  cv2.imshow(desc, img)
  cv2.waitKey(0)