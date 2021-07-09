from pandas.core.frame import DataFrame
from pytesseract import Output
import pytesseract

def confidence(img):
  text = pytesseract.image_to_data(img, output_type=Output.DATAFRAME)
  text = text[text.conf != -1]

  # Add the groupby feature based on the confidence level

  print(text.head())
