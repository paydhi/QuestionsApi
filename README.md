# QuestionsApi

### Requirements

1. Git
2. Docker
3. Docker-compose >= 3.9

### How to run app

1. `git clone https://github.com/paydhi/QuestionsApi.git`
2. `cd QuestionsApi`
3. `docker compose up -d`

Backend now runs on localhost:8000, postgres runs on localhost:5432.

`USER:PASSWORD` for DB is `postgres:postgres`, as stated in `settings.py` and
`docker-compose.yml`

To stop app just run `docker compose stop`.

To completely remove containers, volumes and networks, run `docker compose down -v`.

### What requests to send

You need to send requests to URL `http://localhost:8000/api/questions/`.

Send `POST` request with JSON that looks like this: `{"questions_num": int}`,
where `int` must be integer, not string or float, and greater than 0.

Additionally, you can use Postman collection, named `questions_api.postman_collection.json`,
located in root of this repo. 

Also, you can send `OPTIONS` request to see what is expected, and
what you will receive.