import os
import streamlit as st
import pandas as pd
import numpy as np
import calendar
from datetime import datetime
from decouple import config
from sqlalchemy import create_engine

# Configurações do banco
TIME_ZONE = 'America/Sao_Paulo'
USE_L10N = True
USE_TZ = True

SECRET_KEY = config('SECRET_KEY', default='')
DB_TYPE = config("DB_TYPE", default='')
DB_HOST = config("DB_HOST", default='')
DB_PORT = config("DB_PORT", default='1433')
DB_USER = config("DB_USER", default='')
DB_PASSWORD = config("DB_PASSWORD", default='')
DB_NAME = config("DB_NAME", default='')
# String de conexão
CONNECTION_STRING = f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server"

st.set_page_config(layout="wide")

# Criação do engine
@st.cache_resource
def get_engine():
    return create_engine(CONNECTION_STRING)

# Consulta ao banco de dados
@st.cache_data(ttl=300)  # Cache por 5 minutos
def consultar_dados(query):
    try:
        with get_engine().connect() as connection:
            return pd.read_sql(query, connection)
    except Exception as e:
        st.error(f"Erro na consulta SQL: {e}")
        return None

# # Interface do Streamlit
# st.title("Dashboard com SQLAlchemy")

sql_file_path = os.path.join(os.path.dirname(__file__), "query.sql")

# Abrir e ler o conteúdo do arquivo .sql
with open(sql_file_path, "r", encoding="utf-8") as file:
    sql_script = file.read()
dados = consultar_dados(sql_script)

df = pd.DataFrame(dados)

if dados is not None and len(dados) > 0:
    # Convertendo colunas para tipos apropriados (se necessário)
    df['Programado_Inicio'] = pd.to_datetime(df['Programado_Inicio'], errors='coerce')
    df['Real_Inicio'] = pd.to_datetime(df['Real_Inicio'], errors='coerce')
    df['Programado_Fim'] = pd.to_datetime(df['Programado_Fim'], errors='coerce')
    df['Real_Fim'] = pd.to_datetime(df['Real_Fim'], errors='coerce')
    
    df.drop_duplicates(subset=['Id', 'Pergunta', 'Real_Fim'])
    # st.dataframe(df)
    try:
        # Pivotando os dados
        pivoted_df = df.pivot_table(
            index=['Verificação','Nome_Tarefa','Programado_Inicio','Real_Inicio','Programado_Fim','Real_Fim','Usuario','Local','PDF'],
            columns='Pergunta',
            values='Resposta',
            aggfunc='first',
        ).reset_index()
        
        # Exibindo o DataFrame no Streamlit
        st.markdown(
            """
            <style>
            [data-testid="stMainBlockContainer"] {
                padding: 6rem 2rem 1rem;
            }
            [data-testid="stHeader"] {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 80px;
                background-color: #123a57; 
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Divisão superior
        col1, col2 = st.columns([3, 2])

        # Gráfico Esquerda (60%)
        with col1:

            # Criando dados e exibindo um gráfico nativo do Streamlit
            min_data = df["Real_Fim"].min()
            max_data = df["Real_Fim"].max()

            # Gerando um intervalo de datas baseado no mínimo e máximo
            dates = pd.date_range(start=min_data, end=max_data, freq="D")

            # Transformando as datas em strings para exibição no gráfico
            df["Real_Fim"] = df["Real_Fim"].dt.strftime('%Y-%m-%d')
            contagem_distinta = df['Id'].value_counts()

            # Criando o gráfico de barras nativo
            st.bar_chart(data=df.set_index(df["Real_Fim"])[df["Id"]])

        # Gráfico Direita (40%)
        with col2:
            # Criando outro gráfico nativo do Streamlit
            data = pd.DataFrame(
                np.random.randn(20, 3),
                columns=['X', 'Y', 'Z']
            )
            st.bar_chart(data)

        # Parte inferior (100%)

        # Gráfico inferior
        st.dataframe(pivoted_df)
    except Exception as e:
        st.error(f"Erro ao pivotar os dados: {e}")
else:
    st.warning("Nenhum dado encontrado para exibir.")

# with st.sidebar:
#     st.header("Filtros")
    
#     # Filtro de Ano
#     ano_atual = datetime.now().year
#     anos = list(range(ano_atual - 5, ano_atual + 1))  # últimos 5 anos até o atual
#     ano_selecionado = st.selectbox("Selecione o Ano", anos)
    
#     # Filtro de Mês
#     meses = list(range(1, 13))
#     mes_nomes = [calendar.month_name[mes] for mes in meses]  # nomes dos meses
#     mes_selecionado = st.selectbox("Selecione o Mês", meses, format_func=lambda x: calendar.month_name[x])
# Estilo CSS para o layout

