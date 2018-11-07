FROM python:3

RUN pip3 install pyquery

COPY . .

CMD [ "python3", "main.py" ]
