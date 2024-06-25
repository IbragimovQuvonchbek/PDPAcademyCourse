FROM python:slim

WORKDIR /netlix

COPY requirements.txt /netlix/

RUN pip install -r requirements.txt

COPY . /netlix/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]