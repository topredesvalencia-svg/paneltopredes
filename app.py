"""Panel de aplicaciones Top Redes Valencia / SOSMADERA S.L."""
import os

import streamlit as st

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, "assets", "logo.png")

st.set_page_config(page_title="Panel Top Redes", page_icon=LOGO, layout="centered")

# ---------------------------------------------------------------- aplicaciones
# Edita aquí títulos, descripciones o URLs si cambian.
APPS = [
    {
        "titulo": "Facturación SOS Madera",
        "descripcion": "Generar facturas en PDF y Word con numeración correlativa.",
        "url": "https://facturacionsosmadera.streamlit.app/",
        "icono": "🧾",
    },
    {
        "titulo": "Presupuestos Top Redes",
        "descripcion": "Crear presupuestos para clientes.",
        "url": "https://presupuestostopredes.streamlit.app/",
        "icono": "📝",
    },
    {
        "titulo": "Calcular precios instalaciones",
        "descripcion": "Estimar el precio de una instalación de red.",
        "url": "https://calcularpreciosinstalaciones.streamlit.app/",
        "icono": "🧮",
    },
    {
        "titulo": "Fichajes Top Redes",
        "descripcion": "Registro de jornada y fichajes del equipo.",
        "url": "https://fichajes-topredes.streamlit.app/",
        "icono": "⏱️",
    },
]

ALTURA_TARJETA = 200  # píxeles; todas las tarjetas tienen el mismo tamaño

# ---------------------------------------------------------------- estilos
st.markdown(
    """
    <style>
      /* Botones en magenta corporativo (sobrescribe el rojo por defecto) */
      a[data-testid="stLinkButton"],
      a[data-testid^="stBaseButton"],
      [data-testid="stLinkButton"] a {
        background-color: #E01B7D !important;
        border-color: #E01B7D !important;
        color: #FFFFFF !important;
      }
      a[data-testid="stLinkButton"]:hover,
      a[data-testid^="stBaseButton"]:hover,
      [data-testid="stLinkButton"] a:hover {
        background-color: #C2146A !important;
        border-color: #C2146A !important;
        color: #FFFFFF !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- cabecera
col_logo, col_titulo = st.columns([1, 4], vertical_alignment="center")
with col_logo:
    st.image(LOGO, width=90)
with col_titulo:
    st.markdown(
        "<h1 style='color:#E01B7D;margin:0;font-size:3.4rem;line-height:1.1'>Top Redes Valencia</h1>"
        "<p style='color:#666;margin:4px 0 0 0;font-size:1.1rem'>Panel de aplicaciones internas</p>",
        unsafe_allow_html=True,
    )
st.write("")

# ---------------------------------------------------------------- tarjetas
cols = st.columns(2)
for i, app in enumerate(APPS):
    with cols[i % 2]:
        with st.container(border=True, height=ALTURA_TARJETA):
            st.markdown(f"##### {app['icono']} {app['titulo']}")
            st.caption(app["descripcion"])
            st.link_button("Abrir", app["url"], use_container_width=True, type="primary")
        st.write("")

st.caption("Las aplicaciones se abren en una pestaña nueva.")
