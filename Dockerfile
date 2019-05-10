from python:alpine

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/app/entrypoint.sh"]

WORKDIR /app

COPY resources/entrypoint.sh ./
COPY . ./

RUN apk upgrade --no-cache \
	&& apk add --no-cache dos2unix \
	&& apk add --no-cache bash \
	&& apk add --no-cache curl \
	&& pip install . \
	&& dos2unix entrypoint.sh \
	&& chmod +x entrypoint.sh
