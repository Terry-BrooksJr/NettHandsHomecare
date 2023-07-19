# Fetching official base image for python
FROM python:3.11-bullseye as web
RUN apt-get update -y
RUN apt-get install ufw -y 
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./pyproject.toml .
RUN pip install --upgrade poetry
RUN poetry config virtualenvs.create false
RUN poetry config virtualenvs.options.always-copy true
RUN poetry install 
RUN ufw allow 8000
COPY . /app
# Setting up the work directory
WORKDIR /app
COPY ./entrypoint.sh /

# Preventing python from writing
# pyc to docker container
ENV PYTHONDONTWRITEBYTECODE 1

# Flushing out python buffer
ENV PYTHONUNBUFFERED 1
ENTRYPOINT ["/entrypoint.sh"]
