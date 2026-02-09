import streamlit as st

from pathlib import Path
import re

# =========================
# BENEFITS (standalone HTML)
# =========================
def cargar_benefits_standalone_html():
    """Carga benefits-standalone.html desde el repo (para incrustarlo en HOME).
    Si no existe, deja un placeholder visible para que no 'desaparezca' la sección.
    """
    candidatos = []
    try:
        candidatos.append(Path(__file__).resolve().parent / "benefits-standalone.html")
    except Exception:
        pass
    candidatos.append(Path("benefits-standalone.html"))
    candidatos.append(Path("SIVO/benefits-standalone.html"))

    for p in candidatos:
        try:
            if p.exists():
                raw = p.read_text(encoding="utf-8", errors="ignore")
                # Tomar contenido del <body> si existe
                m_body = re.search(r"<body[^>]*>(.*?)</body>", raw, flags=re.I | re.S)
                body = m_body.group(1) if m_body else raw

                # Mantener <style>, <script> y links (estén donde estén)
                styles = re.findall(r"<style[^>]*>.*?</style>", raw, flags=re.I | re.S)
                scripts = re.findall(r"<script[^>]*>.*?</script>", raw, flags=re.I | re.S)
                links = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', raw, flags=re.I)

                head = ""
                if styles:
                    head += "\n".join(styles) + "\n"
                if links:
                    head += "\n".join(links) + "\n"

                footer = ""
                if scripts:
                    footer = "\n" + "\n".join(scripts)

                return f"""\
{head}
{body}
{footer}
"""
        except Exception:
            continue

    # Fallback visible (para que no quede vacío si falta el archivo)
    return """\
<div style="background:#ffffff; padding:64px 20px;">
  <div style="max-width:1280px; margin:0 auto; text-align:center;">
    <h2 style="margin:0 0 10px 0; font-size:28px; font-weight:800; color:#111827;">
      Beneficios de tener un SIVO
    </h2>
    <p style="margin:0; color:#6b7280;">
      Falta el archivo <b>benefits-standalone.html</b> en el proyecto (no se pudo cargar).
    </p>
  </div>
</div>
"""

HTML_BENEFITS_STANDALONE = cargar_benefits_standalone_html()


# =========================
# INTEGRACIONES (standalone HTML)
# =========================
def cargar_integraciones_standalone_html():
    """Integraciones inline - no necesita archivo externo"""
    return """
<style>
.integraciones-wrap{max-width:1000px;margin:auto;padding:30px 20px;text-align:center;font-family:system-ui}
.integraciones-wrap h1{margin:0;font-size:34px;font-weight:700}
.integraciones-carousel{margin-top:26px;overflow:hidden}
.integraciones-track{display:flex;gap:16px;width:max-content;animation:integraciones-scroll 14s linear infinite}
.integraciones-card{min-width:130px;flex-shrink:0;background:#fff;padding:18px 14px;border-radius:14px;box-shadow:0 3px 10px rgba(0,0,0,.06);transition:.3s}
.integraciones-card:hover{transform:translateY(-5px)}
.integraciones-iconBox{width:44px;height:44px;margin:auto;margin-bottom:8px;border-radius:11px;display:flex;align-items:center;justify-content:center;background:radial-gradient(14px 14px at 30% 30%, rgba(37,99,235,.16), transparent 60%),radial-gradient(17px 17px at 70% 70%, rgba(249,115,22,.16), transparent 60%),white;box-shadow:0 3px 10px rgba(0,0,0,.06);font-size:20px}
.integraciones-label{font-weight:600;font-size:13px;margin-bottom:3px}
.integraciones-sub{font-size:11px;color:#667085}
@keyframes integraciones-scroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
</style>
<div class="integraciones-wrap">
<h1>Conecta con lo que ya usás</h1>
<div class="integraciones-carousel"><div class="integraciones-track">
<div class="integraciones-card"><div class="integraciones-iconBox">📷</div><div class="integraciones-label">Instagram</div><div class="integraciones-sub">DMs automatizados</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">🌐</div><div class="integraciones-label">Web</div><div class="integraciones-sub">Chat en tu sitio</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">🛍️</div><div class="integraciones-label">Shopify</div><div class="integraciones-sub">Catálogo + pedidos</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">💳</div><div class="integraciones-label">Mercado Pago</div><div class="integraciones-sub">Cobros y links</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">📧</div><div class="integraciones-label">Email</div><div class="integraciones-sub">Seguimiento automático</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">💬</div><div class="integraciones-label">WhatsApp</div><div class="integraciones-sub">Ventas + soporte</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">📷</div><div class="integraciones-label">Instagram</div><div class="integraciones-sub">DMs automatizados</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">🌐</div><div class="integraciones-label">Web</div><div class="integraciones-sub">Chat en tu sitio</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">🛍️</div><div class="integraciones-label">Shopify</div><div class="integraciones-sub">Catálogo + pedidos</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">💳</div><div class="integraciones-label">Mercado Pago</div><div class="integraciones-sub">Cobros y links</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">📧</div><div class="integraciones-label">Email</div><div class="integraciones-sub">Seguimiento automático</div></div>
<div class="integraciones-card"><div class="integraciones-iconBox">💬</div><div class="integraciones-label">WhatsApp</div><div class="integraciones-sub">Ventas + soporte</div></div>
</div></div>
</div>
"""

HTML_INTEGRACIONES_STANDALONE = cargar_integraciones_standalone_html()

# =========================
# CONFIGURACIÓN NORMAL APP
# =========================
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# =========================
# SESSION STATE - LOGIN
# =========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_email" not in st.session_state:
    st.session_state.user_email = ""


# =========================
# FULL WIDTH STREAMLIT
# =========================
st.markdown(
    """
    <style>
    /* Eliminar TODO el padding y margin de Streamlit */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    section[data-testid="stAppViewContainer"] {
        padding: 0 !important;
    }

    section.main > div {
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* Ocultar header, footer y toolbar */
    header[data-testid="stHeader"],
    .stAppHeader,
    footer,
    #MainMenu,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
    }

    /* Eliminar scroll horizontal */
    html, body, [data-testid="stAppViewContainer"], section.main {
        overflow-x: hidden !important;
        max-width: 100vw !important;
    }

    /* FORZAR FONDO BLANCO EN ABSOLUTAMENTE TODO STREAMLIT */
    html, body,
    .stApp,
    [data-testid="stApp"],
    [data-testid="stAppViewContainer"],
    [data-testid="stVerticalBlock"],
    [data-testid="stElementContainer"],
    [data-testid="element-container"],
    [data-testid="stHtml"],
    section.main,
    section.main > div,
    .main,
    .main .block-container,
    .block-container,
    .element-container,
    div[data-testid="stVerticalBlock"] > div,
    div[data-testid="stElementContainer"],
    .stMarkdown,
    div.stHtml {
        background-color: #ffffff !important;
        background: #ffffff !important;
    }

    /* El iframe debe ocupar exactamente el espacio */
    iframe {
        width: 100% !important;
        border: none !important;
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
    }


    /* Zoom 80% para sección de beneficios solo en PC */
    @media (min-width: 769px) {
        #benefits-section {
            zoom: 0.8;
            -moz-transform: scale(0.8);
            -moz-transform-origin: 0 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# VISTA
# =========================
try:
    vista = st.query_params.get("vista", "home")
except Exception:
    qp = st.experimental_get_query_params()
    vista = qp.get("vista", ["home"])[0]

BASE_URL = "https://gvelazcamp.github.io/SIVO/"

# =========================
# HTML COMPLETO
# =========================
HTML_BASE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    overflow-x: hidden;
    width: 100%;
    height: 100%;
    background: #ffffff !important;
}

body {
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    background: #ffffff !important;
    color: #111 !important;
    margin: 0;
    padding: 0;
    width: 100%;
    overflow-x: hidden;
    min-height: 100vh;
}

h1, h2, h3, h4, h5, h6 {
    color: #111;
}

.page-container {
    width: 100%;
    max-width: 100%;
    overflow-x: hidden;
    background: #ffffff !important;
}

/* =========================
   HEADER MEJORADO CON MENÚ HAMBURGUESA
========================= */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 5%;
    width: 100%;
    border-bottom: 1px solid #f0f0f0;
    position: relative;
}

.logo {
    display: flex;
    align-items: center;
    text-decoration: none;
    white-space: nowrap;
    gap: 12px;
}

.logo-img {
    height: 150px;
    width: auto;
}

.logo-text {
    font-size: 28px;
    font-weight: 800;
    color: #111;
}

.logo span { color: #60a5fa; }

.nav {
    display: flex;
    gap: 36px;
    font-weight: 500;
    font-size: 16px;
    color: #111;
    align-items: center;
}

.nav a {
    text-decoration: none;
    color: #111;
    cursor: pointer;
    white-space: nowrap;
    font-size: 16px;
    font-weight: 500;
    transition: color 0.2s;
}

.nav a:hover {
    color: #555;
}

.nav-buttons {
    display: flex;
    gap: 12px;
    align-items: center;
    margin-left: 20px;
}

.btn-login {
    background: transparent;
    color: #111;
    padding: 10px 24px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
    white-space: nowrap;
    border: 1.5px solid #d1d5db;
    text-decoration: none;
    transition: all 0.2s;
}

.btn-login:hover {
    border-color: #111;
    background: #f9f9f9;
}

.user-greeting {
    font-size: 14px;
    font-weight: 600;
    color: #3b82f6;
    white-space: nowrap;
}

.btn-demo {
    background: #111;
    color: #fff;
    padding: 10px 24px;
    border-radius: 999px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
    white-space: nowrap;
    border: 1.5px solid #111;
    text-decoration: none;
    transition: all 0.2s;
}

.btn-demo:hover {
    background: #333;
}

/* Checkbox oculto para menú hamburguesa CSS-only */
#menu-toggle {
    display: none;
}

/* Label como botón hamburguesa (oculto por defecto en desktop) */
.hamburger {
    display: none;
    flex-direction: column;
    justify-content: space-around;
    width: 30px;
    height: 25px;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 0;
    z-index: 1001;
}

.hamburger span {
    display: block;
    width: 30px;
    height: 3px;
    background: #111;
    border-radius: 10px;
    transition: all 0.3s;
    transform-origin: center;
}

/* Animación X cuando checkbox está checked */
#menu-toggle:checked ~ .hamburger span:nth-child(1) {
    transform: translateY(11px) rotate(45deg);
}

#menu-toggle:checked ~ .hamburger span:nth-child(2) {
    opacity: 0;
}

#menu-toggle:checked ~ .hamburger span:nth-child(3) {
    transform: translateY(-11px) rotate(-45deg);
}

/* Mostrar nav cuando checkbox está checked */
#menu-toggle:checked ~ .nav {
    transform: translateX(0) !important;
}

/* =========================
   RESPONSIVE MÓVIL - MENÚ HAMBURGUESA
========================= */
@media (max-width: 768px) {
    /* Header: logo a la izquierda, hamburguesa a la derecha */
    .header {
        padding: 12px 20px;
        flex-direction: row !important;
        justify-content: space-between !important;
        align-items: center !important;
        gap: 0 !important;
        text-align: left !important;
        position: relative;
        z-index: 1002;
    }

    /* Logo más grande en móvil */
    .logo {
        gap: 10px;
        flex-direction: row !important;
        align-items: center !important;
    }

    .logo-img {
        height: 70px !important;
        width: auto;
    }

    .logo-text {
        font-size: 26px !important;
        margin: 0 !important;
    }

    /* Mostrar hamburguesa a la DERECHA */
    .hamburger {
        display: flex !important;
        order: 2;
        margin-left: auto;
    }

    /* Header fijo para que quede visible con el menú abierto */
    .header {
        position: sticky !important;
        top: 0 !important;
        z-index: 1002 !important;
        background: white !important;
    }

    /* Menú fullscreen debajo del header */
    .nav {
        position: fixed !important;
        top: 95px !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        height: calc(100vh - 95px) !important;
        background: white !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: flex-start !important;
        padding: 30px 30px 40px 30px !important;
        gap: 0 !important;
        box-shadow: none !important;
        transform: translateX(100%) !important;
        transition: transform 0.3s ease !important;
        z-index: 1000 !important;
        overflow-y: auto !important;
    }

    .nav a {
        font-size: 28px !important;
        font-weight: 800 !important;
        color: #111 !important;
        width: 100% !important;
        padding: 24px 0 !important;
        border-bottom: 1px solid #eee !important;
        text-align: left !important;
        text-decoration: none !important;
        border-radius: 0 !important;
        letter-spacing: -0.5px !important;
    }

    .nav a:last-of-type {
        border-bottom: none !important;
    }

    .nav-buttons {
        margin-left: 0 !important;
        margin-top: 30px !important;
        width: auto !important;
        flex-direction: row !important;
        gap: 12px !important;
    }

    .nav .nav-buttons a.btn-login {
        background: #e8e8e8 !important;
        color: #333 !important;
        width: auto !important;
        text-align: center !important;
        padding: 14px 36px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        border-radius: 50px !important;
        border: none !important;
        border-bottom: none !important;
        display: inline-block !important;
        letter-spacing: 0 !important;
    }
}


/* =========================
   HERO IMPACT
========================= */
.hero-impact {
    background: linear-gradient(135deg, #1a6fb5 0%, #0d4a7a 50%, #1a3a5c 100%);
    padding: 80px 20px;
    text-align: center;
    color: #ffffff;
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 60vh;
    border-radius: 40px;
    margin: 20px;
    box-shadow: 0 25px 80px rgba(0,0,0,0.4);
}

.hero-impact-content {
    max-width: 900px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
    opacity: 0;
    transform: translateY(60px) scale(0.9);
    animation: fadeInCard 1.2s ease-out forwards;
}

@keyframes fadeInCard {
    from {
        opacity: 0;
        transform: translateY(60px) scale(0.9);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.hero-impact-title {
    font-size: 48px;
    font-weight: 600;
    line-height: 1.3;
    margin: 0 0 30px 0;
    color: #ffffff;
    opacity: 0;
    animation: fadeInText 0.6s ease-out 1s forwards;
}

.hero-impact-subtitle {
    display: block;
    font-size: 52px;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 40px 0;
    line-height: 1.3;
    opacity: 0;
    animation: fadeInText 0.6s ease-out 1.4s forwards;
}

@keyframes fadeInText {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-impact-text {
    font-size: 22px;
    line-height: 1.8;
    color: #ffffff;
    margin: 0 0 50px 0;
    max-width: 750px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0;
    animation: fadeInText 0.6s ease-out 1.8s forwards;
}

.hero-impact-actions {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
    opacity: 0;
    animation: fadeInButton 0.6s ease-out 2.2s forwards;
}

@keyframes fadeInButton {
    from {
        opacity: 0;
        transform: translateY(30px) scale(0.85);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.hero-impact-btn-primary {
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    color: #ffffff;
    padding: 20px 50px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 20px;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    border: none;
    cursor: pointer;
}

.hero-impact-btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5);
}

.hero-impact-btn-secondary {
    background: transparent;
    color: #FFC107;
    padding: 20px 50px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 20px;
    text-decoration: none;
    display: inline-block;
    border: 2px solid #FFC107;
    transition: all 0.3s ease;
}

.hero-impact-btn-secondary:hover {
    background-color: rgba(255, 193, 7, 0.1);
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(255, 193, 7, 0.3);
}

/* Tablet */
@media (max-width: 1024px) {
    .hero-impact {
        padding: 60px 50px;
    }
    
    .hero-impact-title {
        font-size: 40px;
    }
    
    .hero-impact-subtitle {
        font-size: 44px;
    }
    
    .hero-impact-text {
        font-size: 20px;
    }
    
    .hero-impact-btn-primary,
    .hero-impact-btn-secondary {
        padding: 18px 45px;
        font-size: 19px;
    }
}

/* Mobile */
@media (max-width: 768px) {
    .hero-impact {
        padding: 40px 30px;
        min-height: 50vh;
    }
    
    .hero-impact-title {
        font-size: 28px;
        margin-bottom: 20px;
    }
    
    .hero-impact-subtitle {
        font-size: 32px;
        margin-bottom: 30px;
    }
    
    .hero-impact-text {
        font-size: 17px;
        margin-bottom: 40px;
    }
    
    .hero-impact-btn-primary,
    .hero-impact-btn-secondary {
        padding: 16px 40px;
        font-size: 18px;
    }
}

@media (max-width: 480px) {
    .hero-impact {
        padding: 30px 20px;
    }
    
    .hero-impact-title {
        font-size: 24px;
    }
    
    .hero-impact-subtitle {
        font-size: 28px;
    }
    
    .hero-impact-text {
        font-size: 16px;
    }
    
    .hero-impact-btn-primary,
    .hero-impact-btn-secondary {
        padding: 14px 35px;
        font-size: 17px;
    }
}

/* =========================
   HERO
========================= */
.hero {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 15px;
    padding: 10px 5%;
    align-items: center;
    width: 100%;
}

.hero-content {
    max-width: 600px;
}

.hero h1 {
    font-size: 38px;
    line-height: 1.15;
    margin: 0 0 18px 0;
    color: #111;
}

.hero p {
    font-size: 16px;
    color: #555;
    margin: 0 0 22px 0;
}

.hero-image {
    text-align: center;
}

.hero-image img {
    max-width: 100%;
    width: auto;
    height: auto;
    max-height: 400px;
}

.hero-actions {
    display: flex;
    align-items: center;
    gap: 18px;
    flex-wrap: wrap;
}

.btn-primary {
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    color: #ffffff;
    padding: 12px 22px;
    border-radius: 14px;
    font-weight: 700;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    transition: all 0.3s;
    border: none;
    white-space: nowrap;
}

.btn-primary:hover {
    box-shadow: 0 6px 25px rgba(59, 130, 246, 0.4);
    transform: translateY(-2px);
}

.btn-secondary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    color: #555;
    cursor: pointer;
    text-decoration: none;
    white-space: nowrap;
}

/* =========================
   NUEVO: HERO CHAT DEMO
   (solo agrega, no rompe)
========================= */
.hero-chat {
    background: #ffffff;
    border-radius: 24px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    overflow: hidden;
    border: 1px solid rgba(0,0,0,0.06);
}

.chat-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 16px;
    background: linear-gradient(180deg, #ffffff, #ffffff);
    border-bottom: 1px solid rgba(0,0,0,0.06);
}

.chat-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 900;
    font-size: 13px;
    color: #111;
}

.dot {
    width: 10px;
    height: 10px;
    border-radius: 999px;
    background: #f4b400;
    box-shadow: 0 0 0 4px rgba(244,180,0,0.18);
}

.chat-pill {
    font-size: 12px;
    font-weight: 800;
    color: #7a5a00;
    background: rgba(244,180,0,0.18);
    border: 1px solid rgba(244,180,0,0.45);
    padding: 6px 10px;
    border-radius: 999px;
    white-space: nowrap;
}

.chat-body {
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    min-height: 260px;
}

.bubble {
    max-width: 88%;
    padding: 10px 12px;
    border-radius: 14px;
    font-size: 13px;
    line-height: 1.35;
    box-shadow: 0 6px 16px rgba(0,0,0,0.05);
}

.bubble.user {
    align-self: flex-end;
    background: #111;
    color: #fff;
    border-bottom-right-radius: 6px;
}

.bubble.bot {
    align-self: flex-start;
    background: #ffffff;
    color: #222;
    border: 1px solid rgba(0,0,0,0.06);
    border-bottom-left-radius: 6px;
}

.chat-meta {
    margin-top: 4px;
    font-size: 11px;
    color: #888;
}

.chat-input {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 14px 16px;
    border-top: 1px solid rgba(0,0,0,0.06);
    background: #fff;
}

.fake-input {
    flex: 1;
    background: #ffffff;
    border: 1px solid rgba(0,0,0,0.06);
    padding: 10px 12px;
    border-radius: 14px;
    font-size: 13px;
    color: #777;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.send-btn {
    background: #f4b400;
    border: none;
    padding: 10px 14px;
    border-radius: 14px;
    font-weight: 900;
    cursor: pointer;
}

.send-btn:hover {
    background: #e5a500;
}

.trust-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 14px;
}

.trust-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #fff;
    padding: 10px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
}

/* =========================
   NUEVO: CÓMO FUNCIONA (3 pasos)
========================= */
.steps {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 18px;
    max-width: 1200px;
    margin: 0 auto;
}

.step {
    background: #fff;
    border-radius: 22px;
    padding: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    text-align: left;
}

.step-num {
    width: 34px;
    height: 34px;
    border-radius: 12px;
    background: rgba(244,180,0,0.20);
    border: 1px solid rgba(244,180,0,0.45);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 900;
    color: #7a5a00;
    margin-bottom: 12px;
}

.step h3 {
    font-size: 16px;
    margin-bottom: 8px;
}

.step p {
    font-size: 13px;
    color: #666;
    line-height: 1.45;
}

/* NUEVOS STEPS SIMPLES */
.steps-simple {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 30px;
    max-width: 1200px;
    margin: 5px auto;
    flex-wrap: wrap;
}

.step-simple {
    background: #fff;
    border-radius: 24px;
    padding: 20px 15px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    flex: 1;
    min-width: 250px;
    max-width: 300px;
}

.step-icon {
    font-size: 64px;
    margin-bottom: 20px;
}

.step-simple h3 {
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 12px;
    color: #000;
}

.step-simple p {
    font-size: 14px;
    color: #666;
    line-height: 1.6;
}

.step-arrow {
    font-size: 32px;
    color: #f4b400;
    font-weight: 800;
}

@media (max-width: 768px) {
    .step-arrow {
        display: none;
    }
    
    .steps-simple {
        flex-direction: column;
        gap: 20px;
    }
}

/* =========================
   SECTION
========================= */
.section {
    padding: 5px 5%;
    width: 100%;
}

.section h2 {
    text-align: center;
    font-size: 32px;
    margin: 0 0 10px 0;
}

.subtitle {
    text-align: center;
    font-size: 14px;
    color: #777;
    margin: 0 0 10px 0;
}

/* =========================
   CARDS
========================= */
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 22px;
    width: 100%;
    max-width: 1400px;
    margin: 0 auto;
}

.card {
    background: #fff;
    border-radius: 22px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.card img {
    width: 100%;
    max-width: 200px;
    height: 130px;
    object-fit: contain;
    margin: 0 auto;
    display: block;
}

.card h3 {
    margin: 16px 0 10px 0;
    font-size: 18px;
}

.card p {
    font-size: 13px;
    color: #666;
    margin: 0 0 14px 0;
    flex-grow: 1;
}

.card button {
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    color: #ffffff;
    border: none;
    padding: 12px 24px;
    border-radius: 12px;
    font-weight: 700;
    cursor: pointer;
    margin-top: auto;
    width: 100%;
    min-height: 44px;
    box-sizing: border-box;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    transition: all 0.3s;
}

.card button:hover {
    box-shadow: 0 6px 25px rgba(59, 130, 246, 0.4);
    transform: translateY(-2px);
}

/* =========================
   PRECIOS
========================= */
.pricing {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    max-width: 1200px;
    margin: 20px auto 0 auto;
    align-items: stretch;
}

.plan {
    background: #ffffff;
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.06);
    display: flex;
    flex-direction: column;
    height: 100%;
    position: relative;
}

.plan.pro {
    border: 2px solid rgba(244,180,0,0.9);
}

.badge {
    position: absolute;
    top: 16px;
    right: 16px;
    background: rgba(244,180,0,0.15);
    border: 1px solid rgba(244,180,0,0.6);
    color: #7a5a00;
    font-weight: 800;
    font-size: 12px;
    padding: 6px 12px;
    border-radius: 999px;
}

.plan-name {
    font-size: 18px;
    font-weight: 800;
}

.plan-desc {
    font-size: 13px;
    color: #777;
    margin-top: 6px;
    min-height: 34px;
}

.plan-price {
    margin-top: 16px;
    font-size: 34px;
    font-weight: 900;
    letter-spacing: -0.02em;
    min-height: 44px;
}

.plan-price span {
    font-size: 13px;
    font-weight: 700;
    color: #777;
    margin-left: 6px;
}

.plan-note {
    font-size: 13px;
    color: #777;
    margin-top: 6px;
    min-height: 18px;
}

.plan-list {
    list-style: none;
    padding: 0;
    margin: 18px 0 0 0;
    flex: 1;
}

.plan-list li {
    display: flex;
    gap: 10px;
    padding: 9px 0;
    font-size: 13px;
    color: #555;
    border-bottom: 1px solid #f2f2f2;
}

.plan-btn {
    margin-top: auto;
    width: 100%;
    text-align: center;
}

/* =========================
   TESTIMONIOS
========================= */
.testimonios {
    padding: 5px 5%;
    background: #fff;
}

.testimonios h2 {
    font-size: 36px;
    text-align: center;
    margin: 0 0 10px 0;
}

.testimonios-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
}

.testimonio-card {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    position: relative;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.testimonio-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.1);
}

.testimonio-quote {
    font-size: 16px;
    line-height: 1.6;
    color: #333;
    margin: 0 0 20px 0;
    font-style: italic;
}

.testimonio-author {
    display: flex;
    align-items: center;
    gap: 12px;
}

.testimonio-avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 800;
    color: #000;
    font-size: 18px;
}

.testimonio-info h4 {
    margin: 0 0 4px 0;
    font-size: 15px;
    font-weight: 700;
    color: #000;
}

.testimonio-info p {
    margin: 0;
    font-size: 13px;
    color: #666;
}

.testimonio-stat {
    display: inline-block;
    background: rgba(244, 180, 0, 0.1);
    color: #c29400;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    margin-top: 15px;
}

@media (max-width: 768px) {
    .testimonios-grid {
        grid-template-columns: 1fr;
    }
}

/* =========================
   CTA FINAL
========================= */
.cta {
    margin: 5px 5%;
    background: linear-gradient(180deg, #eef2f7, #ffffff);
    border-radius: 40px;
    padding: 20px;
    text-align: center;
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
}

.cta h2 {
    font-size: 32px;
    margin: 0 0 10px 0;
}

.cta p {
    font-size: 14px;
    color: #666;
    margin: 0 0 10px 0;
}

.cta-form {
    display: flex;
    gap: 12px;
    justify-content: center;
    align-items: center;
    max-width: 600px;
    margin: 0 auto 30px;
    flex-wrap: wrap;
}

.cta-form input {
    flex: 1;
    min-width: 200px;
    padding: 14px 18px;
    border-radius: 12px;
    border: 2px solid #e0e0e0;
    font-size: 15px;
    font-family: inherit;
}

.cta-form input:focus {
    outline: none;
    border-color: #3b82f6;
}

.cta-form button {
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    color: #ffffff;
    padding: 14px 28px;
    border-radius: 12px;
    font-weight: 800;
    border: none;
    cursor: pointer;
    font-size: 15px;
    white-space: nowrap;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    transition: all 0.3s;
}

.cta-form button:hover {
    box-shadow: 0 6px 25px rgba(59, 130, 246, 0.4);
    transform: translateY(-2px);
}

.cta button {
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    color: #ffffff;
    padding: 14px 28px;
    border-radius: 16px;
    font-weight: 800;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    transition: all 0.3s;
}

.cta button:hover {
    box-shadow: 0 6px 25px rgba(59, 130, 246, 0.4);
    transform: translateY(-2px);
}

/* =========================
   FEATURES
========================= */
.features {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 24px;
    flex-wrap: wrap;
}

.feature {
    display: flex;
    align-items: center;
    gap: 8px;
    background: #fff;
    padding: 10px 16px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
}

/* =========================
   FAQ
========================= */
.faq-section {
    padding: 5px 5%;
    background: #fff;
    max-width: 1200px;
    margin: 0 auto;
}

.faq-section h2 {
    text-align: center;
    font-size: 36px;
    margin-bottom: 10px;
}

.faq-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 25px;
}

.faq-item {
    background: #ffffff;
    padding: 25px;
    border-radius: 16px;
    border-left: 4px solid #f4b400;
}

.faq-question {
    font-size: 16px;
    font-weight: 700;
    color: #000;
    margin-bottom: 10px;
}

.faq-answer {
    font-size: 14px;
    color: #666;
    line-height: 1.6;
}

/* =========================
   SIVO SECTION (LIMPIA)
========================= */
.sivo-section {
    padding: 32px 5% 26px;
    margin-top: 0;
    margin-bottom: 0;
    background: white;
    text-align: center;
}

.sivo-badge-top {
    display: inline-block;
    background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
    color: white;
    padding: 16px 40px;
    border-radius: 30px;
    font-weight: 700;
    font-size: 18px;
    margin-bottom: 22px;
    box-shadow: 0 4px 15px rgba(255, 107, 53, 0.25);
}

.sivo-card-clean {
    max-width: 1000px;
    margin: 0 auto;
    background: #fafbfc;
    border-radius: 24px;
    padding: 30px;
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 30px;
    align-items: center;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.sivo-image-side {
    display: flex;
    justify-content: center;
}

.sivo-img {
    width: 100%;
    max-width: 280px;
    height: auto;
    border-radius: 16px;
}

.sivo-content-side {
    text-align: left;
}

.sivo-content-side h3 {
    font-size: 30px;
    font-weight: 800;
    color: #1e3a8a;
    margin: 0 0 20px 0;
}

.sivo-subtitle {
    font-size: 16px;
    color: #64748b;
    line-height: 1.75;
    margin: 0 0 34px 0;
}

.sivo-features-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin-bottom: 34px;
}

.sivo-feat {
    font-size: 15px;
    color: #475569;
    line-height: 1.7;
}

.sivo-actions {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
}

.sivo-btn-primary {
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    color: white;
    padding: 14px 28px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 16px;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}

.sivo-btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(59, 130, 246, 0.4);
}

.sivo-btn-secondary {
    background: white;
    color: #3b82f6;
    padding: 14px 28px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 16px;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    border: 2px solid #e0f2fe;
}

.sivo-btn-secondary:hover {
    border-color: #60a5fa;
    background: #f0f9ff;
}

@media (max-width: 968px) {
    .sivo-card-clean {
        grid-template-columns: 1fr;
        padding: 40px 30px;
        gap: 35px;
    }
    
    .sivo-content-side {
        text-align: center;
    }
    
    .sivo-content-side h3 {
        font-size: 26px;
    }
    
    .sivo-features-list {
        text-align: left;
    }
    
    .sivo-actions {
        justify-content: center;
    }
}

@media (max-width: 600px) {
    .sivo-section {
        padding: 20px 5% 5px;
}
    
    .sivo-card-clean {
        padding: 30px 20px;
    }
    
    .sivo-content-side h3 {
        font-size: 22px;
    }
    
    .sivo-subtitle {
        font-size: 15px;
    }
    
    .sivo-feat {
        font-size: 14px;
    }
    
    .sivo-actions {
        flex-direction: column;
        width: 100%;
    }
    
    .sivo-btn-primary,
    .sivo-btn-secondary {
        width: 100%;
        text-align: center;
    }
}

/* =========================
   INTEGRACIONES
========================= */

/* =========================
   INTEGRACIONES
========================= */
.integrations-section {
    padding: 0 5%;
    margin-top: -20px;
    background: linear-gradient(180deg, #ffffff, #fff);
    text-align: center;
}

.integrations-section h2 {
    font-size: 36px;
    margin-bottom: 5px;
}

.integrations-subtitle {
    font-size: 16px;
    color: #666;
    margin-bottom: 5px;
}

.integrations-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 30px;
    max-width: 900px;
    margin: 0 auto;
}

.integration-logo {
    background: #fff;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    transition: transform 0.3s ease;
}

.integration-logo:hover {
    transform: translateY(-5px);
}

.integration-logo p {
    margin-top: 10px;
    font-size: 14px;
    font-weight: 600;
    color: #333;
}

/* =========================
   FOOTER
========================= */
.footer {
    border-top: 1px solid #eee;
    padding: 20px 5%;
    font-size: 13px;
    color: #888;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: 20px;
}

/* =========================
   RESPONSIVE
========================= */
@media (max-width: 1100px) {
    .hero {
        grid-template-columns: 1fr;
        text-align: center;
    }

    .hero-content {
        max-width: 100%;
    }

    .hero-actions {
        justify-content: center;
    }

    .trust-row {
        justify-content: center;
    }

    .steps {
        grid-template-columns: 1fr;
    }

    .hero-chat {
        text-align: left;
    }
}

@media (max-width: 768px) {
    /* FORZAR FONDO GRIS EN MOBILE - TODO EXCEPTO HERO-IMPACT */
    html, body {
        background: #ffffff !important;
        background-color: #ffffff !important;
    }
    
    .page-container,
    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stApp"],
    .hero,
    .hero-content,
    .section,
    .steps,
    .step,
    .cards,
    .card,
    .features,
    .feature,
    .testimonios,
    .testimonios-grid,
    .trust-row,
    .trust-pill,
    .cat,
    .chat-body,
    main,
    section {
        background: #ffffff !important;
        background-color: #ffffff !important;
    }
    
    /* Colores heredados del desktop - sin overrides */
    
    .header {
        flex-direction: column;
        gap: 12px;
        padding: 16px 4%;
        background: #ffffff !important;
    }

    .nav {
        gap: 14px;
        font-size: 14px;
    }

    .nav-buttons {
        margin-left: 0;
    }

    .hero {
        padding: 20px 4%;
    }

    .hero h1 {
        font-size: 28px;
    }

    .section {
        padding: 5px 4%;
    }

    .section h2 {
        font-size: 26px;
    }

    .cards {
        grid-template-columns: 1fr;
    }

    .cta {
        margin: 30px 4% 20px;
        padding: 30px 20px;
    }

    /* FIX MOBILE: oscurecer texto de features (evita que quede blanco/tenue) */
    .features {
        opacity: 1 !important;
    }
    .feature {
        color: #111827 !important;
        opacity: 1 !important;
    }
    .feature strong {
        color: #111827 !important;
    }


    .footer {
        flex-direction: column;
        gap: 10px;
        text-align: center;
        padding: 20px 4%;
    }

    .pricing {
        grid-template-columns: 1fr;
    }
    
    /* REDUCIR ESPACIO ENTRE SIVO COCINA E INTEGRACIONES EN MÓVIL */
    .sivo-section {
        padding-bottom: 0 !important;
        margin-bottom: 0 !important;
    }
    
    .sivo-card-clean {
        margin-bottom: 0 !important;
        padding-bottom: 25px !important;
    }
    
    .integrations-section {
        margin-top: -250px !important;
        padding-top: 15px !important;
    }
    
    .integrations-section h2 {
        font-size: 28px !important;
        margin-bottom: 8px !important;
    }
    
    .integrations-subtitle {
        font-size: 14px !important;
        margin-bottom: 25px !important;
    }
    
    /* Ajustar grid de integraciones para móvil */
    .integrations-grid {
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 15px !important;
        padding: 0 !important;
    }
    
    .integration-logo {
        padding: 20px 10px !important;
    }
    
    .integration-logo span {
        font-size: 36px !important;
    }
    
    .integration-logo p {
        font-size: 12px !important;
        margin-top: 8px !important;
    }
}

/* =========================
   CHATBOT FLOTANTE
========================= */
#chatbot-button {
    position: fixed !important;
    bottom: 20px !important;
    right: 20px !important;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(244, 180, 0, 0.5);
    display: flex !important;
    align-items: center;
    justify-content: center;
    z-index: 999999 !important;
    transition: all 0.3s ease;
}

#chatbot-button:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 25px rgba(244, 180, 0, 0.6);
}

#chatbot-button svg {
    width: 30px !important;
    height: 30px !important;
    fill: white !important;
    display: block !important;
}

#chatbot-button svg path {
    fill: white !important;
}

#chatbot-container {
    position: fixed !important;
    bottom: 100px !important;
    right: 20px !important;
    width: 380px;
    height: 550px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    display: none;
    flex-direction: column;
    z-index: 999998 !important;
    overflow: hidden;
    animation: slideIn 0.3s ease;
}

#chatbot-container.open {
    display: flex !important;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.chat-header {
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    color: white;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.chat-header-info {
    display: flex;
    align-items: center;
    gap: 12px;
}

.chat-avatar {
    width: 40px;
    height: 150px;
    border-radius: 50%;
    background: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}

.chat-header-text h3 {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 2px;
}

.chat-header-text p {
    font-size: 12px;
    opacity: 0.9;
}

.close-button {
    background: none;
    border: none;
    color: white;
    font-size: 24px;
    cursor: pointer;
    padding: 0;
    width: 30px;
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: background 0.2s;
}

.close-button:hover {
    background: rgba(255,255,255,0.2);
}

.chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    background: #f8f9fa;
}

.message {
    margin-bottom: 16px;
    display: flex;
    gap: 10px;
}

.message.bot {
    flex-direction: row;
}

.message.user {
    flex-direction: row-reverse;
}

.message-avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
}

.message.bot .message-avatar {
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    color: white;
}

.message.user .message-avatar {
    background: #e9ecef;
}

.message-content {
    max-width: 70%;
    padding: 12px 16px;
    border-radius: 18px;
    font-size: 14px;
    line-height: 1.5;
}

.message.bot .message-content {
    background: white;
    color: #333;
    border-bottom-left-radius: 4px;
}

.message.user .message-content {
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    color: white;
    border-bottom-right-radius: 4px;
}

.typing-indicator {
    display: flex;
    gap: 4px;
    padding: 12px 16px;
    background: white;
    border-radius: 18px;
    border-bottom-left-radius: 4px;
    width: fit-content;
}

.typing-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #f4b400;
    animation: typing 1.4s infinite;
}

.typing-dot:nth-child(2) {
    animation-delay: 0.2s;
}

.typing-dot:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes typing {
    0%, 60%, 100% {
        transform: translateY(0);
    }
    30% {
        transform: translateY(-10px);
    }
}

.chat-input {
    padding: 20px;
    background: white;
    border-top: 1px solid #e9ecef;
    display: flex;
    gap: 10px;
}

.chat-input input {
    flex: 1;
    padding: 12px 16px;
    border: 1px solid #e9ecef;
    border-radius: 24px;
    font-size: 14px;
    outline: none;
    transition: border-color 0.2s;
}

.chat-input input:focus {
    border-color: #f4b400;
}

.send-button {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f4b400 0%, #ff6b00 100%);
    border: none;
    color: white;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
}

.send-button:hover {
    transform: scale(1.05);
}

.send-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.send-button svg {
    width: 20px;
    height: 20px;
    fill: white;
}

@media (max-width: 768px) {
    #chatbot-container {
        width: calc(100vw - 40px);
        height: calc(100vh - 140px);
        bottom: 90px;
    }
}

.chat-messages::-webkit-scrollbar {
    width: 6px;
}

.chat-messages::-webkit-scrollbar-track {
    background: #f1f1f1;
}

.chat-messages::-webkit-scrollbar-thumb {
    background: #f4b400;
    border-radius: 3px;
}

.chat-messages::-webkit-scrollbar-thumb:hover {
    background: #ff6b00;
}

/* =========================
   SCROLL REVEAL - APARECEN AL SCROLLEAR
========================= */
.reveal {
    opacity: 0;
    transform: translateY(40px);
    transition: opacity 0.7s ease-out, transform 0.7s ease-out;
}
.reveal.reveal-visible {
    opacity: 1 !important;
    transform: translateY(0) !important;
}
.reveal-left {
    opacity: 0;
    transform: translateX(-60px);
    transition: opacity 0.7s ease-out, transform 0.7s ease-out;
}
.reveal-left.reveal-visible {
    opacity: 1 !important;
    transform: translateX(0) !important;
}
.reveal-right {
    opacity: 0;
    transform: translateX(60px);
    transition: opacity 0.7s ease-out, transform 0.7s ease-out;
}
.reveal-right.reveal-visible {
    opacity: 1 !important;
    transform: translateX(0) !important;
}

/* Delays escalonados para hijos dentro de reveal-children */
.reveal-children.reveal-visible > * { opacity: 1 !important; transform: none !important; }
.reveal-children > * {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.5s ease-out, transform 0.5s ease-out;
}
.reveal-children > *:nth-child(1) { transition-delay: 0s; }
.reveal-children > *:nth-child(2) { transition-delay: 0.12s; }
.reveal-children > *:nth-child(3) { transition-delay: 0.24s; }
.reveal-children > *:nth-child(4) { transition-delay: 0.36s; }
.reveal-children > *:nth-child(5) { transition-delay: 0.48s; }
.reveal-children > *:nth-child(6) { transition-delay: 0.6s; }
</style>
</head>
<body>
<div class="page-container">
"""

def get_header():
    if st.session_state.logged_in:
        user_name = st.session_state.user_name or "Usuario"
        nav_buttons = f'''
            <div class="nav-buttons" style="display:flex;align-items:center;gap:14px;">
                <span class="user-greeting">Hola, {user_name}</span>
                <a href="?vista=logout" class="btn-login" style="font-size:13px;padding:8px 18px;">Cerrar sesión</a>
            </div>'''
    else:
        nav_buttons = '''
            <div class="nav-buttons">
                <a href="?vista=login" class="btn-login">Login</a>
            </div>'''
    return f"""
    <div class="header">
        <a class="logo" href="?vista=home">
            <img src="https://gvelazcamp.github.io/SIVO/LogoSivo.svg" alt="SIVO" class="logo-img">
        </a>

        <input type="checkbox" id="menu-toggle">
        <label class="hamburger" for="menu-toggle" aria-label="Menu">
            <span></span>
            <span></span>
            <span></span>
        </label>

        <div class="nav" id="nav">
            <a href="?vista=home">Inicio</a>
            <a href="?vista=asistentes">Asistentes</a>
            <a href="?vista=precios">Precios</a>
            <a href="?vista=quehace">¿Qué hace SIVO?</a>
            {nav_buttons}
        </div>
    </div>
"""

HEADER = get_header()

# FOOTER SIN CIERRE (para st.html) - el body/html se cierra en FOOTER_CHATBOT
FOOTER = """
    <div class="footer" style="display: none;">
    </div>
</div>
</body>
</html>
"""

# FOOTER + CHATBOT JUNTOS (para components.html)
FOOTER_SIMPLE = """
<!DOCTYPE html>
<html>
<head>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body {
    background: #1a1a2e;
    font-family: Inter, -apple-system, BlinkMacSystemFont, sans-serif;
    margin: 0;
    padding: 0;
    color: white;
    width: 100%;
    height: 100%;
    overflow: hidden;
}
.footer-container {
    background: #1a1a2e;
    width: 100%;
    height: 100%;
    padding: 50px 20px 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
}
.footer-logo {
    height: 100px;
    width: auto;
    opacity: 0.9;
}
.footer-copyright {
    font-size: 14px;
    color: rgba(255, 255, 255, 0.5);
    letter-spacing: 0.3px;
}
</style>
</head>
<body>
<div class="footer-container">
    <img src="https://gvelazcamp.github.io/SIVO/LogoSivoDark.svg" alt="SIVO" class="footer-logo">
    <p class="footer-copyright">&copy; 2026 SIVO. Todos los derechos reservados.</p>
</div>
<script>
(function(){
    try {
        var iframe = window.frameElement;
        if (!iframe) return;
        var el = iframe;
        var dark = '#1a1a2e';
        // Subir por todos los contenedores padre y aplicar estilos
        while (el && el.parentElement) {
            el = el.parentElement;
            el.style.setProperty('background', dark, 'important');
            el.style.setProperty('background-color', dark, 'important');
            el.style.setProperty('max-width', '100vw', 'important');
            el.style.setProperty('width', '100vw', 'important');
            el.style.setProperty('margin-left', 'calc(-50vw + 50%)', 'important');
            el.style.setProperty('padding', '0', 'important');
            el.style.setProperty('margin-bottom', '0', 'important');
            el.style.setProperty('padding-bottom', '0', 'important');
            el.style.setProperty('gap', '0', 'important');
            // Parar en el main block-container
            if (el.classList && (el.classList.contains('block-container') || el.classList.contains('stApp'))) break;
        }
        // El iframe mismo
        iframe.style.setProperty('background', dark, 'important');
        iframe.style.setProperty('background-color', dark, 'important');
        iframe.style.setProperty('width', '100%', 'important');
    } catch(e) { console.log('Footer style error:', e); }
})();
</script>
</body>
</html>
"""

# =========================
# HOME (MODIFICADO: chatbot protagonista)
# =========================
HTML_HOME_PARTE_1 = """""" + HTML_BASE + """
<style>
/* ===========================
   TARJETA SIVO - TODO INLINE, FONDO BLANCO PURO
=========================== */
html, body, .page-container {
    background: #ffffff !important;
    background-color: #ffffff !important;
}

.sivo-card-wrapper {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    min-height: 100vh;
    padding: 20px;
    background: #ffffff !important;
    background-color: #ffffff !important;
    overflow: hidden !important;
    margin: 0 !important;
}

.sivo-card {
    background: linear-gradient(135deg, #1a6fb5 0%, #0d4a7a 50%, #1a3a5c 100%);
    border-radius: 40px;
    padding: 100px 80px;
    text-align: center;
    color: #ffffff;
    max-width: 1400px;
    width: 95%;
    min-height: 85vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);

    /* ANIMACIÓN: ENTRA DESDE LA IZQUIERDA */
    opacity: 0;
    transform: translateX(-100%) scale(0.95);
    animation: slideFromLeft 1s ease-out forwards;
}

@keyframes slideFromLeft {
    0% {
        opacity: 0;
        transform: translateX(-100%) scale(0.95);
    }
    100% {
        opacity: 1;
        transform: translateX(0) scale(1);
    }
}

.sivo-card h1 {
    font-size: 64px;
    margin-bottom: 40px;
    font-weight: 600;
    color: #ffffff;
    opacity: 0;
    animation: slideTextFromLeft 0.6s ease-out 0.5s forwards;
}

.sivo-card .highlight {
    color: #ffffff;
    font-size: 72px;
    display: block;
    margin-bottom: 50px;
    font-weight: 700;
    line-height: 1.3;
    opacity: 0;
    animation: slideTextFromLeft 0.6s ease-out 0.8s forwards;
}

.sivo-card p {
    font-size: 28px;
    line-height: 1.8;
    color: #ffffff;
    margin-bottom: 60px;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
    opacity: 0;
    animation: slideTextFromLeft 0.6s ease-out 1.1s forwards;
}

.sivo-card .button {
    display: inline-block;
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    color: #ffffff;
    padding: 24px 60px;
    border-radius: 50px;
    text-decoration: none;
    font-size: 22px;
    font-weight: 600;
    transition: all 0.3s;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    opacity: 0;
    animation: slideTextFromLeft 0.6s ease-out 1.4s forwards;
}

@keyframes slideTextFromLeft {
    0% {
        opacity: 0;
        transform: translateX(-40px);
    }
    100% {
        opacity: 1;
        transform: translateX(0);
    }
}

.sivo-card .button:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 25px rgba(59, 130, 246, 0.4);
}

/* Tablet */
@media (max-width: 1024px) {
    .sivo-card {
        padding: 80px 60px;
        max-width: 95%;
        min-height: 80vh;
        border-radius: 35px;
    }
    .sivo-card h1 { font-size: 52px; }
    .sivo-card .highlight { font-size: 60px; }
    .sivo-card p { font-size: 24px; }
    .sivo-card .button { padding: 22px 55px; font-size: 21px; }
}

/* Mobile */
@media (max-width: 768px) {
    .sivo-card-wrapper {
        padding: 10px !important;
        background: #ffffff !important;
    }
    .sivo-card {
        padding: 50px 35px;
        border-radius: 30px;
        min-height: 75vh;
        width: 92%;
        box-shadow: none !important;
    }
    .sivo-card h1 { font-size: 36px; margin-bottom: 25px; }
    .sivo-card .highlight { font-size: 42px; margin-bottom: 35px; }
    .sivo-card p { font-size: 19px; margin-bottom: 45px; }
    .sivo-card .button { padding: 18px 45px; font-size: 19px; }
}

@media (max-width: 480px) {
    .sivo-card-wrapper {
        padding: 5px !important;
        background: #ffffff !important;
    }
    .sivo-card {
        padding: 30px 20px;
        border-radius: 25px;
        box-shadow: none !important;
    }
    .sivo-card h1 { font-size: 24px; }
    .sivo-card .highlight { font-size: 28px; }
    .sivo-card p { font-size: 16px; }
    .sivo-card .button { padding: 14px 35px; font-size: 17px; }
}
</style>
""" + HEADER + """
    <!-- HERO TARJETA SIVO -->
    <div class="sivo-card-wrapper">
        <div class="sivo-card">
            <h1>Pregúntale a tus datos.</h1>
            <span class="highlight">No esperes por la información, SIVO la encuentra por vos.</span>
            <p>Responde al instante con la información de tu negocio, tanto para uso interno como para atención a clientes.</p>
            <a href="?vista=asistentes" class="button">Ver SIVO Digitales →</a>
        </div>
    </div>

    <div class="hero">
        <div class="hero-content">
            <h1>Tu negocio atendido<br>por un <span style="color:#1e40af;">Empleado Digital</span></h1>
            <p>
                SIVO es un empleado polifuncional con IA que se adapta a distintos rubros de industrias, desde ecommerce y finanzas hasta turnos médicos y viajes. Responde a tus clientes 24/7 con tus reglas y tus datos.
                Elegí uno de los tantos rubros donde SIVO se desempeña y lo dejamos funcionando.
            </p>

            <div class="trust-row" style="margin-top: 30px;">
                
                
                
            </div>
        </div>

        <!-- TARJETAS NUMÉRICAS SIVO -->
        <div class="sivo-stats-cards">
            <style>
                .sivo-stats-cards {
                    max-width: 500px;
                    margin: 0;
                }
                .sivo-stats-cards .stat-card {
                    background: #fff;
                    border: 1px solid #e6eaf2;
                    border-radius: 22px;
                    padding: 40px 30px;
                    margin-bottom: 22px;
                    text-align: center;
                    box-shadow: 0 8px 25px rgba(0,0,0,0.06);
                    transition: transform 0.3s, box-shadow 0.3s;
                }
                .sivo-stats-cards .stat-card:hover {
                    transform: translateY(-4px);
                    box-shadow: 0 12px 35px rgba(0,0,0,0.12);
                }
                .sivo-stats-cards .stat-number {
                    font-size: 64px;
                    font-weight: 800;
                    color: #2f7df6;
                    line-height: 1;
                }
                .sivo-stats-cards .stat-number-small {
                    font-size: 40px;
                    font-weight: 800;
                    color: #2f7df6;
                    letter-spacing: 1px;
                    line-height: 1;
                }
                .sivo-stats-cards .stat-label {
                    font-size: 22px;
                    margin-top: 12px;
                    font-weight: 600;
                    color: #0b1220;
                }
                .sivo-stats-cards .stat-desc {
                    opacity: 0.65;
                    margin-top: 10px;
                    font-size: 15px;
                    color: #4a5568;
                }
            </style>

            <div class="stat-card">
                <div class="stat-number" id="stat-num-1" data-target="100">0</div>
                <div class="stat-label">Conversaciones simultáneas</div>
                <div class="stat-desc">Atiende múltiples clientes al mismo tiempo</div>
            </div>

            <div class="stat-card">
                <div class="stat-number" id="stat-num-2" data-target="60">0</div>
                <div class="stat-label">Mensajes por minuto</div>
                <div class="stat-desc">Respuestas en tiempo real</div>
            </div>

            <div class="stat-card">
                <div class="stat-number-small" id="stat-alpha">A</div>
                <div class="stat-label">Fuentes de conocimiento</div>
                <div class="stat-desc">Entrenable con cualquier información del negocio</div>
            </div>
        </div>

        <!-- Contadores animados por scroll via components.html -->
    </div>

    

    <!-- ====== SECCIÓN CÓMO FUNCIONA CON TARJETAS ANIMADAS ====== -->
    <style>
        .como-funciona-container {
            max-width: 1100px;
            margin: 0 auto;
            padding: 60px 20px;
        }

        .como-funciona-header {
            text-align: center;
            color: #333;
            margin-bottom: 60px;
        }

        .como-funciona-header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        .como-funciona-header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        /* ====== FILA HORIZONTAL (PC) ====== */
        .cards-row {
            display: flex;
            gap: 30px;
            align-items: stretch;
        }

        .card {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            text-align: center;

            /* Animación INFINITA - Se repite constantemente */
            animation-duration: 4s;
            animation-iteration-count: infinite;
            animation-timing-function: ease-in-out;

            /* Para que queden TODAS iguales en altura */
            flex: 1 1 0;
            min-width: 260px;
            display: flex;
            flex-direction: column;
            min-height: 320px;
        }

        .card-icon {
            font-size: 80px;
            margin-bottom: 20px;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card h2 {
            font-size: 1.8rem;
            color: #333;
            margin-bottom: 15px;
            min-height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .card p {
            font-size: 1rem;
            color: #666;
            line-height: 1.6;
            flex-grow: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        /* ====== ANIMACIONES (Abajo / Arriba / Abajo) ====== */
        @keyframes slideInUp {
            0% {
                transform: translateY(30px);
                opacity: 0.3;
            }
            50% {
                transform: translateY(0);
                opacity: 1;
            }
            100% {
                transform: translateY(30px);
                opacity: 0.3;
            }
        }

        @keyframes slideInDown {
            0% {
                transform: translateY(-30px);
                opacity: 0.3;
            }
            50% {
                transform: translateY(0);
                opacity: 1;
            }
            100% {
                transform: translateY(-30px);
                opacity: 0.3;
            }
        }

        .slide-up { animation-name: slideInUp; }
        .slide-down { animation-name: slideInDown; }

        /* Delays ESCALONADOS para animación infinita */
        .cards-row .card:nth-child(1) { animation-delay: 0s; }
        .cards-row .card:nth-child(2) { animation-delay: 0.5s; }
        .cards-row .card:nth-child(3) { animation-delay: 1s; }

        /* ====== Responsive: si achica, apilar ====== */
        @media (max-width: 900px) {
            .como-funciona-container {
                max-width: 600px;
            }

            .cards-row {
                flex-direction: column;
            }

            .card {
                padding: 30px 20px;
                min-height: auto;
            }

            .card-icon {
                font-size: 60px;
                height: 60px;
            }

            .card h2 {
                font-size: 1.5rem;
                min-height: auto;
            }
        }
    </style>

    <div class="como-funciona-container">
        <div class="como-funciona-header">
            <h1>Cómo funciona</h1>
            <p>Simple y rápido. En 3 pasos tenés tu asistente funcionando.</p>
        </div>

        <div class="cards-row">
            <!-- Tarjeta 1: Abajo -> Arriba -->
            <div class="card slide-up">
                <div class="card-icon">🔌</div>
                <h2>Conectás</h2>
                <p>Vinculás tus datos, productos, servicios o información del negocio.</p>
            </div>

            <!-- Tarjeta 2: Arriba -> Abajo (entra desde arriba) -->
            <div class="card slide-down">
                <div class="card-icon">🧠</div>
                <h2>Entrenás</h2>
                <p>El asistente aprende tu negocio: precios, stock, políticas, horarios.</p>
            </div>

            <!-- Tarjeta 3: Abajo -> Arriba -->
            <div class="card slide-up">
                <div class="card-icon">🚀</div>
                <h2>Lanzás</h2>
                <p>Lo instalamos en tu web o WhatsApp y empieza a atender clientes.</p>
            </div>
        </div>
    </div>
    <!-- ====== FIN SECCIÓN CÓMO FUNCIONA ====== -->

    
<div id="benefits-section">
<!-- BENEFICIOS (cargado desde benefits-standalone.html) -->
__BENEFITS_STANDALONE__
</div>

<!-- Inline event handlers are used on cards for better compatibility -->

""" + FOOTER + """
"""


# Inyectar beneficios standalone en HOME (sin cambiar el resto)
try:
    HTML_HOME_PARTE_1 = HTML_HOME_PARTE_1.replace("__BENEFITS_STANDALONE__", HTML_BENEFITS_STANDALONE)
except Exception:
    pass

HTML_HOME_PARTE_2 = f"""    <!-- TESTIMONIOS -->
    <div class="testimonios">
        <h2>Lo que dicen nuestros clientes</h2>
        
        <div class="testimonios-grid">
            <div class="testimonio-card">
                <div class="testimonio-quote">
                    "Desde que instalé el chatbot, las consultas se responden automáticamente. Las ventas subieron un 40% y ya no pierdo clientes por demoras en responder."
                </div>
                <div class="testimonio-author">
                    <div class="testimonio-avatar">M</div>
                    <div class="testimonio-info">
                        <h4>Martín González</h4>
                        <p>Tienda de deportes online</p>
                    </div>
                </div>
                <div class="testimonio-stat">📈 +40% ventas</div>
            </div>

            <div class="testimonio-card">
                <div class="testimonio-quote">
                    "Antes pasaba 3 horas al día respondiendo las mismas preguntas. Ahora el bot responde al instante y yo me enfoco en atender consultas complejas. Un antes y después."
                </div>
                <div class="testimonio-author">
                    <div class="testimonio-avatar">L</div>
                    <div class="testimonio-info">
                        <h4>Laura Fernández</h4>
                        <p>Restaurante</p>
                    </div>
                </div>
                <div class="testimonio-stat">⏰ -3hs diarias</div>
            </div>

            <div class="testimonio-card">
                <div class="testimonio-quote">
                    "Implementamos el asistente de turnos y las reservas se duplicaron. Los clientes reservan a cualquier hora y el sistema confirma automáticamente. Impresionante."
                </div>
                <div class="testimonio-author">
                    <div class="testimonio-avatar">C</div>
                    <div class="testimonio-info">
                        <h4>Carlos Ruiz</h4>
                        <p>Clínica odontológica</p>
                    </div>
                </div>
                <div class="testimonio-stat">📅 2x reservas</div>
            </div>

            <div class="testimonio-card">
                <div class="testimonio-quote">
                    "Las consultas por propiedades llegan las 24hs. El bot responde características, precios y agenda visitas automáticamente. Ahora atendemos 3 veces más clientes con el mismo equipo."
                </div>
                <div class="testimonio-author">
                    <div class="testimonio-avatar">A</div>
                    <div class="testimonio-info">
                        <h4>Ana Rodríguez</h4>
                        <p>Inmobiliaria</p>
                    </div>
                </div>
                <div class="testimonio-stat">🏠 3x más consultas</div>
            </div>

            <div class="testimonio-card">
                <div class="testimonio-quote">
                    "Redujimos los llamados al gimnasio en un 70%. Ahora los socios consultan horarios, reservan clases y cancelan turnos directamente con el asistente. Increíble eficiencia."
                </div>
                <div class="testimonio-author">
                    <div class="testimonio-avatar">D</div>
                    <div class="testimonio-info">
                        <h4>Diego Martínez</h4>
                        <p>Gimnasio y centro deportivo</p>
                    </div>
                </div>
                <div class="testimonio-stat">📞 -70% llamados</div>
            </div>

            <div class="testimonio-card">
                <div class="testimonio-quote">
                    "El chatbot responde consultas de stock, precios y envíos las 24 horas. Los clientes están más satisfechos y nosotros cerramos ventas incluso de madrugada."
                </div>
                <div class="testimonio-author">
                    <div class="testimonio-avatar">S</div>
                    <div class="testimonio-info">
                        <h4>Sofía Méndez</h4>
                        <p>Ecommerce de tecnología</p>
                    </div>
                </div>
                <div class="testimonio-stat">🌙 Ventas 24/7</div>
            </div>
        </div>
    </div>

    <div class="cta" id="soporte">
        <h2>Agendá una demo gratuita</h2>
        <p>Probá 7 días gratis. Sin tarjeta de crédito. Cancelá cuando quieras.</p>
        
        <form class="cta-form" onsubmit="event.preventDefault(); alert('¡Gracias! Te contactamos en 24 hs.');">
            <input type="text" placeholder="Tu nombre" required>
            <input type="email" placeholder="Tu email" required>
            <button type="submit">Agendar demo</button>
        </form>

        <div class="features">
            <div class="feature">⚡ Fácil y rápido</div>
            <div class="feature">⚙️ Totalmente configurable</div>
            <div class="feature">🔒 Seguro y escalable</div>
            <div class="feature">💬 Soporte incluido</div>
        </div>
    </div>

    <!-- FAQ -->
    <div class="faq-section">
        <h2>Preguntas frecuentes</h2>

        <div class="faq-grid">
            <div class="faq-item">
                <div class="faq-question">¿Necesito saber programar?</div>
                <div class="faq-answer">No. Nosotros configuramos todo por vos. Vos solo nos pasás la información de tu negocio y nosotros lo dejamos funcionando.</div>
            </div>

            <div class="faq-item">
                <div class="faq-question">¿Funciona con WhatsApp?</div>
                <div class="faq-answer">Sí. Podés integrar el chatbot con WhatsApp, Instagram, tu sitio web, Shopify y más plataformas.</div>
            </div>

            <div class="faq-item">
                <div class="faq-question">¿Puedo cancelar cuando quiera?</div>
                <div class="faq-answer">Sí. No hay permanencia. Cancelás cuando quieras sin costos adicionales ni penalizaciones.</div>
            </div>

            <div class="faq-item">
                <div class="faq-question">¿Qué pasa si el bot no sabe responder?</div>
                <div class="faq-answer">El bot deriva la consulta a un humano o toma tus datos para que te contactemos. Nunca deja al cliente sin respuesta.</div>
            </div>

            <div class="faq-item">
                <div class="faq-question">¿Los datos están seguros?</div>
                <div class="faq-answer">Sí. Toda la información está encriptada y cumplimos con normativas de protección de datos. Tus datos y los de tus clientes están 100% seguros.</div>
            </div>

            <div class="faq-item">
                <div class="faq-question">¿Cuánto tarda la implementación?</div>
                <div class="faq-answer">Depende de la complejidad. Te damos un timeline al inicio.</div>
            </div>
        </div>
    </div>

    <!-- NOVEDAD SIVO -->
    <div class="sivo-section">
        <div class="sivo-badge-top">🔥 Recién Lanzado - Enero 2026</div>
        
        <div class="sivo-card-clean">
            <div class="sivo-image-side">
                <img src="https://gvelazcamp.github.io/SIVO/Asistentetelefonico.png" alt="SIVO SIVO Telefónico" class="sivo-img">
            </div>
            
            <div class="sivo-content-side">
                <h3>SIVO - Tu SIVO Telefónico IA</h3>
                <p class="sivo-subtitle">
                    Atiende llamadas automáticamente, agenda citas y responde consultas 
                    mientras vos te enfocás en hacer crecer tu negocio
                </p>
                
                <div class="sivo-features-list">
                    <div class="sivo-feat">✅ <strong>Atiende 24/7:</strong> Nunca más pierdas un cliente</div>
                    <div class="sivo-feat">✅ <strong>Agenda automática:</strong> Turnos en tu calendario</div>
                    <div class="sivo-feat">✅ <strong>Voz natural:</strong> Conversaciones profesionales</div>
                    <div class="sivo-feat">✅ <strong>Derivación inteligente:</strong> Transfiere cuando es necesario</div>
                    <div class="sivo-feat">✅ <strong>Respuestas instantáneas:</strong> Precios y disponibilidad</div>
                    <div class="sivo-feat">✅ <strong>Integración total:</strong> Se integra con tu sistema</div>
                </div>
                
                <div class="sivo-actions">
                    <a href="#soporte" class="sivo-btn-primary">Agendá tu demo</a>
                    <a href="?vista=asistentes" class="sivo-btn-secondary">Ver asistentes →</a>
                </div>
            </div>
        </div>
    </div>

    <!-- INTEGRACIONES -->
    <div class="integrations-section">
{HTML_INTEGRACIONES_STANDALONE}
</div>

{FOOTER}
"""

# =========================
# SLIDER SIVOs (HTML EMBEBIDO)
# =========================
SIVO_SLIDER_COMPONENT_HTML = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <style>
      body { margin:0; background: transparent; font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
      .sivo-slider-wrap{
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 8px 18px 8px;
      }
      .sivo-slider-title{
        text-align: center;
        font-size: 44px;
        font-weight: 800;
        margin: 0 0 10px 0;
        color: #0b1320;
      }
      .sivo-slider-subtitle{
        text-align: center;
        font-size: 15px;
        color: #64748b;
        margin: 0 0 22px 0;
      }
      .sivo-slider-frame{
        width: 100%;
        height: 560px; /* PC: reduce espacio */
        border: 0;
        border-radius: 18px;
        overflow: hidden;
        background: transparent;
        display: block;
        box-shadow: 0 20px 60px rgba(15, 23, 42, 0.12);
      }

      @media (max-width: 900px){
        .sivo-slider-wrap{ padding: 26px 14px 0px; } /* Eliminar padding-bottom */
        .sivo-slider-title{ font-size: 34px; }
        .sivo-slider-frame{ height: 560px; } /* mobile: un poco más alto */
      }
    </style>
  </head>
  <body>
    <div class="sivo-slider-wrap">
<iframe
        class="sivo-slider-frame"
        src="https://gvelazcamp.github.io/SIVO/slider_sivos_imagenes_reales.html"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        allow="fullscreen"
       scrolling="no"></iframe>
    </div>
  </body>
</html>
"""


# =========================
# SIVOS (SLIDER) - PC / MOBILE (2 HTMLs distintos)
# =========================
SIVO_SLIDER_COMPONENT_HTML_PC = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    body { margin:0; padding:0; font-family: Inter, system-ui, -apple-system, sans-serif; background:#ffffff; }
    .wrap { padding: 10px 0; background:#ffffff; }
    iframe { width:100%; height: 980px; border:0; display:block; background:#ffffff; }
  </style>
</head>
<body>
  <div class="wrap">
    <iframe
      src="https://gvelazcamp.github.io/SIVO/slider_sivos_imagenes_reales_pc.html"
      title="SIVOs - PC"
      loading="lazy"
    ></iframe>
  </div>
</body>
</html>
"""

SIVO_SLIDER_COMPONENT_HTML_MOBILE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    body { margin:0; padding:0; font-family: Inter, system-ui, -apple-system, sans-serif; background:#ffffff; }
    .wrap { padding: 6px 0; background:#ffffff; }
    iframe { width:100%; height: 560px; border:0; display:block; background:#ffffff; }
  </style>
</head>
<body>
  <div class="wrap">
    <iframe
      src="https://gvelazcamp.github.io/SIVO/slider_sivos_imagenes_reales_mobile.html"
      title="SIVOs - Mobile"
      loading="lazy"
      scrolling="no"
    ></iframe>
  </div>
</body>
</html>
"""

# =========================
# SIVO SLIDER RESPONSIVE (SOLUCIÓN MEJORADA)
# =========================
# Este slider se adapta automáticamente usando CSS Media Queries
# No necesita recarga de página ni parámetros URL
SIVO_SLIDER_COMPONENT_RESPONSIVE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { 
      margin:0; 
      padding:0; 
      font-family: Inter, system-ui, -apple-system, sans-serif; 
      background:#ffffff; 
      overflow-x: hidden;
    }
    
    /* Contenedor principal - SIN PADDING para que las secciones estén pegadas */
    .slider-container { 
      padding: 0; 
      background:#ffffff; 
      width: 100%;
      overflow: hidden;
    }
    
    /* IFRAME PC - visible por defecto */
    .slider-pc {
      width: 100%; 
      height: 760px; 
      border: 0; 
      display: block; 
      background: #ffffff;
    }
    
    /* IFRAME MOBILE - oculto por defecto */
    .slider-mobile {
      width: 100%; 
      height: 600px; 
      border: 0; 
      display: none; 
      background: #ffffff;
    }
    
    /* MEDIA QUERY: En móviles (<=900px), ocultar PC y mostrar MOBILE */
    @media (max-width: 900px) {
      .slider-container {
        padding: 0;
      }
      
      .slider-pc {
        display: none !important;
      }
      
      .slider-mobile {
        display: block !important;
      }
    }
  </style>
</head>
<body>
  <div class="slider-container">
    <!-- Slider PC - se muestra en pantallas grandes -->
    <iframe
      class="slider-pc"
      src="https://gvelazcamp.github.io/SIVO/slider_sivos_imagenes_reales_pc.html"
      title="SIVOs - PC"
      loading="lazy"
      scrolling="no"
    ></iframe>
    
    <!-- Slider MOBILE - se muestra en pantallas pequeñas -->
    <iframe
      class="slider-mobile"
      src="https://gvelazcamp.github.io/SIVO/slider_sivos_imagenes_reales_mobile.html"
      title="SIVOs - Mobile"
      loading="lazy"
      scrolling="no"
    ></iframe>
  </div>
  
  <script>
    // Ajustar altura dinámicamente según el iframe visible (para evitar huecos)
    function adjustHeight() {
      const isMobile = window.innerWidth <= 900;
      const el = document.querySelector(isMobile ? '.slider-mobile' : '.slider-pc');
      let h = 0;

      try {
        if (el) {
          h = el.getBoundingClientRect().height;
        }
      } catch (e) {}

      if (!h) {
        h = isMobile ? 600 : 760;
      }

      h = Math.ceil(h);

      // Notificar a Streamlit del cambio de altura
      try {
        window.parent.postMessage(
          { isStreamlitMessage: true, type: 'streamlit:setFrameHeight', height: h },
          '*'
        );
      } catch (e) {}
    }

    // Ajustar al cargar
    try { window.addEventListener('load', adjustHeight); } catch (e) {}
    adjustHeight();

    // Ajustar al cambiar tamaño de ventana
    let resizeTimer;
    window.addEventListener('resize', function() {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(adjustHeight, 120);
    });
  </script>
</body>
</html>
"""

# =========================
# ASISTENTES
# =========================
HTML_ASISTENTES = f"""{HTML_BASE}
{HEADER}

    <div class="section">
        <h2>Todos los asistentes IA</h2>
        <div class="subtitle">Estos son los asistentes disponibles en SIVO.</div>

        <div class="cards">

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistentecocina.png" alt="Cocina">
                <h3>SIVO Cocina</h3>
                <p>Recetas, consejos y conversiones.</p>
                <a href="https://demorestaurante.streamlit.app/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><button>Probar demo</button></a>
            </div>

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistenteecommerce.png" alt="Ecommerce">
                <h3>SIVO Ecommerce</h3>
                <p>Soporte para productos y pedidos.</p>
                <a href="https://demoecommerce.streamlit.app/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><button>Probar demo</button></a>
            </div>

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistentefinanzas.png" alt="Finanzas">
                <h3>SIVO Finanzas</h3>
                <p>Cotizaciones y análisis financiero.</p>
                <a href="?vista=demo&asistente=finanzas" style="text-decoration: none;"><button>Ver Asistente</button></a>
            </div>

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistentestock.png" alt="Stock">
                <h3>SIVO Stock</h3>
                <p>Control de inventario y alertas.</p>
                <a href="https://demostockuy.streamlit.app/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><button>Probar demo</button></a>
            </div>

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistenteinmobiliaria.png" alt="Inmobiliaria">
                <h3>SIVO Inmobiliaria</h3>
                <p>Consultas de propiedades y agendado.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistenteagendas.png" alt="Agenda">
                <h3>SIVO Turnos</h3>
                <p>Reserva de turnos y recordatorios.</p>
                <a href="https://demoturnos.streamlit.app/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><button>Probar demo</button></a>
            </div>

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistentedental.png" alt="Dental">
                <h3>SIVO Dental</h3>
                <p>Turnos y precios orientativos.</p>
                <button>Ver asistente</button>
            </div>


            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistentedetiendaderopa.png" alt="Tienda de Ropa">
                <h3>SIVO Tienda de Ropa</h3>
                <p>Consultas sobre productos, talles y envíos.</p>
                <a href="https://demoropa.streamlit.app/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><button>Probar demo</button></a>
            </div>

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistentedepeluqueria.png" alt="Peluquería">
                <h3>SIVO Peluquería</h3>
                <p>Turnos, servicios y precios de salón.</p>
                <a href="https://demopelu.streamlit.app/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><button>Probar demo</button></a>
            </div>

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistentedeviaje.png" alt="Viajes">
                <h3>SIVO Viajes</h3>
                <p>Paquetes turísticos, vuelos y hoteles.</p>
                <a href="https://demo-viajes.streamlit.app/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><button>Probar demo</button></a>
            </div>

            <div class="card">
                <img src="https://gvelazcamp.github.io/SIVO/Asistentetelefonico.png" alt="Telefónico">
                <h3>SIVO Telefónico</h3>
                <p>Atiende llamadas reales con IA conversacional.</p>
                <a href="https://demotelefonico.streamlit.app/" target="_blank" rel="noopener noreferrer" style="text-decoration: none;"><button>Probar ahora</button></a>
            </div>
        </div>
    </div>

    <div class="cta">
        <h2>Integra en minutos</h2>
        <p>Instalá un asistente virtual IA en tu web fácilmente.</p>
        <button>Probar gratis</button>

        <div class="features">
            <div class="feature">⚡ Fácil y rápido</div>
            <div class="feature">⚙️ Configurable</div>
            <div class="feature">🔒 Seguro</div>
            <div class="feature">💬 Soporte</div>
        </div>
    </div>

{FOOTER}
"""

# =========================
# PRECIOS
# =========================
HTML_PRECIOS = f"""{HTML_BASE}
{HEADER}

<div class="section" style="padding-top: 40px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 50px;">
        <p style="font-size: 15px; color: #666; line-height: 1.6;">
            <strong>Paso 1:</strong> Implementación inicial (pago único).<br>
            <strong>Paso 2:</strong> Plan mensual para mantener y mejorar tu asistente.
        </p>
    </div>

    <div class="pricing">
        <!-- IMPLEMENTACIÓN INICIAL -->
        <div class="plan">
            <div class="plan-name">Implementación inicial</div>
            <div class="plan-desc">Dejamos tu asistente funcionando sobre tus datos reales</div>
            
            <div class="plan-price">Desde US$ 250<span>pago único</span></div>
            <div class="plan-note">1 asistente · 1 sitio</div>
            
            <ul class="plan-list">
                <li>✅ Creación del asistente IA</li>
                <li>✅ Conexión a base de datos / archivos</li>
                <li>✅ Configuración de preguntas</li>
                <li>✅ Instalación en web (iframe o sitio)</li>
                <li>✅ Ajustes iniciales</li>
                <li>✅ Soporte de arranque</li>
            </ul>
            
            <div class="plan-btn">
                <a class="btn-primary" href="?vista=home#soporte" style="text-decoration: none; display: block; text-align: center;">
                    Iniciar implementación
                </a>
            </div>
        </div>

        <!-- PRO MENSUAL -->
        <div class="plan pro">
            <div class="badge">Más elegido</div>
            <div class="plan-name">Pro mensual</div>
            <div class="plan-desc">Uso, mantenimiento y evolución continua</div>
            
            <div class="plan-price">US$ 100<span>/mes</span></div>
            <div class="plan-note">1 asistente · 1 sitio</div>
            <div class="plan-note" style="font-size: 12px; color: #999; margin-top: 4px;">
                Requiere implementación inicial previa
            </div>
            
            <ul class="plan-list">
                <li>✅ Asistentes entrenados con tus datos</li>
                <li>✅ Interpretación avanzada (IA + reglas)</li>
                <li>✅ Ajustes y mejoras mensuales</li>
                <li>✅ Reportes de uso</li>
                <li>✅ Soporte prioritario</li>
            </ul>
            
            <div class="plan-btn">
                <a class="btn-primary" href="?vista=home#soporte" style="text-decoration: none; display: block; text-align: center;">
                    Contratar plan Pro
                </a>
            </div>
        </div>

        <!-- ENTERPRISE -->
        <div class="plan">
            <div class="plan-name">Enterprise</div>
            <div class="plan-desc">IA integrada a la operación de tu empresa</div>
            
            <div class="plan-price">A medida<span>/mes</span></div>
            <div class="plan-note">Asistentes ilimitados · Multi-sitio</div>
            
            <ul class="plan-list">
                <li>✅ Integraciones ERP / CRM</li>
                <li>✅ Roles y permisos</li>
                <li>✅ SLA y soporte dedicado</li>
                <li>✅ Seguridad y escalabilidad</li>
                <li>✅ Onboarding completo</li>
            </ul>
            
            <div class="plan-btn">
                <a class="btn-primary" href="?vista=home#soporte" style="text-decoration: none; display: block; text-align: center;">
                    Hablar con ventas
                </a>
            </div>
        </div>
    </div>
</div>

{FOOTER}
"""

# =========================
# ¿QUÉ HACE SIVO?
# =========================
HTML_QUEHACE = f"""{HTML_BASE}
{HEADER}
<style>
html, body, .page-container {{
    background: #ffffff !important;
}}
.qh-hero {{
    text-align: center;
    padding: 60px 5% 40px;
    max-width: 800px;
    margin: 0 auto;
}}
.qh-hero h1 {{
    font-size: 42px;
    font-weight: 800;
    color: #111;
    margin: 0 0 16px;
    line-height: 1.2;
}}
.qh-hero p {{
    font-size: 18px;
    color: #666;
    line-height: 1.6;
    margin: 0;
}}
.qh-badge {{
    display: inline-block;
    background: linear-gradient(135deg, #dbeafe, #ede9fe);
    color: #3b5998;
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 20px;
}}
.qh-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    padding: 0 5% 60px;
    max-width: 900px;
    margin: 0 auto;
}}
.qh-card {{
    background: linear-gradient(135deg, #1e3a5f 0%, #1a1a2e 100%);
    border: none;
    border-radius: 20px;
    padding: 32px 24px;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
    color: white;
}}
.qh-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.15);
}}
.qh-card-icon {{
    width: 50px;
    height: 50px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    margin-bottom: 16px;
    background: rgba(96,165,250,0.15);
}}
.qh-card h3 {{
    font-size: 18px;
    font-weight: 700;
    color: white;
    margin: 0 0 10px;
}}
.qh-card p {{
    font-size: 14px;
    color: rgba(255,255,255,0.75);
    line-height: 1.6;
    margin: 0;
}}
.qh-card .qh-tag {{
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 6px;
    margin-top: 14px;
    background: rgba(96,165,250,0.2);
    color: #93c5fd;
}}
/* Featured card full-width */
.qh-featured {{
    grid-column: 1 / -1;
    background: linear-gradient(135deg, #1e3a5f 0%, #1a1a2e 100%);
    color: white;
    padding: 40px 32px;
    border: none;
}}
.qh-featured h3 {{
    color: white;
    font-size: 22px;
}}
.qh-featured p {{
    color: rgba(255,255,255,0.75);
    font-size: 15px;
}}
.qh-featured .qh-tag {{
    background: rgba(96,165,250,0.2);
    color: #93c5fd;
}}
.qh-cta {{
    text-align: center;
    padding: 0 5% 60px;
}}
.qh-cta a {{
    display: inline-block;
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    color: white;
    padding: 16px 40px;
    border-radius: 14px;
    font-size: 16px;
    font-weight: 700;
    text-decoration: none;
    box-shadow: 0 4px 15px rgba(59,130,246,0.3);
    transition: all 0.2s;
}}
.qh-cta a:hover {{
    box-shadow: 0 6px 25px rgba(59,130,246,0.4);
    transform: translateY(-2px);
}}

@media (max-width: 768px) {{
    .qh-hero h1 {{ font-size: 28px; }}
    .qh-hero p {{ font-size: 15px; }}
    .qh-grid {{ grid-template-columns: 1fr; gap: 16px; }}
    .qh-card {{ padding: 24px 20px; }}
    .qh-featured {{ padding: 30px 24px; }}
}}
</style>

<div class="qh-hero">
    <span class="qh-badge">Novedades SIVO</span>
    <h1>¿Qué puede hacer SIVO por tu negocio?</h1>
    <p>Descubrí todo lo que un empleado digital puede automatizar, responder y gestionar por vos, 24/7.</p>
</div>

<div class="qh-grid">

    <!-- FEATURED: Reportes -->
    <div class="qh-card qh-featured">
        <div class="qh-card-icon">📊</div>
        <h3>Genera reportes automáticos de cada conversación</h3>
        <p>SIVO crea reportes detallados de atención al cliente: cuántas consultas hubo, tiempos de respuesta, temas más frecuentes, nivel de satisfacción y ventas cerradas. Todo en tiempo real, sin que toques nada.</p>
        <span class="qh-tag">NUEVO</span>
    </div>

    <!-- Card: WhatsApp -->
    <div class="qh-card">
        <div class="qh-card-icon">💬</div>
        <h3>Atención por WhatsApp 24/7</h3>
        <p>Responde consultas, toma pedidos, agenda turnos y cierra ventas directamente en WhatsApp, sin descanso.</p>
        <span class="qh-tag">VENTAS</span>
    </div>

    <!-- Card: Multi-idioma -->
    <div class="qh-card">
        <div class="qh-card-icon">🌎</div>
        <h3>Habla en cualquier idioma</h3>
        <p>Detecta el idioma del cliente automáticamente y responde en su lengua. Español, inglés, portugués y más.</p>
        <span class="qh-tag">GLOBAL</span>
    </div>

    <!-- Card: Stock -->
    <div class="qh-card">
        <div class="qh-card-icon">📦</div>
        <h3>Control de stock inteligente</h3>
        <p>Consultá disponibilidad en tiempo real. SIVO revisa tu inventario y le dice al cliente si hay stock, colores, talles y alternativas.</p>
        <span class="qh-tag">INVENTARIO</span>
    </div>

    <!-- Card: Agendas -->
    <div class="qh-card">
        <div class="qh-card-icon">📅</div>
        <h3>Agenda turnos y reservas</h3>
        <p>Tu asistente coordina horarios, confirma turnos y envía recordatorios. Perfecto para clínicas, peluquerías y consultorios.</p>
        <span class="qh-tag">TURNOS</span>
    </div>

    <!-- Card: Reportes detalle -->
    <div class="qh-card">
        <div class="qh-card-icon">📈</div>
        <h3>Dashboard con métricas clave</h3>
        <p>Visualizá conversiones, tiempos de respuesta, horarios pico y los productos más consultados desde un panel simple.</p>
        <span class="qh-tag">ANALYTICS</span>
    </div>

    <!-- Card: Cobros -->
    <div class="qh-card">
        <div class="qh-card-icon">💳</div>
        <h3>Cobra sin salir del chat</h3>
        <p>Genera links de pago de Mercado Pago directo en la conversación. El cliente paga y vos recibís la confirmación al instante.</p>
        <span class="qh-tag">PAGOS</span>
    </div>

    <!-- Card: Entrenamiento -->
    <div class="qh-card">
        <div class="qh-card-icon">🧠</div>
        <h3>Entrenalo con tu información</h3>
        <p>Subí PDFs, catálogos, menús o cualquier documento. SIVO aprende tu negocio y responde con datos reales, no genéricos.</p>
        <span class="qh-tag">IA</span>
    </div>

    <!-- Card: Escalado humano -->
    <div class="qh-card">
        <div class="qh-card-icon">👤</div>
        <h3>Escala a un humano cuando es necesario</h3>
        <p>Si la consulta es compleja, SIVO transfiere la conversación a un agente real con todo el contexto previo.</p>
        <span class="qh-tag">SOPORTE</span>
    </div>

</div>

<div class="qh-cta">
    <a href="?vista=asistentes">Ver SIVO Digitales →</a>
</div>

{FOOTER}
"""

# =========================
# LOGIN
# =========================
HTML_LOGIN = f"""{HTML_BASE}
<style>
html, body, .page-container {{
    background: #f5f7fa !important;
    min-height: 100vh;
}}
.login-wrapper {{
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 20px;
}}
.login-card {{
    background: #ffffff;
    border-radius: 24px;
    padding: 50px 40px;
    max-width: 420px;
    width: 100%;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.08);
    text-align: center;
}}
.login-logo {{
    height: 80px;
    width: auto;
    margin-bottom: 30px;
}}
.login-title {{
    font-size: 24px;
    font-weight: 800;
    color: #111;
    margin: 0 0 8px;
}}
.login-subtitle {{
    font-size: 14px;
    color: #888;
    margin: 0 0 30px;
}}
.login-form {{
    display: flex;
    flex-direction: column;
    gap: 16px;
    text-align: left;
}}
.login-label {{
    font-size: 13px;
    font-weight: 600;
    color: #333;
    margin-bottom: 4px;
    display: block;
}}
.login-input {{
    width: 100%;
    padding: 14px 16px;
    border: 1.5px solid #e0e0e0;
    border-radius: 12px;
    font-size: 15px;
    font-family: Inter, sans-serif;
    outline: none;
    transition: border-color 0.2s;
    background: #fafafa;
    box-sizing: border-box;
}}
.login-input:focus {{
    border-color: #60a5fa;
    background: #fff;
}}
.login-input::placeholder {{
    color: #aaa;
}}
.login-options {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 4px;
}}
.login-remember {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: #555;
    cursor: pointer;
}}
.login-remember input {{
    width: 16px;
    height: 16px;
    accent-color: #3b82f6;
    cursor: pointer;
}}
.login-forgot {{
    font-size: 13px;
    color: #3b82f6;
    text-decoration: none;
    font-weight: 500;
}}
.login-forgot:hover {{
    text-decoration: underline;
}}
.login-btn {{
    width: 100%;
    padding: 15px;
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    color: white;
    border: none;
    border-radius: 14px;
    font-size: 16px;
    font-weight: 700;
    font-family: Inter, sans-serif;
    cursor: pointer;
    transition: all 0.2s;
    margin-top: 8px;
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
}}
.login-btn:hover {{
    box-shadow: 0 6px 25px rgba(59, 130, 246, 0.4);
    transform: translateY(-1px);
}}
.login-divider {{
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 8px 0;
    color: #ccc;
    font-size: 12px;
}}
.login-divider::before,
.login-divider::after {{
    content: '';
    flex: 1;
    height: 1px;
    background: #e8e8e8;
}}
.login-back {{
    margin-top: 20px;
    font-size: 14px;
    color: #888;
}}
.login-back a {{
    color: #3b82f6;
    text-decoration: none;
    font-weight: 600;
}}
.login-back a:hover {{
    text-decoration: underline;
}}
@media (max-width: 768px) {{
    .login-card {{
        padding: 40px 24px;
        border-radius: 20px;
    }}
    .login-logo {{
        height: 60px;
    }}
    .login-title {{
        font-size: 22px;
    }}
}}
</style>

<div class="login-wrapper">
    <div class="login-card">
        <img src="https://gvelazcamp.github.io/SIVO/LogoSivo.svg" alt="SIVO" class="login-logo">
        <h1 class="login-title">Bienvenido de vuelta</h1>
        <p class="login-subtitle">Ingresá a tu cuenta para continuar</p>

        <form class="login-form" onsubmit="return false;">
            <div>
                <label class="login-label">Email</label>
                <input type="email" class="login-input" placeholder="tucorreo@ejemplo.com">
            </div>
            <div>
                <label class="login-label">Contraseña</label>
                <input type="password" class="login-input" placeholder="Tu contraseña">
            </div>
            <div class="login-options">
                <label class="login-remember">
                    <input type="checkbox"> Recordarme
                </label>
                <a href="#" class="login-forgot">¿Olvidaste tu contraseña?</a>
            </div>
            <button type="submit" class="login-btn">Iniciar sesión</button>
            <div class="login-divider">o</div>
            <div class="login-back">
                <a href="?vista=home">← Volver al inicio</a>
            </div>
        </form>
    </div>
</div>

</div>
</body>
</html>
"""

# =========================
# DEMO FÚTBOL
# =========================
HTML_DEMO_FUTBOL = f"""{HTML_BASE}
{HEADER}

<style>
.demo-container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
}}

.demo-header {{
    text-align: center;
    margin-bottom: 40px;
}}

.demo-header img {{
    width: 120px;
    height: 150px;
    object-fit: contain;
    margin-bottom: 20px;
}}

.demo-header h1 {{
    font-size: 32px;
    margin-bottom: 10px;
}}

.demo-header p {{
    color: #666;
    font-size: 16px;
}}

.demo-chat {{
    background: #fff;
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}}

.demo-message {{
    margin-bottom: 20px;
}}

.demo-bubble {{
    padding: 12px 16px;
    border-radius: 16px;
    margin-bottom: 6px;
    max-width: 85%;
    font-size: 14px;
    line-height: 1.5;
}}

.demo-user {{
    background: #111;
    color: #fff;
    margin-left: auto;
    border-bottom-right-radius: 6px;
}}

.demo-bot {{
    background: #ffffff;
    color: #222;
    border-bottom-left-radius: 6px;
}}

.demo-label {{
    font-size: 12px;
    color: #888;
    margin-bottom: 4px;
    font-weight: 600;
}}

.demo-back {{
    text-align: center;
    margin-top: 40px;
}}

.demo-back a {{
    background: #f4b400;
    color: #000;
    padding: 12px 24px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
}}

.cta-demo {{
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    margin: 40px 0;
    color: #fff;
}}

.cta-demo h2 {{
    font-size: 28px;
    margin-bottom: 10px;
    color: #fff;
}}

.cta-demo p {{
    font-size: 16px;
    margin-bottom: 25px;
    opacity: 0.95;
}}

.btn-live {{
    background: #fff;
    color: #f4b400;
    padding: 16px 40px;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

.btn-live:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}}
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="https://gvelazcamp.github.io/SIVO/Asistentefutbol.png" alt="Fútbol">
        <h1>SIVO Fútbol</h1>
        <p>Demo interactivo con 20 conversaciones de ejemplo</p>
    </div>
    
    <div class="demo-chat">
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto sale ser socio?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Tenemos 3 planes disponibles:<br>
            • <strong>Socio Básico:</strong> $15.000/mes<br>
            • <strong>Socio Pleno:</strong> $25.000/mes<br>
            • <strong>Socio VIP:</strong> $45.000/mes<br>
            Cada plan incluye diferentes beneficios. ¿Te gustaría saber qué incluye cada uno?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué incluye cada plan de socio?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot"><strong>Socio Básico:</strong> Acceso a tribunas, descuento 20% en buffet<br>
            <strong>Socio Pleno:</strong> Todo lo anterior + gimnasio, pileta, canchas de paddle<br>
            <strong>Socio VIP:</strong> Todo lo anterior + palcos, estacionamiento, invitados gratis</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué instalaciones puedo usar como socio?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Como socio tenés acceso a:<br>
            • Gimnasio equipado (Pleno y VIP)<br>
            • Pileta climatizada (Pleno y VIP)<br>
            • 4 canchas de paddle (Pleno y VIP)<br>
            • 2 canchas de fútbol 5<br>
            • Buffet con descuentos<br>
            • Vestuarios y duchas<br>
            • Estacionamiento (solo VIP)</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuándo juega el primer equipo este fin de semana?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">El primer equipo juega el domingo 28 de enero a las 17:00 hs de local contra San Lorenzo por la fecha 3 del torneo. Las entradas ya están a la venta en boletería y online.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo saco entrada para el partido del domingo?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Podés sacar tu entrada de 3 formas:<br>
            1. <strong>Online:</strong> www.clubfutbol.com/entradas<br>
            2. <strong>Boletería:</strong> Lunes a sábado 10-18hs<br>
            3. <strong>Día del partido:</strong> Desde las 14:00 hs<br>
            Los socios tienen 30% de descuento. Precios: Platea $8.000, Popular $5.000</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto sale la cuota de las inferiores?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Las cuotas de fútbol infantil son:<br>
            • Categorías 2016-2018: $12.000/mes<br>
            • Categorías 2013-2015: $14.000/mes<br>
            • Categorías 2010-2012: $16.000/mes<br>
            Incluye entrenamiento 3 veces por semana, camiseta oficial y seguro.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen escuela de fútbol para niños?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Nuestra escuelita acepta niños desde 4 años:<br>
            • <strong>Iniciación (4-6 años):</strong> Sábados 10-11:30hs - $8.000/mes<br>
            • <strong>Intermedio (7-9 años):</strong> Martes y jueves 17-18:30hs - $10.000/mes<br>
            • <strong>Avanzado (10-12 años):</strong> Lunes, miércoles y viernes 18-19:30hs - $12.000/mes</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué horarios tiene el gimnasio?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">El gimnasio está disponible para socios Pleno y VIP:<br>
            • <strong>Lunes a viernes:</strong> 7:00 a 22:00 hs<br>
            • <strong>Sábados:</strong> 9:00 a 20:00 hs<br>
            • <strong>Domingos:</strong> 10:00 a 18:00 hs<br>
            Contamos con máquinas de última generación y profesores disponibles.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo alquilar una cancha siendo socio?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Los socios tienen prioridad y descuento:<br>
            • <strong>Fútbol 5:</strong> $12.000/hora (no socios $15.000)<br>
            • <strong>Paddle:</strong> $8.000/hora (no socios $10.000)<br>
            Podés reservar por teléfono, WhatsApp o en recepción con 48hs de anticipación.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Dónde se juega el próximo partido de visitante?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">El próximo partido de visitante es el sábado 3 de febrero a las 19:15 hs contra Independiente en Avellaneda. Estamos organizando un micro para socios (cupos limitados). ¿Te interesa anotarte?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hay descuentos para familiares de socios?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Los familiares directos de socios tienen beneficios:<br>
            • <strong>Cónyuge:</strong> 40% descuento en cuota social<br>
            • <strong>Hijos menores de 18:</strong> 50% descuento<br>
            • <strong>Hermanos:</strong> 20% descuento<br>
            Además, los socios VIP pueden traer 2 invitados gratis por mes.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo me hago socio?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">El proceso es muy simple:<br>
            1. Completá el formulario online o vení personalmente<br>
            2. Presentá DNI, comprobante de domicilio y 2 fotos 4x4<br>
            3. Pagá la cuota de inscripción ($5.000) + primera cuota<br>
            4. ¡Listo! Tu credencial estará en 48hs<br>
            ¿Querés que te envíe el link del formulario?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿El socio tiene descuento en las entradas?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Los socios tienen importantes beneficios en entradas:<br>
            • <strong>Socio Básico:</strong> 30% descuento<br>
            • <strong>Socio Pleno:</strong> 50% descuento<br>
            • <strong>Socio VIP:</strong> Entrada gratis + 1 acompañante<br>
            Además, tenés acceso prioritario sin hacer fila.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen pileta climatizada?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Contamos con pileta climatizada semiolímpica (25m) disponible todo el año para socios Pleno y VIP. Horarios:<br>
            • <strong>Lunes a viernes:</strong> 8:00 a 21:00 hs<br>
            • <strong>Fines de semana:</strong> 10:00 a 19:00 hs<br>
            También dictamos clases de natación para todas las edades.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuál es la dirección del club?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Estamos en Av. Libertador 4500, a 2 cuadras de la estación de subte. Horarios de atención:<br>
            • <strong>Secretaría:</strong> Lunes a viernes 9-18hs<br>
            • <strong>Instalaciones:</strong> Todos los días 7-23hs<br>
            • <strong>Boletería:</strong> Según calendario de partidos<br>
            Líneas de colectivo: 15, 29, 60, 130</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo pausar mi cuota de socio en vacaciones?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí, podés solicitar la suspensión temporaria:<br>
            • <strong>Mínimo:</strong> 1 mes<br>
            • <strong>Máximo:</strong> 3 meses por año<br>
            • <strong>Costo:</strong> $2.000 por mes de suspensión<br>
            Debés solicitarlo con 15 días de anticipación en secretaría. Al reactivar, mantenés tu antigüedad.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Organizan torneos para socios?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Claro! Organizamos varios torneos durante el año:<br>
            • <strong>Torneo Apertura de Fútbol 5:</strong> Marzo-Junio<br>
            • <strong>Torneo de Paddle:</strong> Abril y Septiembre<br>
            • <strong>Copa de Verano:</strong> Enero-Febrero<br>
            • <strong>Campeonato Interno:</strong> Todo el año<br>
            La inscripción es gratuita para socios. ¿Te interesa alguno?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hay buffet en el club?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Nuestro buffet está abierto todos los días:<br>
            • <strong>Lunes a viernes:</strong> 12:00 a 23:00 hs<br>
            • <strong>Fines de semana:</strong> 11:00 a 00:00 hs<br>
            Ofrecemos minutas, parrilla, pizzas y bebidas. Los socios tienen 20% de descuento. En días de partido, menú especial disponible.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿A qué hora abren las boleterías el día del partido?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Las boleterías abren 3 horas antes del partido. Para el partido del domingo a las 17:00, abrimos a las 14:00 hs. Recomendamos:<br>
            • Comprá online para evitar filas<br>
            • Los socios tienen acceso prioritario<br>
            • Taquillas exclusivas para socios VIP<br>
            Aceptamos efectivo, débito, crédito y Mercado Pago.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen estacionamiento?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí, contamos con estacionamiento:<br>
            • <strong>Socios VIP:</strong> Estacionamiento gratuito incluido (150 lugares)<br>
            • <strong>Otros socios:</strong> $2.000 por día<br>
            • <strong>No socios:</strong> $3.000 por día<br>
            También hay estacionamiento público a 2 cuadras ($1.500). En días de partido, te recomendamos venir con anticipación.</div>
        </div>
    </div>
    
    <div class="cta-demo">
        <h2>💬 ¿Querés probarlo en vivo?</h2>
        <p>Chateá con el asistente y hacele las preguntas que quieras</p>
        <a href="https://DEPLOYAR-demo-futbol.streamlit.app" target="_blank" style="text-decoration: none;">
            <button class="btn-live">🚀 Probar ahora</button>
        </a>
    </div>

    <div class="demo-back">
        <a href="?vista=asistentes">← Volver a Asistentes</a>
    </div>
</div>

{FOOTER}
"""

# =========================
# DEMO COCINA
# =========================
HTML_DEMO_COCINA = f"""{HTML_BASE}
{HEADER}

<style>
.demo-container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
}}

.demo-header {{
    text-align: center;
    margin-bottom: 40px;
}}

.demo-header img {{
    width: 120px;
    height: 150px;
    object-fit: contain;
    margin-bottom: 20px;
}}

.demo-header h1 {{
    font-size: 32px;
    margin-bottom: 10px;
}}

.demo-header p {{
    color: #666;
    font-size: 16px;
}}

.demo-chat {{
    background: #fff;
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}}

.demo-message {{
    margin-bottom: 20px;
}}

.demo-bubble {{
    padding: 12px 16px;
    border-radius: 16px;
    margin-bottom: 6px;
    max-width: 85%;
    font-size: 14px;
    line-height: 1.5;
}}

.demo-user {{
    background: #111;
    color: #fff;
    margin-left: auto;
    border-bottom-right-radius: 6px;
}}

.demo-bot {{
    background: #ffffff;
    color: #222;
    border-bottom-left-radius: 6px;
}}

.demo-label {{
    font-size: 12px;
    color: #888;
    margin-bottom: 4px;
    font-weight: 600;
}}

.demo-back {{
    text-align: center;
    margin-top: 40px;
}}

.demo-back a {{
    background: #f4b400;
    color: #000;
    padding: 12px 24px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
}}

.cta-demo {{
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    margin: 40px 0;
    color: #fff;
}}

.cta-demo h2 {{
    font-size: 28px;
    margin-bottom: 10px;
    color: #fff;
}}

.cta-demo p {{
    font-size: 16px;
    margin-bottom: 25px;
    opacity: 0.95;
}}

.btn-live {{
    background: #fff;
    color: #f4b400;
    padding: 16px 40px;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

.btn-live:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}}
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="https://gvelazcamp.github.io/SIVO/Asistentecocina.png" alt="Cocina">
        <h1>SIVO Cocina</h1>
        <p>Demo interactivo - Restaurante</p>
    </div>
    
    <div class="demo-chat">
    <div class="demo-chat">
        <!-- ESCENA 1: Primera consulta con gancho inmediato -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Hola, ¿tienen mesa para esta noche?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Hola! 👋 Sí, tenemos disponibilidad para esta noche.<br>
            • ¿Para cuántas personas?<br>
            • ¿Preferís interior o terraza?<br>
            • ¿Alguna ocasión especial? (te armamos algo lindo 🎉)</div>
        </div>

        <!-- ESCENA 2: Confirmación + Upselling sutil -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Para 2 personas, terraza si hay</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Perfecto 🌟 Mesa en terraza para 2 personas.<br>
            • <strong>Horario sugerido:</strong> 20:30 - 21:00 hs (mejores mesas disponibles)<br>
            • <strong>Terraza climatizada</strong> y vista al jardín<br><br>
            💡 <strong>Tip del chef:</strong> Los viernes tenemos menú degustación sorpresa ($15.000 x 2). ¿Te interesa?</div>
        </div>

        <!-- ESCENA 3: Cierre de reserva rápido -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Reserva para las 21hs</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">✅ <strong>Reserva confirmada:</strong><br>
            📅 Hoy 21:00 hs - Mesa terraza para 2<br>
            📱 Te enviamos recordatorio por WhatsApp<br><br>
            ¿Querés ver la carta ahora o te sorprendemos esta noche? 😊</div>
        </div>

        <!-- ESCENA 4: Consulta de menú con recomendación del chef -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué recomiendan para cenar?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">🔥 <strong>Especialidades del Chef:</strong><br>
            • <strong>Bife de chorizo</strong> (400g) - $18.500<br>
            • <strong>Risotto de hongos</strong> con trufa - $12.000<br>
            • <strong>Salmón rosado</strong> al limón - $14.500<br><br>
            ⭐ <strong>Lo + pedido hoy:</strong> El bife está increíble, en su punto perfecto.<br>
            ¿Alguna preferencia de carne, pescado o vegetariano?</div>
        </div>

        <!-- ESCENA 5: Manejo de restricciones alimentarias -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen opciones sin gluten?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Sí! 100% del menú es adaptable 👨‍🍳<br>
            <strong>Opciones sin gluten destacadas:</strong><br>
            • Ensalada Caesar (sin crutones) - $8.500<br>
            • Milanesa de pollo (rebozado especial) - $11.000<br>
            • Pasta sin gluten con salsa a elección - $9.500<br>
            • Todos nuestros postres tienen versión sin TACC<br><br>
            <strong>Importante:</strong> Cocina separada para celíacos certificados. ¿Querés que avisemos a la cocina?</div>
        </div>

        <!-- ESCENA 6: Venta de bebidas con maridaje -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué vinos tienen?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">🍷 <strong>Carta de vinos (60+ etiquetas):</strong><br>
            <strong>Tintos recomendados:</strong><br>
            • Malbec reserva - $12.000<br>
            • Cabernet blend - $15.500<br>
            • Syrah premium - $22.000<br>
            <strong>Blancos:</strong><br>
            • Chardonnay - $10.000<br>
            • Sauvignon Blanc - $11.500<br><br>
            💡 Si pedís entrada + principal, el sommelier te arma maridaje perfecto. ¿Qué vas a comer?</div>
        </div>

        <!-- ESCENA 7: Urgencia por disponibilidad limitada -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿El salmón viene con guarnición?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 😊 El salmón incluye:<br>
            • Puré de calabaza<br>
            • Verduras grilladas<br>
            • Reducción de cítricos<br><br>
            ⚠️ <strong>Aviso:</strong> Quedan solo <strong>3 porciones</strong> de salmón para esta noche (ingrediente del día).<br>
            ¿Lo reservamos para vos?</div>
        </div>

        <!-- ESCENA 8: Agregar valor con experiencia -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen algo especial para cumpleaños?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Obvio! 🎂🎉<br>
            <strong>Experiencia Cumpleaños incluye:</strong><br>
            ✅ Postre sorpresa de la casa (GRATIS)<br>
            ✅ Cantamos si querés 🎵<br>
            ✅ Foto profesional de regalo<br>
            ✅ Copa de champagne de cortesía<br><br>
            Solo avisanos al reservar. ¿Es para hoy o lo programamos? 🥳</div>
        </div>

        <!-- ESCENA 9: Cross-selling de postres -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué postres tienen?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">🍰 <strong>Postres caseros:</strong><br>
            • Volcán de chocolate - $6.500<br>
            • Cheesecake frutos rojos - $5.800<br>
            • Tiramisú del chef - $6.000<br>
            • Flan mixto - $4.500<br><br>
            🔥 <strong>Combo dulce:</strong> Principal + Postre + Café = $8.000 descuento<br>
            ¿Ya sabés qué vas a pedir de principal?</div>
        </div>

        <!-- ESCENA 10: Takeaway con incentivo -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen para llevar?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 📦 <strong>Servicio Take Away:</strong><br>
            • <strong>15% OFF</strong> en todos los platos<br>
            • Listo en 20-30 minutos<br>
            • Packaging ecológico<br>
            • Pago al retirar o por transferencia<br><br>
            💡 <strong>Hoy:</strong> Promo 2x1 en pastas take away. ¿Pedimos?</div>
        </div>

        <!-- ESCENA 11: Delivery con gestión de expectativas -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Entregan a domicilio?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 🛵 <strong>Delivery propio:</strong><br>
            • Radio: 5 km del restaurante<br>
            • Tiempo: 30-45 min<br>
            • Costo: $1.500<br>
            • <strong>GRATIS</strong> en pedidos +$15.000<br><br>
            Decime tu dirección y te confirmo si llegamos 📍</div>
        </div>

        <!-- ESCENA 12: Menú ejecutivo / almuerzo -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen menú del día?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 🍽️ <strong>Menú Ejecutivo</strong> (Lun-Vie 12-16hs):<br>
            <strong>$8.500 incluye:</strong><br>
            • Entrada (3 opciones)<br>
            • Principal (5 opciones)<br>
            • Postre o café<br>
            • Bebida<br><br>
            ⚡ Servicio rápido (ideal para el mediodía). ¿Venís hoy?</div>
        </div>

        <!-- ESCENA 13: Eventos / salón privado -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Se puede reservar para un grupo grande?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Claro! 🎊 <strong>Salón privado:</strong><br>
            • Capacidad: 15-40 personas<br>
            • Menú personalizado desde $12.000 x persona<br>
            • Incluye: decoración, mozos, música<br>
            • Ideal para: cumpleaños, empresas, eventos<br><br>
            ¿Para cuántas personas sería? Te armo un presupuesto 📋</div>
        </div>

        <!-- ESCENA 14: Transparencia y confianza (higiene/calidad) -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo garantizan la calidad de los ingredientes?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">🥇 <strong>Calidad premium garantizada:</strong><br>
            ✅ Carne de productores locales certificados<br>
            ✅ Verduras orgánicas del mercado (diarias)<br>
            ✅ Pescado fresco (no congelado)<br>
            ✅ Cocina a la vista - podés ver todo<br>
            ✅ Certificación bromatológica A<br><br>
            <strong>Nuestro chef:</strong> 15 años de experiencia. ¿Querés conocer su historia?</div>
        </div>

        <!-- ESCENA 15: Fidelización con programa de beneficios -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen descuentos para clientes frecuentes?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí ⭐ <strong>Club Gourmet:</strong><br>
            • 1 punto cada $100<br>
            • 100 puntos = $1.000 descuento<br><br>
            <strong>Beneficios VIP:</strong><br>
            🥉 Bronce: 5% descuento permanente<br>
            🥈 Plata: 10% + reserva prioritaria<br>
            🥇 Oro: 15% + acceso a cenas privadas con el chef<br><br>
            ¿Te registro? Es gratis y empezás a sumar hoy 🎁</div>
        </div>
    </div>
    
    <div class="cta-demo">
        <h2>💬 ¿Querés probarlo en vivo?</h2>
        <p>Chateá con el asistente y hacele las preguntas que quieras</p>
        <a href="https://demorestaurante.streamlit.app/" target="_blank" style="text-decoration: none;">
            <button class="btn-live">🚀 Probar ahora</button>
        </a>
    </div>

    <div class="demo-back">
        <a href="?vista=asistentes">← Volver a Asistentes</a>
    </div>
</div>

{FOOTER}
"""

# =========================
# DEMO ECOMMERCE
# =========================
HTML_DEMO_ECOMMERCE = f"""{HTML_BASE}
{HEADER}

<style>
.demo-container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
}}

.demo-header {{
    text-align: center;
    margin-bottom: 40px;
}}

.demo-header img {{
    width: 120px;
    height: 150px;
    object-fit: contain;
    margin-bottom: 20px;
}}

.demo-header h1 {{
    font-size: 32px;
    margin-bottom: 10px;
}}

.demo-header p {{
    color: #666;
    font-size: 16px;
}}

.demo-chat {{
    background: #fff;
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}}

.demo-message {{
    margin-bottom: 20px;
}}

.demo-bubble {{
    padding: 12px 16px;
    border-radius: 16px;
    margin-bottom: 6px;
    max-width: 85%;
    font-size: 14px;
    line-height: 1.5;
}}

.demo-user {{
    background: #111;
    color: #fff;
    margin-left: auto;
    border-bottom-right-radius: 6px;
}}

.demo-bot {{
    background: #ffffff;
    color: #222;
    border-bottom-left-radius: 6px;
}}

.demo-label {{
    font-size: 12px;
    color: #888;
    margin-bottom: 4px;
    font-weight: 600;
}}

.demo-back {{
    text-align: center;
    margin-top: 40px;
}}

.demo-back a {{
    background: #f4b400;
    color: #000;
    padding: 12px 24px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
}}

.cta-demo {{
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    margin: 40px 0;
    color: #fff;
}}

.cta-demo h2 {{
    font-size: 28px;
    margin-bottom: 10px;
    color: #fff;
}}

.cta-demo p {{
    font-size: 16px;
    margin-bottom: 25px;
    opacity: 0.95;
}}

.btn-live {{
    background: #fff;
    color: #f4b400;
    padding: 16px 40px;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

.btn-live:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}}
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="https://gvelazcamp.github.io/SIVO/Asistenteecommerce.png" alt="Ecommerce">
        <h1>SIVO Ecommerce</h1>
        <p>Demo interactivo - Tienda Online</p>
    </div>
    
    <div class="demo-chat">
        <!-- ESCENA 1: Bienvenida con recomendación inmediata -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Hola</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Hola! 👋 Bienvenido a TechStore.<br>
            ¿Qué estás buscando hoy?<br><br>
            📱 Celulares | 💻 Notebooks | 🎧 Accesorios | 🎮 Gaming<br><br>
            💡 <strong>Lo más vendido hoy:</strong> iPhone 15 Pro con 20% OFF<br>
            ⏰ <strong>Oferta termina en:</strong> 4 horas</div>
        </div>

        <!-- ESCENA 2: Consulta de producto con stock en tiempo real -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Busco un iPhone 15</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">📱 <strong>iPhone 15 disponible:</strong><br><br>
            <strong>iPhone 15 Pro 256GB</strong> - $1.299.990<br>
            ✅ <strong>Stock:</strong> 3 unidades (Azul titanio)<br>
            🚚 Envío gratis<br>
            💳 12 cuotas sin interés<br>
            ⭐ 4.8/5 (2.341 reviews)<br><br>
            <strong>iPhone 15 128GB</strong> - $999.990<br>
            ✅ <strong>Stock:</strong> 8 unidades<br>
            🚚 Llega mañana<br>
            💳 6 cuotas sin interés<br><br>
            ⚠️ <strong>Alerta:</strong> El Pro en azul tiene bajo stock, ¡aprovechá!<br>
            ¿Cuál te interesa?</div>
        </div>

        <!-- ESCENA 3: Comparación de productos -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuál me conviene más?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">📊 <strong>iPhone 15 vs iPhone 15 Pro:</strong><br><br>
            <strong>Precio:</strong><br>
            • iPhone 15: $999.990<br>
            • iPhone 15 Pro: $1.299.990<br><br>
            <strong>Cámara:</strong><br>
            • iPhone 15: 48MP dual<br>
            • iPhone 15 Pro: 48MP triple + Tele<br><br>
            <strong>Pantalla:</strong><br>
            • iPhone 15: 60Hz<br>
            • iPhone 15 Pro: 120Hz ProMotion<br><br>
            <strong>Batería:</strong><br>
            • iPhone 15: 20hs<br>
            • iPhone 15 Pro: 23hs<br><br>
            💡 <strong>Mi recomendación:</strong><br>
            Si sacás muchas fotos y usás apps pesadas → <strong>Pro</strong><br>
            Si es para uso normal → <strong>Estándar</strong> (ahorrás $300k)<br><br>
            🔥 <strong>Bonus:</strong> Con el Pro te regalo funda + vidrio ($15.000)<br><br>
            ¿Agregamos uno al carrito?</div>
        </div>

        <!-- ESCENA 4: Agregar al carrito con upsell -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Dale, el Pro</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">✅ <strong>iPhone 15 Pro 256GB</strong> agregado al carrito<br><br>
            🛒 <strong>Tu carrito:</strong> $1.299.990<br><br>
            💡 <strong>Clientes que compraron esto también llevaron:</strong><br>
            📦 AirPods Pro 2 - $349.990 (Combo -15%)<br>
            🔋 Cargador MagSafe - $49.990<br>
            📱 Funda Apple original - $29.990<br><br>
            🔥 <strong>OFERTA ESPECIAL:</strong> Si agregás AirPods → <strong>Envío express GRATIS</strong> (24hs)<br><br>
            ¿Agregamos algo más o cerramos la compra?</div>
        </div>

        <!-- ESCENA 5: Consulta de envío y tiempos -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuándo llega a Córdoba?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">📦 <strong>Envío a Córdoba Capital:</strong><br><br>
            <strong>Opciones disponibles:</strong><br>
            🚚 <strong>Estándar:</strong> 3-5 días hábiles - GRATIS<br>
            ⚡ <strong>Express:</strong> 24-48hs - $8.990<br>
            🏪 <strong>Retiro en sucursal:</strong> Gratis, listo mañana<br><br>
            📍 <strong>Sucursales en Córdoba:</strong><br>
            • Shopping Patio Olmos (Centro)<br>
            • Av. Rafael Núñez 4501 (Cerro)<br><br>
            💡 <strong>Tip:</strong> Con envío express llega antes del finde 😊<br><br>
            ¿Cómo preferís recibirlo?</div>
        </div>

        <!-- ESCENA 6: Medios de pago y financiación -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo pagarlo en cuotas?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">💳 <strong>Formas de pago:</strong><br><br>
            <strong>TARJETA DE CRÉDITO:</strong><br>
            ✅ 3 cuotas sin interés - $433.330/mes<br>
            ✅ 6 cuotas sin interés - $216.665/mes<br>
            ✅ 12 cuotas - $118.000/mes (TNA 65%)<br><br>
            <strong>DÉBITO/TRANSFERENCIA:</strong><br>
            💰 5% OFF - Precio final: $1.234.990<br><br>
            <strong>MERCADO PAGO:</strong><br>
            ✅ Hasta 18 cuotas - $82.500/mes<br><br>
            <strong>AHORA 12/18:</strong><br>
            ✅ 12 cuotas - $108.332/mes<br><br>
            🎁 <strong>Bonus:</strong> Pagando con transferencia te damos $65k de descuento.<br><br>
            ¿Cómo querés pagar?</div>
        </div>

        <!-- ESCENA 7: Validación de stock antes de pagar -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">6 cuotas sin interés</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Perfecto! 💳<br><br>
            ⚠️ <strong>IMPORTANTE:</strong> Hay mucha demanda del iPhone 15 Pro azul.<br><br>
            📊 <strong>Stock actual:</strong><br>
            🔵 Azul titanio - <strong>2 unidades</strong> (bajó de 3)<br>
            ⚫ Negro espacial - 5 unidades<br>
            ⚪ Blanco - 4 unidades<br><br>
            ⏰ <strong>8 personas</strong> están mirando este producto AHORA.<br><br>
            💡 ¿Cerramos la compra para que no te quedes sin stock?<br>
            Te lo reservo <strong>10 minutos</strong> sin compromiso.</div>
        </div>

        <!-- ESCENA 8: Proceso de checkout guiado -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Sí, compralo</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Genial! 🎉 Vamos paso a paso:<br><br>
            <strong>PASO 1/3 - Datos de envío:</strong><br>
            📧 Email: [Ingresá tu email]<br>
            📱 Teléfono: [Tu WhatsApp]<br>
            📍 Dirección: [Calle, número, depto]<br>
            🏙️ CP: [Código postal Córdoba]<br><br>
            💡 Te voy a mandar actualizaciones por WhatsApp.<br>
            ¿Seguimos?</div>
        </div>

        <!-- ESCENA 9: Confirmación de compra con expectativas claras -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Listo, completo los datos</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">✅ <strong>¡Compra confirmada!</strong><br><br>
            📦 <strong>Pedido #45821</strong><br>
            iPhone 15 Pro 256GB Azul - $1.299.990<br>
            Pago: 6 cuotas sin interés<br><br>
            🚚 <strong>Envío:</strong><br>
            Llega a Córdoba en 3-5 días hábiles<br>
            📍 Dirección: [tu dirección]<br><br>
            📧 <strong>Te enviamos:</strong><br>
            ✅ Email con factura<br>
            ✅ WhatsApp con tracking<br>
            ✅ Link para seguir el pedido<br><br>
            🎁 <strong>BONUS:</strong> Te agregamos funda + vidrio ($15k) GRATIS<br><br>
            <strong>Número de seguimiento:</strong> AR1234567890<br>
            [🔍 Rastrear pedido]</div>
        </div>

        <!-- ESCENA 10: Consulta de pedido / tracking -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Dónde está mi pedido?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">📦 <strong>Estado de tu pedido #45821:</strong><br><br>
            ✅ Pago confirmado (Hoy 14:30)<br>
            ✅ Preparando pedido (Hoy 15:45)<br>
            🚚 En camino a Córdoba (Hoy 18:20)<br>
            ⏳ En distribución (Mañana estimado)<br>
            📍 Entregado (2-3 días)<br><br>
            📍 <strong>Última ubicación:</strong> Centro de distribución Rosario<br>
            🚛 <strong>Transportista:</strong> Andreani<br>
            📞 <strong>Contacto:</strong> 0810-122-1100<br><br>
            💡 Te avisamos por WhatsApp cuando esté cerca de tu casa.<br>
            ¿Necesitás algo más?</div>
        </div>

        <!-- ESCENA 11: Cambios y devoluciones -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo cambiar el color?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">🔄 <strong>Cambios y devoluciones:</strong><br><br>
            <strong>Tu pedido aún NO salió</strong> del depósito, podemos cambiarlo:<br><br>
            🔵 Azul titanio (actual)<br>
            ⚫ Negro espacial ✅ Disponible<br>
            ⚪ Blanco ✅ Disponible<br>
            🩶 Titanio natural ✅ Disponible<br><br>
            ¿A qué color lo cambiamos? Lo modifico ahora mismo.<br><br>
            💡 Si ya te llegó, tenés <strong>30 días</strong> para cambiarlo gratis.</div>
        </div>

        <!-- ESCENA 12: Consulta técnica de producto -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿El iPhone es liberado?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">📱 <strong>Especificaciones iPhone 15 Pro:</strong><br><br>
            ✅ <strong>Liberado de fábrica</strong> (funciona con cualquier chip)<br>
            ✅ <strong>Garantía oficial Apple</strong> - 1 año<br>
            ✅ <strong>Nuevo sellado</strong> (no refurbished)<br>
            ✅ <strong>Compatible:</strong> Todas las redes 4G/5G Argentina<br><br>
            📋 <strong>Incluye:</strong><br>
            • iPhone 15 Pro<br>
            • Cable USB-C a USB-C<br>
            • Documentación<br>
            • <strong>NO incluye</strong> cargador (se vende aparte)<br><br>
            🎁 <strong>BONUS de TechStore:</strong><br>
            • Funda protectora<br>
            • Vidrio templado<br><br>
            ¿Alguna otra duda técnica?</div>
        </div>

        <!-- ESCENA 13: Problemas con el pedido -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">No me llegó el mail de confirmación</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">😟 Disculpá las molestias. Te ayudo:<br><br>
            🔍 <strong>Verificando pedido #45821...</strong><br><br>
            ✅ El pedido ESTÁ confirmado en el sistema<br>
            📧 Email registrado: cliente@mail.com<br><br>
            💡 <strong>Posibles causas:</strong><br>
            • Revisá spam/correo no deseado<br>
            • El mail puede demorar hasta 15 min<br><br>
            🆘 <strong>Solución inmediata:</strong><br>
            Te reenvío ahora mismo el mail ✅<br>
            También te mando por WhatsApp 📱<br><br>
            📞 ¿Querés que un asesor te llame? (estamos disponibles 9-20hs)</div>
        </div>

        <!-- ESCENA 14: Cross-selling inteligente post-venta -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Ya me llegó el iPhone, gracias</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Genial! 🎉 Esperamos que lo disfrutes.<br><br>
            💡 <strong>Para aprovechar al máximo tu iPhone 15 Pro:</strong><br><br>
            <strong>Accesorios recomendados:</strong><br>
            🎧 AirPods Pro 2 - $349.990 (25% OFF para clientes)<br>
            ⌚ Apple Watch Series 9 - $649.990<br>
            💾 iCloud 200GB - $299/mes (primer mes gratis)<br>
            🔋 Power Bank MagSafe - $39.990<br><br>
            📱 <strong>Protección extra:</strong><br>
            🛡️ Seguro contra robo/rotura - $4.990/mes<br><br>
            🎁 <strong>TU DESCUENTO:</strong> IPHONE15 para 30% OFF en accesorios<br>
            ⏰ Válido por <strong>48hs</strong><br><br>
            ¿Te interesa algo?</div>
        </div>

        <!-- ESCENA 15: Programa de fidelización -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen programa de puntos?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">⭐ <strong>TechClub - Programa VIP:</strong><br><br>
            Con tu compra sumaste <strong>12.999 puntos</strong> 🎉<br><br>
            💰 <strong>Tus puntos:</strong> 12.999<br>
            🎁 <strong>Canjeables por:</strong> $1.299 en próxima compra<br><br>
            <strong>BENEFICIOS TECHCLUB:</strong><br>
            🥉 <strong>Bronce</strong> (0-20k pts): 5% OFF permanente<br>
            🥈 <strong>Plata</strong> (20k-50k pts): 10% OFF + envíos gratis ← <strong>PRÓXIMO NIVEL</strong><br>
            🥇 <strong>Oro</strong> (50k+ pts): 15% OFF + preventa exclusiva<br><br>
            📊 <strong>Te faltan 7.001 pts para nivel Plata</strong><br><br>
            💡 <strong>Próxima compra:</strong> Ganás puntos dobles (esta semana)<br><br>
            ¿Querés ver el catálogo de canjes?</div>
        </div>
    </div>
    
    <div class="cta-demo">
        <h2>💬 ¿Querés probarlo en vivo?</h2>
        <p>Chateá con el asistente y hacele las preguntas que quieras</p>
        <a href="https://demoecommerce.streamlit.app/" target="_blank" style="text-decoration: none;">
            <button class="btn-live">🚀 Probar ahora</button>
        </a>
    </div>
    <div class="demo-back">
        <a href="?vista=asistentes">← Volver a Asistentes</a>
    </div>
</div>

{FOOTER}
"""

# =========================
# DEMO FINANZAS
# =========================
HTML_DEMO_FINANZAS = f"""{HTML_BASE}
{HEADER}

<style>
.demo-container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
}}

.demo-header {{
    text-align: center;
    margin-bottom: 40px;
}}

.demo-header img {{
    width: 120px;
    height: 150px;
    object-fit: contain;
    margin-bottom: 20px;
}}

.demo-header h1 {{
    font-size: 32px;
    margin-bottom: 10px;
}}

.demo-header p {{
    color: #666;
    font-size: 16px;
}}

.demo-chat {{
    background: #fff;
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}}

.demo-message {{
    margin-bottom: 20px;
}}

.demo-bubble {{
    padding: 12px 16px;
    border-radius: 16px;
    margin-bottom: 6px;
    max-width: 85%;
    font-size: 14px;
    line-height: 1.5;
}}

.demo-user {{
    background: #111;
    color: #fff;
    margin-left: auto;
    border-bottom-right-radius: 6px;
}}

.demo-bot {{
    background: #ffffff;
    color: #222;
    border-bottom-left-radius: 6px;
}}

.demo-label {{
    font-size: 12px;
    color: #888;
    margin-bottom: 4px;
    font-weight: 600;
}}

.demo-back {{
    text-align: center;
    margin-top: 40px;
}}

.demo-back a {{
    background: #f4b400;
    color: #000;
    padding: 12px 24px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
}}

.cta-demo {{
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    margin: 40px 0;
    color: #fff;
}}

.cta-demo h2 {{
    font-size: 28px;
    margin-bottom: 10px;
    color: #fff;
}}

.cta-demo p {{
    font-size: 16px;
    margin-bottom: 25px;
    opacity: 0.95;
}}

.btn-live {{
    background: #fff;
    color: #f4b400;
    padding: 16px 40px;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

.btn-live:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}}
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="https://gvelazcamp.github.io/SIVO/Asistentefinanzas.png" alt="Finanzas">
        <h1>SIVO Finanzas</h1>
        <p>Demo interactivo - Asesoramiento Financiero</p>
    </div>
    
    <div class="demo-chat">
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿A cuánto está el dólar hoy?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Cotizaciones del dólar al 26/01/2026:<br>
            💵 <strong>Oficial:</strong> $1.050 compra / $1.090 venta<br>
            💵 <strong>Blue:</strong> $1.280 compra / $1.300 venta<br>
            💵 <strong>MEP:</strong> $1.210<br>
            💵 <strong>CCL:</strong> $1.225<br>
            💵 <strong>Cripto (USDT):</strong> $1.285<br>
            <strong>Variación:</strong> +0.3% vs ayer<br>
            ¿Te interesa alguna operación en particular?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Conviene invertir en plazo fijo o fondos comunes?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Depende de tu perfil y horizonte temporal:<br>
            📊 <strong>Plazo Fijo tradicional:</strong><br>
            • Tasa: 110% anual (9.2% mensual)<br>
            • Riesgo: Muy bajo<br>
            • Liquidez: 30-60 días<br>
            📈 <strong>Fondos Comunes de Inversión:</strong><br>
            • Money Market: 120% anual - Riesgo bajo<br>
            • Renta fija: 130-150% - Riesgo medio<br>
            • Renta mixta: Potencial 160%+ - Riesgo medio-alto<br>
            <strong>Mi recomendación:</strong> Diversificá: 50% PF + 50% FCI. ¿Cuánto querés invertir?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo abro una cuenta para invertir?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Abrir tu cuenta es simple y 100% online:<br>
            1. <strong>Completá el formulario</strong> (5 minutos)<br>
            2. <strong>Validá tu identidad:</strong> DNI + selfie<br>
            3. <strong>Firmá digitalmente</strong><br>
            4. <strong>Transferí fondos</strong> desde tu banco<br>
            5. <strong>¡Empezá a invertir!</strong><br>
            <strong>Requisitos:</strong><br>
            • Ser mayor de 18 años<br>
            • DNI argentino<br>
            • CBU/CVU propio<br>
            ¿Te ayudo a empezar el proceso?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué son los bonos y cómo funcionan?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Los bonos son títulos de deuda:<br>
            📝 <strong>Cómo funcionan:</strong><br>
            • Le prestás plata al gobierno o empresa<br>
            • Te pagan intereses periódicos (renta)<br>
            • Al vencimiento te devuelven el capital<br>
            <strong>Tipos principales:</strong><br>
            💰 <strong>Bonos en pesos:</strong> CER, BADLAR, tasa fija<br>
            💵 <strong>Bonos dollar-linked:</strong> Ajustados por dólar<br>
            🌎 <strong>Bonos en USD:</strong> Renta en dólares<br>
            <strong>Rendimiento actual:</strong> Entre 8% y 15% anual en USD<br>
            ¿Te interesa algún bono en particular?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuál es la diferencia entre CEDEARs y acciones?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Excelente pregunta:<br>
            🇺🇸 <strong>CEDEARs:</strong><br>
            • Certificados que representan acciones extranjeras<br>
            • Cotizan en pesos en Argentina<br>
            • Accedés a Apple, Tesla, Google, etc.<br>
            • Podés comprar fracciones<br>
            🇦🇷 <strong>Acciones locales:</strong><br>
            • Empresas argentinas (YPF, Galicia, Pampa)<br>
            • Cotizan en pesos<br>
            • Mercado más pequeño<br>
            <strong>Ventaja CEDEARs:</strong> Diversificación internacional en pesos.<br>
            Top CEDEARs: AAPL, GOOGL, MSFT, TSLA</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tengo que pagar impuestos por invertir?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí, hay impuestos a considerar:<br>
            💰 <strong>Ganancias de capital:</strong><br>
            • Acciones/CEDEARs: 15% sobre la ganancia<br>
            • Bonos en pesos: Exento<br>
            • Bonos en USD: 15% sobre la ganancia<br>
            💵 <strong>Impuesto a los Bienes Personales:</strong><br>
            • Si tu portafolio supera cierto mínimo<br>
            • Tasa progresiva según monto<br>
            🏦 <strong>Retención automática:</strong><br>
            • El broker retiene y deposita por vos<br>
            <strong>Consejo:</strong> Llevá registro de todas tus operaciones. ¿Querés asesoramiento impositivo?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto necesito para empezar a invertir?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Podés empezar con muy poco:<br>
            💵 <strong>Monto mínimo:</strong><br>
            • Fondos Comunes: Desde $1.000<br>
            • Plazo Fijo: Desde $1.000<br>
            • CEDEARs: Desde $5.000 (fraccionados)<br>
            • Acciones locales: Desde $3.000<br>
            • Bonos: Desde $10.000<br>
            <strong>Recomendación inicial:</strong><br>
            Con $50.000 podés armar un portafolio diversificado:<br>
            • 40% FCI Money Market<br>
            • 30% CEDEARs<br>
            • 30% Bonos CER<br>
            ¿Con cuánto te gustaría empezar?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué es un portafolio diversificado?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Diversificar es no poner todos los huevos en la misma canasta:<br>
            🎯 <strong>Portafolio conservador:</strong><br>
            • 60% Fondos de renta fija<br>
            • 30% Plazo fijo / Money Market<br>
            • 10% CEDEARs blue chips<br>
            ⚖️ <strong>Portafolio moderado:</strong><br>
            • 40% Bonos (CER + USD)<br>
            • 30% CEDEARs<br>
            • 20% FCI renta mixta<br>
            • 10% Cripto<br>
            🚀 <strong>Portafolio agresivo:</strong><br>
            • 50% Acciones/CEDEARs<br>
            • 30% Cripto<br>
            • 20% Bonos<br>
            ¿Cuál es tu perfil de riesgo?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Conviene invertir en criptomonedas?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Las cripto tienen alto potencial pero también alto riesgo:<br>
            ⚠️ <strong>Pros:</strong><br>
            • Potencial de alta rentabilidad<br>
            • Descentralizadas<br>
            • Liquidez 24/7<br>
            • Cobertura contra inflación<br>
            ⚠️ <strong>Contras:</strong><br>
            • Muy volátiles<br>
            • Sin respaldo ni garantías<br>
            • Riesgo de hackeos<br>
            <strong>Mi recomendación:</strong><br>
            • Máximo 10-15% de tu portafolio<br>
            • Empezá con BTC y ETH (las más consolidadas)<br>
            • Usá exchanges regulados<br>
            ¿Tenés experiencia en cripto?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo saco mi dinero si lo necesito?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">La liquidez varía según el instrumento:<br>
            ⚡ <strong>Liquidez inmediata:</strong><br>
            • Fondos Money Market: 24-48hs<br>
            • Acciones/CEDEARs: T+2 (vendés hoy, cobras en 2 días)<br>
            • Cripto: Instantáneo<br>
            📅 <strong>Liquidez con plazo:</strong><br>
            • Plazo Fijo: Al vencimiento (30-60 días)<br>
            • Bonos: Vendés en mercado secundario (T+2)<br>
            💸 <strong>Extracción:</strong><br>
            • Transferís a tu cuenta bancaria<br>
            • Sin comisiones<br>
            • Demora: 24-48hs hábiles<br>
            ¿Necesitás liquidez inmediata?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué comisiones cobran?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Nuestras comisiones son competitivas:<br>
            📊 <strong>Acciones/CEDEARs:</strong><br>
            • Compra/venta: 0.6% por operación<br>
            • Derechos de mercado: 0.05%<br>
            💰 <strong>Fondos Comunes:</strong><br>
            • Sin comisión de compra/venta<br>
            • Fee del fondo: 1-3% anual<br>
            🏦 <strong>Otros:</strong><br>
            • Custodia: GRATIS<br>
            • Transferencias: GRATIS<br>
            • Mantenimiento de cuenta: GRATIS<br>
            ¿Tenés dudas sobre alguna comisión?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Ofrecen asesoramiento personalizado?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Tenemos varios niveles de asesoramiento:<br>
            🤖 <strong>Básico (GRATIS):</strong><br>
            • Robo-advisor automático<br>
            • Sugerencias de portafolio<br>
            • Alertas y recomendaciones<br>
            👤 <strong>Premium ($15.000/mes):</strong><br>
            • Asesor financiero personal<br>
            • Reuniones mensuales<br>
            • Análisis detallado de cartera<br>
            💎 <strong>VIP ($50.000/mes):</strong><br>
            • Gestor de patrimonio dedicado<br>
            • Estrategias personalizadas<br>
            • Acceso a productos exclusivos<br>
            • Atención prioritaria 24/7<br>
            ¿Te interesa agendar una consulta inicial gratuita?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo está el Merval hoy?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Situación del mercado argentino hoy:<br>
            📊 <strong>Merval:</strong> 1.456.789 puntos (+2.3%)<br>
            <strong>Acciones destacadas:</strong><br>
            📈 <strong>Suben:</strong><br>
            • YPF: $35.800 (+5.2%)<br>
            • Galicia: $245 (+3.8%)<br>
            • Pampa: $89 (+2.1%)<br>
            📉 <strong>Bajan:</strong><br>
            • GGAL: $198 (-1.5%)<br>
            • ALUA: $12.50 (-0.8%)<br>
            💰 <strong>Volumen operado:</strong> $28.500 millones<br>
            ¿Te interesa alguna acción en particular?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué es el riesgo país y cómo me afecta?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">El riesgo país mide la confianza en Argentina:<br>
            📉 <strong>Riesgo país actual:</strong> 580 puntos básicos<br>
            🔍 <strong>Qué significa:</strong><br>
            • Sobretasa que Argentina debe pagar vs. bonos seguros (USA)<br>
            • Cuanto más alto = más riesgo perciben los inversores<br>
            💼 <strong>Cómo te afecta:</strong><br>
            • Baja ⬇️: Bonos suben, acciones suben, dólar estable<br>
            • Sube ⬆️: Bonos bajan, incertidumbre, dólar presionado<br>
            <strong>Contexto:</strong> 580 puntos es moderado-alto.<br>
            Ideal: Por debajo de 400 puntos.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo invertir en el exterior desde Argentina?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí, hay varias formas:<br>
            🌎 <strong>1. CEDEARs (la más fácil):</strong><br>
            • Invertís en empresas USA en pesos<br>
            • Sin límites ni trabas<br>
            💵 <strong>2. Broker internacional:</strong><br>
            • Abrís cuenta en Interactive Brokers, TD Ameritrade, etc.<br>
            • Necesitás dólares afuera<br>
            • Acceso total a mercados globales<br>
            🏦 <strong>3. ETFs internacionales:</strong><br>
            • A través de ciertos brokers locales<br>
            • Diversificación global<br>
            <strong>Más popular:</strong> CEDEARs por simplicidad.<br>
            ¿Te interesa alguna empresa en particular?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué es el carry trade?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">El carry trade es una estrategia financiera:<br>
            💰 <strong>Cómo funciona:</strong><br>
            1. Invertís en pesos a tasa alta (ej: 110% anual)<br>
            2. Esperás que el dólar suba menos que esa tasa<br>
            3. Al vencimiento, vendés a dólares con ganancia<br>
            ⚠️ <strong>Ejemplo:</strong><br>
            • Invertís $1.000.000 al 110% anual = $1.100.000<br>
            • Si el dólar sube 80%, igual ganaste 30%<br>
            ⚠️ <strong>Riesgos:</strong><br>
            • Si el dólar sube más que la tasa, perdés<br>
            • Devaluaciones bruscas<br>
            • Cambios de reglas<br>
            <strong>¿Conviene ahora?</strong> Depende de expectativas de dólar.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen cursos o material educativo?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Tenemos una academia completa:<br>
            📚 <strong>Cursos gratuitos:</strong><br>
            • Introducción a las inversiones (3 módulos)<br>
            • Cómo leer un balance<br>
            • Análisis técnico básico<br>
            🎓 <strong>Cursos premium:</strong><br>
            • Trading avanzado ($25.000)<br>
            • Value investing ($30.000)<br>
            • Análisis fundamental ($28.000)<br>
            📊 <strong>Recursos adicionales:</strong><br>
            • Webinars semanales gratis<br>
            • Blog con análisis diarios<br>
            • Newsletter con las mejores oportunidades<br>
            • Simulador de trading<br>
            ¿Te interesa algún curso en particular?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué pasa con mis inversiones si quiebra el broker?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Tus inversiones están protegidas:<br>
            ����️ <strong>Custodia segregada:</strong><br>
            • Tus activos están a TU nombre<br>
            • Depositados en Caja de Valores<br>
            • NO son activos del broker<br>
            📋 <strong>Si el broker quiebra:</strong><br>
            • Tus acciones/bonos siguen siendo tuyas<br>
            • Podés transferirlos a otro broker<br>
            • El efectivo en la cuenta tiene garantía CNV<br>
            ✅ <strong>Regulaciones:</strong><br>
            • Supervisión de la CNV<br>
            • Auditorías periódicas<br>
            • Fondo de garantía<br>
            Estamos regulados y tus inversiones están protegidas.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo me contacto con un asesor?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Tenés varias formas de contactarnos:<br>
            📞 <strong>Teléfono:</strong> 0800-555-INVER (gratuito)<br>
            &nbsp;&nbsp;&nbsp;Lun-Vie 9-18hs<br>
            💬 <strong>WhatsApp:</strong> +54 9 11 5555-INVER<br>
            &nbsp;&nbsp;&nbsp;Respuesta en minutos<br>
            📧 <strong>Email:</strong> asesores@broker.com.ar<br>
            &nbsp;&nbsp;&nbsp;Respuesta en 24hs<br>
            💻 <strong>Chat web:</strong> En nuestra página<br>
            &nbsp;&nbsp;&nbsp;Lun-Vie 9-20hs<br>
            📅 <strong>Agenda videollamada:</strong> Gratuita 30 min<br>
            ¿Preferís que te llame un asesor o agendamos una videollamada?</div>
        </div>
    </div>
    
    <div class="cta-demo">
        <h2>💬 ¿Querés probarlo en vivo?</h2>
        <p>Chateá con el asistente y hacele las preguntas que quieras</p>
        <a href="https://DEPLOYAR-demo-finanzas.streamlit.app" target="_blank" style="text-decoration: none;">
            <button class="btn-live">🚀 Probar ahora</button>
        </a>
    </div>

    <div class="demo-back">
        <a href="?vista=asistentes">← Volver a Asistentes</a>
    </div>
</div>

{FOOTER}
"""

# =========================
# DEMO TIENDA DE ROPA
# =========================
HTML_DEMO_ROPA = f"""{HTML_BASE}
{HEADER}

<style>
.demo-container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
}}

.demo-header {{
    text-align: center;
    margin-bottom: 40px;
}}

.demo-header img {{
    width: 120px;
    height: 150px;
    object-fit: contain;
    margin-bottom: 20px;
}}

.demo-header h1 {{
    font-size: 32px;
    margin-bottom: 10px;
}}

.demo-header p {{
    color: #666;
    font-size: 16px;
}}

.demo-chat {{
    background: #fff;
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}}

.demo-message {{
    margin-bottom: 20px;
}}

.demo-bubble {{
    padding: 12px 16px;
    border-radius: 16px;
    margin-bottom: 6px;
    max-width: 85%;
    font-size: 14px;
    line-height: 1.5;
}}

.demo-user {{
    background: #111;
    color: #fff;
    margin-left: auto;
    border-bottom-right-radius: 6px;
}}

.demo-bot {{
    background: #ffffff;
    color: #222;
    border-bottom-left-radius: 6px;
}}

.demo-label {{
    font-size: 12px;
    color: #888;
    margin-bottom: 4px;
    font-weight: 600;
}}

.demo-back {{
    text-align: center;
    margin-top: 40px;
}}

.demo-back a {{
    background: #f4b400;
    color: #000;
    padding: 12px 24px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
}}

.cta-demo {{
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    margin: 40px 0;
    color: #fff;
}}

.cta-demo h2 {{
    font-size: 28px;
    margin-bottom: 10px;
    color: #fff;
}}

.cta-demo p {{
    font-size: 16px;
    margin-bottom: 25px;
    opacity: 0.95;
}}

.btn-live {{
    background: #fff;
    color: #f4b400;
    padding: 16px 40px;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

.btn-live:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}}
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="https://gvelazcamp.github.io/SIVO/Asistentedetiendaderopa.png" alt="Tienda de Ropa">
        <h1>SIVO Tienda de Ropa</h1>
        <p>Demo interactivo - Tienda Online</p>
    </div>
    
    <div class="demo-chat">
        <!-- ESCENA 1: El cliente entra y duda (inicio real) -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Hola, estoy viendo la remera básica blanca</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Hola! 👋 Veo que estás mirando la remera básica. ¿Querés ayuda con el talle, colores o precio?</div>
        </div>

        <!-- ESCENA 2: Talle con recomendación -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen talle M?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 😊 Está disponible en talle M.<br>
            • <strong>Colores:</strong> blanco, negro, gris, azul marino<br>
            • <strong>Precio:</strong> $8.999<br>
            • <strong>Stock:</strong> 15 unidades<br><br>
            Por tu elección, el M es el más vendido. ¿La agregamos al carrito?</div>
        </div>

        <!-- ESCENA 3: Acción concreta -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Sí, agregala</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">✅ Listo, ya la agregué al carrito.<br><br>
            💡 <strong>Tip:</strong> Sumando otra prenda tenés 15% OFF automático. ¿Querés que te recomiende un jean que combine?</div>
        </div>

        <!-- ESCENA 4: Venta cruzada -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Dale, mostrame jeans</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Perfecto 👖 Te recomiendo estos:<br>
            • <strong>Jean clásico</strong> – $24.999<br>
            • <strong>Jean elastizado</strong> – $28.999<br>
            • <strong>Jean mom fit</strong> – $26.999<br><br>
            🔥 <strong>Promo activa:</strong> 3x2 en jeans esta semana<br>
            ¿Buscás algo más clásico o más ajustado?</div>
        </div>

        <!-- ESCENA 5: Selección específica -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">El clásico en negro</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Excelente elección 🙌<br>
            • <strong>Color:</strong> Negro<br>
            • <strong>Talles disponibles:</strong> 36 al 48<br>
            • <strong>Precio:</strong> $24.999<br><br>
            ¿Qué talle necesitás para agregarlo al carrito?</div>
        </div>

        <!-- ESCENA 6: Carrito y beneficio visible -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Talle 40</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">✅ Jean talle 40 agregado al carrito.<br><br>
            📦 Con esta compra te faltan $4.000 para envío gratis. ¿Querés sumar una remera más y aprovecharlo?</div>
        </div>

        <!-- ESCENA 7: Envío contextual -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen envíos a Córdoba?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 🚚 Envíos a Córdoba Capital:<br>
            • <strong>Estándar:</strong> 5–7 días – $2.800<br>
            • <strong>Express:</strong> 3–4 días – $4.200<br><br>
            🎁 En compras mayores a $50.000 el envío es GRATIS. ¿Querés que lo calcule exacto con tu compra actual?</div>
        </div>

        <!-- ESCENA 8: Pago sin fricción -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo pagar con tarjeta?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 💳<br>
            • Hasta 12 cuotas sin interés<br>
            • Mercado Pago: hasta 18 cuotas<br>
            • Transferencia: 15% OFF adicional<br><br>
            ¿Preferís cuotas o aprovechar el descuento por transferencia?</div>
        </div>

        <!-- ESCENA 9: Confianza (local físico) -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen local físico?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 🏪<br>
            📍 <strong>Palermo</strong> – Av. Santa Fe 4200<br>
            📍 <strong>Belgrano</strong> – Av. Cabildo 1800<br><br>
            Podés comprar online y retirar GRATIS en tienda. ¿Querés envío o retiro en local?</div>
        </div>

        <!-- ESCENA 10: Cambio y tranquilidad -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Y si no me queda?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">No hay problema 👍 Tenés 30 días para cambios o devoluciones.<br>
            • <strong>Cambio de talle/color:</strong> GRATIS<br>
            • <strong>Devolución:</strong> reembolso 100%<br><br>
            Comprás tranquilo/a, nosotros nos ocupamos.</div>
        </div>

        <!-- ESCENA 11: Guía de talles asistida -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Nunca sé bien qué talle soy</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Te ayudo 😊 Si querés, decime tu altura y peso y te recomiendo el talle ideal. Además, cada producto tiene una guía exacta en cm.<br><br>
            ¿Querés que lo veamos ahora?</div>
        </div>

        <!-- ESCENA 12: Promos activas -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hay promociones hoy?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 🔥<br>
            • 3x2 en jeans<br>
            • 2x1 en remeras básicas<br>
            • 20% OFF primera compra<br>
            • Envío gratis desde $50.000<br><br>
            Los descuentos se aplican automáticamente en el carrito.</div>
        </div>

        <!-- ESCENA 13: Reserva inteligente -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo reservar?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 😊<br>
            • <strong>Online:</strong> el carrito te reserva el producto por 2 horas<br>
            • <strong>En local:</strong> lo apartamos 48 hs<br><br>
            ¿Querés seguir con la compra o reservar para más tarde?</div>
        </div>

        <!-- ESCENA 14: Facturación -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Dan factura?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí 🧾<br>
            • Factura B automática<br>
            • Factura A ingresando CUIT<br><br>
            La recibís por email apenas se confirma el pago.</div>
        </div>

        <!-- ESCENA 15: Fidelización -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen programa de puntos?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí ⭐ <strong>Club ROPA VIP</strong><br>
            • 1 punto cada $100<br>
            • 100 puntos = $500 de descuento<br><br>
            Además, los clientes VIP acceden a preventas exclusivas. ¿Querés registrarte gratis?</div>
        </div>
    </div>
    </div>
    
    <div class="cta-demo">
        <h2>💬 ¿Querés probarlo en vivo?</h2>
        <p>Chateá con el asistente y hacele las preguntas que quieras</p>
        <a href="https://demoropa.streamlit.app/" target="_blank" style="text-decoration: none;">
            <button class="btn-live">🚀 Probar ahora</button>
        </a>
    </div>

    <div class="demo-back">
        <a href="?vista=asistentes">← Volver a Asistentes</a>
    </div>
</div>

{FOOTER}
"""

# =========================
# DEMO PELUQUERÍA
# =========================
HTML_DEMO_PELUQUERIA = f"""{HTML_BASE}
{HEADER}

<style>
.demo-container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
}}

.demo-header {{
    text-align: center;
    margin-bottom: 40px;
}}

.demo-header img {{
    width: 120px;
    height: 150px;
    object-fit: contain;
    margin-bottom: 20px;
}}

.demo-header h1 {{
    font-size: 32px;
    margin-bottom: 10px;
}}

.demo-header p {{
    color: #666;
    font-size: 16px;
}}

.demo-chat {{
    background: #fff;
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}}

.demo-message {{
    margin-bottom: 20px;
}}

.demo-bubble {{
    padding: 12px 16px;
    border-radius: 16px;
    margin-bottom: 6px;
    max-width: 85%;
    font-size: 14px;
    line-height: 1.5;
}}

.demo-user {{
    background: #111;
    color: #fff;
    margin-left: auto;
    border-bottom-right-radius: 6px;
}}

.demo-bot {{
    background: #ffffff;
    color: #222;
    border-bottom-left-radius: 6px;
}}

.demo-label {{
    font-size: 12px;
    color: #888;
    margin-bottom: 4px;
    font-weight: 600;
}}

.demo-back {{
    text-align: center;
    margin-top: 40px;
}}

.demo-back a {{
    background: #f4b400;
    color: #000;
    padding: 12px 24px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
}}

.cta-demo {{
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    margin: 40px 0;
    color: #fff;
}}

.cta-demo h2 {{
    font-size: 28px;
    margin-bottom: 10px;
    color: #fff;
}}

.cta-demo p {{
    font-size: 16px;
    margin-bottom: 25px;
    opacity: 0.95;
}}

.btn-live {{
    background: #fff;
    color: #f4b400;
    padding: 16px 40px;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

.btn-live:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}}
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="https://gvelazcamp.github.io/SIVO/Asistentedepeluqueria.png" alt="Peluquería">
        <h1>SIVO Peluquería</h1>
        <p>Demo interactivo - Salón de Belleza</p>
    </div>
    
    <div class="demo-chat">
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto sale un corte de pelo?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Nuestros precios de corte:<br>• <strong>Mujer:</strong> $8.500<br>• <strong>Hombre:</strong> $6.000<br>• <strong>Niños (hasta 12 años):</strong> $5.000<br>Incluye lavado, corte y secado. ¿Querés sacar turno?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen turnos disponibles para mañana?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Mañana tenemos disponibilidad:<br>• 10:00 hs<br>• 14:30 hs<br>• 16:00 hs<br>• 18:00 hs<br>¿Cuál horario te viene bien? ¿Qué servicio necesitás?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen coloración?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Servicios de color:<br>• <strong>Color completo:</strong> $18.000<br>• <strong>Retoque de raíz:</strong> $12.000<br>• <strong>Balayage:</strong> $25.000<br>• <strong>Mechas tradicionales:</strong> $20.000<br>Usamos productos de alta gama (Loreal, Wella). Incluye lavado, color y brushing.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto dura un tratamiento de keratina?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">El tratamiento de keratina:<br>• <strong>Duración:</strong> 3-4 horas<br>• <strong>Precio:</strong> $35.000<br>• <strong>Efecto:</strong> Dura 3-4 meses<br>• <strong>Incluye:</strong> Lavado, aplicación, planchado, brushing<br>Te deja el pelo liso y sin frizz. ¿Reservamos turno?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Atienden con turno o sin turno?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Trabajamos principalmente CON TURNO:<br>• <strong>Con turno:</strong> Atención garantizada a horario<br>• <strong>Sin turno:</strong> Según disponibilidad<br>Te recomendamos sacar turno para asegurar tu horario. Podés reservar por:<br>• WhatsApp: +54 11 5555-PELO<br>• Web: www.peluqueria.com<br>• Teléfono: 011 4444-4444</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen peinados para eventos?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Peinados para eventos:<br>• <strong>Recogido simple:</strong> $12.000<br>• <strong>Recogido elaborado:</strong> $18.000<br>• <strong>Semi-recogido:</strong> $15.000<br>• <strong>Peinado con rulos:</strong> $14.000<br>Incluye prueba previa si reservás con 1 semana de anticipación. ¿Es para algún evento especial?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto sale mechas balayage?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Balayage completo: $25.000<br>• <strong>Incluye:</strong> Diagnóstico, decoloración, tonalización, tratamiento, brushing<br>• <strong>Duración:</strong> 3-4 horas<br>• <strong>Productos:</strong> Loreal Professionnel<br>• <strong>Efecto:</strong> Natural, iluminado, sin marcas<br>Dura 3-4 meses. ¿Te interesa agendar una consulta?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Trabajan con novias?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Servicio completo para novias:<br>• <strong>Peinado novia:</strong> $25.000<br>• <strong>Maquillaje novia:</strong> $22.000<br>• <strong>Combo peinado + makeup:</strong> $42.000<br>• <strong>Prueba previa:</strong> Incluida<br>• <strong>Atención a domicilio:</strong> Disponible<br>También peinamos a las madrinas. ¿Para cuándo es el casamiento?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Aceptan tarjetas?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Todas las formas de pago:<br>• <strong>Efectivo:</strong> 10% descuento<br>• <strong>Débito:</strong> Precio de lista<br>• <strong>Crédito:</strong> Hasta 6 cuotas sin interés<br>• <strong>Mercado Pago:</strong> Hasta 12 cuotas<br>Aceptamos Visa, Mastercard, Amex, Naranja.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo cancelar mi turno?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí, podés cancelar o reprogramar:<br>• <strong>Con 24hs de anticipación:</strong> Sin cargo<br>• <strong>Menos de 24hs:</strong> Se cobra 50% del servicio<br>• <strong>No show:</strong> Se cobra 100%<br>Para cancelar llamá, escribí por WhatsApp o entrá a tu cuenta en la web. ¿Necesitás cancelar o reprogramar?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen barbería también?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Servicios de barbería:<br>• <strong>Corte + barba:</strong> $8.500<br>• <strong>Corte simple:</strong> $6.000<br>• <strong>Barba y perfilado:</strong> $4.500<br>• <strong>Afeitado clásico:</strong> $3.500<br>Usamos navajas profesionales y productos premium. ¿Sacamos turno?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto sale un brushing?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Brushing profesional: $4.500<br>• <strong>Incluye:</strong> Lavado + secado con cepillo<br>• <strong>Duración:</strong> 30-40 minutos<br>• <strong>Con plancha:</strong> +$1.000<br>• <strong>Con rulos:</strong> +$1.500<br>Ideal para eventos o salidas. ¿Para cuándo lo necesitás?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen servicios de manicura?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Servicios de uñas:<br>• <strong>Manicura clásica:</strong> $5.000<br>• <strong>Manicura permanente:</strong> $8.000<br>• <strong>Pedicura clásica:</strong> $6.500<br>• <strong>Pedicura permanente:</strong> $9.500<br>• <strong>Kapping gel:</strong> $12.000<br>Usamos productos de primera calidad. ¿Reservamos turno?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué productos usan?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Trabajamos con marcas premium:<br>• <strong>Color:</strong> Loreal Professionnel, Wella<br>• <strong>Tratamientos:</strong> Kerastase, Olaplex<br>• <strong>Styling:</strong> Sebastian, Moroccanoil<br>• <strong>Keratina:</strong> Inoar, Cadiveu<br>Todos nuestros productos son profesionales de alta gama. ¡Cuidamos tu cabello!</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Dónde están ubicados?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Estamos en:<br>📍 Av. Santa Fe 2800, Palermo<br>🚇 <strong>Subte:</strong> Línea D (Bulnes) - 3 cuadras<br>🚌 <strong>Colectivos:</strong> 12, 39, 55, 110<br><strong>Horarios:</strong><br>• Lun-Vie: 9:00 a 20:00<br>• Sábados: 9:00 a 19:00<br>• Domingos: Cerrado<br>📞 Teléfono: 011 4444-4444</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto tiempo dura el servicio de color?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Duración según servicio:<br>• <strong>Color completo:</strong> 2-2.5 horas<br>• <strong>Retoque raíz:</strong> 1.5-2 horas<br>• <strong>Balayage:</strong> 3-4 horas<br>• <strong>Mechas:</strong> 2.5-3 horas<br>Incluye tiempo de pose, lavado y secado. Te recomendamos venir con tiempo! ¿Qué servicio querés hacer?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen alisado permanente?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Alisados disponibles:<br>• <strong>Alisado con keratina:</strong> $35.000 (dura 3-4 meses)<br>• <strong>Alisado japonés:</strong> $45.000 (permanente)<br>• <strong>Nanoplastia:</strong> $40.000 (dura 4-5 meses)<br>• <strong>Botox capilar:</strong> $28.000 (dura 2-3 meses)<br>Cada uno tiene diferentes resultados. ¿Querés una asesoría personalizada?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen descuentos para estudiantes?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Promociones especiales:<br>• <strong>Estudiantes:</strong> 15% OFF presentando credencial<br>• <strong>Jubilados:</strong> 20% OFF (lunes a miércoles)<br>• <strong>Primera vez:</strong> 10% OFF<br>• <strong>Martes y miércoles:</strong> 2x1 en cortes hasta 14hs<br>Los descuentos no son acumulables. ¿Tenés credencial de estudiante?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo ver fotos de trabajos anteriores?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Claro! Podés ver nuestro trabajo en:<br>📸 <strong>Instagram:</strong> @peluqueria (500+ fotos)<br>📘 <strong>Facebook:</strong> Peluqueria Palermo<br>🌐 <strong>Web:</strong> www.peluqueria.com/galeria<br>Subimos fotos de trabajos todos los días. También tenemos reseñas de clientes en Google (4.8★). ¿Te interesa algún estilo en particular?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo reprogramo mi turno?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Para reprogramar tu turno:<br>1. <strong>WhatsApp:</strong> +54 11 5555-PELO<br>2. <strong>Teléfono:</strong> 011 4444-4444<br>3. <strong>Web:</strong> Entrá a tu cuenta<br>4. <strong>Instagram:</strong> Mensaje directo<br>Recordá hacerlo con 24hs de anticipación para evitar cargos. ¿Necesitás cambiar tu turno ahora?</div>
        </div>
    </div>
    
    <div class="cta-demo">
        <h2>💬 ¿Querés probarlo en vivo?</h2>
        <p>Chateá con el asistente y hacele las preguntas que quieras</p>
        <a href="https://DEPLOYAR-demo-peluqueria.streamlit.app" target="_blank" style="text-decoration: none;">
            <button class="btn-live">🚀 Probar ahora</button>
        </a>
    </div>

    <div class="demo-back">
        <a href="?vista=asistentes">← Volver a Asistentes</a>
    </div>
</div>

{FOOTER}
"""

# =========================
# RENDER
# =========================


# =========================
# DEMO VIAJES
# =========================
HTML_DEMO_VIAJES = f"""{HTML_BASE}
{HEADER}

<style>
.demo-container {{
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
}}

.demo-header {{
    text-align: center;
    margin-bottom: 40px;
}}

.demo-header img {{
    width: 120px;
    height: 150px;
    object-fit: contain;
    margin-bottom: 20px;
}}

.demo-header h1 {{
    font-size: 32px;
    margin-bottom: 10px;
}}

.demo-header p {{
    color: #666;
    font-size: 16px;
}}

.demo-chat {{
    background: #fff;
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}}

.demo-message {{
    margin-bottom: 20px;
}}

.demo-bubble {{
    padding: 12px 16px;
    border-radius: 16px;
    margin-bottom: 6px;
    max-width: 85%;
    font-size: 14px;
    line-height: 1.5;
}}

.demo-user {{
    background: #111;
    color: #fff;
    margin-left: auto;
    border-bottom-right-radius: 6px;
}}

.demo-bot {{
    background: #ffffff;
    color: #222;
    border-bottom-left-radius: 6px;
}}

.demo-label {{
    font-size: 12px;
    color: #888;
    margin-bottom: 4px;
    font-weight: 600;
}}

.demo-back {{
    text-align: center;
    margin-top: 40px;
}}

.demo-back a {{
    background: #f4b400;
    color: #000;
    padding: 12px 24px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
}}

.cta-demo {{
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    border-radius: 20px;
    padding: 40px 30px;
    text-align: center;
    margin: 40px 0;
    color: #fff;
}}

.cta-demo h2 {{
    font-size: 28px;
    margin-bottom: 10px;
    color: #fff;
}}

.cta-demo p {{
    font-size: 16px;
    margin-bottom: 25px;
    opacity: 0.95;
}}

.btn-live {{
    background: #fff;
    color: #f4b400;
    padding: 16px 40px;
    border-radius: 12px;
    border: none;
    font-weight: 700;
    font-size: 18px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}}

.btn-live:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}}
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="https://gvelazcamp.github.io/SIVO/Asistentedeviaje.png" alt="Viajes">
        <h1>SIVO Viajes</h1>
        <p>Demo interactivo - Agencia de Turismo</p>
    </div>
    
    <div class="demo-chat">
        <!-- ESCENA 1: Entrada con inspiración inmediata -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Hola, quiero viajar pero no sé a dónde</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Hola! 🌍 Te ayudo a encontrar tu viaje perfecto.<br><br>
            <strong>Decime:</strong><br>
            • ¿Playa o montaña?<br>
            • ¿Aventura o relax?<br>
            • ¿Presupuesto? (económico/medio/premium)<br>
            • ¿Cuándo querés viajar?<br><br>
            💡 <strong>Trending ahora:</strong> Bariloche nieve ❄️ | Caribe playas 🏝️ | Europa cultura 🏛️</div>
        </div>

        <!-- ESCENA 2: Recomendación personalizada con urgencia -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Playa, relax, presupuesto medio, en marzo</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Perfecto! 🏖️ Te recomiendo:<br><br>
            <strong>OPCIÓN 1 — Cancún, México 🇲🇽</strong><br>
            • Vuelo + Hotel 5★ (7 días): USD 1.200/persona<br>
            • Todo incluido (comidas + bebidas)<br>
            • Playa turquesa + vida nocturna<br>
            ⚠️ Quedan solo <strong>3 paquetes</strong> a este precio para marzo<br><br>
            <strong>OPCIÓN 2 — Punta Cana 🇩🇴</strong><br>
            • Vuelo + Resort (7 días): USD 1.350<br>
            • All inclusive premium<br>
            • Excursiones incluidas<br><br>
            <strong>OPCIÓN 3 — Florianópolis 🇧🇷</strong><br>
            • Vuelo + Hotel boutique (5 días): USD 800<br>
            • Playas paradisíacas<br>
            • Más económico, cerca<br><br>
            ¿Cuál te llama más? 😊</div>
        </div>

        <!-- ESCENA 3: Profundizar en la opción elegida -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Cancún me gusta</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Excelente elección! 🇲🇽<br><br>
            <strong>Paquete Cancún Premium incluye:</strong><br>
            ✅ Vuelos directos Buenos Aires → Cancún<br>
            ✅ Hotel 5★ frente al mar (7 noches)<br>
            ✅ All inclusive (desayuno, almuerzo, cena, bar)<br>
            ✅ Traslados aeropuerto ↔ hotel<br>
            ✅ Excursión a Chichén Itzá GRATIS<br>
            ✅ Snorkel en cenotes GRATIS<br><br>
            <strong>Salidas disponibles:</strong><br>
            • 5 de marzo → USD 1.200<br>
            • 12 de marzo → USD 1.280<br>
            • 19 de marzo → USD 1.350<br><br>
            💡 Reservando HOY: <strong>$50 USD de descuento + upgrade de habitación</strong><br><br>
            ¿Para cuántas personas es?</div>
        </div>

        <!-- ESCENA 4: Agregar valor (experiencias) -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Para 2 personas</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Perfecto! Para 2 personas: <strong>USD 2.400 total</strong> ✈️<br><br>
            <strong>¿Querés agregar experiencias VIP?</strong><br>
            🌊 Nado con delfines — USD 120/persona<br>
            🏛️ Tour privado Tulum + cenote — USD 150/persona<br>
            🍽️ Cena romántica en la playa — USD 80 para 2<br>
            🎉 Fiesta en catamarán — USD 90/persona<br><br>
            🔥 <strong>Promo:</strong> Contratando 2 experiencias → 3ra al 50% OFF<br><br>
            ¿Te sumo alguna? 😊</div>
        </div>

        <!-- ESCENA 5: Resolver objeciones (fechas/flexibilidad) -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Y si cambio las fechas después?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Buena pregunta! 🗓️<br><br>
            <strong>Opciones de flexibilidad:</strong><br>
            📌 <strong>Estándar:</strong> Cambio de fecha con 30 días anticipación — Cargo USD 100<br>
            📌 <strong>Flex:</strong> Cambio GRATIS hasta 15 días antes — +USD 150<br>
            📌 <strong>Total Flex:</strong> Cambio o cancelación hasta 48hs antes, reembolso 100% — +USD 280<br><br>
            La mayoría elige <strong>Flex</strong> para viajar tranquilo.<br>
            ¿Cuál preferís?</div>
        </div>

        <!-- ESCENA 6: Financiación (clave para cerrar) -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo pagar en cuotas?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Claro! 💳<br><br>
            <strong>Formas de pago:</strong><br>
            💵 <strong>Efectivo/Transferencia:</strong> 5% descuento adicional<br>
            💳 <strong>Tarjeta de crédito:</strong><br>
            &nbsp;&nbsp;&nbsp;• 3 cuotas sin interés<br>
            &nbsp;&nbsp;&nbsp;• 6 cuotas sin interés<br>
            &nbsp;&nbsp;&nbsp;• 12 cuotas (TNA 48%)<br>
            🌎 <strong>Mercado Pago:</strong> Hasta 18 cuotas<br><br>
            <strong>Ejemplo para 2 personas (USD 2.400):</strong><br>
            → 6 cuotas de <strong>USD 400</strong> sin interés<br>
            → 12 cuotas de <strong>USD 220</strong> c/interés<br><br>
            ¿Cómo preferís pagar?</div>
        </div>

        <!-- ESCENA 7: Documentación y requisitos -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Necesito visa para México?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">No 🎉 <strong>Argentinos NO necesitan visa para México</strong><br><br>
            <strong>Requisitos:</strong><br>
            ✅ Pasaporte válido (mínimo 6 meses)<br>
            ✅ Formulario migratorio (te lo damos)<br>
            ✅ Seguro de viaje (obligatorio, lo incluimos)<br><br>
            <strong>¿No tenés pasaporte?</strong><br>
            Te ayudamos a tramitarlo:<br>
            • Turno online → 15 días<br>
            • Entrega en 10-15 días hábiles<br><br>
            🔔 <strong>Importante:</strong> Arrancar YA para viajar en marzo.<br>
            ¿Ya tenés pasaporte vigente?</div>
        </div>

        <!-- ESCENA 8: Upsell de seguro premium -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿El seguro qué cubre?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Buena pregunta! 🛡️<br><br>
            <strong>Seguro Básico (incluido):</strong><br>
            ✅ Gastos médicos hasta USD 50.000<br>
            ✅ Equipaje perdido USD 1.000<br>
            ✅ Cancelación por enfermedad<br><br>
            <strong>Seguro Premium (+USD 80):</strong><br>
            ✅ Gastos médicos USD 150.000<br>
            ✅ COVID cubierto 100%<br>
            ✅ Deportes extremos<br>
            ✅ Equipaje USD 3.000<br>
            ✅ Cancelación por CUALQUIER motivo<br>
            ✅ Asistencia 24/7 en español<br><br>
            💡 El 70% de nuestros clientes elige <strong>Premium</strong> para viajar tranquilo.<br>
            ¿Lo sumamos?</div>
        </div>

        <!-- ESCENA 9: Crear urgencia con disponibilidad real -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Déjame pensarlo</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Perfecto! 😊 Te entiendo.<br><br>
            ⚠️ <strong>Datos importantes:</strong><br>
            • Este precio es válido solo <strong>hasta mañana 18hs</strong><br>
            • Quedan <strong>2 habitaciones</strong> disponibles para 5 de marzo<br>
            • Los vuelos directos se agotan rápido en temporada alta<br><br>
            🎁 <strong>Si reservás HOY:</strong><br>
            → Te guardamos el precio 24hs SIN pagar<br>
            → Upgrade de habitación GRATIS (vista al mar)<br>
            → Late check-out incluido<br><br>
            ¿Te lo reservo mientras pensás? (sin compromiso)</div>
        </div>

        <!-- ESCENA 10: Comparación con competencia -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Vi en otra agencia más barato</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Buenísimo que compares! 👍<br><br>
            <strong>¿Qué incluye ese otro paquete?</strong><br>
            Muchas veces no incluyen:<br>
            ❌ Traslados (USD 80)<br>
            ❌ Tasas e impuestos (USD 150)<br>
            ❌ Seguro de viaje (USD 60)<br>
            ❌ Excursiones<br><br>
            <strong>Nuestro precio INCLUYE TODO:</strong><br>
            ✅ Sin cargos ocultos<br>
            ✅ Sin sorpresas al pagar<br>
            ✅ Precio final USD 2.400<br><br>
            Pasame el link y te hago el breakdown exacto 😊<br>
            Seguro que nuestro paquete tiene más valor.</div>
        </div>

        <!-- ESCENA 11: Grupos/familias -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Somos 6 personas (4 adultos + 2 niños)</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Genial viaje en familia! 👨‍👩‍👧‍👦<br><br>
            <strong>Paquete Familiar Cancún:</strong><br>
            💰 <strong>Precio:</strong> USD 5.400 total (USD 900/adulto, niños 50% OFF)<br>
            🏨 <strong>Habitaciones:</strong> 2 conectadas con vista al mar<br>
            🍽️ <strong>All inclusive</strong> para toda la familia<br>
            🎠 <strong>Kids club</strong> incluido (4-12 años)<br><br>
            <strong>BONUS familiar:</strong><br>
            🎁 1 adulto GRATIS en grupos de 6+<br>
            🎢 Parque acuático 1 día GRATIS<br>
            📸 Sesión de fotos familiar incluida<br><br>
            ¿Los niños qué edad tienen? (importante para los servicios)</div>
        </div>

        <!-- ESCENA 12: Luna de miel / Romántico -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Es para nuestra luna de miel</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡¡¡FELICITACIONES!!! 💍🥂<br><br>
            <strong>Paquete Luna de Miel Cancún:</strong><br>
            ✨ Todo lo del paquete normal +<br>
            🍾 Champagne + fresas en la habitación<br>
            🌹 Decoración romántica (pétalos de rosa)<br>
            🍽️ Cena romántica en la playa (1 noche)<br>
            💆 Masaje de pareja en el spa<br>
            📸 Sesión de fotos profesional<br>
            🛏️ Upgrade automático a suite<br><br>
            <strong>Precio:</strong> USD 2.600 (solo USD 200 más)<br><br>
            🎁 <strong>Regalo especial:</strong> Álbum digital de la luna de miel<br><br>
            ¿Para cuándo es la boda? 😍</div>
        </div>

        <!-- ESCENA 13: Solo/aventurero -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Viajo solo, busco algo más aventura</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Perfecto! 🎒 Te armo algo épico.<br><br>
            <strong>Ruta Aventura México (10 días):</strong><br>
            🏛️ <strong>Día 1-2:</strong> CDMX (Teotihuacán, museos)<br>
            🏖️ <strong>Día 3-5:</strong> Playa del Carmen (buceo, cenotes)<br>
            🌴 <strong>Día 6-7:</strong> Tulum (ruinas, playa)<br>
            🏔️ <strong>Día 8-10:</strong> Chiapas (selva, cascadas)<br><br>
            <strong>Incluye:</strong><br>
            ✅ Vuelos internos<br>
            ✅ Hostels/hoteles<br>
            ✅ Todas las excursiones<br>
            ✅ Grupo de viajeros solos (conocés gente)<br><br>
            <strong>Precio:</strong> USD 1.800 (todo incluido)<br><br>
            ¿Te copa este estilo o preferís más playa?</div>
        </div>

        <!-- ESCENA 14: Última milla / Whatsapp -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Ok, quiero reservar</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡GENIAAAL! 🎉<br><br>
            <strong>Para confirmar necesito:</strong><br>
            📝 Datos de los pasajeros (nombre completo, DNI, fecha nac.)<br>
            📧 Email de contacto<br>
            📱 WhatsApp<br><br>
            <strong>Opciones para continuar:</strong><br>
            💬 <strong>Opción 1:</strong> Seguimos por WhatsApp (+54 9 11 1234-5678)<br>
            &nbsp;&nbsp;&nbsp;→ Te mando formulario + link de pago<br><br>
            📞 <strong>Opción 2:</strong> Te llamo en 5 minutos<br>
            &nbsp;&nbsp;&nbsp;→ Cerramos todo por teléfono<br><br>
            📧 <strong>Opción 3:</strong> Te mando todo por email<br><br>
            ¿Cuál preferís? 😊</div>
        </div>

        <!-- ESCENA 15: Post-reserva / Fidelización -->
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">Ya pagué, ¿ahora qué?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Excelente! ✅ Ya estás reservado.<br><br>
            <strong>Próximos pasos:</strong><br>
            📧 Te llega email con:<br>
            &nbsp;&nbsp;&nbsp;• Vouchers de hotel y vuelos<br>
            &nbsp;&nbsp;&nbsp;• Itinerario completo<br>
            &nbsp;&nbsp;&nbsp;• Guía de Cancún (restaurants, tips)<br>
            &nbsp;&nbsp;&nbsp;• Checklist para el viaje<br><br>
            📱 <strong>App MercadoTravel:</strong><br>
            &nbsp;&nbsp;&nbsp;• Descargala para tener todo en un lugar<br>
            &nbsp;&nbsp;&nbsp;• Itinerario interactivo<br>
            &nbsp;&nbsp;&nbsp;• Asistencia 24/7<br><br>
            🎁 <strong>Bonus viajero frecuente:</strong><br>
            En tu próximo viaje tenés 10% OFF automático.<br><br>
            ¿Alguna duda antes de viajar? ¡Que lo disfrutes! 🌴✈️</div>
        </div>
    </div>
    
    <div class="cta-demo">
        <h2>💬 ¿Querés probarlo en vivo?</h2>
        <p>Chateá con el asistente y hacele las preguntas que quieras</p>
        <a href="https://demo-viajes.streamlit.app//" target="_blank" style="text-decoration: none;">
            <button class="btn-live">🚀 Probar ahora</button>
        </a>
    </div>

    <div class="demo-back">
        <a href="?vista=asistentes">← Volver a Asistentes</a>
    </div>
</div>

{FOOTER}
"""

# Página principal con st.html
if vista == "demo":
    try:
        asistente = st.query_params.get("asistente", "futbol")
    except:
        asistente = "futbol"
    
    if asistente == "futbol":
        st.html(HTML_DEMO_FUTBOL)
    elif asistente == "cocina":
        st.html(HTML_DEMO_COCINA)
    elif asistente == "ecommerce":
        st.html(HTML_DEMO_ECOMMERCE)
    elif asistente == "finanzas":
        st.html(HTML_DEMO_FINANZAS)
    elif asistente == "ropa":
        st.html(HTML_DEMO_ROPA)
    elif asistente == "viajes":
        st.html(HTML_DEMO_VIAJES)
    elif asistente == "peluqueria":
        st.html(HTML_DEMO_PELUQUERIA)
    else:
        st.html(HTML_DEMO_FUTBOL)

elif vista == "asistentes":
    st.html(HTML_ASISTENTES)

elif vista == "precios":
    st.html(HTML_PRECIOS)

elif vista == "quehace":
    st.html(HTML_QUEHACE)

elif vista == "logout":
    st.session_state.logged_in = False
    st.session_state.user_name = ""
    st.session_state.user_email = ""
    st.query_params["vista"] = "home"
    st.rerun()

elif vista == "login":
    if st.session_state.logged_in:
        st.query_params["vista"] = "asistentes"
        st.rerun()

    # CSS login compacto
    st.markdown("""
    <style>
    .stApp, [data-testid="stAppViewContainer"], section.main, .main .block-container,
    section.main > div { background: #f5f7fa !important; }
    header[data-testid="stHeader"] { background: #f5f7fa !important; }
    .stTextInput > label { display: none !important; }
    .stTextInput > div > div > input {
        padding: 12px 14px !important; border: 1.5px solid #e0e0e0 !important;
        border-radius: 10px !important; font-size: 14px !important;
        background: #fafafa !important; font-family: Inter, sans-serif !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #60a5fa !important; background: #fff !important;
    }
    .stFormSubmitButton > button {
        width: 100% !important; padding: 12px !important;
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%) !important;
        color: white !important; border: none !important; border-radius: 12px !important;
        font-size: 15px !important; font-weight: 700 !important;
        font-family: Inter, sans-serif !important;
        box-shadow: 0 4px 15px rgba(59,130,246,0.3) !important; margin-top: 8px !important;
    }
    .stFormSubmitButton > button:hover { box-shadow: 0 6px 25px rgba(59,130,246,0.4) !important; }
    [data-testid="stForm"] { border: none !important; padding: 0 !important; margin-top: 10px !important; }
    div[data-testid="stVerticalBlock"] { gap: 0.75rem !important; }
    /* Forzar mismo ancho ambos inputs */
    .stTextInput > div, .stTextInput > div > div { width: 100% !important; background: transparent !important; }
    .stTextInput > div > div > input { width: 100% !important; box-sizing: border-box !important; }
    /* Password: el toggle del ojo no achica el input */
    .stTextInput [data-testid="stTextInputRootElement"] {
        display: flex !important; width: 100% !important; background: transparent !important;
    }
    .stTextInput [data-testid="stTextInputRootElement"] > div { flex: 1 !important; }
    .stTextInput [data-testid="stTextInputRootElement"] input { width: 100% !important; }
    .stTextInput [data-testid="stTextInputRootElement"] button {
        position: absolute !important; right: 8px !important; top: 50% !important;
        transform: translateY(-50%) !important; background: transparent !important;
        border: none !important; z-index: 2 !important;
    }
    .stTextInput [data-testid="stTextInputRootElement"] { position: relative !important; }
    /* Eliminar TODA línea/fondo/borde de contenedores internos */
    .stElementContainer, .stMarkdown, [data-testid="stMarkdownContainer"],
    .stElementContainer div, [data-testid="stForm"] div,
    .element-container, .stMarkdown div {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
        border-top: none !important;
        border-bottom: none !important;
    }
    /* La columna central ES la card */
    [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:nth-child(2) > [data-testid="stVerticalBlock"] {
        background: white !important;
        border-radius: 20px !important;
        padding: 35px 30px 28px !important;
        box-shadow: 0 8px 30px rgba(0,0,0,0.08) !important;
        margin-top: 30px !important;
    }
    /* Password input: mismo ancho visual que email (compensar ojo) */
    input[type="password"] { padding-right: 40px !important; }
    </style>
    """, unsafe_allow_html=True)

    # Centrado con columns
    _left, center_col, _right = st.columns([1, 1, 1])
    with center_col:
        st.markdown("""
        <div style="text-align:center;margin-bottom:10px;">
            <img src="https://gvelazcamp.github.io/SIVO/LogoSivo.svg" style="height:55px;margin-bottom:10px;">
            <h1 style="font-size:20px;font-weight:800;color:#111;margin:0 0 4px;font-family:Inter,sans-serif;">Bienvenido de vuelta</h1>
            <p style="font-size:13px;color:#888;margin:0;font-family:Inter,sans-serif;">Ingresá a tu cuenta para continuar</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form"):
            st.markdown('<p style="font-size:13px;font-weight:600;color:#333;margin:0 0 2px;font-family:Inter,sans-serif;">Email</p>', unsafe_allow_html=True)
            email = st.text_input("Email", placeholder="tucorreo@ejemplo.com", label_visibility="collapsed")
            st.markdown('<p style="font-size:13px;font-weight:600;color:#333;margin:8px 0 2px;font-family:Inter,sans-serif;">Contraseña</p>', unsafe_allow_html=True)
            password = st.text_input("Contraseña", type="password", placeholder="Tu contraseña", label_visibility="collapsed")
            submitted = st.form_submit_button("Iniciar sesión")

        if submitted and email:
            nombre = email.split("@")[0].replace(".", " ").replace("_", " ").title()
            st.session_state.logged_in = True
            st.session_state.user_name = nombre
            st.session_state.user_email = email
            st.query_params["vista"] = "asistentes"
            st.rerun()

        st.markdown('<div style="text-align:center;margin-top:12px;"><a href="?vista=home" style="color:#3b82f6;text-decoration:none;font-weight:600;font-size:14px;font-family:Inter,sans-serif;">← Volver al inicio</a></div>', unsafe_allow_html=True)

else:
    st.html(HTML_HOME_PARTE_1)

    # =========================
    # FIX: ANIMACIÓN DE CONTADORES (JS) PARA st.html
    # (st.html no ejecuta <script>, así que lo inyectamos vía components.html)
    # =========================
    components.html(
        """
        <script>
        (function () {
          var ran = false;

          function countTo(el, target, duration) {
            var start = null;
            function step(ts) {
              if (!start) start = ts;
              var p = Math.min((ts - start) / duration, 1);
              try { el.textContent = String(Math.floor(target * p)); } catch(e) {}
              if (p < 1) requestAnimationFrame(step);
              else try { el.textContent = String(target); } catch(e) {}
            }
            requestAnimationFrame(step);
          }

          function runAnimation(el1, el2, elA) {
            try { el1.textContent='0'; el2.textContent='0'; elA.textContent='A'; } catch(e){}
            countTo(el1, 100, 1200);
            countTo(el2, 60, 1200);
            var letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ", idx=0;
            var at = setInterval(function(){
              try {
                if(idx<letters.length){ elA.textContent=letters[idx]; idx++; }
                else { clearInterval(at); setTimeout(function(){ try{elA.textContent="ILIMITADO";}catch(e){} },200); }
              } catch(e){ clearInterval(at); }
            }, 50);
          }

          function tryRun() {
            var doc = null;
            try { doc = window.parent.document; } catch (e) { return false; }
            if (!doc) return false;

            var el1 = doc.getElementById('stat-num-1');
            var el2 = doc.getElementById('stat-num-2');
            var elA = doc.getElementById('stat-alpha');
            if (!el1 || !el2 || !elA) return false;

            // Poner en 0 desde el inicio
            try { el1.textContent='0'; el2.textContent='0'; elA.textContent='A'; } catch(e){}

            // Encontrar el contenedor stHtml que tiene los stats
            var statsContainer = el1.closest('div[data-testid="stHtml"]') || el1.parentElement;

            // Observer: cuando la sección de stats sea visible, animar
            var observer = new IntersectionObserver(function(entries) {
              entries.forEach(function(entry) {
                if (entry.isIntersecting && !ran) {
                  ran = true;
                  observer.disconnect();
                  // Primera animación
                  runAnimation(el1, el2, elA);
                  // Repetir UNA vez más
                  setTimeout(function() { runAnimation(el1, el2, elA); }, 2800);
                }
              });
            }, { threshold: 0.15 });

            observer.observe(statsContainer);
            return true;
          }

          // Reintentar hasta encontrar los elementos
          var attempts = 0;
          var t = setInterval(function () {
            attempts++;
            if (tryRun() || attempts >= 80) clearInterval(t);
          }, 150);
        })();
        </script>
        """,
        height=0,
        scrolling=False
    )
    
    components.html("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; }
    </style>
    
    <div style="width: 100%; background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%); padding: 80px 5%; margin: 0;">
        <div style="max-width: 1200px; margin: 0 auto;">
            <div style="text-align: center; margin-bottom: 50px;">
                <h2 style="font-size: 36px; font-weight: 800; margin-bottom: 15px; color: #1a1a1a; font-family: 'Inter', sans-serif;">
                    ¿Cómo responden nuestros Empleados Digitales?
                </h2>
                <p style="font-size: 18px; color: #666; font-family: 'Inter', sans-serif;">
                    Mirá conversaciones reales con clientes en diferentes industrias
                </p>
            </div>
            
            <div style="background: white; border-radius: 20px; padding: 30px; box-shadow: 0 20px 60px rgba(0,0,0,0.1);">
                <iframe 
                    src="https://gvelazcamp.github.io/SIVO/mercadobot-demo.html" 
                    style="width: 100%; height: 850px; border: none; border-radius: 15px; display: block;"
                    frameborder="0"
                    allowfullscreen>
                </iframe>
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <p style="font-size: 16px; color: #666; font-family: 'Inter', sans-serif;">
                    ⚡ Demo interactiva - Seleccioná una industria y mirá cómo responde el asistente
                </p>
            </div>
    

    <script>
    (function(){
      function apply(){
        try{
          var w = (window.parent && window.parent.innerWidth) ? window.parent.innerWidth : window.innerWidth;
          var isMobile = w <= 768;
          var iframe = window.frameElement;
          if(!iframe) return;
          var host = iframe.closest('div[data-testid="stElementContainer"]') || iframe.parentElement;
          if(!host) host = iframe;
          if(isMobile){
            host.style.display = 'none';
            host.style.height = '0px';
            host.style.margin = '0';
            host.style.padding = '0';
          } else {
            host.style.display = '';
            host.style.height = '';
            host.style.margin = '';
            host.style.padding = '';
          }
        }catch(e){}
      }
      apply();
      try { window.parent.addEventListener('resize', apply); } catch(e) {}
    })();
    </script>
    </div>
    </div>
    """, height=1100, scrolling=False)

    components.html("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: #ffffff; }
        </style>

        <div style="width: 100%; background: #ffffff; padding: 18px 14px; margin: 0;">
            <div style="max-width: 480px; margin: 0 auto; text-align: center;">
                <h2 style="font-size: 24px; font-weight: 900; letter-spacing: -0.3px; color: #111827; margin: 0;">
                    Demo WhatsApp
                </h2>
                <p style="font-size: 15px; color: #4b5563; margin: 8px 0 12px;">
                    Mirá cómo responden nuestros asistentes en tiempo real
                </p>

                <div style="max-width: 440px; margin: 0 auto;">
                    <video
                        autoplay
                        loop
                        muted
                        playsinline
                        preload="auto"
                        style="width: 100%; height: auto; display: block; border-radius: 22px; background: transparent;"
                    >
                        <source src="https://gvelazcamp.github.io/SIVO/mercadobot_whatsapp_demo-19.mp4" type="video/mp4">
                        <source src="https://raw.githubusercontent.com/gvelazcamp/SIVO/main/mercadobot_whatsapp_demo-19.mp4" type="video/mp4">
                    </video>
                </div>
            </div>
        </div>

        <script>
        (function(){
          function setFrameHeight(){
            try{
              var h = Math.max(
                document.documentElement.scrollHeight || 0,
                document.body ? document.body.scrollHeight : 0
              );
              if(window.parent && window.parent.postMessage){
                window.parent.postMessage(
                  { isStreamlitMessage: true, type: "streamlit:setFrameHeight", height: h },
                  "*"
                );
              }
            }catch(e){}
          }

          function apply(){
            try{
              var w = (window.parent && window.parent.innerWidth) ? window.parent.innerWidth : window.innerWidth;
              var isMobile = w <= 768;
              var iframe = window.frameElement;
              if(!iframe) return;
              var host = iframe.closest('div[data-testid="stElementContainer"]') || iframe.parentElement;
              if(!host) host = iframe;

              // Fondo blanco en el contenedor del componente
              try { host.style.background = '#ffffff'; } catch(e) {}

              if(!isMobile){
                host.style.display = 'none';
                host.style.height = '0px';
                host.style.margin = '0';
                host.style.padding = '0';
              } else {
                host.style.display = '';
                host.style.height = '';
                host.style.margin = '';
                host.style.padding = '';
                // Ajustar altura del iframe al contenido (evita hueco)
                setFrameHeight();
                setTimeout(setFrameHeight, 200);
                setTimeout(setFrameHeight, 800);
                setTimeout(setFrameHeight, 1500);
              }
            }catch(e){}
          }

          // Eventos
          try { window.addEventListener('load', function(){ apply(); setFrameHeight(); }); } catch(e) {}
          try { window.addEventListener('resize', function(){ apply(); setFrameHeight(); }); } catch(e) {}

          // Recalcular cuando el video esté listo
          try {
            var v = document.querySelector('video');
            if(v){
              v.addEventListener('loadedmetadata', setFrameHeight);
              v.addEventListener('canplay', setFrameHeight);
              v.addEventListener('play', setFrameHeight);
            }
          } catch(e) {}

          apply();
          try { window.parent.addEventListener('resize', apply); } catch(e) {}
        })();
        </script>
        """, height=640, scrolling=False)
    _home_partes = HTML_HOME_PARTE_2.split("<!-- INTEGRACIONES -->", 1)
    if len(_home_partes) == 2:
        st.html(_home_partes[0])
        # Slider de SIVOs (debajo de “Lo que dicen nuestros clientes”, antes de Integraciones)

        # Detectar ancho (mobile/desktop) y setear query param ?m=1/0 (una sola vez)
        components.html("""<script>
            (function() {
                try {
                    var w = window.innerWidth || document.documentElement.clientWidth || 9999;
                    var isMobile = (w <= 900) ? '1' : '0';
                    var url = new URL(window.location.href);
                    if (url.searchParams.get('m') !== isMobile) {
                        url.searchParams.set('m', isMobile);
                        window.location.replace(url.toString());
                    }
                } catch (e) {}
            })();
        </script>""", height=0)

        _m = None
        try:
            _m = st.query_params.get("m")
            if isinstance(_m, list):
                _m = _m[0] if _m else None
        except Exception:
            try:
                _m = st.experimental_get_query_params().get("m", [None])[0]
            except Exception:
                _m = None

        _is_mobile = (str(_m) == "1")

        # SOLUCIÓN MEJORADA: Usar slider responsive que se adapta automáticamente
        components.html(SIVO_SLIDER_COMPONENT_RESPONSIVE, height=(620 if _is_mobile else 780), scrolling=False)

        st.html("<!-- INTEGRACIONES -->" + _home_partes[1])
    else:
        st.html(HTML_HOME_PARTE_2)
# =========================
# SCROLL REVEAL (via components.html que SÍ ejecuta JS)
# Observa los contenedores de st.html en el documento padre
# =========================
components.html("""
<script>
(function() {
    try {
        var parentDoc = window.parent.document;
        if (!parentDoc) return;

        // Encontrar todos los contenedores de iframes st.html
        var containers = parentDoc.querySelectorAll('div[data-testid="stHtml"]');
        if (!containers || containers.length < 2) return;

        // Estilos de transición para contenedores padre
        var style = parentDoc.createElement('style');
        style.textContent = `
            .scroll-hidden {
                opacity: 0 !important;
                transform: translateY(50px) !important;
                transition: opacity 0.8s ease-out, transform 0.8s ease-out !important;
            }
            .scroll-visible {
                opacity: 1 !important;
                transform: translateY(0) !important;
            }
        `;
        parentDoc.head.appendChild(style);

        // Saltar el primer bloque (hero, ya visible) - esconder el resto
        for (var i = 1; i < containers.length; i++) {
            containers[i].classList.add('scroll-hidden');
        }

        // Observer para contenedores padre
        var observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('scroll-visible');
                    entry.target.classList.remove('scroll-hidden');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.08,
            rootMargin: '0px 0px -30px 0px'
        });

        for (var i = 1; i < containers.length; i++) {
            observer.observe(containers[i]);
        }

        // También observar contenedores de components.html
        var compContainers = parentDoc.querySelectorAll('div[data-testid="element-container"]:has(iframe[height="1100"]), div[data-testid="element-container"]:has(iframe[height="640"])');
        compContainers.forEach(function(el) {
            el.classList.add('scroll-hidden');
            observer.observe(el);
        });

    } catch(e) {
        console.log('Scroll reveal error:', e);
    }
})();
</script>
""", height=0, scrolling=False)

# CSS para overflow visible
st.markdown("""
<style>
div[data-testid="element-container"]:has(iframe[height="550"]) {
    overflow: visible !important;
}
div[data-testid="element-container"]:has(iframe[height="550"]) iframe {
    overflow: visible !important;
}
</style>
""", unsafe_allow_html=True)

# Footer con JS que auto-elimina márgenes del iframe padre
components.html(FOOTER_SIMPLE, height=250)


# Chatbot flotante COMPLETO
CHATBOT = """
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="margin:0;padding:0;overflow:visible;">

<style>
/* ============================================
   ESTILOS DEL CHATBOT - RESPONSIVE COMPLETO
============================================ */
#bot-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 15px rgba(244, 180, 0, 0.5);
    font-size: 28px;
    z-index: 999999;
    transition: transform 0.3s;
}

#bot-btn:hover {
    transform: scale(1.1);
}

#bot-box {
    display: none;
    position: fixed;
    bottom: 90px;
    right: 20px;
    width: 350px;
    height: 450px;
    background: #fff;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    flex-direction: column;
    z-index: 999998;
    overflow: hidden;
}

#bot-box.open {
    display: flex;
}

.h {
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    color: #fff;
    padding: 16px;
    border-radius: 20px 20px 0 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-shrink: 0;
}

.h h3 {
    font-size: 16px;
    font-weight: 600;
    margin: 0;
}

.h button {
    background: none;
    border: none;
    color: #fff;
    font-size: 24px;
    cursor: pointer;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    flex-shrink: 0;
}

.h button:hover {
    background: rgba(255, 255, 255, 0.2);
}

#msgs {
    flex: 1;
    overflow-y: auto;
    padding: 16px;
    background: #f8f9fa;
}

#msgs::-webkit-scrollbar {
    width: 6px;
}

#msgs::-webkit-scrollbar-thumb {
    background: #d1d5db;
    border-radius: 3px;
}

.m {
    margin-bottom: 12px;
    display: flex;
    gap: 8px;
}

.m.u {
    flex-direction: row-reverse;
}

.m .a {
    font-size: 24px;
    width: 32px;
    height: 32px;
    flex-shrink: 0;
}

.m .b {
    max-width: calc(100% - 50px);
    padding: 10px 14px;
    border-radius: 16px;
    font-size: 14px;
    line-height: 1.4;
    word-wrap: break-word;
    overflow-wrap: break-word;
}

.m:not(.u) .b {
    background: #fff;
    border: 1px solid #e9ecef;
    color: #333;
}

.m.u .b {
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    color: #fff;
}

.inp {
    padding: 12px;
    background: #fff;
    border-top: 1px solid #e9ecef;
    display: flex;
    gap: 8px;
    flex-shrink: 0;
}

.inp input {
    flex: 1;
    padding: 10px 16px;
    border: 1px solid #e0e0e0;
    border-radius: 20px;
    font-size: 14px;
    outline: none;
    min-width: 0;
}

.inp input:focus {
    border-color: #f4b400;
}

.inp button {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: linear-gradient(135deg, #f4b400, #ff6b00);
    border: none;
    cursor: pointer;
    font-size: 18px;
    color: #fff;
    flex-shrink: 0;
}

.clickable-option {
    cursor: pointer;
    color: #f4b400;
    text-decoration: none;
    display: inline-block;
    padding: 4px 0;
    transition: all 0.2s;
}

.clickable-option:hover {
    color: #ff6b00;
    transform: translateX(4px);
}

/* ============================================
   RESPONSIVE PARA MÓVILES (CRÍTICO)
============================================ */
@media (max-width: 768px) {
    #bot-btn {
        width: 56px !important;
        height: 56px !important;
        bottom: 16px !important;
        right: 16px !important;
        font-size: 26px !important;
    }
    
    #bot-box {
        bottom: 0 !important;
        right: 0 !important;
        left: 0 !important;
        top: 0 !important;
        width: 100vw !important;
        max-width: 100vw !important;
        height: 100vh !important;
        max-height: 100vh !important;
        border-radius: 0 !important;
        margin: 0 !important;
    }
    
    .h {
        padding: 14px 16px !important;
        border-radius: 0 !important;
    }
    
    .h h3 {
        font-size: 16px !important;
    }
    
    #msgs {
        padding: 16px 12px !important;
    }
    
    .m .a {
        width: 28px !important;
        height: 28px !important;
        font-size: 20px !important;
    }
    
    .m .b {
        padding: 10px 14px !important;
        font-size: 14px !important;
        max-width: calc(100% - 48px) !important;
    }
    
    .inp {
        padding: 12px !important;
        gap: 8px !important;
    }
    
    .inp input {
        padding: 10px 14px !important;
        font-size: 15px !important;
    }
    
    .inp button {
        width: 40px !important;
        height: 40px !important;
        font-size: 18px !important;
    }
}

@media (max-width: 400px) {
    .m .b {
        font-size: 13px !important;
        padding: 9px 12px !important;
    }
    
    .inp input {
        font-size: 14px !important;
        padding: 9px 12px !important;
    }
}
</style>

<button id="bot-btn" onclick="toggle()">💬</button>

<div id="bot-box">
<div class="h"><h3>🤖 SIVO</h3><button onclick="toggle()">×</button></div>
<div id="msgs">
<div class="m"><div class="a">🤖</div><div class="b">¡Hola! 👋 Soy SIVO, tu asistente virtual. ¿En qué puedo ayudarte hoy?<br><br>Puedo contarte sobre:<br><span class="clickable-option" onclick="sendOption('Qué es SIVO')">• Qué es SIVO</span><br><span class="clickable-option" onclick="sendOption('Precios y planes')">• Precios y planes</span><br><span class="clickable-option" onclick="sendOption('Integraciones')">• Integraciones</span><br><span class="clickable-option" onclick="sendOption('Cómo funciona')">• Cómo funciona</span></div></div>
</div>
<div class="inp">
<input id="in" placeholder="Escribe tu mensaje..." onkeypress="if(event.key==='Enter')send()">
<button onclick="send()">📤</button>
</div>
</div>

<script>
function toggle(){document.getElementById('bot-box').classList.toggle('open');}
function add(t,u){var m=document.getElementById('msgs'),d=document.createElement('div');d.className='m'+(u?' u':'');d.innerHTML='<div class="a">'+(u?'👤':'🤖')+'</div><div class="b">'+t+'</div>';m.appendChild(d);m.scrollTop=m.scrollHeight;}

// Función para enviar opciones clickeables
function sendOption(text){
    document.getElementById('in').value = text;
    send();
}

function send(){
    var i=document.getElementById('in'),msg=i.value.trim();
    if(!msg)return;
    add(msg,true);
    i.value='';
    
    setTimeout(function(){
        var l=msg.toLowerCase(),r;
        
        // 1. Saludos
        if(l.includes('hola')||l.includes('buenos')||l.includes('buenas')||l.includes('hey'))
            r='¡Hola! 👋 Soy SIVO, tu asistente virtual. ¿En qué puedo ayudarte hoy?<br><br>Puedo contarte sobre:<br>• Qué es SIVO<br>• Precios y planes<br>• Integraciones<br>• Cómo funciona';
        
        // 2. ¿Qué es SIVO?
        else if(l.includes('que es')||l.includes('qué es')||l.includes('sivo'))
            r='<strong>SIVO</strong> es una plataforma de chatbots con IA que automatiza tu atención al cliente 24/7. 🤖<br><br>✅ Responde consultas automáticamente<br>✅ Aumenta conversiones<br>✅ Libera tiempo de tu equipo<br>✅ Se integra con tus sistemas<br><br>¿Te gustaría conocer los precios?';
        
        // 3. Precios
        else if(l.includes('precio')||l.includes('costo')||l.includes('cuanto')||l.includes('plan'))
            r='💰 <strong>Nuestros Planes:</strong><br><br><strong>Implementación inicial - US$ 250</strong><br>• Pago único<br>• 1 asistente · 1 sitio<br>• Creación del asistente IA<br>• Conexión a base de datos<br>• Instalación en web<br><br><strong>PRO - US$ 100/mes</strong><br>• 1 asistente · 1 sitio<br>• Asistentes entrenados con tus datos<br>• Ajustes y mejoras mensuales<br>• Soporte prioritario<br><br><strong>ENTERPRISE - A medida/mes</strong><br>• Asistentes ilimitados<br>• Multi-sitio<br>• Soporte dedicado<br><br>🎁 <strong>7 días gratis</strong> para probar!';
        
        // 4. Integraciones
        else if(l.includes('integra')||l.includes('whatsapp')||l.includes('instagram')||l.includes('plataforma'))
            r='🔌 <strong>Integraciones disponibles:</strong><br><br>✅ WhatsApp<br>✅ Instagram<br>✅ Web (widget)<br>✅ Shopify<br>✅ Mercado Pago<br>✅ Email<br>✅ API personalizada<br><br>¿Cuál te interesa más?';
        
        // 5. ¿Cómo funciona?
        else if(l.includes('funciona')||l.includes('como')||l.includes('cómo'))
            r='⚙️ <strong>Es súper simple:</strong><br><br>1️⃣ <strong>Conectás</strong> tus datos y productos<br>2️⃣ <strong>Entrenamos</strong> el asistente con tu info<br>3️⃣ <strong>Instalamos</strong> en tus canales<br>4️⃣ <strong>Listo!</strong> Empieza a atender clientes<br><br>Todo el proceso lleva entre 2-7 días. ⚡';
        
        // 6. Demo
        else if(l.includes('demo')||l.includes('prueba')||l.includes('probar'))
            r='🎯 <strong>¡Probá SIVO GRATIS!</strong><br><br>✅ 7 días sin compromiso<br>✅ No necesitás tarjeta<br>✅ Acceso completo<br><br>Para empezar:<br>📧 Escribinos a <strong>hola@sivo.com</strong><br>📅 O agendá tu demo personalizada<br><br>¿Empezamos?';
        
        // 7. Contacto
        else if(l.includes('contacto')||l.includes('email')||l.includes('hablar')||l.includes('asesor'))
            r='📞 <strong>Contactanos por:</strong><br><br>📧 Email: <strong>hola@sivo.com</strong><br>💬 Chat: ¡Estás hablando conmigo! 😊<br>📱 WhatsApp: +54 9 11 1234-5678<br><br>⏰ Respondemos en menos de 24hs';
        
        // 8. Cancelación
        else if(l.includes('cancelar')||l.includes('permanencia')||l.includes('contrato'))
            r='✅ <strong>Sin permanencia ni compromisos:</strong><br><br>• Cancelás cuando quieras<br>• Sin penalizaciones<br>• Proceso simple y rápido<br>• 100% transparente<br><br>Queremos que te quedes porque funciona, no por obligación. 💯';
        
        // 9. ¿Necesito programar?
        else if(l.includes('programa')||l.includes('tecnic')||l.includes('código')||l.includes('codigo'))
            r='🎉 <strong>¡NO necesitás saber programar!</strong><br><br>Nosotros nos encargamos de TODO:<br>✅ Instalación completa<br>✅ Configuración<br>✅ Entrenamiento del bot<br>✅ Integraciones<br>✅ Soporte continuo<br><br>Vos solo nos pasás tu información y listo! 🚀';
        
        // 10. Tiempo de implementación
        else if(l.includes('tiempo')||l.includes('demora')||l.includes('rapido')||l.includes('rápido'))
            r='⚡ <strong>Tiempos de implementación:</strong><br><br><strong>Casos simples:</strong> 2-3 días<br>• Chatbot básico con info estándar<br><br><strong>Casos complejos:</strong> 1-2 semanas<br>• Múltiples integraciones<br>• Datos complejos<br><br>Te damos un timeline claro desde el inicio. 📅';
        
        // 11. Seguridad
        else if(l.includes('segur')||l.includes('dato')||l.includes('privacidad'))
            r='🔒 <strong>Tu información 100% protegida:</strong><br><br>✅ Encriptación de datos<br>✅ Cumplimos GDPR y normativas locales<br>✅ Servidores seguros<br>✅ Acceso restringido<br>✅ Backups diarios<br><br>Tanto tus datos como los de tus clientes están seguros. 💯';
        
        // 12. IA y personalización
        else if(l.includes('ia')||l.includes('inteligencia')||l.includes('personali'))
            r='🧠 <strong>IA Conversacional Avanzada:</strong><br><br>✅ Entiende lenguaje natural<br>✅ Aprende de cada conversación<br>✅ Se personaliza 100% a tu negocio<br>✅ Mejora continuamente<br><br>No es un bot con respuestas rígidas, es una IA que conversa naturalmente. 🤖';
        
        // 13. Idiomas
        else if(l.includes('idioma')||l.includes('lenguaje')||l.includes('inglés')||l.includes('ingles'))
            r='🌎 <strong>Soporte multiidioma:</strong><br><br>✅ Español<br>✅ Inglés<br>✅ Portugués<br>✅ Otros bajo pedido<br><br>El bot puede detectar el idioma automáticamente y responder en el idioma del cliente. 🗣️';
        
        // 14. Casos de uso
        else if(l.includes('uso')||l.includes('industria')||l.includes('rubro')||l.includes('ejemplo'))
            r='💼 <strong>Casos de uso exitosos:</strong><br><br>🛍️ E-commerce: Consultas de productos<br>💈 Servicios: Agendar turnos<br>🏨 Hotelería: Reservas y consultas<br>🏥 Salud: Info y turnos<br>📚 Educación: Inscripciones<br>🍕 Gastronomía: Pedidos<br><br>¿Cuál es tu rubro?';
        
        // 15. Ventajas vs competencia
        else if(l.includes('ventaja')||l.includes('mejor')||l.includes('diferencia')||l.includes('competencia'))
            r='⭐ <strong>Por qué elegir SIVO:</strong><br><br>✅ Setup en días, no meses<br>✅ IA más natural y conversacional<br>✅ Soporte en español 24/7<br>✅ Integraciones nativas<br>✅ Precio accesible<br>✅ Sin letra chica<br><br>Probalo gratis y compará! 🚀';
        
        // 16. Analíticas
        else if(l.includes('analitica')||l.includes('reporte')||l.includes('estadistica')||l.includes('métrica'))
            r='📊 <strong>Dashboard con métricas en tiempo real:</strong><br><br>✅ Cantidad de conversaciones<br>✅ Tasa de resolución<br>✅ Horarios pico<br>✅ Consultas frecuentes<br>✅ Satisfacción del cliente<br>✅ Reportes exportables<br><br>Todo desde un panel intuitivo. 📈';
        
        // 17. Escalabilidad
        else if(l.includes('escala')||l.includes('crecer')||l.includes('grande')||l.includes('volumen'))
            r='📈 <strong>Escala con tu negocio:</strong><br><br>• Empieza con 1.000 consultas/mes<br>• Crece hasta ilimitado<br>• Sin interrupciones<br>• Mismo servicio premium<br><br>De startup a enterprise, te acompañamos en todo el camino. 🚀';
        
        // 18. Soporte
        else if(l.includes('soporte')||l.includes('ayuda')||l.includes('asistencia'))
            r='🆘 <strong>Soporte que realmente ayuda:</strong><br><br>📧 Email: Respuesta en 24hs<br>💬 Chat: Respuesta inmediata<br>📞 Llamada: Para clientes Pro y Enterprise<br>📚 Documentación completa<br>🎥 Video tutoriales<br><br>Nunca te dejamos solo. 🤝';
        
        // 19. Actualizaciones
        else if(l.includes('actualiza')||l.includes('mejora')||l.includes('nuevo'))
            r='🆕 <strong>Mejoras constantes incluidas:</strong><br><br>✅ Actualizaciones automáticas<br>✅ Nuevas funciones sin costo extra<br>✅ Mejoras de IA continuas<br>✅ Nuevas integraciones<br><br>Tu plan siempre incluye lo más nuevo. Sin sorpresas. 🎁';
        
        // 20. Despedida
        else if(l.includes('gracias'))
            r='¡De nada! 😊 Estoy acá para ayudarte.<br><br>¿Algo más que quieras saber sobre SIVO?';
        else if(l.includes('chau')||l.includes('adios')||l.includes('bye'))
            r='¡Hasta pronto! 👋<br><br>Si tenés más dudas, acá estoy 24/7. También podés escribirnos a <strong>hola@sivo.com</strong>';
        
        // Default
        else
            r='🤔 Interesante pregunta. Podés consultarme sobre:<br><br>• Qué es SIVO<br>• Precios y planes<br>• Integraciones disponibles<br>• Cómo funciona<br>• Demo gratuita<br><br>O escribinos a <strong>hola@sivo.com</strong> para consultas específicas.';
        
        add(r,false);
    },500);
}

// TELEPORT: Mover el chatbot al body principal de la página
(function teleport() {
    try {
        const parentDoc = window.parent.document;
        const btn = document.getElementById('bot-btn');
        const box = document.getElementById('bot-box');
        
        if (btn && box && parentDoc && parentDoc.body) {
            // Clonar y agregar al body principal
            const btnClone = btn.cloneNode(true);
            const boxClone = box.cloneNode(true);
            
            // Agregar al body principal (fuera del iframe)
            parentDoc.body.appendChild(btnClone);
            parentDoc.body.appendChild(boxClone);
            
            // Ocultar originales
            btn.style.display = 'none';
            box.style.display = 'none';
            
            // Re-conectar eventos en los clones
            btnClone.onclick = () => boxClone.classList.toggle('open');
            boxClone.querySelector('.h button').onclick = () => boxClone.classList.toggle('open');
            
            const inputClone = boxClone.querySelector('#in');
            const sendFunc = () => {
                const msg = inputClone.value.trim();
                if (!msg) return;
                const msgsDiv = boxClone.querySelector('#msgs');
                const addMsg = (t,u) => {
                    const d = parentDoc.createElement('div');
                    d.className = 'm' + (u?' u':'');
                    d.innerHTML = '<div class="a">' + (u?'👤':'🤖') + '</div><div class="b">' + t + '</div>';
                    msgsDiv.appendChild(d);
                    msgsDiv.scrollTop = msgsDiv.scrollHeight;
                };
                addMsg(msg, true);
                inputClone.value = '';
                setTimeout(() => {
                    const l = msg.toLowerCase();
                    let r;
                    if(l.includes('hola')||l.includes('buenos')||l.includes('buenas')||l.includes('hey')) r='¡Hola! 👋 Soy SIVO, tu asistente virtual. ¿En qué puedo ayudarte hoy?<br><br>Puedo contarte sobre:<br>• Qué es SIVO<br>• Precios y planes<br>• Integraciones<br>• Cómo funciona';
                    else if(l.includes('que es')||l.includes('qué es')||l.includes('sivo')) r='<strong>SIVO</strong> es una plataforma de chatbots con IA que automatiza tu atención al cliente 24/7. 🤖<br><br>✅ Responde consultas automáticamente<br>✅ Aumenta conversiones<br>✅ Libera tiempo de tu equipo<br>✅ Se integra con tus sistemas<br><br>¿Te gustaría conocer los precios?';
                    else if(l.includes('precio')||l.includes('costo')||l.includes('cuanto')||l.includes('plan')) r='💰 <strong>Nuestros Planes:</strong><br><br><strong>Implementación inicial - US$ 250</strong><br>• Pago único<br>• 1 asistente · 1 sitio<br>• Creación del asistente IA<br>• Conexión a base de datos<br>• Instalación en web<br><br><strong>PRO - US$ 100/mes</strong><br>• 1 asistente · 1 sitio<br>• Asistentes entrenados con tus datos<br>• Ajustes y mejoras mensuales<br>• Soporte prioritario<br><br><strong>ENTERPRISE - A medida/mes</strong><br>• Asistentes ilimitados<br>• Multi-sitio<br>• Soporte dedicado<br><br>🎁 <strong>7 días gratis</strong> para probar!';
                    else if(l.includes('integra')||l.includes('whatsapp')||l.includes('instagram')||l.includes('plataforma')) r='🔌 <strong>Integraciones disponibles:</strong><br><br>✅ WhatsApp<br>✅ Instagram<br>✅ Web (widget)<br>✅ Shopify<br>✅ Mercado Pago<br>✅ Email<br>✅ API personalizada<br><br>¿Cuál te interesa más?';
                    else if(l.includes('funciona')||l.includes('como')||l.includes('cómo')) r='⚙️ <strong>Es súper simple:</strong><br><br>1️⃣ <strong>Conectás</strong> tus datos y productos<br>2️⃣ <strong>Entrenamos</strong> el asistente con tu info<br>3️⃣ <strong>Instalamos</strong> en tus canales<br>4️⃣ <strong>Listo!</strong> Empieza a atender clientes<br><br>Todo el proceso lleva entre 2-7 días. ⚡';
                    else if(l.includes('demo')||l.includes('prueba')||l.includes('probar')) r='🎯 <strong>¡Probá SIVO GRATIS!</strong><br><br>✅ 7 días sin compromiso<br>✅ No necesitás tarjeta<br>✅ Acceso completo<br><br>Para empezar:<br>📧 Escribinos a <strong>hola@sivo.com</strong><br>📅 O agendá tu demo personalizada<br><br>¿Empezamos?';
                    else if(l.includes('contacto')||l.includes('email')||l.includes('hablar')||l.includes('asesor')) r='📞 <strong>Contactanos por:</strong><br><br>📧 Email: <strong>hola@sivo.com</strong><br>💬 Chat: ¡Estás hablando conmigo! 😊<br>📱 WhatsApp: +54 9 11 1234-5678<br><br>⏰ Respondemos en menos de 24hs';
                    else if(l.includes('cancelar')||l.includes('permanencia')||l.includes('contrato')) r='✅ <strong>Sin permanencia ni compromisos:</strong><br><br>• Cancelás cuando quieras<br>• Sin penalizaciones<br>• Proceso simple y rápido<br>• 100% transparente<br><br>Queremos que te quedes porque funciona, no por obligación. 💯';
                    else if(l.includes('programa')||l.includes('tecnic')||l.includes('código')||l.includes('codigo')) r='🎉 <strong>¡NO necesitás saber programar!</strong><br><br>Nosotros nos encargamos de TODO:<br>✅ Instalación completa<br>✅ Configuración<br>✅ Entrenamiento del bot<br>✅ Integraciones<br>✅ Soporte continuo<br><br>Vos solo nos pasás tu información y listo! 🚀';
                    else if(l.includes('tiempo')||l.includes('demora')||l.includes('rapido')||l.includes('rápido')) r='⚡ <strong>Tiempos de implementación:</strong><br><br><strong>Casos simples:</strong> 2-3 días<br>• Chatbot básico con info estándar<br><br><strong>Casos complejos:</strong> 1-2 semanas<br>• Múltiples integraciones<br>• Datos complejos<br><br>Te damos un timeline claro desde el inicio. 📅';
                    else if(l.includes('segur')||l.includes('dato')||l.includes('privacidad')) r='🔒 <strong>Tu información 100% protegida:</strong><br><br>✅ Encriptación de datos<br>✅ Cumplimos GDPR y normativas locales<br>✅ Servidores seguros<br>✅ Acceso restringido<br>✅ Backups diarios<br><br>Tanto tus datos como los de tus clientes están seguros. 💯';
                    else if(l.includes('ia')||l.includes('inteligencia')||l.includes('personali')) r='🧠 <strong>IA Conversacional Avanzada:</strong><br><br>✅ Entiende lenguaje natural<br>✅ Aprende de cada conversación<br>✅ Se personaliza 100% a tu negocio<br>✅ Mejora continuamente<br><br>No es un bot con respuestas rígidas, es una IA que conversa naturalmente. 🤖';
                    else if(l.includes('idioma')||l.includes('lenguaje')||l.includes('inglés')||l.includes('ingles')) r='🌎 <strong>Soporte multiidioma:</strong><br><br>✅ Español<br>✅ Inglés<br>✅ Portugués<br>✅ Otros bajo pedido<br><br>El bot puede detectar el idioma automáticamente y responder en el idioma del cliente. 🗣️';
                    else if(l.includes('uso')||l.includes('industria')||l.includes('rubro')||l.includes('ejemplo')) r='💼 <strong>Casos de uso exitosos:</strong><br><br>🛍️ E-commerce: Consultas de productos<br>💈 Servicios: Agendar turnos<br>🏨 Hotelería: Reservas y consultas<br>🏥 Salud: Info y turnos<br>📚 Educación: Inscripciones<br>🍕 Gastronomía: Pedidos<br><br>¿Cuál es tu rubro?';
                    else if(l.includes('ventaja')||l.includes('mejor')||l.includes('diferencia')||l.includes('competencia')) r='⭐ <strong>Por qué elegir SIVO:</strong><br><br>✅ Setup en días, no meses<br>✅ IA más natural y conversacional<br>✅ Soporte en español 24/7<br>✅ Integraciones nativas<br>✅ Precio accesible<br>✅ Sin letra chica<br><br>Probalo gratis y compará! 🚀';
                    else if(l.includes('analitica')||l.includes('reporte')||l.includes('estadistica')||l.includes('métrica')) r='📊 <strong>Dashboard con métricas en tiempo real:</strong><br><br>✅ Cantidad de conversaciones<br>✅ Tasa de resolución<br>✅ Horarios pico<br>✅ Consultas frecuentes<br>✅ Satisfacción del cliente<br>✅ Reportes exportables<br><br>Todo desde un panel intuitivo. 📈';
                    else if(l.includes('escala')||l.includes('crecer')||l.includes('grande')||l.includes('volumen')) r='📈 <strong>Escala con tu negocio:</strong><br><br>• Empieza con 1.000 consultas/mes<br>• Crece hasta ilimitado<br>• Sin interrupciones<br>• Mismo servicio premium<br><br>De startup a enterprise, te acompañamos en todo el camino. 🚀';
                    else if(l.includes('soporte')||l.includes('ayuda')||l.includes('asistencia')) r='🆘 <strong>Soporte que realmente ayuda:</strong><br><br>📧 Email: Respuesta en 24hs<br>💬 Chat: Respuesta inmediata<br>📞 Llamada: Para clientes Pro y Enterprise<br>📚 Documentación completa<br>🎥 Video tutoriales<br><br>Nunca te dejamos solo. 🤝';
                    else if(l.includes('actualiza')||l.includes('mejora')||l.includes('nuevo')) r='🆕 <strong>Mejoras constantes incluidas:</strong><br><br>✅ Actualizaciones automáticas<br>✅ Nuevas funciones sin costo extra<br>✅ Mejoras de IA continuas<br>✅ Nuevas integraciones<br><br>Tu plan siempre incluye lo más nuevo. Sin sorpresas. 🎁';
                    else if(l.includes('gracias')) r='¡De nada! 😊 Estoy acá para ayudarte.<br><br>¿Algo más que quieras saber sobre SIVO?';
                    else if(l.includes('chau')||l.includes('adios')||l.includes('bye')) r='¡Hasta pronto! 👋<br><br>Si tenés más dudas, acá estoy 24/7. También podés escribirnos a <strong>hola@sivo.com</strong>';
                    else r='🤔 Interesante pregunta. Podés consultarme sobre:<br><br>• Qué es SIVO<br>• Precios y planes<br>• Integraciones disponibles<br>• Cómo funciona<br>• Demo gratuita<br><br>O escribinos a <strong>hola@sivo.com</strong> para consultas específicas.';
                    addMsg(r, false);
                }, 500);
            };
            inputClone.onkeypress = (e) => { if (e.key === 'Enter') sendFunc(); };
            inputClone.onkeypress = (e) => { if (e.key === 'Enter') sendFunc(); };
            boxClone.querySelector('.inp button').onclick = sendFunc;
            
            // Función sendOption para opciones clickeables en el clon
            const sendOptionFunc = (text) => {
                inputClone.value = text;
                sendFunc();
            };
            
            // Reconectar eventos de opciones clickeables
            boxClone.querySelectorAll('.clickable-option').forEach(option => {
                const optionText = option.textContent.trim();
                option.onclick = () => sendOptionFunc(optionText);
            });
            
            // Copiar estilos al documento principal
            const style = parentDoc.createElement('style');
            style.textContent = document.querySelector('style').textContent;
            parentDoc.head.appendChild(style);
        }
    } catch (e) {
        console.log('Teleport failed:', e);
    }
})();
</script>

</script>

</body>
</html>
"""

# CSS RESPONSIVE ADICIONAL PARA MÓVILES
st.markdown("""
<style>

/* ============================================
   CSS RESPONSIVE PARA CHATBOT EN MÓVILES
   (Aplicado al documento principal de Streamlit)
============================================ */

/* Responsive para móviles */
@media (max-width: 768px) {
    /* Botón del chatbot más pequeño */
    #bot-btn {
        width: 56px !important;
        height: 56px !important;
        bottom: 16px !important;
        right: 16px !important;
        font-size: 26px !important;
    }
    
    /* Chatbot FULLSCREEN en móviles */
    #bot-box {
        position: fixed !important;
        bottom: 0 !important;
        right: 0 !important;
        left: 0 !important;
        top: 0 !important;
        width: 100vw !important;
        max-width: 100vw !important;
        height: 100vh !important;
        max-height: 100vh !important;
        border-radius: 0 !important;
        margin: 0 !important;
    }
    
    /* Header sin border-radius en móvil */
    #bot-box .h {
        padding: 14px 16px !important;
        border-radius: 0 !important;
    }
    
    #bot-box .h h3 {
        font-size: 16px !important;
    }
    
    /* Mensajes con menos padding */
    #bot-box #msgs {
        padding: 16px 12px !important;
    }
    
    /* Avatares más pequeños */
    #bot-box .m .a {
        width: 28px !important;
        height: 28px !important;
        font-size: 20px !important;
    }
    
    /* Mensajes con ancho ajustado */
    #bot-box .m .b {
        padding: 10px 14px !important;
        font-size: 14px !important;
        max-width: calc(100% - 48px) !important;
    }
    
    /* Input más compacto */
    #bot-box .inp {
        padding: 12px !important;
        gap: 8px !important;
    }
    
    #bot-box .inp input {
        padding: 10px 14px !important;
        font-size: 15px !important;
    }
    
    #bot-box .inp button {
        width: 40px !important;
        height: 40px !important;
        font-size: 18px !important;
    }
}

/* Para pantallas MUY pequeñas */
@media (max-width: 400px) {
    #bot-box .m .b {
        font-size: 13px !important;
        padding: 9px 12px !important;
    }
    
    #bot-box .inp input {
        font-size: 14px !important;
        padding: 9px 12px !important;
    }
}

</style>
""", unsafe_allow_html=True)

# CSS para que el iframe del chatbot NO ocupe espacio visual
st.markdown("""
<style>
/* Ocultar el contenedor del iframe */
div[data-testid="stVerticalBlock"]:has(iframe[height="0"]),
div[data-testid="element-container"]:has(iframe[height="0"]) {
    height: 0 !important;
    overflow: visible !important;
    margin: 0 !important;
    padding: 0 !important;
    display: block !important;
}

/* El iframe en sí */
iframe[height="0"] {
    position: fixed !important;
    bottom: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 100vh !important;
    border: none !important;
    pointer-events: none !important;
    z-index: 999999 !important;
}

iframe[height="0"] * {
    pointer-events: auto !important;
}
</style>
""", unsafe_allow_html=True)

components.html(CHATBOT, height=0)
