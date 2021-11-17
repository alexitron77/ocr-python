from fastapi import FastAPI, File, UploadFile
from typing import List
from pydantic import BaseModel
import time
import asyncio 
import api.ocr 
import commons.utils
import uvicorn 
from db.session import session, engine
from models.base import Base

app = FastAPI()

@app.post("/ocr")
async def imageToText(images: List[UploadFile] = File(...)):
	start_time = time.time()
	task = []
	for i in images:
		temp_file = utils.saveImageToServer(i)
		task.append(asyncio.create_task(ocr.readText(temp_file, "eng")))
	res = await asyncio.gather(*task)
	end_time = time.time()
	return {"response": res, "time_elapsed": (end_time - start_time)}	

if __name__ == "__main__":
	Base.metadata.create_all(bind=engine)
	uvicorn.run(app, host="0.0.0.0", port=8001)

