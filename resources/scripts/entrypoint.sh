#!/bin/bash

echo $LISTEN_HOST
echo $LISTEN_PORT
echo $ES_URL
echo $ES_HOST
echo $ES_PORT

while true; do
	resp=$(curl -s "http://es:9200")
	[ "$?" -eq "0" ] && break
	echo "no connection to ES instance"
	sleep 4
done

python manage.py populate_indices
rm -r resources/corpus/
python manage.py runserver 0.0.0.0:8000
