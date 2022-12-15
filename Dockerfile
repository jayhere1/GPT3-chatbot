FROM python:3.10

WORKDIR /var/task

COPY / /var/task/

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "main.py" ]