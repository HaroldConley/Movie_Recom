# Código para generar el DB de trabajo, teniendo en mente lo descubierto en el EDA (Jupyter notebook).

import pandas as pd

# Importar data raw
movies = pd.read_csv('data/raw/0_inicial/movies.csv')
print(movies.columns)

# Limpiar columnas que no se van a utilizar
movies.drop(['Unnamed: 0', 'Genre', 'Wiki Page', 'title'], inplace=True, axis=1)

# Guardar
movies.to_csv('data/processed/movies_clean.csv')
