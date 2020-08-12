#!/bin/bash

CMD=runserver
DAT=sample.tar.gz
DIR=resources

LF_FILE="${DIR}/link-formatters.json"
if [ ! -e "${LF_FILE}" ]; then
    echo "link formatters config file ${LF_FILE} not found."
    echo "download external ID link formatters..."
    python webd/manage.py dl_link_formatters
fi

if [ $# -ge 1 ]; then
    if [[ "$1" = "ingest" ]]; then
        CMD=populate
        echo "download && extract corpus file at ${SAMPLE_URL}.."
        wget -q "${SAMPLE_URL}" -O "${DAT}"
        tar -xzf sample.tar.gz -C "${DIR}"
    fi
fi

while true; do
	resp=$(curl -s "$ES_URL")
	[ $? -eq 0 ] && break
	echo "no connection to ES instance"
	sleep 4
done

if [[ "${CMD}" = "populate" ]]; then
    if [ -e "resources/corpus/" ]; then
        echo "ingest corpus data..."
        python webd/manage.py populate_indices
        echo "rm corpus data..."
        rm "${DAT}"
        rm -r "${DIR}/corpus/"
    fi
fi

if [[ "${CMD}" = "runserver" ]]; then
    echo "start server..."
    python webd/manage.py migrate
    python webd/manage.py runserver 0.0.0.0:8000
fi
