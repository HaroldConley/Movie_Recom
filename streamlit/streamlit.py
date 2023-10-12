# Code for Streamlit webapp

import streamlit as st


# Título WebApp
st.title('Chat con Documentos')

# Subtítulo
st.subheader('Elige el documento y escribe tu pregunta.')

# Creamos las listas desplegables en la interfaz
documento_seleccionado = st.selectbox('Documento:', vectorstore)

# Ingreso de la pregunta.
query = st.text_area("Escribe tu pregunta aquí:")

# Generación de la respuesta.
# Agregue un botón "Responder" a la interfaz de usuario
if st.button('Responder'):
    with st.spinner('Leyendo el texto...'):
        # Procesamiento
        result = qa({"query": query})

        # Muestra de la respuesta y las páginas (fuentes)
        st.markdown(result['result'], unsafe_allow_html=True)