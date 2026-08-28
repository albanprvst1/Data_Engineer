import pandas as pd
from db.database import engine

# Rédiger une requête SQL qui renvoie les 10 jours où il y a eu le plus de volume d'échange sur cet ETF.
sql_query = "SELECT date,volume FROM etf_prices ORDER BY volume DESC LIMIT 10;"

# Rédiger une seconde requête SQL qui calcule le prix de clôture (Close) moyen, minimum et maximum de l'actif.
sql_query2 = "SELECT ticker, AVG(close_price) AS MOYENNE ,MAX(close_price) AS MAX ,MIN(close_price) AS MIN FROM etf_prices GROUP BY ticker;"

# Pandas lit la BDD et affiche un vrai tableau
df = pd.read_sql(sql_query, con=engine)
print(df)
df = pd.read_sql(sql_query2, con=engine)
print(df)