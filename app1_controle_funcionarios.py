import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


# layout='wide',
# TÍTULO DA PÁGINA
st.set_page_config(
    page_title='Lista Completa de Solicitações - BIAPÓ',
    page_icon="https://biapo.com.br/wp-content/uploads/2018/08/logo-open-graph.jpg",
    initial_sidebar_state='auto'
)

# CONECTAR À GSHEETS E PREPARAR PLANILHA
url = "https://docs.google.com/spreadsheets/d/1kB0oWRD6vOnNHzilJdofS6AF1u-hBTHYPP-ELi0GADo/edit?usp=sharing"
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url,worksheet="258115823") #,index_col=2)
df = df.drop(df.columns[[1,11,12,13,14,15]], axis=1)
df.set_index(df.columns[1], inplace=True)
df = df.dropna(subset=['SOLICITANTE'])
df = df.sort_values(by='ORDEM', ascending=False)

st.divider()


# CRIAR BOTÃO QUE ABRE O FORMULÁRIO
url2="https://docs.google.com/forms/d/e/1FAIpQLSfJBAV_3q-3EN1R0qmIMYXrJHydjG2l0YzeZGn03qw5BsxojQ/viewform"
st.link_button("Clique aqui para abrir um formulário de todas as solicitações", url2)

# CRIAR BOTÕES PARA PESQUISA DE SOLICITAÇÃO ESPECÍFICA 
colunas = list(df.columns)
unique_index_values = df.index.unique().tolist()
col4, col5, col6 = st.columns(3)
valor_filtro2=col4.selectbox('Selecione uma solicitação para consultar os dados detalhados', unique_index_values)
status_filtrar2 = col5.button('Ver detalhes')
status_limpar2 = col5.button('Limpar pesquisa')
#st.divider()

if status_filtrar2:
    texto1=valor_filtro2
    series= df.loc[texto1]
    df2=pd.DataFrame(series, index=colunas)
    st.dataframe(df2,height=500,width=800)

if status_limpar2:
    st.write("")

st.divider()

# CRIAR BOTÕES E MULTISELECT PARA EDITAR TABELA COM LISTA COMPLETA
col1, col2,col3 = st.columns(3)
col_filtro = col1.selectbox('Selecione a coluna', [c for c in colunas if c not in ['OBRA SOLICIT:']])
valor_filtro = col1.selectbox('Selecione o valor', list(df[col_filtro].unique()))

status_limpar = button('Ver tabela completa')
status_filtrar = col2.button('Filtrar tabela')
status_ocultar = col2.button('Ocultar tabela')
colunas_selecionadas = st.multiselect('Selecione as colunas:', colunas, ['TIPO', 'SOLICITANTE', 'SOLICITADO EM:', 'SITUACAO', 'ORDEM'])
st.divider()

if status_filtrar:
    st.markdown('# Lista Completa de Solicitações')
    st.dataframe(df.loc[df[col_filtro] == valor_filtro, colunas_selecionadas], height=800,width=800)
elif status_limpar:
    st.markdown('# Lista Completa de Solicitações')
    st.dataframe(df[colunas_selecionadas],height=800,width=800)
elif status_ocultar:
    st.write("")
    st.write("")
else:
    st.write("")
    st.write("")
    
