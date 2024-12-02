FROM python:3.10-alpine

WORKDIR /hcmus-dstn

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT [ "python", "check.py" ]
