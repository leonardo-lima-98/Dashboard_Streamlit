
import streamlit as st
import pandas as pd
from decouple import config
from sqlalchemy import create_engine

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

# Criação da conexão
engine = create_engine(f"{DB_TYPE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?driver=ODBC+Driver+17+for+SQL+Server")

# Título do Dashboard
st.title("Dashboard com Dados do SQL")

# Sidebar para selecionar filtros
st.sidebar.header("Filtros")
tabela = st.sidebar.text_input("Nome da Tabela", "minha_tabela")
limite = st.sidebar.number_input("Limite de Linhas", min_value=1, max_value=1000, value=100)

# Consulta ao Banco de Dados
@st.cache_data(ttl=300)  # Cache de 5 minutos para otimizar o desempenho
def consultar_dados(tabela, limite):
    query = f"SELECT * FROM {tabela} LIMIT {limite}"
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

# Executar consulta e exibir resultados
if tabela:
    try:
        dados = consultar_dados(tabela, limite)
        st.write(f"Exibindo os primeiros {limite} registros da tabela `{tabela}`:")
        st.dataframe(dados)  # Mostrar os dados como uma tabela interativa

        # Gráfico (se houver dados numéricos)
        st.write("Gráfico dos Dados:")
        if not dados.empty:
            st.line_chart(dados.select_dtypes(include=['number']))
    except Exception as e:
        st.error(f"Erro ao consultar a tabela: {e}")
