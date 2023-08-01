FROM python:3.9-buster

COPY requirements.txt /wedding_bot/requirements.txt
COPY main.py /wedding_bot/main.py

RUN pip install -r wedding_bot/requirements.txt

CMD ["python3", "wedding_bot/main.py"]