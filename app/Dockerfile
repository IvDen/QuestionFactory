# syntax=docker/dockerfile:1
FROM python:3.10.6-slim-buster
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
#CMD ["/bin/sh", "-c", "ls", "&&", "uvicorn", "app.main:app"]
CMD ls && echo "$PATH" && uvicorn app.main:app