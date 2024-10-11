import streamlit as st
import pandas as pd

st.set_page_config(page_title='Home')

st.title('Home')
st.sidebar.success('Selecione uma página acima')


page = 'Home'
# Menu de navegação
page = st.sidebar.selectbox("Navegação", ["Home", "Pizza", "Contratos"])

# Função para carregar a página selecionada
if page == "Home":
    st.write("Bem-vindo à Página Principal!")
else:
    # Lê o conteúdo do arquivo da página e executa o código
    with open(f"pages/{page}.py") as file:
        exec(file.read())

    
