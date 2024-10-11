import streamlit as st
import os

st.set_page_config(page_title='Home')

st.title('Home')
st.sidebar.success('Selecione uma página acima')

# Menu de navegação
page = st.sidebar.selectbox("Navegação", ["Home", "Pizza", "Contratos"])

# Função para carregar a página selecionada
if page == "Home":
    st.write("Bem-vindo à Página Principal!")
else:
    # Diretório onde o arquivo Home.py está localizado
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Caminho absoluto do diretório atual
    file_path = os.path.join(base_dir, "pages", f"{page}.py")  # Caminho para o arquivo da página

    # Verifica se o arquivo existe antes de tentar carregá-lo
    if os.path.exists(file_path):
        st.write(f"Carregando a página: {file_path}")  # Mensagem de depuração
        with open(file_path) as file:
            exec(file.read())
    else:
        st.error(f"Página não encontrada: {file_path}")  # Mensagem de erro detalhada
