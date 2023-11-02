# Code for Streamlit webapp

import streamlit as st
from src.models.plot_similarity_finder import plot_simil


# WebApp title and subtitle
st.title('Movie Recommendation.')
st.subheader('Write you movie plot and find a similar one.')

# Plot input.
user_plot = st.text_area("Write the plot here...")


# Generación de la respuesta.
# Agregue un botón "Responder" a la interfaz de usuario
if st.button('Search'):
    with st.spinner('Reading plot...'):
        # Procesamiento
        result = plot_simil(user_plot)

        # Muestra de la respuesta y las páginas (fuentes)
        st.markdown(f'{str.capitalize(result[0][1])}, {result[0][0]}')
        st.markdown(f'{str.capitalize(result[1][1])}, {result[1][0]}')
        st.markdown(f'{str.capitalize(result[2][1])}, {result[2][0]}')
        st.markdown(f'{str.capitalize(result[3][1])}, {result[3][0]}')
        st.markdown(f'{str.capitalize(result[4][1])}, {result[4][0]}')
