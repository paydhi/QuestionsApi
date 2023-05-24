FROM alpine
WORKDIR /app
COPY questions_api .
COPY ./requirements.txt .
ENV PG_USER=postgres
RUN apk update && apk add python3 py3-pip && pip install -r requirements.txt
COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh","entrypoint.sh"]
