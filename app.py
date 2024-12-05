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
menu = st.sidebar.radio("Menu", ["Home", "Kanban"])
cor_selecionada = st.sidebar.color_picker("Escolha uma cor", "#00f900")
numero = st.sidebar.slider("Escolha um número", 0, 100, 50)

# Página Kanban
if menu == "Kanban":
    st.header("Kanban Board")
    # Configuração inicial do Kanban
    if "tasks" not in st.session_state:
        tasks = {"To Do": [], "In Progress": [], "Done": []}
    else:
        tasks = st.session_state["tasks"]
    
    # Carregar tarefas de um arquivo de texto
    try:
        with open("kanban_data.txt", "r") as file:
            tasks = eval(file.read())
    except FileNotFoundError:
        pass

    # Mostrar colunas do Kanban com botões para mover tarefas
    cols = st.columns(3)
    for i, (col_name, task_list) in enumerate(tasks.items()):
        with cols[i]:
            st.subheader(col_name)
            for idx, task in enumerate(task_list):
                st.text(task)
                if col_name != "Done":
                    next_col = "In Progress" if col_name == "To Do" else "Done"
                    if st.button(f"Mover para {next_col}", key=f"{task}-{next_col}-{idx}"):
                        tasks[next_col].append(task)
                        tasks[col_name].remove(task)
                        st.session_state["tasks"] = tasks
                        with open("kanban_data.txt", "w") as file:
                            file.write(str(tasks))
                        st.experimental_rerun()

    # Adicionar nova tarefa
    new_task = st.text_input("Nova Tarefa")
    if st.button("Adicionar Tarefa"):
        tasks["To Do"].append(new_task)
        with open("kanban_data.txt", "w") as file:
            file.write(str(tasks))
        st.session_state["tasks"] = tasks

# Página Home
elif menu == "Home":
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
