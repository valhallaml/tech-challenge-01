FROM python:3.10-slim

WORKDIR /app

RUN addgroup \
        --gid 1000 \
        app \
    && adduser \
        --uid 1000 \
        --gid 1000 \
        --disabled-password \
        --quiet \
        app \
    && chown app:app /app/

USER app

COPY --chown=app:app requirements.txt requirements.txt

ENV PATH="/home/app/.local/bin:${PATH}"

RUN pip install \
    --user \
    --no-cache-dir \
    --upgrade \
    -r requirements.txt \
    && rm -f requirements.txt

COPY --chown=app:app --chmod=0400 src/ .
COPY --chown=app:app --chmod=0400 embrapa/ embrapa/

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port", "8000" ]

EXPOSE 8000
