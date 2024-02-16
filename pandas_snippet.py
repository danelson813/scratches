# pandas_snippet.py

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite://mydb")

df = pd.read_csv('population_total.csv')

df.to_sql('population', engine)
