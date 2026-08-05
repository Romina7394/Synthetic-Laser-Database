# Synthetic Laser Database

A Streamlit application for searching, filtering, and visualizing synthetic laser experiment data.

## Project Background

This application was originally developed as part of my work as a student research assistant (HiWi) at a university.

For this public GitHub repository, the original database connection, credentials, institutional resources, and real experimental data were removed and replaced with a fully synthetic dataset.

No confidential university or laboratory data is included in this repository.

## About the Dataset

The included dataset is completely synthetic and was created only for software development, database testing, filtering, and visualization.

It contains:

* No real laboratory measurements
* No personal information
* No confidential university data
* No proprietary research data

Names beginning with `SYN-` indicate artificial experiment IDs, laser systems, scanners, and measurement devices.

The numerical values are generated for demonstration purposes and must not be interpreted as scientific results.

## Project Features

* Display laser experiment data
* Detect numeric columns
* Filter data using minimum and maximum values
* Display descriptions of technical parameters
* Visualize selected parameters using scatter plots
* Prepare logical data groups for future database normalization

## Project Files

```text
laser_database_app_github.py
synthetic_laser_databank.csv
requirements.txt
README.md
```

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run laser_database_app_github.py
```

Alternatively, on Windows:

```powershell
py -m streamlit run laser_database_app_github.py
```

## Technologies

* Python
* Streamlit
* Pandas
* Matplotlib

## Important Notice

This public version uses synthetic CSV data instead of the original university database.

The original database credentials, server address, real experimental data, and Streamlit secrets are not included in this repository.
