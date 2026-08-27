import pandas as pd
import yfinance as yf
import datetime 

time_end = datetime.datetime.now()
time_start = time_end.replace(year=time_end.year-1)

print(time_end)
print(time_start)

def fetch_etf_data(ticker_symbol) :
    try :
        print('coucou')
    except :
        print('Erreur de téléchargement')

fetch_etf_data(1)