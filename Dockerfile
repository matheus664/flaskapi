FROM python:3.11.2

WORKDIR /app

COPY . /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 80

ENV NAME appflask

CMD ["python","app.py"]