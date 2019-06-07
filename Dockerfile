from python:alpine

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/app/entrypoint.sh"]

WORKDIR /app

COPY resources/scripts/entrypoint.sh ./
COPY webd/ ./webd
COPY resources ./resources

ARG sample_url

RUN apk upgrade --no-cache \
	&& apk add --no-cache bash curl \
	&& apk add --no-cache -t .build-deps wget tar \
	&& pip install -e ./webd \
	&& wget -q "${sample_url}" -O sample.tar.gz \
	&& tar -xzf sample.tar.gz -C resources \
	&& rm sample.tar.gz \
	&& chmod +x entrypoint.sh \
	&& apk del .build-deps
