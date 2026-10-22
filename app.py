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
        "titulo": "Generador de Facturas Top Redes",
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
        "titulo": "Calculador",
        "descripcion": "Estimar el precio de una instalación de red.",
        "url": "https://calcularpreciosinstalaciones.streamlit.app/",
        "icono": "🧮",
    },
    {
        "titulo": "Fichador Top Redes",
        "descripcion": "Registro de jornada y fichajes del equipo.",
        "url": "https://fichajes-topredes.streamlit.app/",
        "icono": "⏱️",
    },
]

ALTURA_TARJETA = 200   # px: altura total de cada tarjeta
ALTURA_TEXTO = 110     # px: zona de título + descripción (igual en todas)

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
      /* Títulos del panel centrados */
      .cabecera { text-align:center; }
      .cabecera h1 { color:#E01B7D; font-size:3.4rem; line-height:1.1; margin:8px 0 0 0; }
      .cabecera p  { color:#666; font-size:1.1rem; margin:6px 0 0 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- cabecera (centrada)
_, col_logo, _ = st.columns([2, 1, 2])
with col_logo:
    st.image(LOGO, width=110)
st.markdown(
    "<div class='cabecera'><h1>Top Redes Valencia</h1>"
    "<p>Panel de aplicaciones internas</p></div>",
    unsafe_allow_html=True,
)
st.write("")

# ---------------------------------------------------------------- tarjetas
cols = st.columns(2)
for i, app in enumerate(APPS):
    with cols[i % 2]:
        with st.container(border=True, height=ALTURA_TARJETA):
            # Bloque de texto con altura fija y centrado vertical + horizontal
            st.markdown(
                f"<div style='height:{ALTURA_TEXTO}px;display:flex;flex-direction:column;"
                f"justify-content:center;align-items:center;text-align:center;'>"
                f"<div style='font-weight:600;font-size:1.05rem;color:#262730;'>"
                f"{app['icono']} {app['titulo']}</div>"
                f"<div style='color:#777;font-size:0.9rem;margin-top:6px;'>"
                f"{app['descripcion']}</div></div>",
                unsafe_allow_html=True,
            )
            # El botón va siempre debajo, a la misma altura en todas las tarjetas
            st.link_button("Abrir", app["url"], use_container_width=True, type="primary")
        st.write("")

st.caption("Las aplicaciones se abren en una pestaña nueva.")
