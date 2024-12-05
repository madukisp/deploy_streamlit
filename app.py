import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Demonstração Streamlit",
    page_icon="✨",
    layout="wide"
)

# Título principal
st.title("🎨 Demonstração das Funcionalidades do Streamlit")

# Sidebar
st.sidebar.header("Configurações")
cor_selecionada = st.sidebar.color_picker("Escolha uma cor", "#00f900")
numero = st.sidebar.slider("Escolha um número", 0, 100, 50)

# Layout em colunas
col1, col2 = st.columns(2)

with col1:
    st.header("Entrada de Dados")
    
    # Demonstração de diferentes inputs
    nome = st.text_input("Digite seu nome")
    idade = st.number_input("Digite sua idade", min_value=0, max_value=150, value=25)
    data = st.date_input("Selecione uma data")
    opcao = st.selectbox("Escolha uma opção", ["Opção 1", "Opção 2", "Opção 3"])
    
    if st.button("Clique aqui!"):
        st.success(f"Olá {nome}! Você tem {idade} anos.")

with col2:
    st.header("Visualização de Dados")
    
    # Criando dados de exemplo
    dados = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'tamanho': np.random.randint(1, 10, 100)
    })
    
    # Gráfico interativo com Plotly
    fig = px.scatter(dados, x='x', y='y', size='tamanho',
                    color_discrete_sequence=[cor_selecionada])
    st.plotly_chart(fig)

# Demonstração de métricas
st.header("Métricas")
col3, col4, col5 = st.columns(3)
with col3:
    st.metric(label="Temperatura", value="24 °C", delta="1.2 °C")
with col4:
    st.metric(label="Humidade", value="82%", delta="-5%")
with col5:
    st.metric(label="Valor", value=f"R$ {numero}", delta=f"{numero/2:.2f}")

# Demonstração de elementos de markdown e código
st.header("Markdown e Código")
st.markdown("""
### Exemplo de Markdown
- Você pode usar **negrito**
- Também pode usar *itálico*
- E criar listas como esta
""")

codigo = '''
def hello_world():
    print("Hello, Streamlit!")
'''
st.code(codigo, language='python')

# Demonstração de arquivo upload
st.header("Upload de Arquivo")
arquivo = st.file_uploader("Escolha um arquivo", type=['csv', 'txt'])
if arquivo is not None:
    st.write("Arquivo carregado com sucesso!")
    
# Demonstração de progresso
st.header("Barra de Progresso")
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)

# Footer
st.markdown("---")
st.markdown("### Criado com ❤️ usando Streamlit")
