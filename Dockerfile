FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "server", "run", "--host=0.0.0.0" ]

EXPOSE 5000
