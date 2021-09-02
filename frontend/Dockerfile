FROM python:3.8-buster

WORKDIR /usr/src/frontend-app

COPY ./frontend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./frontend/ .

EXPOSE 5000

CMD [ "python", "./app.py" ]