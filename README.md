# test-python-prisma
Playing with python prisma

# Setup
Install dependencies
```pip install -r requirements.txt```

Generate prisma client
```prisma generate```

Run the postgres server with docker compose
```docker compose up```

Run the api 
```uvicorn app.main:app```
