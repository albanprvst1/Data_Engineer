import pandas as pd
import yfinance as yf
import datetime 
from sqlalchemy import *
from db.database import init_db,ETFData, SessionLocal

time_end = datetime.datetime.now()
time_start = time_end.replace(year=time_end.year-1)


def fetch_etf_data(ticker_symbol) :
    try :
        df = yf.download(
        tickers=ticker_symbol,
        group_by="ticker",
        interval = "1d",
        multi_level_index=False,
        start=time_start,
        end=time_end,
        )
        df = df[["Open","Close", "High", "Low", "Volume"]]
        print(df)
        return df
    except :
        print('Erreur de téléchargement')

def save_to_database(df):

    # 1. Créer la table dans la base SQLite si elle n'existe pas encore
    init_db()

    # 2. Ouvrir une session de connexion
    session = SessionLocal()

    try:
    # 3. Instancier une nouvelle ligne de données

        for date,row in df.iterrows():
            nouvel_etf = ETFData(
                ticker=ETF,
                date = str(date),
                open_price=float(row["Open"]),
                high_price=float(row["High"]),
                low_price=float(row["Low"]),
                close_price=float(row["Close"]),
                volume=int(row["Volume"]),
            )
            session.add(nouvel_etf)

        session.commit()
        

    except Exception as e:
        # En cas d'erreur, on annule les modifications
        session.rollback()
        print(f"Erreur lors de l'insertion : {e}")

    try:
        # Récupérer toutes les lignes de la table
        toutes_les_donnees = session.query(ETFData).all()

        if not toutes_les_donnees:
            print("La base de données est vide.")
            return

        # 3. Parcourir et afficher chaque ligne
        for ligne in toutes_les_donnees:
            print(
                f"Ticker: {ligne.ticker} | Date: {ligne.date} | Clôture: {ligne.close_price}$"
            )

    except Exception as e:
        print(f"Erreur lors de la lecture : {e}")


    #Toujours fermer la session
    session.close()

if __name__ == "__main__":
    print(time_end)
    print(time_start)
    ETF = 'NVDA' #print(str(input('ETF : ? ')))
    df = fetch_etf_data(ETF)
    save_to_database(df)