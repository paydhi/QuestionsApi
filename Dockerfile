FROM alpine
WORKDIR /app
COPY ./requirements.txt .
RUN apk update && apk add python3 py3-pip && pip install -r requirements.txt
COPY ./entrypoint.sh .
RUN chmod +x entrypoint.sh
COPY questions_api .
ENTRYPOINT ["sh","entrypoint.sh"]
