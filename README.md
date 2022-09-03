# QuestionFactory
Test task

app:
    start: uvicorn app.main:app


docker:
    db:
        need a init scripts in db/secrets/pg_init.sh
            w/ create table and users w/ priveleges for it
        need root pass scripts in secrets/root_pass
    app:
        need a dsn in app/secrets/postgres_dsn

docker-compose run --build -d

