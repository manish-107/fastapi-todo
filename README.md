# fastapi-todo

A simple To-Do app built with FastAPI that lets users create, update, delete, and manage tasks easily. Fast, lightweight, and easy to use.

`built-in venv module to create a virtual environment.`

```
python -m venv venv
.\venv\Scripts\Activate
```

`to deactivate`
deactivate

```
pip freeze > requirements.txt
```

`to run:`

```
uvicorn app.main:app --reload
```

```
netstat -ano | findstr LISTENING
taskkill /F /IM python.exe
```

docker run --name alembic-demo -p 5432:5432 -e POSTGRES_PASSWORD=secret -d postgres

docker exec -ti alembic-demo createdb -U postgres alembic_db

```
alembic upgrade head
alembic revision --autogenerate -m "Added employee model"
```

### get into docker postgre and list tables

```
docker exec -it alembic-demo psql -U postgres -d alembic_db -c "\dt"`
```
