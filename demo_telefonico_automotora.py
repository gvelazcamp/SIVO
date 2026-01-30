import streamlit as st
import streamlit.components.v1 as components

# ==========================================================
# MERCADOBOT - UI (fondo blanco + tarjetas con acento naranja)
# Cambios: SOLO CSS (fondo blanco + tarjetas: 1ra y última naranja)
# ==========================================================

st.set_page_config(
    page_title="MercadoBot",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# FULL WIDTH STREAMLIT
# =========================
st.markdown(
    """
    <style>
    /* =========================
       RESET STREAMLIT / FULL WIDTH
       ========================= */

    /* Eliminar TODO el padding y margin de Streamlit */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    section[data-testid="stAppViewContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
        background: #ffffff !important;
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
        background: #ffffff !important;
    }

    /* =========================
       TIPOGRAFÍA / PALETA
       ========================= */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    :root{
        --mb-blue: #0b3b60;
        --mb-blue2: #1677c7;
        --mb-sky: #4bb3ff;
        --mb-ink: #0b1220;
        --mb-muted: #5b6b7a;
        --mb-border: #e6eaf0;

        --mb-orange: #ff7a18;
        --mb-orange2:#ffb347;
        --mb-orange-soft:#fff3e8;

        --mb-bg: #ffffff;
        --mb-bg2: #f6f8fb;
    }

    body{
        font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif !important;
        background: var(--mb-bg) !important;
        color: var(--mb-ink) !important;
    }

    /* =========================
       LAYOUT GENERAL EN HTML
       ========================= */
    .mb-page{
        width: 100%;
        background: var(--mb-bg);
    }

    .mb-container{
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 18px;
    }

    /* =========================
       NAVBAR
       ========================= */
    .mb-nav{
        position: sticky;
        top: 0;
        z-index: 50;
        width: 100%;
        background: rgba(255,255,255,.92);
        border-bottom: 1px solid var(--mb-border);
        backdrop-filter: blur(10px);
    }

    .mb-nav-inner{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 0;
        gap: 14px;
    }

    .mb-brand{
        display:flex;
        align-items:center;
        gap: 10px;
        text-decoration:none;
        color: var(--mb-blue);
        font-weight: 800;
        letter-spacing: .4px;
        font-size: 18px;
    }

    .mb-links{
        display:flex;
        align-items:center;
        gap: 14px;
        flex-wrap: wrap;
    }

    .mb-link{
        text-decoration: none;
        color: var(--mb-muted);
        font-weight: 600;
        font-size: 14px;
        padding: 8px 10px;
        border-radius: 10px;
    }

    .mb-link:hover{
        background: var(--mb-bg2);
        color: var(--mb-blue);
    }

    .mb-login{
        text-decoration:none;
        font-weight: 700;
        font-size: 14px;
        padding: 10px 14px;
        border-radius: 12px;
        color: #fff;
        background: linear-gradient(135deg, var(--mb-blue) 0%, var(--mb-blue2) 100%);
        box-shadow: 0 10px 25px rgba(11,59,96,.18);
        white-space: nowrap;
    }

    /* =========================
       HERO
       ========================= */
    .mb-hero{
        padding: 64px 0 44px 0;
        background:
          radial-gradient(900px 380px at 10% -10%, rgba(75,179,255,.16), transparent 60%),
          radial-gradient(900px 380px at 90% -10%, rgba(11,59,96,.12), transparent 60%),
          linear-gradient(180deg, #ffffff 0%, #ffffff 65%, var(--mb-bg2) 100%);
        border-bottom: 1px solid var(--mb-border);
    }

    .mb-hero-grid{
        display: grid;
        grid-template-columns: 1.25fr .75fr;
        gap: 22px;
        align-items: center;
    }

    .hero-title{
        margin: 0 0 10px 0;
        font-size: 44px;
        line-height: 1.05;
        color: var(--mb-blue);
        letter-spacing: -.8px;
    }

    .hero-subtitle{
        margin: 0 0 18px 0;
        color: var(--mb-muted);
        font-size: 16px;
        line-height: 1.5;
        max-width: 56ch;
    }

    .hero-impact{
        margin: 0 0 20px 0;
        font-size: 18px;
        font-weight: 800;
        color: var(--mb-blue);
    }

    .hero-impact span{
        display:block;
        margin-top: 6px;
        font-size: 14px;
        font-weight: 600;
        color: var(--mb-muted);
    }

    .hero-actions{
        display:flex;
        gap: 12px;
        flex-wrap: wrap;
        margin-top: 8px;
    }

    .btn{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        gap: 10px;
        padding: 12px 16px;
        border-radius: 14px;
        font-weight: 800;
        text-decoration: none;
        font-size: 14px;
        border: 1px solid transparent;
        cursor: pointer;
        transition: transform .12s ease, box-shadow .12s ease, background .12s ease;
        white-space: nowrap;
    }

    .btn:active{ transform: translateY(1px); }

    .btn-primary{
        color:#fff;
        background: linear-gradient(135deg, var(--mb-orange) 0%, var(--mb-orange2) 100%);
        box-shadow: 0 14px 28px rgba(255,122,24,.22);
    }

    .btn-primary:hover{
        box-shadow: 0 18px 34px rgba(255,122,24,.26);
        transform: translateY(-1px);
    }

    .btn-outline{
        color: var(--mb-blue);
        background: #ffffff;
        border-color: var(--mb-border);
        box-shadow: 0 12px 24px rgba(11,59,96,.10);
    }

    .btn-outline:hover{
        border-color: rgba(255,122,24,.45);
        box-shadow: 0 16px 30px rgba(11,59,96,.12);
        transform: translateY(-1px);
    }

    .mb-hero-side{
        background: #ffffff;
        border: 1px solid var(--mb-border);
        border-radius: 20px;
        padding: 16px;
        box-shadow: 0 18px 40px rgba(11,59,96,.10);
    }

    .mb-badges{
        display:flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 10px;
    }

    .badge{
        font-weight: 800;
        font-size: 12px;
        padding: 8px 10px;
        border-radius: 999px;
        color: var(--mb-blue);
        background: var(--mb-bg2);
        border: 1px solid var(--mb-border);
    }

    /* =========================
       SECCIONES
       ========================= */
    .mb-section{
        padding: 44px 0;
        background: #ffffff;
    }

    .mb-section.alt{
        background: var(--mb-bg2);
        border-top: 1px solid var(--mb-border);
        border-bottom: 1px solid var(--mb-border);
    }

    .section-title{
        margin: 0 0 10px 0;
        font-size: 22px;
        font-weight: 900;
        color: var(--mb-blue);
        letter-spacing: -.2px;
    }

    .section-subtitle{
        margin: 0 0 18px 0;
        color: var(--mb-muted);
        font-weight: 600;
        font-size: 14px;
        line-height: 1.45;
        max-width: 70ch;
    }

    /* =========================
       CARDS
       ========================= */
    .cards{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
    }

    .card{
        background: #ffffff;
        border: 1px solid var(--mb-border);
        border-radius: 18px;
        padding: 16px;
        box-shadow: 0 14px 30px rgba(11,59,96,.08);
        transition: transform .12s ease, box-shadow .12s ease, border-color .12s ease;
        display:flex;
        flex-direction: column;
        min-height: 220px;
    }

    .card:hover{
        transform: translateY(-2px);
        box-shadow: 0 18px 36px rgba(11,59,96,.12);
        border-color: rgba(75,179,255,.35);
    }

    .card h3{
        margin: 10px 0 6px 0;
        font-size: 16px;
        color: var(--mb-blue);
        font-weight: 900;
    }

    .card p{
        margin: 0 0 12px 0;
        color: var(--mb-muted);
        font-weight: 600;
        font-size: 13px;
        line-height: 1.45;
        flex: 1;
    }

    .card a{
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width: fit-content;
        padding: 10px 12px;
        border-radius: 12px;
        text-decoration:none;
        font-weight: 900;
        font-size: 13px;
        color: #ffffff;
        background: linear-gradient(135deg, var(--mb-blue) 0%, var(--mb-blue2) 100%);
        box-shadow: 0 12px 24px rgba(11,59,96,.14);
    }

    .card a:hover{
        box-shadow: 0 16px 30px rgba(11,59,96,.18);
        transform: translateY(-1px);
    }

    /* ✅ Pedido: tarjetas al inicio y al final naranja (sin tocar HTML) */
    .cards .card:first-child,
    .cards .card:last-child{
        background: linear-gradient(135deg, var(--mb-orange-soft) 0%, #ffffff 70%);
        border-color: rgba(255,122,24,.40);
        box-shadow: 0 18px 38px rgba(255,122,24,.14);
        position: relative;
        overflow: hidden;
    }

    .cards .card:first-child::before,
    .cards .card:last-child::before{
        content:"";
        position:absolute;
        top:0;
        left:0;
        right:0;
        height: 6px;
        background: linear-gradient(90deg, var(--mb-orange) 0%, var(--mb-orange2) 100%);
    }

    /* =========================
       PRECIOS (cards 3)
       ========================= */
    .plan-grid{
        display:grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
    }

    .plan{
        background:#ffffff;
        border: 1px solid var(--mb-border);
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 18px 40px rgba(11,59,96,.10);
        display:flex;
        flex-direction: column;
        min-height: 260px;
    }

    .plan:first-child,
    .plan:last-child{
        background: linear-gradient(135deg, var(--mb-orange-soft) 0%, #ffffff 70%);
        border-color: rgba(255,122,24,.40);
    }

    .plan h3{
        margin: 0 0 6px 0;
        font-size: 16px;
        font-weight: 900;
        color: var(--mb-blue);
    }

    .plan-price{
        margin: 0 0 8px 0;
        font-size: 34px;
        font-weight: 1000;
        color: var(--mb-blue);
        letter-spacing: -1px;
    }

    .plan-price span{
        font-size: 14px;
        font-weight: 800;
        color: var(--mb-muted);
        margin-left: 6px;
    }

    .plan-note{
        color: var(--mb-muted);
        font-weight: 700;
        font-size: 13px;
        margin-bottom: 12px;
    }

    .plan ul{
        margin: 0 0 14px 18px;
        color: var(--mb-muted);
        font-weight: 600;
        font-size: 13px;
        line-height: 1.6;
        flex: 1;
    }

    .plan .btn{
        width: 100%;
    }

    /* =========================
       RESPONSIVE
       ========================= */
    @media (max-width: 1020px){
        .mb-hero-grid{ grid-template-columns: 1fr; }
        .cards{ grid-template-columns: repeat(2, 1fr); }
        .plan-grid{ grid-template-columns: 1fr; }
        .hero-title{ font-size: 38px; }
    }

    @media (max-width: 560px){
        .cards{ grid-template-columns: 1fr; }
        .hero-title{ font-size: 34px; }
        .mb-links{ gap: 8px; }
        .mb-link{ padding: 8px 8px; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# CONFIG DE IMÁGENES
# (Dejé BASE_URL como variable única para no tocar el resto)
# =========================
# Si tus imágenes están en GitHub, usa el RAW base. Ej:
# BASE_URL = "https://raw.githubusercontent.com/TU_USUARIO/TU_REPO/main"
BASE_URL = "https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main"

IMG = {
    "asistente": f"{BASE_URL}/Asistente.png",
    "cocina": f"{BASE_URL}/Asistentecocina.png",
    "ecommerce": f"{BASE_URL}/Asistentecocina.png",
    "finanzas": f"{BASE_URL}/Asistentefinanzas.png",
    "futbol": f"{BASE_URL}/Asistentefutbol.png",
    "stock": f"{BASE_URL}/Asistente.png",
}

# =========================
# HTML PAGES
# =========================
HTML_HOME = f"""
<div class="mb-page">
  <div class="mb-nav">
    <div class="mb-container">
      <div class="mb-nav-inner">
        <a class="mb-brand" href="/?vista=home">MERCADOBOT</a>
        <div class="mb-links">
          <a class="mb-link" href="/?vista=home">Inicio</a>
          <a class="mb-link" href="/?vista=asistentes">Asistentes</a>
          <a class="mb-link" href="/?vista=precios">Precios</a>
          <a class="mb-link" href="/?vista=soporte">Soporte</a>
        </div>
        <a class="mb-login" href="/?vista=login">Iniciar sesión</a>
      </div>
    </div>
  </div>

  <section class="mb-hero">
    <div class="mb-container">
      <div class="mb-hero-grid">
        <div>
          <h1 class="hero-title">El marketplace<br/>de asistentes IA</h1>
          <p class="hero-subtitle">
            Automatizá tu negocio con asistentes virtuales inteligentes que responden, informan y asisten a tus clientes.
          </p>

          <p class="hero-impact">
            Preguntale a tus datos.
            <span>No busques entre miles de archivos: tu asistente responde con la información del negocio.</span>
          </p>

          <div class="hero-actions">
            <a class="btn btn-primary" href="/?vista=asistentes">Explorar asistentes</a>
            <a class="btn btn-outline" href="/?vista=demo&asistente=futbol">▶ Ver demo en vivo</a>
          </div>

          <div class="mb-badges">
            <span class="badge">⚽ Fútbol</span>
            <span class="badge">👨‍🍳 Cocina</span>
            <span class="badge">🛒 Ecommerce</span>
            <span class="badge">💰 Finanzas</span>
          </div>
        </div>

        <div class="mb-hero-side">
          <img src="{IMG["asistente"]}" alt="MercadoBot" style="width:100%; border-radius:16px; border:1px solid var(--mb-border);" />
          <div style="margin-top:12px; color:var(--mb-muted); font-weight:700; font-size:13px; line-height:1.4;">
            Demo lista para mostrar la potencialidad del asistente en distintos rubros.
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="mb-section">
    <div class="mb-container">
      <h2 class="section-title">Asistentes IA listos para potenciar tu negocio</h2>
      <p class="section-subtitle">
        Explorá, elegí e instalá asistentes inteligentes según tus necesidades.
      </p>

      <div class="cards">
        <div class="card">
          <img src="{IMG["futbol"]}" alt="Fútbol" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Fútbol</h3>
          <p>Resultados, fixtures, posiciones y análisis rápido para hinchas y clubes.</p>
          <a href="/?vista=demo&asistente=futbol">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["cocina"]}" alt="Cocina" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Cocina</h3>
          <p>Recetas, conversiones, menú semanal y ayuda paso a paso.</p>
          <a href="/?vista=demo&asistente=cocina">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["finanzas"]}" alt="Finanzas" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Finanzas</h3>
          <p>Cotizaciones, cálculos, presupuestos y consultas rápidas.</p>
          <a href="/?vista=demo&asistente=finanzas">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["ecommerce"]}" alt="Ecommerce" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Ecommerce</h3>
          <p>Soporte para productos, stock, envíos, medios de pago y pedidos.</p>
          <a href="/?vista=demo&asistente=ecommerce">Ver asistente</a>
        </div>
      </div>
    </div>
  </section>

  <section class="mb-section alt">
    <div class="mb-container">
      <h2 class="section-title">¿Qué cambia con MercadoBot?</h2>
      <p class="section-subtitle">
        Menos tiempo respondiendo lo mismo. Más tiempo vendiendo.
      </p>

      <div class="cards">
        <div class="card">
          <h3>Atiende 24/7</h3>
          <p>Responde al instante sin depender de una persona conectada.</p>
          <a href="/?vista=precios">Ver planes</a>
        </div>
        <div class="card">
          <h3>Respuestas consistentes</h3>
          <p>Precios, stock, turnos, horarios y políticas siempre claras.</p>
          <a href="/?vista=asistentes">Ver asistentes</a>
        </div>
        <div class="card">
          <h3>Escalable</h3>
          <p>Más consultas atendidas sin sumar carga operativa.</p>
          <a href="/?vista=asistentes">Explorar</a>
        </div>
        <div class="card">
          <h3>Adaptable a tu rubro</h3>
          <p>Demos por sector. Luego se entrena con los datos reales del negocio.</p>
          <a href="/?vista=soporte">Hablar</a>
        </div>
      </div>
    </div>
  </section>

  <section class="mb-section">
    <div class="mb-container">
      <div style="display:flex; align-items:center; justify-content:space-between; gap:14px; flex-wrap:wrap; padding:18px; border:1px solid var(--mb-border); border-radius:18px; background:#fff;">
        <div>
          <div style="font-weight:1000; color:var(--mb-blue); font-size:18px;">Probá la demo</div>
          <div style="color:var(--mb-muted); font-weight:700; font-size:13px; margin-top:4px;">
            E imaginá lo que pueden hacer con tus datos.
          </div>
        </div>
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
          <a class="btn btn-primary" href="/?vista=demo&asistente=ecommerce">Probar demo</a>
          <a class="btn btn-outline" href="/?vista=soporte">Contactar</a>
        </div>
      </div>
    </div>
  </section>
</div>
"""

HTML_ASISTENTES = f"""
<div class="mb-page">
  <div class="mb-nav">
    <div class="mb-container">
      <div class="mb-nav-inner">
        <a class="mb-brand" href="/?vista=home">MERCADOBOT</a>
        <div class="mb-links">
          <a class="mb-link" href="/?vista=home">Inicio</a>
          <a class="mb-link" href="/?vista=asistentes">Asistentes</a>
          <a class="mb-link" href="/?vista=precios">Precios</a>
          <a class="mb-link" href="/?vista=soporte">Soporte</a>
        </div>
        <a class="mb-login" href="/?vista=login">Iniciar sesión</a>
      </div>
    </div>
  </div>

  <section class="mb-section">
    <div class="mb-container">
      <h2 class="section-title">Todos los asistentes IA</h2>
      <p class="section-subtitle">Estos son los asistentes disponibles en MercadoBot.</p>

      <div class="cards">
        <div class="card">
          <img src="{IMG["cocina"]}" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Cocina</h3>
          <p>Recetas, consejos y conversiones.</p>
          <a href="/?vista=demo&asistente=cocina">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["ecommerce"]}" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Ecommerce</h3>
          <p>Soporte para productos y pedidos.</p>
          <a href="/?vista=demo&asistente=ecommerce">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["finanzas"]}" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Finanzas</h3>
          <p>Cotizaciones y consultas rápidas.</p>
          <a href="/?vista=demo&asistente=finanzas">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["stock"]}" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Stock</h3>
          <p>Control de inventario y alertas.</p>
          <a href="/?vista=demo&asistente=stock">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["futbol"]}" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Fútbol</h3>
          <p>Fixtures, posiciones, resultados y estadísticas.</p>
          <a href="/?vista=demo&asistente=futbol">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["asistente"]}" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente de Turnos</h3>
          <p>Reserva de turnos y recordatorios.</p>
          <a href="/?vista=demo&asistente=turnos">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["asistente"]}" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente Inmobiliario</h3>
          <p>Consultas de propiedades y agendado.</p>
          <a href="/?vista=demo&asistente=inmobiliaria">Ver asistente</a>
        </div>

        <div class="card">
          <img src="{IMG["asistente"]}" style="width:100%; border-radius:14px; border:1px solid var(--mb-border);" />
          <h3>Asistente Dental</h3>
          <p>Turnos y precios orientativos.</p>
          <a href="/?vista=demo&asistente=dental">Ver asistente</a>
        </div>
      </div>
    </div>
  </section>

  <section class="mb-section alt">
    <div class="mb-container">
      <div style="display:flex; align-items:center; justify-content:space-between; gap:14px; flex-wrap:wrap; padding:18px; border:1px solid var(--mb-border); border-radius:18px; background:#fff;">
        <div>
          <div style="font-weight:1000; color:var(--mb-blue); font-size:18px;">¿Querés uno para tu negocio?</div>
          <div style="color:var(--mb-muted); font-weight:700; font-size:13px; margin-top:4px;">
            Subís tus datos y preparamos tu demo.
          </div>
        </div>
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
          <a class="btn btn-primary" href="/?vista=soporte">Hablemos</a>
          <a class="btn btn-outline" href="/?vista=precios">Ver precios</a>
        </div>
      </div>
    </div>
  </section>
</div>
"""

HTML_PRECIOS = """
<div class="mb-page">
  <div class="mb-nav">
    <div class="mb-container">
      <div class="mb-nav-inner">
        <a class="mb-brand" href="/?vista=home">MERCADOBOT</a>
        <div class="mb-links">
          <a class="mb-link" href="/?vista=home">Inicio</a>
          <a class="mb-link" href="/?vista=asistentes">Asistentes</a>
          <a class="mb-link" href="/?vista=precios">Precios</a>
          <a class="mb-link" href="/?vista=soporte">Soporte</a>
        </div>
        <a class="mb-login" href="/?vista=login">Iniciar sesión</a>
      </div>
    </div>
  </div>

  <section class="mb-section">
    <div class="mb-container">
      <h2 class="section-title">Planes</h2>
      <p class="section-subtitle">Elegí el plan que mejor se ajuste a tu negocio.</p>

      <div class="plan-grid">
        <div class="plan">
          <h3>Starter</h3>
          <div class="plan-price">US$ 99<span>/mes</span></div>
          <div class="plan-note">1 asistente · 1 sitio</div>
          <ul>
            <li>Demo por rubro</li>
            <li>Instalación en web</li>
            <li>Soporte básico</li>
          </ul>
          <a class="btn btn-primary" href="/?vista=soporte">Solicitar</a>
        </div>

        <div class="plan">
          <h3>Pro</h3>
          <div class="plan-price">US$ 150<span>/mes</span></div>
          <div class="plan-note">1 asistente · 1 sitio</div>
          <ul>
            <li>Entrenado con datos del negocio</li>
            <li>Respuestas 24/7</li>
            <li>Soporte prioritario</li>
          </ul>
          <a class="btn btn-primary" href="/?vista=soporte">Solicitar</a>
        </div>

        <div class="plan">
          <h3>Business</h3>
          <div class="plan-price">A medida</div>
          <div class="plan-note">Integraciones + múltiples canales</div>
          <ul>
            <li>Web + WhatsApp + Instagram</li>
            <li>Automatizaciones</li>
            <li>Panel y métricas</li>
          </ul>
          <a class="btn btn-primary" href="/?vista=soporte">Hablar</a>
        </div>
      </div>
    </div>
  </section>
</div>
"""

HTML_SOPORTE = """
<div class="mb-page">
  <div class="mb-nav">
    <div class="mb-container">
      <div class="mb-nav-inner">
        <a class="mb-brand" href="/?vista=home">MERCADOBOT</a>
        <div class="mb-links">
          <a class="mb-link" href="/?vista=home">Inicio</a>
          <a class="mb-link" href="/?vista=asistentes">Asistentes</a>
          <a class="mb-link" href="/?vista=precios">Precios</a>
          <a class="mb-link" href="/?vista=soporte">Soporte</a>
        </div>
        <a class="mb-login" href="/?vista=login">Iniciar sesión</a>
      </div>
    </div>
  </div>

  <section class="mb-section">
    <div class="mb-container">
      <h2 class="section-title">Soporte</h2>
      <p class="section-subtitle">
        Contame tu rubro y qué querés automatizar. Preparamos una demo con tu información.
      </p>

      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
        <div style="background:#fff; border:1px solid var(--mb-border); border-radius:18px; padding:18px; box-shadow:0 18px 40px rgba(11,59,96,.10);">
          <div style="font-weight:1000; color:var(--mb-blue); margin-bottom:6px;">Qué podés pedir</div>
          <div style="color:var(--mb-muted); font-weight:700; font-size:13px; line-height:1.6;">
            • Demo por rubro<br/>
            • Asistente con tus datos (Excel / Sheets / sistema)<br/>
            • Instalación en web / WhatsApp / Instagram<br/>
            • Integraciones y automatizaciones
          </div>
        </div>

        <div style="background:#fff; border:1px solid var(--mb-border); border-radius:18px; padding:18px; box-shadow:0 18px 40px rgba(11,59,96,.10);">
          <div style="font-weight:1000; color:var(--mb-blue); margin-bottom:6px;">Contacto</div>
          <div style="color:var(--mb-muted); font-weight:700; font-size:13px; line-height:1.6;">
            Escribime por donde te quede cómodo:<br/>
            • WhatsApp<br/>
            • Instagram<br/>
            • Email
          </div>
          <div style="margin-top:12px;">
            <a class="btn btn-primary" href="/?vista=home">Volver al inicio</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>
"""

def html_demo(asistente: str) -> str:
    titulo = {
        "futbol": "Asistente de Fútbol",
        "cocina": "Asistente de Cocina",
        "ecommerce": "Asistente de Ecommerce",
        "finanzas": "Asistente de Finanzas",
        "stock": "Asistente de Stock",
        "turnos": "Asistente de Turnos",
        "inmobiliaria": "Asistente Inmobiliario",
        "dental": "Asistente Dental",
    }.get(asistente, "Demo de Asistente")

    return f"""
    <div class="mb-page">
      <div class="mb-nav">
        <div class="mb-container">
          <div class="mb-nav-inner">
            <a class="mb-brand" href="/?vista=home">MERCADOBOT</a>
            <div class="mb-links">
              <a class="mb-link" href="/?vista=home">Inicio</a>
              <a class="mb-link" href="/?vista=asistentes">Asistentes</a>
              <a class="mb-link" href="/?vista=precios">Precios</a>
              <a class="mb-link" href="/?vista=soporte">Soporte</a>
            </div>
            <a class="mb-login" href="/?vista=login">Iniciar sesión</a>
          </div>
        </div>
      </div>

      <section class="mb-section">
        <div class="mb-container">
          <h2 class="section-title">{titulo}</h2>
          <p class="section-subtitle">
            Ejemplos de lo que puede responder. (Demo visual)
          </p>

          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px; align-items:start;">
            <div style="background:#fff; border:1px solid var(--mb-border); border-radius:18px; padding:18px; box-shadow:0 18px 40px rgba(11,59,96,.10);">
              <div style="font-weight:1000; color:var(--mb-blue); margin-bottom:10px;">Preguntas típicas</div>
              <div style="color:var(--mb-muted); font-weight:700; font-size:13px; line-height:1.7;">
                • ¿Tenés stock / disponibilidad?<br/>
                • ¿Cuánto cuesta y qué incluye?<br/>
                • ¿Cuál es el horario / turnos disponibles?<br/>
                • ¿Qué opciones recomendás según lo que busco?<br/>
                • ¿Me lo podés comparar con otra opción?
              </div>

              <div style="margin-top:14px; display:flex; gap:10px; flex-wrap:wrap;">
                <a class="btn btn-primary" href="/?vista=soporte">Quiero esto en mi negocio</a>
                <a class="btn btn-outline" href="/?vista=asistentes">Volver</a>
              </div>
            </div>

            <div style="background:#fff; border:1px solid var(--mb-border); border-radius:18px; padding:18px; box-shadow:0 18px 40px rgba(11,59,96,.10);">
              <div style="font-weight:1000; color:var(--mb-blue); margin-bottom:10px;">Vista previa</div>
              <img src="{IMG.get(asistente, IMG["asistente"])}" alt="Demo" style="width:100%; border-radius:16px; border:1px solid var(--mb-border);" />
              <div style="margin-top:10px; color:var(--mb-muted); font-weight:700; font-size:13px; line-height:1.45;">
                Probá la demo e imaginá lo que puede hacer cuando se entrena con tus datos reales.
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    """

# =========================
# ROUTER POR QUERY PARAMS
# =========================
def get_query_params():
    # Compatible con versiones nuevas y viejas de Streamlit
    try:
        qp = dict(st.query_params)
        # st.query_params devuelve valores tipo list en algunas versiones
        vista = qp.get("vista", "home")
        asistente = qp.get("asistente", "futbol")
        if isinstance(vista, list):
            vista = vista[0] if vista else "home"
        if isinstance(asistente, list):
            asistente = asistente[0] if asistente else "futbol"
        return vista, asistente
    except Exception:
        qp = st.experimental_get_query_params()
        vista = qp.get("vista", ["home"])[0]
        asistente = qp.get("asistente", ["futbol"])[0]
        return vista, asistente

vista, asistente = get_query_params()

if vista == "home":
    components.html(HTML_HOME, height=2300, scrolling=True)
elif vista == "asistentes":
    components.html(HTML_ASISTENTES, height=2200, scrolling=True)
elif vista == "precios":
    components.html(HTML_PRECIOS, height=1600, scrolling=True)
elif vista == "soporte":
    components.html(HTML_SOPORTE, height=1500, scrolling=True)
elif vista == "demo":
    components.html(html_demo(asistente), height=1700, scrolling=True)
else:
    components.html(HTML_HOME, height=2300, scrolling=True)
