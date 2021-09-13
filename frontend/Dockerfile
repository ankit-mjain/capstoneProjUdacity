FROM python:3.8-slim

WORKDIR /frontend

CPY ./requirements.txt ./ 

RUN pip install --no-cache-dir -r requirements.txt

COPY ./frontend/ .

EXPOSE 5000

CMD [ "python", "./app.py" ]
