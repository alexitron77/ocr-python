import cv2
from func.boxes import *
from func.filter import *
from func.dataframe import *
from func.text import *
import sys


src = sys.argv[1]
img = cv2.imread(src)

# get_grayscale(img)
# drawBoxes(img)
# confidence(img)
text_extraction(img)


