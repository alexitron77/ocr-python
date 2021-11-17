from models.baseclass import Base
from sqlalchemy import Column, Float, String, Integer


class Ocr(Base):
	__tablename__ = "ocr"
	id = Column(Integer, primary_key=True, index=True)
	timestamp = Column(String)
	converted_text = Column(String)
	time = Column(Float)
