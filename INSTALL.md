## TLA Webdesign Demo

Die TLA Webdesign-Demo besteht aus einer Django-Webapplikation zur Simulation unterschiedlicher
geplanter Suchfunktionen des im Aufbau befindlichen Thesaurus Linguae Aegyptiae inklusive
Darstellung aktueller Corpusdaten im neuen Webdesign.

### Installationsanleitung

Die empfohlene Methode zur Installation der Anwendung ist die Verwendung von `docker-compose`.
Dazu musz folgende Software vorhanden sein:

- [Docker](https://docs.docker.com/install/#desktop)
- [docker-compose](https://docs.docker.com/compose/install/)

`Docker-compose` verwendet Docker, um zwei Container zu starten; 
der erste enthaelt eine Instanz der Suchmaschine Elasticsearch mit den notwendigen Daten, 
der zweite enthaelt die Webapplikation.

Dieses Projektverzeichnis enthaelt die Datei `.env`, in der mittels Umgebungsvariablen
angegeben werden kann, wo diese beiden Dienste erreichbar sind und wo die Beispieldaten
heruntergeladen werden:

		SAMPLE_URL=http://aaew64.bbaw.de/resources/sample/sample-xy.tar.gz
		ES_PORT=9202
		LISTEN_PORT=9005

Die hier gesetzten Werte der Umgebungsvariablen `ES_PORT` und `LISTEN_PORT` bedeuten,
dasz bei laufenden Containern die Elasticsearch-Instanz unter `http://localhost:9202` und
die Webanwendung unter `http://localhost:9005` erreichbar sind.

Waehrend der Installation wird eine Verbindung zum Internet benoetigt.

Um die Webdesign-Demo zu starten, navigieren Sie in der Kommandozeilenumgebung Ihres
Systems in das Projektverzeichnis und fuehren dort aus:

```shell
$ docker-compose up
```

Docker wird nun beginnen, die fuer den Betrieb der beiden Container benoetigten Images
herunterzuladen und das Image fuer den Container mit der Webanwendung zu erstellen.
Dieser Schritt beinhaltet das Herunterladen von Beispieldaten von einem Server der BBAW.

Sie koennen diese Vorgaenge in der Ausgabe Ihrer Kommandozeile verfolgen.

Beim ersten Starten des Containers mit der Webdesign-Demo werden die Beispieldaten in der
Suchmaschine im Elasticsearch-Container abgespeichert. Das kann eine Weile in Anspruch nehmen,
musz aber beim naechsten Starten des Containers nicht wiederholt werden.

Als letztes startet im Container der Webanwendung (`tla_1`) ein Django-Server.
Die Webdesign-Demo ist nun unter der dem in `.env` definierten Port `LISTEN_PORT` erreichbar,
z.B. [http://localhost:9005/](http://localhost:9005).


### 
