import streamlit as st
import pandas as pd


with st.container():
    st.title('Contratos 2024')
    st.write('Inforamações sobre contratos ao longo do ano de 2024')
    st.write ('Quer saber mais? [clique aqui](www.google.com.br)')
    print('oi')

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('resultados.csv')
    return tabela

with st.container():
    st.write('--------')
    st.title('Dash Contratos')
    dados = carregar_dados()
    qtd_dias = st.selectbox('Selecione o periodo',['Semanal','Quinzenal','Mensal','Ano'])
    if(qtd_dias=='Semanal'):
        nmrdias = 7
    elif(qtd_dias=='Quinzenal'):
        nmrdias = 15
    elif(qtd_dias=='Mensal'):
        nmrdias = 30
    else:
        nmrdias = 360
    dados = dados[-nmrdias:]
    st.area_chart(dados, x='Data', y='Contratos')
    

    