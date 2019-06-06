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

Obwohl die Anwendung innerhalb des Containers ausgefuehrt wird, werden Aenderungen an Programmcode,
HTML-Templates und Assets sofort sichtbar, da das Quellverzeichnis `webd` direkt vom Dateisystem
des Hosts in das des Containers gemounted wird.


### Inhaltsuebersicht

Saemtlicher Programmcode, die HTML-Templates und assets wie Fonts, Grafiken, Styles und 
Javascript-Bibliotheken befinden sich im Unterverzeichnis `webd/`.
Die wichtigsten Verzeichnisse darin sind die folgenden:

- `templates/`: Hier befinden sich die HTML-Templates. Diese stehen ueber den Django-Tag `{% extends %}` untereinander in Vererbungsbeziehung
- `static/`: Das asset-Verzeichnis der Anwendung. Es enthaelt Fonts, Grafiken, Styles und JS-Bibliotheken
- `search/`: Enthaelt URL-Mappings und Handler fuer die Suchseiten
- `detail/`: Enthaelt URL-Mappings und Handler fuer die Detailseiten
- `store/`: Darin sind die Suchanfragen an Elasticsearch implementiert

Im folgenden wird auf die einzelnen Bereiche genauer eingegangen:


#### `webd/templates/`

Dieses Verzeichnis enthaelt die Template-Dateien, die durch Verarbeitung von Django-Template-Tags mit dynamischen Inhalten gefuellt werden.
Das Basis-Template liegt in der Datei `webd/templates/base.html`. Die Templates fuer die konkreten einzelnen Webseiten erben von diesem
Basis-Template und muessen deshalb bestimmte wiederkehrende Inhalte nicht selber definieren. So kuemmert sich das Basis-Template z.B. um
die Einbindung von Ressourcen wie JQuery, Bootstrap, fontawesome, den Akademiefont, ResJS und so weiter im HTML-Header. Die erbenden Templates koennen allerdings
auch bestimmte Bereiche des Basis-Templates ueberschreiben. Die Bereiche, die dafuer zugelassen sind, werden im Basis-Template mit dem Template-Tag `{% block xy %}...{%endblock%}`
ausgewiesen.

Die Unterverzeichnisse `webd/templates/details/` und `webd/templates/search/` enthalten Templates fuer Detailansicht- bzw. Such- und Suchergebnisseiten.

Vom Basis-Template direkt erben die Templates `webd/templates/details/lemma.html` und `webd/templates/search/index.html`.
Auch das Template `webd/templates/search_results.html` erbt direkt vom Basis-Template, ist aber genau wie dieses kein Template fuer eine eigenstaendige Seite, sondern
dient ebenfalls der Vererbung, und zwar fuer die Suchergebnisseiten-Templates `webd/templates/search/dict.html` und `/webd/templates/search/occurrences.html`.

Die HTML-Templates, welche im Handler referenziert werden, werden durch die Django-Templating-Engine mit vom Handler mitgegebenen Inhalten gefuellt.
Die Syntax der Templating Language, mit welcher diese Inhalte im Template evaluiert werden, ist beschrieben unter https://docs.djangoproject.com/en/2.2/topics/templates/#syntax


#### `webd/static/`

Im assets-Verzeichnis `webd/static/` befinden sich allerlei Ressourcen, welche extern in die Webseiten eingebunden werden, also Bilder, Javascript, CSS und so weiter.
Dazu ist die Verwendung des Django-Tags `{%static "../pfad/datei.ext"%}` noetig, wie zum Beispiel bei der Einbindung des Webseiten-spezifischen Stylesheets im `<head>`-Element des Basis-Templates
`base.html`:
```html
	<link href="{% static "css/tla-styles.css" %}" rel="stylesheet" type="text/css">
```

#### `webd/search/`

Im `search`-package befinden sich die handler fuer Woerterbuch- und Belegstellensuche. Beide sind im Modul `webd/search/views.py`, und zwar in Form der beiden 
Funktionen `search_dict` bzw. `search_text_words`. Welche Funktionen fuer die Behandlung von Anfragen an welchen URL-Pfad verantwortlich sind, kann man
in den verschiedenen `urls.py` Modulen des Projekts nachvollziehen. Zum Beispiel sieht man in `webd/search/urls.py`, dasz URLS, deren letztes Pfadsegment `dict` lautet,
von der Funktion `search_dict` behandelt werden. Dasz dabei das erste Pfadsegment `search` sein musz, sieht man an der Einbindung des `webd/search/urls.py` Moduls in
`/webd/webd/urls.py` mithilfe von `include('search.urls`)`.

Die Request-Handler-Funktionen `search_dict` und `search_text_words` geben bei ihrer Rueckgabe jeweils das HTML-Template an, welches sie mit entsprechenden Inhalten befuellen wollen.
Das gleiche macht der Handler `search`, der aber nur die Suchseite mit den Suchformularen ausliefert.
Daraus ergibt sich folgende Zuordnung von URLs zu HTML-Template-Dateien:

- `/search`: `/webd/templates/search/index.html`
- `/search/dict`: `webd/templates/search/dict.html`
- `/search/occurrences`: `webd/templates/search/occurrences.html`

Die HTML-Templates, welche im Handler referenziert werden, werden durch die Django-Templating-Engine mit vom Handler mitgegebenen Inhalten gefuellt.
Die Syntax der Templating Language, mit welcher diese Inhalte im Template evaluiert werden, ist beschrieben unter https://docs.djangoproject.com/en/2.2/topics/templates/#syntax

##### Woerterbuchsuche

Das Template `search/dict.html` bekommt folgende Daten geliefert:

| Name         | Inhalt                                                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `hitcount`   | Anzahl der Suchergebnisse                                                                                                                           |
| `page`       | Die Nummer der aktuell aufgeblaetterten Seite mit Suchergebnissen auf Basis der Paginierung                                                         |
| `start`      | Position des ersten auf der aktuellen Seite angezeigten Suchergebnisses innerhalb der Suchergebnisliste                                             |
| `end`        | Position des letzten auf der aktuellen Seite angezeigte Suchergebnisses innerhalb der Suchergebnisliste                                             |
| `pagination` | Eine Liste von Listen mit jeweils zwei Elementen, von denen das erste eine Seitenzahl und das zweite den Link zu dieser Suchergebnisseite darstellt |
| `hits`       | Die tatsaechlichen Suchergebnisse im Woerterbuch die auf der aktuell aufgeblaetterten Seite (as in Paginierung) angezeigt werden sollen             |

Die einzelnen Eintraege in der `hits`-Liste der Woerterbuchsuche bestehen jeweils aus drei Werten: dem Grad der Einrueckung (`0`-`2`), die optionale Beziehung, welche fuer die Einrueckung
verantwortlich ist (z.b. `rootOf`), und als drittes schlieszlich das tatsaechliche Lemma. Zur Veranschaulichung dieser Struktur befindet sich ein solches Suchergebnis in der Datei
`resources/examples/lemma_hit.json`.

##### Belegstellensuche

Die Daten, welche in das Template `search/occurrences.html` eingetragen werden, aehneln denen in der Woerterbuchsuche. Sie unterscheiden sich aber natuerlich in der Struktur der einzelnen 
Suchergebnisse. Jedes einzelne Suchergebnis besteht aus einem `occurrence`, einem `sentence` und einem `text` Objekt. Wie das ungefaehr aussieht, veranschaulicht das Beispielsuchergebnis
in der Datei `resources/examples/occurrence_hit.json`.


#### `webd/detail/`

Im Paket `detail` befindet sich der Handler fuer die Lemmadetailseite, und zwar in der Funktion `lemma_details_page` im Modul `views.py`. Die Daten, die der Handler an das HTML-Template
in `webd/templates/details/lemma.html` liefert, wo sie ueber die Django-Template-Language eingebunden werden koennen, beinhalten die folgenden Felder:

| Name          | Inhalt                                                                                                                                                               |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `lemma`       | Der Woerterbucheintrag, der angezeigt werden soll                                                                                                                    |
| `bibl`        | Eine Liste von bibliographischen Angaben                                                                                                                             |
| `coins`       | COinS-Metadaten im KEV-Format (https://helpful.knobs-dials.com/index.php/OpenURL_notes#Serialization)                                                                |
| `occurrences` | Eine Datenstruktur, welche die Anzahl der Vorkommen dieses Lemmas in verschiedenen Bereichen enthaelt, z.B. im Bereich `corpus`                                      |
| `annotations` | Eine Liste der zu diesem Lemmaeintrag gehoerenden Annotationen in vorformatiertem HTML. Jede Annotation besteht aus `title`, `body`, `edited.name` und `edited.date` |

Ein Beispiel fuer ein an das Template ausgeliefertes Einzellemma findet sich in `resources/examples/lemma_details.json`.


#### `webd/store/`