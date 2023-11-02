FROM python:3.10

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./latest_changes /app/latest_changes

ENV PYTHONPATH=/app

CMD ["python", "-m", "latest_changes"]
