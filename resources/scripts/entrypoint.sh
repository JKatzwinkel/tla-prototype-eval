#!/bin/bash

CMD=runserver

if [ $# -ge 1 ]; then
    if [[ "$1" -eq "ingest" ]]; then
        CMD=populate
        echo "download && extract corpus file at ${SAMPLE_URL}.."
        wget -q "${SAMPLE_URL}" -O sample.tar.gz
        tar -xzf sample.tar.gz -C resources
    fi
fi

while true; do
	resp=$(curl -s "$ES_URL")
	[ $? -eq 0 ] && break
	echo "no connection to ES instance"
	sleep 4
done

if [[ "${CMD}" -eq "populate" ]]; then
    if [ -e "resources/corpus/" ]; then
        python webd/manage.py populate_indices
    fi
fi

if [[ "${CMD}" -eq "runserver" ]]; then
    python webd/manage.py migrate
    python webd/manage.py runserver 0.0.0.0:8000
fi
