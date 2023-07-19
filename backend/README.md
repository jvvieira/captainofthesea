## run local
```
uvicorn app.main:app --host localhost --port 8081 --reload

```

## Run migrations
```
alembic revision -m "add player table" --autogenerate

```
