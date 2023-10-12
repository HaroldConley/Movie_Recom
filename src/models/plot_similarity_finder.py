# Code to find the most similar plot, using the embedding index.

from langchain.vectorstores import FAISS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings


# Searching for similar plots to the users plot/input
# Loading embedding function
embedding_function = SentenceTransformerEmbeddings(model_name="sentence-t5-xl")

# Loading vectorstore
db = FAISS.load_local('data/processed/plot_embeddings', embedding_function)


# Find the most similar plots to the user plot/input
def plot_simil(user_plot, num_recom=5):
    """ Find movies with plots similar to the one give by the user.

    :param user_plot: user plot
    :param num_recom: number of recommendations
    :return: list of lists indicating [Release year, Title] for every recommendation

    >>> plot_simil(
    "
    a time-travel adventure film that follows the story of Marty McFly, a high school student, and his eccentric
    scientist friend, Doc Brown. Doc has invented a time machine out of a DeLorean car, and one night, during a test
    run, Marty is accidentally transported from 1985 to 1955. In 1955, Marty encounters his younger parents, George
    and Lorraine, and inadvertently interferes with their meeting, putting his own existence at risk. Marty seeks the
    help of the younger Doc Brown from 1955 to repair the time machine and return to his own time. Along the way, he
    must ensure that his parents meet and fall in love, all while avoiding running into his younger self. Marty also
    has to contend with the school bully, Biff, who makes life difficult for his father.
    ",
    3
    )

    '[[1990, 'back to the future part iii'],
      [1989, 'back to the future part ii'],
      [1985, 'back to the future']]'
    """

    docs = db.similarity_search(user_plot, num_recom)

    recom = []
    for doc in docs:
        year = doc.metadata['Release Year']
        title = doc.metadata['Title']
        recom.append([year, title])

    return recom


