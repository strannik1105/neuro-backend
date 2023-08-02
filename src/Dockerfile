FROM python:3.11-slim

RUN mkdir app
WORKDIR /app/

RUN /usr/local/bin/python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "python3", "-u" , "./main.py"]
