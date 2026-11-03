import streamlit as st
from dados_api import previsao_temperatura

#cidades
cidades = {
    "Vancouver" : [49.2691325141534, -123.16407567990191],
    "Tóquio" : [36.067984438291184, 139.13716088751534],
    "Nova Jersey" : [40.32998425519705, -76.21931766337097],
    "Bahia" : [-10.742652131828912, -42.203347565188],
    
}

#-----SIDEBAR-----
st.sidebar.title("Previsão do Tempo")
st.sidebar.image("logo.png")

cidade = st.sidebar.selectbox("Escolha a Cidade:", cidades.keys())
latitude , longitude = cidades[cidade]

#-----BODY-----
st.title(f'Previsão do tempo em {cidade} para os próximos 7 dias')

st.markdown("---")

# -----Previsão de Temperatura-----
dados, temperatura_media = previsao_temperatura(latitude, longitude)

for i, d in temperatura_media.iterrows():

    with st.container(border=True):
        st.subheader(d['dia_semana'])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Data",f'{int(d['dia'])}/{int(d['mes'])}')

            with col2:
                st.metric("Temperatura média", f"{d['temperatura_media']:.2f}º")

                with col3:
                    if d ['temperatura_media'] < 10:
                        temp = "cold.png"

                    elif d['temperatura_media'] < 18:
                        temp = "cool.png"

                    elif d['temperatura_media'] < 25:
                        temp = "comfort.png"

                    else:
                        temp = "warm.png"

                        st.image(temp, widht=40)