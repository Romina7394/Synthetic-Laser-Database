# 📊 Synthetische Laserdatenbank

Eine modulare Streamlit-Anwendung zum Suchen, Filtern, Verarbeiten und Visualisieren synthetischer Daten aus Laserexperimenten.

## 📌 Projekthintergrund

Diese Anwendung wurde ursprünglich im Rahmen meiner Tätigkeit als studentische Hilfskraft (HiWi) an einer Hochschule entwickelt.

Die ursprüngliche Projektversion arbeitete mit einer internen MySQL-Datenbank und realen Laserexperiment-Daten.

Für dieses öffentliche GitHub-Repository wurden jedoch alle realen Datenbankverbindungen, Zugangsdaten, institutionellen Ressourcen und Versuchsdaten entfernt.

Die öffentliche Version verwendet stattdessen einen vollständig synthetischen Datensatz, der ausschließlich zur Demonstration und zum Testen der Softwarefunktionen dient.

Dieses Repository enthält keine vertraulichen Daten der Hochschule oder des Labors.

## 📂 Über den Datensatz

Der enthaltene Datensatz ist vollständig synthetisch und wurde ausschließlich für Softwareentwicklung, Datenverarbeitung, Filterfunktionen und Visualisierungen erstellt.

Er enthält:

* Keine realen Labormessungen
* Keine personenbezogenen Daten
* Keine vertraulichen Hochschuldaten
* Keine geschützten Forschungsdaten
* Keine realen Datenbank-Zugangsdaten

Bezeichnungen, die mit `SYN-` beginnen, kennzeichnen künstlich erzeugte Versuchs-IDs, Lasersysteme, Scanner und Messgeräte.

Die numerischen Werte wurden zu Demonstrations- und Testzwecken generiert und dürfen nicht als wissenschaftliche Ergebnisse interpretiert werden.

## 🔍 Projektfunktionen

Die Anwendung unterstützt unter anderem:

* Laden und Anzeigen synthetischer Laserexperiment-Daten
* Vorbereitung und Bereinigung der Daten
* Erkennung und Konvertierung numerischer Spalten
* Anzeige technischer Parameter und ihrer Beschreibungen
* Filterung numerischer Parameter anhand von Minimal- und Maximalwerten
* Anzeige der gefilterten Ergebnisse
* Auswahl zweier numerischer Parameter für Visualisierungen
* Darstellung gefilterter Werte als Streudiagramm
* Vorbereitung logischer Datengruppen
* Modulare Trennung von Datenverarbeitung, Filterung, Visualisierung und Benutzeroberfläche

Die Parameter werden in logische Gruppen unterteilt, beispielsweise:

* Entry Information
* Laser Parameters
* Scanner Parameters
* Scan Regime
* Riblet Analysis
* Calculated Parameters

## 🧩 Modulare Projektstruktur

Die Anwendung wurde im weiteren Verlauf des Projekts refaktoriert.

Anstatt die gesamte Programmlogik in einer einzelnen Python-Datei zu speichern, wurden unterschiedliche Verantwortlichkeiten in separate Module aufgeteilt.

Dadurch ist der Code übersichtlicher, leichter wartbar und einfacher erweiterbar.

```text
laser-database/
│
├── assets/
│   └── background.png
│
├── images/
│   ├── app-overview.png
│   ├── filtered-data.png
│   └── scatter-plot.png
│
├── src/
│   └── laser_database/
│       ├── __init__.py
│       ├── background.py
│       ├── config.py
│       ├── database.py
│       ├── data_groups.py
│       ├── data_processing.py
│       ├── descriptions.py
│       ├── filtering.py
│       ├── numeric_processing.py
│       ├── ui.py
│       └── visualization.py
│
├── app.py
├── run.py
├── synthetic_laser_databank.csv
├── requirements.txt
├── pyproject.toml
├── README.md
├── .gitignore
└── LICENSE
```

### Aufgaben der wichtigsten Module

* `data_processing.py` – Vorbereitung und Bereinigung der Daten
* `data_groups.py` – Aufteilung der Parameter in logische Datengruppen
* `numeric_processing.py` – Erkennung und Konvertierung numerischer Spalten
* `filtering.py` – Filterung der Daten und Vorbereitung der Plot-Daten
* `visualization.py` – Erstellung der Visualisierungen
* `descriptions.py` – Beschreibungen technischer Parameter
* `background.py` – Verwaltung des Streamlit-Hintergrunds
* `ui.py` – Aufbau der Streamlit-Benutzeroberfläche
* `config.py` – Zentrale Projektkonfiguration

## 📈 Ergebnisse und Anwendungsbeispiel

Die Anwendung lädt den synthetischen Datensatz und stellt die enthaltenen Laserexperiment-Daten in einer interaktiven Streamlit-Oberfläche dar.

Benutzer können:

* eine logische Datengruppe auswählen,
* technische Parameter und deren Beschreibungen anzeigen,
* numerische Spalten anhand eines Minimal- und Maximalwertes filtern,
* gefilterte Datensätze anzeigen,
* zwei numerische Parameter für eine Visualisierung auswählen,
* mögliche Beziehungen zwischen Parametern mithilfe eines Streudiagramms untersuchen.

### 📈 Übersicht der Anwendung

![Übersicht der Streamlit-Anwendung](images/app-overview.png)

### 📈 Gefilterte Daten

Das folgende Beispiel zeigt die Filterung eines numerischen Parameters innerhalb eines ausgewählten Wertebereichs.

![Gefilterte Laserdaten](images/filtered-data.png)

### 📈 Visualisierung

Die gefilterten Werte können als Streudiagramm dargestellt werden, um mögliche Beziehungen zwischen zwei Parametern zu untersuchen.

![Streudiagramm der synthetischen Daten](images/scatter-plot.png)

Alle dargestellten Ergebnisse basieren ausschließlich auf dem synthetischen Datensatz und stellen keine realen wissenschaftlichen Messergebnisse dar.

## ⚙️ Voraussetzungen

* Python 3.10 oder neuer
* pip

Für die öffentliche Version ist kein Zugang zur ursprünglichen Hochschul- oder Labordatenbank erforderlich.

## 🔧 Installation

### 1. Repository klonen

```bash
git clone <repository-url>
cd laser-database
```

### 2. Virtuelle Umgebung erstellen

```bash
python -m venv .venv
```

### 3. Virtuelle Umgebung aktivieren

Unter Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Unter Windows CMD:

```cmd
.venv\Scripts\activate
```

Unter Linux oder macOS:

```bash
source .venv/bin/activate
```

### 4. Abhängigkeiten installieren

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Lokales Package installieren

```bash
python -m pip install -e .
```

Die Option `-e` installiert das Projekt im Editable Mode. Änderungen innerhalb von `src/laser_database` stehen dadurch direkt zur Verfügung, ohne dass das Package nach jeder Änderung erneut installiert werden muss.

## 🪟 Automatische Installation unter Windows

Unter Windows kann die Einrichtung alternativ über die bereitgestellte BAT-Datei durchgeführt werden.

Das Setup:

1. erstellt automatisch eine virtuelle Umgebung `.venv`,
2. aktiviert die virtuelle Umgebung,
3. aktualisiert `pip`,
4. installiert die Abhängigkeiten aus `requirements.txt`,
5. installiert das lokale Projekt im Editable Mode.

Dadurch muss die virtuelle Umgebung nicht zwischen verschiedenen Computern oder Benutzern kopiert werden.

Jeder Benutzer erstellt seine eigene lokale Umgebung auf Basis der Projektdateien.

## ▶️ Anwendung starten

Nach der Installation kann die Anwendung mit folgendem Befehl gestartet werden:

```bash
python run.py
```

Alternativ kann Streamlit direkt gestartet werden:

```bash
python -m streamlit run app.py
```

## 🕷️ Verwendung mit Spyder

Bei Verwendung von Spyder sollte der Python-Interpreter der projektspezifischen virtuellen Umgebung ausgewählt werden.

Unter Windows befindet sich dieser normalerweise unter:

```text
laser-database\.venv\Scripts\python.exe
```

Dadurch verwendet Spyder dieselben Python-Pakete und Abhängigkeiten wie das Projekt.

Die virtuelle Umgebung `.venv` sollte nicht von einem anderen Computer kopiert werden. Stattdessen sollte sie für jeden Benutzer neu über `requirements.txt` beziehungsweise die bereitgestellte Setup-Datei erstellt werden.

## 🔐 Zugangsdaten und Streamlit Secrets

Die ursprüngliche interne Projektversion verwendete eine lokale Datei:

```text
.streamlit/secrets.toml
```

Darin wurden die für die interne Datenbankverbindung benötigten Informationen wie Benutzername, Passwort, Serveradresse und Datenbankname gespeichert.

Diese Datei ist **nicht Bestandteil dieses öffentlichen Repositorys**.

Ebenso wurden keine realen:

* Benutzernamen
* Passwörter
* Serveradressen
* Datenbanknamen
* Streamlit-Secrets
* institutionellen Netzwerkpfade

in das öffentliche Repository übernommen.

Die öffentliche Version benötigt keine Zugangsdaten zur ursprünglichen Hochschul- oder Labordatenbank.

## 🛠️ Verwendete Technologien

* Python
* Streamlit
* Pandas
* Matplotlib
* Python Virtual Environments
* Python Packaging (`pyproject.toml`)

## 🔒 Datenschutz und öffentliche Version

Dieses Repository stellt ausschließlich eine öffentliche Demonstrationsversion des Projekts dar.

Die Software basiert auf der während des ursprünglichen Projekts entwickelten Anwendung. Für die Veröffentlichung wurden jedoch alle institutionellen und vertraulichen Bestandteile entfernt oder durch synthetische Alternativen ersetzt.

Insbesondere enthält dieses Repository keine:

* realen Versuchsdaten,
* vertraulichen Forschungsdaten,
* Datenbank-Zugangsdaten,
* internen Serverinformationen,
* Streamlit-Secrets,
* personenbezogenen Daten,
* internen Hochschulressourcen.

Der synthetische Datensatz dient ausschließlich dazu, die Softwarearchitektur, Datenverarbeitung, Filterfunktionen und Visualisierung der Anwendung zu demonstrieren.

## 👩‍💻 Autorin

**Romina Emadi**
Data Science Studentin | Ziel: Data Analyst

---

## 📜 License

MIT License
