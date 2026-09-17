import datetime 
import pandas as pd
import yfinance as yf
from google.cloud import storage

time_end = datetime.datetime.now()
time_start = time_end.replace(year=time_end.year - 1)

GCP_KEY_PATH = "gcp-key.json"
GCP_BUCKET_NAME = "etf-raw-data-alban-2026"

def fetch_etf_data(ticker_symbol):
    try:
        df = yf.download(
            tickers=ticker_symbol,
            group_by="ticker",
            interval="1d",
            multi_level_index=False,
            start=time_start,
            end=time_end,
        )
        df = df[["Open", "Close", "High", "Low", "Volume"]]
        return df
    except Exception as e:
        print(f"Erreur de téléchargement : {e}")
        return None

def upload_to_gcs(df, bucket_name, destination_blob_name):
    try:
        # Authentification via la clé JSON
        storage_client = storage.Client.from_service_account_json(GCP_KEY_PATH)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        
        # Conversion du DataFrame en mémoire
        csv_data = df.to_csv(index=True)
        
        # Envoi sur Cloud Storage
        blob.upload_from_string(csv_data, content_type='text/csv')
        print(f" Succès : Données envoyées vers gs://{bucket_name}/{destination_blob_name}")
    except Exception as e:
        print(f" Erreur lors de l'upload : {e}")

if __name__ == "__main__":
    ETF = 'NVDA'
    print(f"Téléchargement des données pour {ETF}...")
    df = fetch_etf_data(ETF)
    
    if df is not None and not df.empty:
        # On définit un chemin avec dossier dans le bucket (ex: raw/NVDA_data.csv)
        destination_path = f"raw/{ETF}_data.csv"
        upload_to_gcs(df, GCP_BUCKET_NAME, destination_path)