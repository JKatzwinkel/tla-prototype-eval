FROM python:alpine AS clone

WORKDIR /app
COPY . /app

RUN apk upgrade --no-cache \
    && apk add --no-cache bash git \
    && git submodule update --init --recursive \
    && rm -rf .git/


FROM clone AS run

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["/app/resources/scripts/entrypoint.sh"]

WORKDIR /app
COPY --from=clone /app/ /app

RUN apk upgrade --no-cache \
    && apk add --no-cache bash wget curl tar git \
    && pip install -e ./webd \
    && chmod +x ./resources/scripts/entrypoint.sh

