FROM python:3.7

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock .

RUN pipenv install --system

COPY . .

EXPOSE 8000

CMD ["python3", "main.py"]
