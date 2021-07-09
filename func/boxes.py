import cv2
from pytesseract import Output
import pytesseract

def drawBoxes(img):
  text = pytesseract.image_to_data(img, output_type=Output.DICT)
  n_boxes = len(text["level"]) 

  for i in range(n_boxes):
    (x, y, w, h) = (text["left"][i], text["top"][i], text["width"][i], text["height"][i])
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

  cv2.imshow("boxes", img)
  cv2.waitKey(0)
