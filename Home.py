import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title='Home')

st.title('Home')
st.sidebar.success('Selecione uma página acima')


if page == "Home":
    st.write("Bem-vindo à Página Principal!")
else:
    # Construindo o caminho completo para o arquivo da página selecionada
    base_dir = os.path.dirname(__file__)  # Caminho do arquivo atual (Home.py)
    file_path = os.path.join(base_dir, "pages", f"{page}.py")  # Caminho para o arquivo da página

    # Verifica se o arquivo existe antes de tentar carregá-lo
    if os.path.exists(file_path):
        with open(file_path) as file:
            exec(file.read())
    else:
        st.error("Página não encontrada.")

    
