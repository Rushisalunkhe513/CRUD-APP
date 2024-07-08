FROM python:3.8-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app/

COPY requirements.txt /app/requirements.txt

EXPOSE 8000

CMD ["flask","run","--debug"]