from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.settings import settings

print(settings.POSTGRES_URL)

try:
	engine = create_engine(settings.POSTGRES_URL)
	session = sessionmaker(autocommit=False, autoFlush=False, bind=engine)
except:
	print("Something went wrong with the database connection")


