## Setup env
```
 python ../scripts/setup_env.py dev
```

## Run local
```
uvicorn app.main:app --host localhost --port 8081 --reload
```

## Run migrations
```
alembic revision -m "add player table" --autogenerate
alembic upgrade head
```

## Publish Docker
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 798616997032.dkr.ecr.us-east-1.amazonaws.com

docker build -t captain-of-the-sea-backend-prod .

docker tag captain-of-the-sea-backend-prod:latest 798616997032.dkr.ecr.us-east-1.amazonaws.com/captain-of-the-sea-backend-prod:latest

docker push 798616997032.dkr.ecr.us-east-1.amazonaws.com/captain-of-the-sea-backend-prod:latest
```
