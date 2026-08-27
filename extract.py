import pandas as pd
import yfinance as yf
import datetime 

time_end = datetime.datetime.now()
time_start = time_end.replace(year=time_end.year-1)



def fetch_etf_data(ticker_symbol) :
    try :
        df = yf.download(
        tickers=ticker_symbol,
        )
        print(df)
    except :
        print('Erreur de téléchargement')



if __name__ == "__main__":
    print(time_end)
    print(time_start)
    ETF = 'NVDA' #print(str(input('ETF : ? ')))
    fetch_etf_data(ETF)