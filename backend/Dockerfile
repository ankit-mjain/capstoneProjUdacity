FROM python:3.8-slim

WORKDIR /backend

COPY ./requirements.txt ./ 

RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend/ .

EXPOSE 5001

CMD [ "python", "./app.py" ]
