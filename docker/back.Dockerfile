FROM python:3.14-slim

WORKDIR /working

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ../src/app/ ./app

WORKDIR /working/app

CMD ["python", "main.py"]
