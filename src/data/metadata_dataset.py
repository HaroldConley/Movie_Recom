# Code to generate the working database, taking into consideration the findings from the Exploratory
# Data Analysis (EDA) in a Jupyter notebook.

import pandas as pd
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_trf")


# Function to remove names of individuals from a text.
def remove_names(text):
    """ Function to remove the names of people from a given text.

    :param text: the text from which names will be removed.
    :return: text without the names.

    >>> remove_names('My name is John Connor, leader of the rebellion.')
    'My name is , leader of the rebellion .'
    """
    doc = nlp(text)
    words_wo_names = [token.text for token in doc if token.ent_type_ != "PERSON"]
    return " ".join(words_wo_names)


# Load raw data
movies = pd.read_csv('../../data/raw/0_inicial/movies.csv')
print(movies.columns)

# Drop not-used columns
movies.drop(['Unnamed: 0', 'Genre', 'Wiki Page', 'title'], inplace=True, axis=1)

# Removing names of plots and creating a new column in the DB
movies['plot_sin_nombres'] = movies['Plot'].apply(remove_names)
movies.drop('Plot', inplace=True, axis=1)


# Save
movies.to_csv('../../data/processed/movies_clean.csv')


if __name__ == '__main__':
    __name__
