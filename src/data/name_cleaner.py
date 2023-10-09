# Código para generar la función para eliminar nombres de personas de textos, junto con todas sus dependencias.

import spacy


nlp = spacy.load("en_core_web_trf")


# Función para eliminar nombres de personas de un texto
def eliminar_nombres(texto):
    """ Función para eliminar los nombres de personas de un texto dado.

    :param texto: el texto de donde se eliminarán los nombres.
    :return: texto sin los nombres.

    >>> eliminar_nombres('Mi nombre es John Connor, lider de la rebelión.')
    'Mi nombre es  , lider de la rebelión.'
    """
    doc = nlp(texto)
    palabras_sin_nombres = [token.text for token in doc if token.ent_type_ != "PERSON"]
    return " ".join(palabras_sin_nombres)
