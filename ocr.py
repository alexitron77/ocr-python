import pytesseract
import cv2

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = cv2.imread("ticket.jpg")

gray = get_grayscale(img)

threshold = thresholding(gray)

cv2.imshow('image',threshold)
cv2.waitKey(0)

res = pytesseract.image_to_string(img)
print(res)
