# Code to find the most similar plot, ussing the embedding index.

from langchain.vectorstores import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings


# Searching for similar plots to the users plot/input
# Loading embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="sentence-t5-xl")

# Loading vectorstore
db = FAISS.load_local('data/processed/plot_embeddings', embedding_function)


# Find the most similar plots to the user plot/input
def plot_simil(user_plot, num_recom=5):
    docs = db.similarity_search(user_plot, num_recom)

    recom =[]
    for doc in docs:
        year = doc.metadata['Release Year']
        title = doc.metadata['Title']
        recom.append([year, title])

    return recom


