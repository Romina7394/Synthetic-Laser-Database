# Synthetische Laserdatenbank

Eine Streamlit-Anwendung zum Suchen, Filtern und Visualisieren synthetischer Daten aus Laserexperimenten.

## Projekthintergrund

Diese Anwendung wurde ursprünglich im Rahmen meiner Tätigkeit als studentische Hilfskraft (HiWi) an einer Hochschule entwickelt.

Für dieses öffentliche GitHub-Repository wurden die ursprüngliche Datenbankverbindung, Zugangsdaten, institutionellen Ressourcen und realen Versuchsdaten entfernt und durch einen vollständig synthetischen Datensatz ersetzt.

Dieses Repository enthält keine vertraulichen Daten der Hochschule oder des Labors.

## Über den Datensatz

Der enthaltene Datensatz ist vollständig synthetisch und wurde ausschließlich für Softwareentwicklung, Datenbanktests, Filterfunktionen und Visualisierungen erstellt.

Er enthält:

* Keine realen Labormessungen
* Keine personenbezogenen Daten
* Keine vertraulichen Hochschuldaten
* Keine geschützten Forschungsdaten

Bezeichnungen, die mit `SYN-` beginnen, kennzeichnen künstlich erzeugte Versuchs-IDs, Lasersysteme, Scanner und Messgeräte.

Die numerischen Werte wurden zu Demonstrationszwecken generiert und dürfen nicht als wissenschaftliche Ergebnisse interpretiert werden.

## Projektfunktionen

* Anzeige von Daten aus Laserexperimenten
* Erkennung numerischer Spalten
* Filterung der Daten anhand von Minimal- und Maximalwerten
* Anzeige von Beschreibungen technischer Parameter
* Visualisierung ausgewählter Parameter mithilfe von Streudiagrammen
* Vorbereitung logischer Datengruppen für eine zukünftige Normalisierung der Datenbank

## Projektdateien

```text
laser_database.py
synthetic_laser_databank.csv
requirements.txt
README.md
```

## Installation

Installation der benötigten Python-Bibliotheken:

```bash
pip install -r requirements.txt
```

## Anwendung starten

```bash
streamlit run laser_database.py
```

Alternativ unter Windows:

```powershell
py -m streamlit run laser_database.py
```

## Verwendete Technologien

* Python
* Streamlit
* Pandas
* Matplotlib

## Wichtiger Hinweis

Diese öffentliche Version verwendet synthetische CSV-Daten anstelle der ursprünglichen Hochschuldatenbank.

Die ursprünglichen Datenbank-Zugangsdaten, die Serveradresse, reale Versuchsdaten und Streamlit-Secrets sind nicht in diesem Repository enthalten.
