FROM python:alpine AS stage

WORKDIR /app
COPY . /app

RUN apk upgrade --no-cache \
	&& apk add --no-cache bash wget curl tar git \
    && git submodule update --init --recursive \
    && rm -rf .git/ \


FROM python:alpine

ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["/app/resources/scripts/entrypoint.sh"]

WORKDIR /app
COPY --from=stage /app /app

RUN pip install -e ./webd \
    && chmod +x ./resources/scripts/entrypoint.sh

