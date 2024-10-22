# Tech Challenge 01 <!-- omit in toc -->

- [Local ENV](#local-env)
  - [Create](#create)
  - [Active](#active)
- [Run local](#run-local)
- [Run with docker compose](#run-with-docker-compose)
- [Docs](#docs)

## Local ENV

### Create

```bash
python -m venv .venv
```

### Active

```bash
source .venv/bin/activate
```

## Run local

```bash
pip install -r requirements.txt
cd src/
python -m uvicorn main:app --reload
```

Access <http://localhost:8000/>

## Run with docker compose

```bash
docker compose up --build --force-recreate
```

## Docs

- <http://localhost:8000/docs>
