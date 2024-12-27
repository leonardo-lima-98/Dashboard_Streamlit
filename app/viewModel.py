# import streamlit as st
# st.set_page_config(layout="wide")

# # Estilo CSS para dividir a altura da tela
# st.markdown(
#     """
#     <style>
#     [data-testid="stElementContainer"], [data-testid="stMainBlockContainer"] {
#         margin: 25px; 
#         padding: 0; 
#     }
#     [data-testid="stHeader"] {
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 80px;
#         background-color: #123a57; 
#         # margin: 0; 
#     }
#     .content {
#         height: 80px;  
#         overflow: hidden;
#         margin-top: 90px; /* Espaço para compensar a altura do cabeçalho fixo */
#     }
#     [data-testid="stAppViewContainer"] {
#         overflow: hidden; /* Remove o scroll do contêiner principal */
#     }
#     [data-testid="stSidebar"] {
#         overflow: hidden; /* Remove o scroll da barra lateral, se necessário */
#     }
#     .upper-container {
#         height: 40vh;
#         padding: 10px;
#         margin: -10px 0px 10px 0px;
#         border-radius: 5px;
#     }
#     .lower-container {
#         height: 35vh;
#         padding: 0px 0px 10px 0px;
#         margin: 5px;
#         border-radius: 5px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown('<div class="stElementContainer">', unsafe_allow_html=True)
# # Divisão vertical
# col1, col2 = st.columns([3, 2])

# with col1:
#     st.markdown(
#         """
#         <div class="upper-container" style="background-color: lightblue; padding: 10px; border-radius: 5px;">
#             <h3>Esquerda (60%)</h3>
#             <p>Conteúdo da esquerda.</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# with col2:
#     st.markdown(
#         """
#         <div class="upper-container" style="background-color: lightgreen; padding: 10px; border-radius: 5px;">
#             <h3>Esquerda (40%)</h3>
#             <p>Conteúdo da esquerda.</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# st.markdown(
#     """
#     <div class="lower-container" style="background-color: lightcoral; padding: 10px; border-radius: 5px;">
#         <h3>Parte inferior (100%)</h3>
#         <p>Conteúdo da parte inferior.</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# Estilo CSS para o layout
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
    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(data)

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
data = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['P', 'Q', 'R']
)
st.area_chart(data)
