
```markdown
# 📈 Pipeline d'Extraction Financière (Phase 1)

Ce projet est un pipeline de données automatisé (ETL) développé en Python. Il permet d'extraire l'historique des cotations boursières sur un an pour l'ETF **MSCI World (CW8.PA)** via l'API Yahoo Finance, de structurer les données sous forme de DataFrames Pandas, puis de les stocker dans une base de données SQLite locale pour permettre des analyses SQL.

---

## 📁 Architecture du Projet

```text
Mon_Projet/
│
├── db/
│   ├── __init__.py        # Déclaration du package Python
│   └── database.py        # Configuration SQLAlchemy & Modèle de table (ETFData)
│
├── extract.py             # Pipeline ETL (Extraction YFinance & Sauvegarde SQLite)
├── query.py               # Script d'exécution des requêtes analytiques avec Pandas
├── analytics.sql          # Requêtes SQL d'analyse (Top Volumes & Statistiques)
├── requirements.txt       # Liste des dépendances du projet
└── .gitignore             # Exclusion des fichiers temporaires (.venv, .db)

```

---

## 🚀 Guide de Démarrage

Suivez ces 3 étapes pour exécuter le projet sur votre machine :

### 1. Cloner le projet et créer l'environnement virtuel

```bash
git clone [https://github.com/votre-compte/votre-depot.git](https://github.com/albanprvst1/Data_Engineer)
cd votre-depot
python -m venv .venv

```

**Activation de l'environnement virtuel :**

* **Windows (PowerShell) :** `.venv\Scripts\Activate.ps1`
* **Mac/Linux :** `source .venv/bin/activate`

### 2. Installer les dépendances

```bash
pip install -r requirements.txt

```

### 3. Lancer le pipeline et exécuter les analyses

```bash
# 1. Extraction et stockage des données dans SQLite
python extract.py

# 2. Exécution des requêtes SQL d'analyse
python query.py

```

---

## 📊 Analyses SQL incluses (`analytics.sql`)

Le fichier `analytics.sql` contient les requêtes utilisées pour l'analyse des cotations :

1. **Top 10 des volumes d'échange :** Sélectionne les 10 journées avec la plus forte liquidité (`ORDER BY volume DESC LIMIT 10`).
2. **Statistiques du prix de clôture :** Calcule le prix moyen (`AVG`), le prix minimum (`MIN`) et le prix maximum (`MAX`) pour l'actif concerné.

---

## 🛠️ Technologies utilisées

* **Python 3.10+**
* **Pandas** : Manipulation des DataFrames et intégration SQL
* **yfinance** : Extraction des données boursières
* **SQLAlchemy & SQLite** : Modélisation ORM et base de données relationnelle locale

```
