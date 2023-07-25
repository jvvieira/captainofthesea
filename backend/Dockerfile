# Pull official latest Python Docker image (Pulished with version 3.11.0)
FROM --platform=linux/amd64 python:latest

WORKDIR /backend/

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock ./.env /backend/

COPY /app/ /backend/app/


ENV PYTHONPATH=${PYTHONPATH}:${PWD}

# Neomodel has shapely and libgeos as dependencies
RUN apt-get update && apt-get install -y libgeos-dev

# Install Poetry
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry shell

# Set the server port
EXPOSE 8000

# Start up the backend serve\
CMD uvicorn app.main:app --reload --workers 4 --host 0.0.0.0 --port 8000
