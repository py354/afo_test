FROM python:3.8-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN apk update && apk add bash
COPY . /app
EXPOSE 5000
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]