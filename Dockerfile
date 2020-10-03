FROM python:3.7

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app /app/app

ENV PYTHONPATH=/app

CMD ["python", "-m", "app"]
