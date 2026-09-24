```markdown
# 🚀 Financial ETF Data Lakehouse Pipeline (GCP & Databricks)

Un pipeline Data Lakehouse moderne, automatisé et scalable permettant d'ingérer, nettoyer, transformer et analyser les cotations boursières financières (NVDA ETF).

---

## 🏗️ Architecture du Pipeline

```text
  [ yfinance API ]
         │
         ▼ (Extract - Python)
 ┌────────────────────────┐
 │  Google Cloud Storage  │  <-- Couche Bronze (Raw CSV)
 └───────────┬────────────┘
             │
             ▼ (Transform - PySpark)
 ┌────────────────────────┐
 │   Databricks Community │  <-- Nettoyage, Cast Schema, Deduplication, KPI
 └───────────┬────────────┘
             │
             ▼ (Export Parquet)
 ┌────────────────────────┐
 │  Google Cloud Storage  │  <-- Couche Silver (Cleaned Parquet)
 └───────────┬────────────┘
             │
             ▼ (Load - BigQuery SDK)
 ┌────────────────────────┐
 │     Google BigQuery    │  <-- Couche Gold (Warehouse Analytics)
 └────────────────────────┘

```

---

## 🛠️ Tech Stack & Services Cloud

* **Extraction & Ingestion :** Python (`yfinance`, `google-cloud-storage`).
* **Data Lake / Storage :** **Google Cloud Storage (GCS)** (Buckets séparés par couches `raw/` et `silver/`).
* **Processing / Compute :** **Apache Spark / PySpark** sur **Databricks Community Edition**.
* **Data Warehouse :** **Google BigQuery** (Dataset `finance_analytics`, Table `fact_etf_cotations`).
* **Orchestration & Sécurité :** Authentification GCP IAM via Service Account (`gcp-key.json`).

---

## 🥇 Architecture Médaillon

1. **Bronze Layer (Raw Data) :**
* Ingestion brute des fichiers CSV issus de l'API `yfinance` directement sur Google Cloud Storage dans le dossier `raw/`.


2. **Silver Layer (Cleaned & Enriched) :**
* Traitement PySpark sous Databricks : correction des types de données, dédoublonnage sur la clé `Date`, et calcul des indicateurs financiers journaliers (`Daily_Variation`, `Daily_Variation_Pct`).
* Exportation sous format binaire compressé **Parquet** dans `silver/`.


3. **Gold Layer (Analytics / Business) :**
* Publication automatique des données Parquet vers une table analytique SQL dédiée dans BigQuery (`fact_etf_cotations`).
* Table optimisée pour les requêtes analytiques SQL et la connexion à des outils de Business Intelligence (Power BI, Looker).



---

## 💻 Structure du Projet

```text
.
├── cluster-etf-pyspark.ipynb   # Notebook Databricks (ETL PySpark & Load BigQuery)
├── extract.py                  # Script d'extraction API yfinance vers GCS (Bronze)
├── analytics.sql               # Requêtes SQL de contrôle analytique dans BigQuery
├── requirements.txt            # Dépendances Python
├── .gitignore                  # Exclusion des clés de sécurité et fichiers temporaires
└── README.md                   # Documentation du projet

```

---

## 🔒 Sécurité & Bonnes Pratiques

* **Protection des identifiants :** La clé de compte de service (`gcp-key.json`) est exclue du suivi de version via le fichier `.gitignore`.
* **Traçabilité :** Pipeline versionné sur GitHub avec suivi des modifications via Git Integration sous Databricks.

```