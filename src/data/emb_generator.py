# Código para generar los embeddings basados en los plots de las películas.

import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings


# Importando DB lista para trabajar
movies = pd.read_csv('../../data/processed/movies_clean.csv')
movies.drop('Unnamed: 0', axis=1, inplace=True)


# Creando el 'documento' con metadata
df_loader = DataFrameLoader(movies, page_content_column='plot_sin_nombres')
df_document = df_loader.load()

# Definiendo el modelo a usar para generar los embeddings
embedding_function = SentenceTransformerEmbeddings(model_name="sentence-t5-xl")
print('Transformer descargado.')

# Creando la base de datos vectorial
db = FAISS.from_documents(df_document, embedding_function)
print('DB vectorial creada.')

# Guardando la base de datos
db.save_local('../../data/processed/plot_embeddings')


if __name__ == '__main__':
    __name__
