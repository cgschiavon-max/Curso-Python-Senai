import streamlit as st 
st.title("🎯Simualação de lançamento de Dardos")
'''Simulação de lançamentos de três dardos. O objetivo do 
aplicativo 
é mostrar o dardo com a maior distância'''

#Entrada de dados 
st.header("Inserir as três distâncias dos dardos lançados pelo jogador.")
coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input("Distância do Dardo 1 (em metros):", min_value=0.0, step=0.1)
with coluna2:
    dardo2 = st.number_input("Distância do Dardo 2 (em metros):", min_value=0.0, step=0.1)
with coluna3:
    dardo3 = st.number_input("Distância do Dardo 3 (em metros):", min_value=0.0, step=0.1)

#Estrutura de controle de decisão
if st.button("Calcular o Dardo Vencedor"):
    if (dardo1 > dardo2) and (dardo1 > dardo3):
        vencedor = "Dardo 1"
        distancia_vencedora = dardo1
    elif (dardo2 > dardo1) and (dardo2 > dardo3):
        vencedor = "Dardo 2"
        distancia_vencedora = dardo2
    elif (dardo3 > dardo1) and (dardo3 > dardo2):
        vencedor = "Dardo 3"
        distancia_vencedora = dardo3
    else:
        vencedor = None

    #Saída de dados
    if vencedor:
        st.success(f"O {vencedor} é o vencedor com uma distância de {distancia_vencedora} metros!")
    else:
        st.info("Houve um empate entre os dardos lançados.")