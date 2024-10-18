FROM python:3.10-slim

WORKDIR /app/src

RUN addgroup \
        --gid 1000 \
        app \
    && adduser \
        --uid 1000 \
        --gid 1000 \
        --disabled-password \
        --quiet \
        app

USER app

COPY --chown=app:app requirements.txt /app/requirements.txt

ENV PATH="/home/app/.local/bin:${PATH}"

RUN pip install \
    --user \
    --no-cache-dir \
    --upgrade \
    -r /app/requirements.txt

COPY ./src .

CMD [ "uvicorn", "main:app", "--host=0.0.0.0" ]

EXPOSE 8000
