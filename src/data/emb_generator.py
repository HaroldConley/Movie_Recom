# Code to generate embeddings based on movie plots.

import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings


# Importing the database ready to work.
movies = pd.read_csv('../../data/processed/movies_clean.csv')
movies.drop('Unnamed: 0', axis=1, inplace=True)


# Creating the 'document' with metadata.
df_loader = DataFrameLoader(movies, page_content_column='plot_sin_nombres')
df_document = df_loader.load()

# Defining the model to use for generating embeddings.
embedding_function = SentenceTransformerEmbeddings(model_name="sentence-t5-xl")
print('Transformer descargado.')

# Creating the vectorial database.
db = FAISS.from_documents(df_document, embedding_function)
print('DB vectorial creada.')

# Saving the database.
db.save_local('plot_embeddings')


if __name__ == '__main__':
    __name__
