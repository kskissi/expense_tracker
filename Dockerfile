FROM python:3.9  # Or any version you prefer
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]  # Modify this based on your app's entry point

