#!/bin/bash

echo $LISTEN_HOST
echo $LISTEN_PORT
echo $ES_URL
echo $ES_HOST
echo $ES_PORT

while true; do
	resp=$(curl -s "$ES_URL")
	[ "$?" -eq "0" ] && break
	echo "no connection to ES instance"
	sleep 4
done

if [ -e "resources/corpus/" ]; then
	python webd/manage.py populate_indices
	#rm -r resources/corpus/
fi

python webd/manage.py migrate
python webd/manage.py runserver 0.0.0.0:8000
