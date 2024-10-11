import streamlit as st
import os

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")



# Verifica se a pasta "pages" existe
if os.path.exists("paginas"):
    pizza = st.Page("paginas/2_Pizza.py", title="Pizza IA", icon=":material/dashboard:")
    contrato = st.Page("paginas/1_Contratos.py", title="Contratos 2024", icon=":material/dashboard:")
else:
    st.error("A pasta 'paginas' não foi encontrada.")


if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Pizza": [pizza],
            "Contrato": [contrato],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()