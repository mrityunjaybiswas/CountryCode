FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
COPY CountryCode_API.py .
COPY data.json .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","CountryCode_API.py"]