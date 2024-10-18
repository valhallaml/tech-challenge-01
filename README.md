# Tech Challenge 01

## Run local

```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Access <http://localhost:8000/>

## Run with docker compose

```bash
docker compose up --build --force-recreate
```

## Docs

- <http://localhost:8000/docs>
