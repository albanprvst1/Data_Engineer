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