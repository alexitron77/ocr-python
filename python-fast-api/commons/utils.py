import os
import shutil
import pathlib

def saveImageToServer(uploaded_file):
        extension = os.path.splitext(uploaded_file.filename)[-1]
        currDir = pathlib.Path(__file__).resolve().parents[0]
        temp_file = os.path.join(str(currDir), uploaded_file.filename)
        with open(temp_file, "wb") as buffer:
                shutil.copyfileobj(uploaded_file.file, buffer)
        return temp_file

