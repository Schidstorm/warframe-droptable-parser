FROM python

RUN pip install pyquery

COPY . .

CMD [ "python", "main.py" ]
