# Código para generar el DB de trabajo, teniendo en mente lo descubierto en el EDA (Jupyter notebook).

import pandas as pd
from name_cleaner import eliminar_nombres

# Importar data raw
movies = pd.read_csv('../../data/raw/0_inicial/movies.csv')
print(movies.columns)

# Limpiar columnas que no se van a utilizar
movies.drop(['Unnamed: 0', 'Genre', 'Wiki Page', 'title'], inplace=True, axis=1)

# Eliminar nombres de los plots y cambiar columna de plots con nombres a sin nombres
movies['plot_sin_nombres'] = movies['Plot'].apply(eliminar_nombres)
movies.drop('Plot', inplace=True, axis=1)


# Guardar
movies.to_csv('../../data/processed/movies_clean.csv')


if __name__ == '__main__':
    __name__
