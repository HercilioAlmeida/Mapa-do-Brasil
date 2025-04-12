import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mapa do Brasil")

tipo_mapa = st.sidebar.selectbox("Escolha o tipo de mapa:", ["Por Estados", "Por Municípios"])

if tipo_mapa == "Por Estados":
    st.markdown(f'<h1 style="text-align: center;">Mapa do Brasil {tipo_mapa}</h1>', unsafe_allow_html=True)
    
    path_shp = 'BR_UF_2023.shp'
    try:
        brasil_estados = gpd.read_file(path_shp)

        figmap, ax = plt.subplots(figsize=(8, 8))
        brasil_estados.plot(ax=ax, color="lightgrey", edgecolor='black', linewidth=0.5)

        ax.set_axis_off()
        figmap.patch.set_visible(False)
        st.pyplot(figmap)
    except Exception as e:
        st.error(f"Erro ao gerar o mapa de Estados: {e}")

if tipo_mapa == "Por Municípios":
    st.markdown(f'<h1 style="text-align: center;">Mapa do Brasil {tipo_mapa}</h1>', unsafe_allow_html=True)

    path_shp = 'BR_Municipios_2023.shp'
    try:
        brasil_municipios = gpd.read_file(path_shp)

        figmap, ax = plt.subplots(figsize=(8, 8))
        brasil_municipios.plot(ax=ax, color="lightgrey", edgecolor='black', linewidth=0.5)

        ax.set_axis_off()
        figmap.patch.set_visible(False)
        st.pyplot(figmap)
    except Exception as e:
        st.error(f"Erro ao gerar o mapa de Municípios: {e}")
