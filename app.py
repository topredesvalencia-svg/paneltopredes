"""Panel de aplicaciones Top Redes Valencia / SOSMADERA S.L."""
import streamlit as st

st.set_page_config(page_title="Panel Top Redes", page_icon="🐾", layout="centered")

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

# ---------------------------------------------------------------- estilos
st.markdown(
    """
    <style>
      .hero h1 {color:#E01B7D; margin-bottom:0;}
      .hero p  {color:#666; margin-top:4px;}
      .card {
        border:1px solid #f2c4dc; border-radius:14px; padding:18px 20px;
        background:#fff; box-shadow:0 2px 8px rgba(224,27,125,.08);
        height:100%;
      }
      .card h3 {margin:0 0 6px 0; font-size:1.1rem;}
      .card p  {color:#555; font-size:.92rem; margin:0 0 12px 0; min-height:2.6em;}
    </style>
    <div class="hero">
      <h1>🐾 Top Redes Valencia</h1>
      <p>Panel de aplicaciones internas</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- tarjetas
cols = st.columns(2)
for i, app in enumerate(APPS):
    with cols[i % 2]:
        st.markdown(
            f"<div class='card'><h3>{app['icono']} {app['titulo']}</h3>"
            f"<p>{app['descripcion']}</p></div>",
            unsafe_allow_html=True,
        )
        st.link_button("Abrir", app["url"], use_container_width=True, type="primary")
        st.write("")

st.caption("Las aplicaciones se abren en una pestaña nueva.")
