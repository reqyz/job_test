FROM python:3
WORKDIR /src
ENV DATABASE_URL postgres://postgres:secret@db:5432/job_test
ENV HOST 0.0.0.0
ENV PORT 8001
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/ .