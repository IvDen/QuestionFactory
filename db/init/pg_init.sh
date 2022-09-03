#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<EOSQL
  \c QuestionFactory;
    CREATE TABLE IF NOT EXISTS questions
  (
    id INTEGER,
    question_body TEXT NOT NULL,
    answer TEXT NOT NULL,
    air_date TIMESTAMP NOT NULL,
    CONSTRAINT questions_pk PRIMARY KEY (id)
  );
  INSERT INTO questions(id, question_body, answer, air_date) VALUES
    (1, 'question', 'answer', '2011-01-01 00:00:00+03');
  CREATE USER question_user WITH PASSWORD 'hackme';
  GRANT ALL PRIVILEGES ON questions TO question_user;
EOSQL
