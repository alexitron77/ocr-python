import pytesseract
import asyncio

async def readText(path, language):
	try:
		text = pytesseract.image_to_string(path, lang=language)
		await asyncio.sleep(5)
		print(text)	 
		return text
	except:
		return "[Error] The conversion to text failed"

