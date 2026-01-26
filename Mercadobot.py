import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

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

    /* El iframe debe ocupar exactamente el espacio */
    iframe {
        width: 100% !important;
        border: none !important;
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
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

BASE_URL = "https://raw.githubusercontent.com/gvelazcamp/Mercadobot/main/"

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
}

body {
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    background: #f6f7fb;
    margin: 0;
    padding: 0;
    width: 100%;
    overflow-x: hidden;
    min-height: 100vh;
}

.page-container {
    width: 100%;
    max-width: 100%;
    overflow-x: hidden;
}

/* =========================
   HEADER
========================= */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 5%;
    width: 100%;
}

.logo {
    font-size: 22px;
    font-weight: 800;
    text-decoration: none;
    color: #000;
    white-space: nowrap;
}
.logo span { color: #f4b400; }

.nav {
    display: flex;
    gap: 28px;
    font-weight: 500;
    color: #555;
    align-items: center;
}

.nav a {
    text-decoration: none;
    color: #555;
    cursor: pointer;
    white-space: nowrap;
}

.nav a:hover {
    color: #f4b400;
}

.btn-login {
    background: #f4b400;
    padding: 8px 16px;
    border-radius: 10px;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
}

/* =========================
   HERO IMPACT
========================= */
.hero-impact {
    background: linear-gradient(135deg, #2a2a2a 0%, #3d3d3d 100%);
    padding: 60px 5% 50px;
    text-align: center;
    color: #fff;
    position: relative;
    overflow: hidden;
}

.hero-impact::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(circle at 30% 50%, rgba(244, 180, 0, 0.08) 0%, transparent 50%);
    pointer-events: none;
}

.hero-impact-content {
    max-width: 900px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

.hero-impact-title {
    font-size: 42px;
    font-weight: 800;
    line-height: 1.1;
    margin: 0 0 15px 0;
    letter-spacing: -0.02em;
}

.hero-impact-subtitle {
    display: block;
    font-size: 38px;
    background: linear-gradient(135deg, #f4b400 0%, #ffd700 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-top: 8px;
}

.hero-impact-text {
    font-size: 17px;
    color: rgba(255, 255, 255, 0.8);
    margin: 0 0 30px 0;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.hero-impact-actions {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
}

.hero-impact-btn-primary {
    background: #f4b400;
    color: #000;
    padding: 14px 28px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 16px;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    box-shadow: 0 6px 20px rgba(244, 180, 0, 0.3);
}

.hero-impact-btn-primary:hover {
    background: #ffd700;
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(244, 180, 0, 0.4);
}

.hero-impact-btn-secondary {
    background: transparent;
    color: #fff;
    padding: 14px 28px;
    border-radius: 12px;
    font-weight: 600;
    font-size: 16px;
    text-decoration: none;
    display: inline-block;
    border: 2px solid rgba(255, 255, 255, 0.3);
    transition: all 0.3s ease;
}

.hero-impact-btn-secondary:hover {
    border-color: #f4b400;
    color: #f4b400;
    transform: translateY(-2px);
}

@media (max-width: 768px) {
    .hero-impact {
        padding: 40px 5% 35px;
    }
    
    .hero-impact-title {
        font-size: 28px;
    }
    
    .hero-impact-subtitle {
        font-size: 26px;
    }
    
    .hero-impact-text {
        font-size: 15px;
    }
    
    .hero-impact-btn-primary,
    .hero-impact-btn-secondary {
        font-size: 15px;
        padding: 12px 22px;
    }
}

/* =========================
   HERO
========================= */
.hero {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 40px;
    padding: 40px 5%;
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
    background: #f4b400;
    color: #000;
    padding: 12px 22px;
    border-radius: 14px;
    font-weight: 700;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    border: none;
    white-space: nowrap;
}

.btn-primary:hover {
    background: #e5a500;
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
    background: linear-gradient(180deg, #ffffff, #f6f7fb);
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
    background: #f6f7fb;
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

/* =========================
   CATEGORÍAS
========================= */
.cats-block {
    text-align: center;
    padding: 20px 5%;
    width: 100%;
}

.cats {
    display: inline-flex;
    gap: 12px;
    background: #fff;
    padding: 10px 14px;
    border-radius: 999px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    flex-wrap: wrap;
}

.cat {
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 600;
    background: #f6f7fb;
    white-space: nowrap;
}

/* =========================
   SECTION
========================= */
.section {
    padding: 20px 5% 40px;
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
    margin: 0 0 30px 0;
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
    min-height: 60px;
    margin: 0 0 14px 0;
}

.card button {
    background: #f4b400;
    border: none;
    padding: 10px 18px;
    border-radius: 12px;
    font-weight: 700;
    cursor: pointer;
}

.card button:hover {
    background: #e5a500;
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
   CTA FINAL
========================= */
.cta {
    margin: 40px 5% 20px;
    background: linear-gradient(180deg, #eef2f7, #ffffff);
    border-radius: 40px;
    padding: 40px;
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
    margin: 0 0 20px 0;
}

.cta button {
    background: #f4b400;
    padding: 14px 28px;
    border-radius: 16px;
    font-weight: 800;
    border: none;
    cursor: pointer;
}

.cta button:hover {
    background: #e5a500;
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
    .header {
        flex-direction: column;
        gap: 15px;
        padding: 16px 4%;
    }

    .nav {
        gap: 16px;
        font-size: 14px;
    }

    .hero {
        padding: 20px 4%;
    }

    .hero h1 {
        font-size: 28px;
    }

    .section {
        padding: 20px 4%;
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

    .footer {
        flex-direction: column;
        gap: 10px;
        text-align: center;
        padding: 20px 4%;
    }

    .pricing {
        grid-template-columns: 1fr;
    }
}
</style>
</head>
<body>
<div class="page-container">
"""

HEADER = """
    <div class="header">
        <a class="logo" href="?vista=home">MERCADO<span>BOT</span></a>
        <div class="nav">
            <a href="?vista=home">Inicio</a>
            <a href="?vista=asistentes">Asistentes</a>
            <a href="?vista=precios">Precios</a>
            <a href="?vista=home#soporte">Soporte</a>
        </div>
        <div class="btn-login">Iniciar sesión</div>
    </div>
"""

FOOTER = """
    <div class="footer">
        <div>Política de privacidad · Términos y condiciones · Contacto</div>
        <div>Facebook · Twitter · LinkedIn</div>
    </div>
</div>
</body>
</html>
"""

# =========================
# HOME (MODIFICADO: chatbot protagonista)
# =========================
HTML_HOME = f"""{HTML_BASE}
{HEADER}

    <!-- HERO IMPACT -->
    <div class="hero-impact">
        <div class="hero-impact-content">
            <h1 class="hero-impact-title">
                Preguntale a tus datos.<br>
                <span class="hero-impact-subtitle">No busques más entre miles de archivos.</span>
            </h1>
            <p class="hero-impact-text">
                Conectá tus datos y hablá con ellos. Tu asistente IA responde al instante.
            </p>
            <div class="hero-impact-actions">
                <a class="hero-impact-btn-primary" href="?vista=asistentes">Ver asistentes →</a>
                <a class="hero-impact-btn-secondary" href="#demo">Demo en vivo</a>
            </div>
        </div>
    </div>

    <div class="hero">
        <div class="hero-content">
            <h1>Tu negocio atendido<br>por un <span style="color:#f4b400;">chatbot IA</span></h1>
            <p>
                Instalamos un asistente virtual que responde a tus clientes 24/7, con tus reglas y tus datos.
                Elegí un rubro (stock, ecommerce, turnos, viajes) y lo dejamos funcionando.
            </p>

            <div class="hero-actions">
                <a class="btn-primary" href="#demo">Ver chatbot en acción</a>
                <a class="btn-secondary" href="?vista=asistentes">Explorar asistentes</a>
            </div>

            <div class="trust-row">
                <div class="trust-pill">⚡ Instalación rápida</div>
                <div class="trust-pill">🔒 Configurable y seguro</div>
                <div class="trust-pill">💬 Soporte incluido</div>
            </div>
        </div>

        <!-- CHAT DEMO (mock visual) -->
        <div class="hero-chat" id="demo">
            <div class="chat-topbar">
                <div class="chat-brand">
                    <div class="dot"></div>
                    Demo de chatbot
                </div>
                <div class="chat-pill">24/7</div>
            </div>

            <div class="chat-body">
                <div class="bubble user">
                    Hola, ¿me podés decir horarios y cómo reservar?
                    <div class="chat-meta">Cliente</div>
                </div>

                <div class="bubble bot">
                    Claro. Podés reservar en 30 segundos:
                    <br><strong>1)</strong> Elegís día y hora
                    <br><strong>2)</strong> Confirmás tus datos
                    <br><strong>3)</strong> Te llega la confirmación
                    <div class="chat-meta">Asistente IA</div>
                </div>

                <div class="bubble user">
                    ¿Y si tengo stock bajo o quiero saber precios?
                    <div class="chat-meta">Cliente</div>
                </div>

                <div class="bubble bot">
                    También. Puedo:
                    <br>• avisar <strong>stock mínimo</strong>
                    <br>• responder <strong>precios</strong> y disponibilidad
                    <br>• derivar a un humano cuando haga falta
                    <div class="chat-meta">Asistente IA</div>
                </div>
            </div>

            <div class="chat-input">
                <div class="fake-input">Escribí una consulta… (demo)</div>
                <button class="send-btn">Enviar</button>
            </div>
        </div>
    </div>

    <div class="cats-block">
        <div class="cats">
            <div class="cat">📦 Stock</div>
            <div class="cat">🛒 Ecommerce</div>
            <div class="cat">📅 Turnos</div>
            <div class="cat">✈️ Viajes</div>
        </div>
    </div>

    <div class="section">
        <h2>Cómo funciona</h2>
        <div class="subtitle">Simple: elegís el asistente y lo dejamos instalado en tu web.</div>

        <div class="steps">
            <div class="step">
                <div class="step-num">1</div>
                <h3>Elegís el asistente</h3>
                <p>Seleccionás el rubro (stock, turnos, ecommerce, etc.) y el estilo de atención.</p>
            </div>

            <div class="step">
                <div class="step-num">2</div>
                <h3>Lo adaptamos a tu negocio</h3>
                <p>Lo configuramos con tus datos, respuestas, reglas y preguntas frecuentes reales.</p>
            </div>

            <div class="step">
                <div class="step-num">3</div>
                <h3>Lo instalamos</h3>
                <p>Lo dejamos funcionando en tu sitio (iframe o web completa) y con soporte incluido.</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>Asistentes IA listos para potenciar tu negocio</h2>
        <div class="subtitle">Estos son ejemplos. El producto principal es el <strong>chatbot instalado</strong>.</div>

        <div class="cards">
            <div class="card">
                <img src="{BASE_URL}Asistentefutbol.png" alt="Fútbol">
                <h3>Asistente de Fútbol</h3>
                <p>Resultados, noticias y estadísticas del mundo del fútbol.</p>
                <a href="?vista=demo&asistente=futbol" style="text-decoration: none;"><button>Ver asistente</button></a>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentecocina.png" alt="Cocina">
                <h3>Asistente de Cocina</h3>
                <p>Recetas rápidas, consejos de cocina y conversiones.</p>
                <a href="?vista=demo&asistente=cocina" style="text-decoration: none;"><button>Ver asistente</button></a>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteecommerce.png" alt="Ecommerce">
                <h3>Asistente de Ecommerce</h3>
                <p>Respuestas automáticas sobre productos y pedidos.</p>
                <a href="?vista=demo&asistente=ecommerce" style="text-decoration: none;"><button>Ver asistente</button></a>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentefinanzas.png" alt="Finanzas">
                <h3>Asistente de Finanzas</h3>
                <p>Información financiera y análisis de inversiones.</p>
                <a href="?vista=demo&asistente=finanzas" style="text-decoration: none;"><button>Ver asistente</button></a>
            </div>
        </div>
    </div>

    <div class="cta" id="soporte">
        <h2>Integra en minutos</h2>
        <p>Instalá un chatbot IA en tu web y empezá a automatizar consultas reales desde el día 1.</p>
        <button>Quiero mi chatbot</button>

        <div class="features">
            <div class="feature">⚡ Fácil y rápido</div>
            <div class="feature">⚙️ Totalmente configurable</div>
            <div class="feature">🔒 Seguro y escalable</div>
            <div class="feature">💬 Soporte incluido</div>
        </div>
    </div>

{FOOTER}
"""

# =========================
# ASISTENTES
# =========================
HTML_ASISTENTES = f"""{HTML_BASE}
{HEADER}

    <div class="section">
        <h2>Todos los asistentes IA</h2>
        <div class="subtitle">Estos son los asistentes disponibles en MercadoBot.</div>

        <div class="cards">
            <div class="card">
                <img src="{BASE_URL}Asistentefutbol.png" alt="Fútbol">
                <h3>Asistente de Fútbol</h3>
                <p>Resultados, noticias y estadísticas del fútbol.</p>
                <a href="?vista=demo&asistente=futbol" style="text-decoration: none;"><button>Ver asistente</button></a>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentecocina.png" alt="Cocina">
                <h3>Asistente de Cocina</h3>
                <p>Recetas, consejos y conversiones.</p>
                <a href="?vista=demo&asistente=cocina" style="text-decoration: none;"><button>Ver asistente</button></a>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteecommerce.png" alt="Ecommerce">
                <h3>Asistente de Ecommerce</h3>
                <p>Soporte para productos y pedidos.</p>
                <a href="?vista=demo&asistente=ecommerce" style="text-decoration: none;"><button>Ver asistente</button></a>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentefinanzas.png" alt="Finanzas">
                <h3>Asistente de Finanzas</h3>
                <p>Cotizaciones y análisis financiero.</p>
                <a href="?vista=demo&asistente=finanzas" style="text-decoration: none;"><button>Ver asistente</button></a>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentestock.png" alt="Stock">
                <h3>Asistente de Stock</h3>
                <p>Control de inventario y alertas.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteinmobiliaria.png" alt="Inmobiliaria">
                <h3>Asistente Inmobiliario</h3>
                <p>Consultas de propiedades y agendado.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteagendas.png" alt="Agenda">
                <h3>Asistente de Turnos</h3>
                <p>Reserva de turnos y recordatorios.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentedental.png" alt="Dental">
                <h3>Asistente Dental</h3>
                <p>Turnos y precios orientativos.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentedeviaje.png" alt="Viaje">
                <h3>Asistente de Viaje</h3>
                <p>Itinerarios y recomendaciones.</p>
                <button>Ver asistente</button>
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

<div class="subtitle">
    <strong>Paso 1:</strong> Implementación inicial (pago único).<br>
    <strong>Paso 2:</strong> Plan mensual para mantener y mejorar tu asistente.
</div>

    <div class="pricing">

        <!-- SETUP -->
        <div class="plan">
            <div class="plan-name">Implementación inicial</div>
            <div class="plan-desc">
                Dejamos tu asistente funcionando sobre tus datos reales
            </div>

            <div class="plan-price">Desde US$ 300<span>pago único</span></div>
            <div class="plan-note">1 asistente · 1 sitio</div>

            <ul class="plan-list">
                <li>✅ Creación del asistente IA</li>
                <li>✅ Conexión a base de datos / archivos</li>
                <li>✅ Configuración de preguntas</li>
                <li>✅ Instalación en web (iframe o sitio)</li>
                <li>✅ Ajustes iniciales</li>
                <li>✅ Soporte de arranque</li>
            </ul>

            <a class="btn-primary plan-btn" href="?vista=home#contacto">
                Iniciar implementación
            </a>
        </div>

        <!-- PRO -->
        <div class="plan pro">
            <div class="badge">Más elegido</div>
            <div class="plan-name">Pro mensual</div>
            <div class="plan-desc">
                Uso, mantenimiento y evolución continua
            </div>

            <div class="plan-price">US$ 120<span>/mes</span></div>
            <div class="plan-note">1 asistente · 1 sitio</div>
            <div class="plan-note" style="font-size:12px; color:#999;">
                Requiere implementación inicial previa
            </div>


            <ul class="plan-list">
                <li>✅ Asistentes entrenados con tus datos</li>
                <li>✅ Interpretación avanzada (IA + reglas)</li>
                <li>✅ Ajustes y mejoras mensuales</li>
                <li>✅ Reportes de uso</li>
                <li>✅ Soporte prioritario</li>
            </ul>

            <a class="btn-primary plan-btn" href="?vista=asistentes">
                Contratar plan Pro
            </a>
        </div>

        <!-- ENTERPRISE -->
        <div class="plan">
            <div class="plan-name">Enterprise</div>
            <div class="plan-desc">
                IA integrada a la operación de tu empresa
            </div>

            <div class="plan-price">A medida<span>/mes</span></div>
            <div class="plan-note">Asistentes ilimitados · Multi-sitio</div>

            <ul class="plan-list">
                <li>✅ Integraciones ERP / CRM</li>
                <li>✅ Roles y permisos</li>
                <li>✅ SLA y soporte dedicado</li>
                <li>✅ Seguridad y escalabilidad</li>
                <li>✅ Onboarding completo</li>
            </ul>

            <a class="btn-primary plan-btn" href="?vista=home#contacto">
                Hablar con ventas
            </a>
        </div>

    </div>

    <div class="mini-note">
        Precios orientativos. Ajustamos planes según volumen y complejidad real.
    </div>
</div>

{FOOTER}
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
    height: 120px;
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
    background: #f6f7fb;
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
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="{BASE_URL}Asistentefutbol.png" alt="Fútbol">
        <h1>Asistente de Fútbol</h1>
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
    height: 120px;
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
    background: #f6f7fb;
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
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="{BASE_URL}Asistentecocina.png" alt="Cocina">
        <h1>Asistente de Cocina</h1>
        <p>Demo interactivo - Restaurante</p>
    </div>
    
    <div class="demo-chat">
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen menú vegano?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Sí! Tenemos opciones veganas en todos nuestros menús:<br>
            • <strong>Entradas:</strong> Hummus de garbanzos, ensalada mediterránea<br>
            • <strong>Principales:</strong> Risotto de hongos, wok de vegetales, hamburguesa vegana<br>
            • <strong>Postres:</strong> Brownie vegano, helado de coco<br>
            También tenemos opciones vegetarianas y sin TACC. ¿Te gustaría reservar?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuál es el horario del restaurante?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Nuestros horarios son:<br>
            <strong>Lunes a viernes:</strong><br>
            • Almuerzo: 12:00 a 16:00 hs<br>
            • Cena: 20:00 a 00:00 hs<br>
            <strong>Sábados y domingos:</strong><br>
            • Servicio continuo: 12:00 a 01:00 hs<br>
            La cocina cierra 30 minutos antes del horario de cierre.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo hacer una reserva para esta noche?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Claro! Tenemos disponibilidad para esta noche. Para reservar necesito:<br>
            • Cantidad de personas<br>
            • Horario preferido (20:00, 21:00 o 22:00)<br>
            • Tu nombre y teléfono<br>
            Podés reservar por WhatsApp (+54 9 11 1234-5678), teléfono o completando el formulario en nuestra web.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto sale el menú del día?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Nuestro menú ejecutivo cuesta $6.500 e incluye:<br>
            • Entrada (3 opciones a elegir)<br>
            • Plato principal (4 opciones a elegir)<br>
            • Postre o café<br>
            • Agua o gaseosa<br>
            Disponible de lunes a viernes de 12:00 a 16:00 hs. ¡No requiere reserva!</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen delivery?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Hacemos delivery por varios medios:<br>
            • <strong>Pedidos Ya:</strong> Sin cargo en pedidos +$8.000<br>
            • <strong>Rappi:</strong> Envío según distancia<br>
            • <strong>Delivery propio:</strong> Radio de 3km, sin cargo +$7.000<br>
            También podés pedir para retirar (15% descuento). Aceptamos todas las formas de pago.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen opciones sin gluten?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Sí! Somos aptos para celíacos con certificación:<br>
            • Pan sin TACC incluido<br>
            • Pastas sin gluten (ñoquis, ravioles, tallarines)<br>
            • Pizzas con masa sin TACC<br>
            • Postres aptos celíacos<br>
            Toda nuestra cocina está preparada para evitar contaminación cruzada. Mencionalo al reservar.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Aceptan tarjetas de crédito?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Aceptamos todas las formas de pago:<br>
            • <strong>Efectivo</strong><br>
            • <strong>Débito:</strong> Todas las tarjetas<br>
            • <strong>Crédito:</strong> Visa, Mastercard, Amex (hasta 6 cuotas sin interés)<br>
            • <strong>Transferencia</strong> y <strong>Mercado Pago</strong><br>
            • <strong>Cripto:</strong> Bitcoin, USDT<br>
            Servicio de mesa 10% sugerido (no obligatorio).</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿El menú incluye bebida?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Depende del menú que elijas:<br>
            • <strong>Menú ejecutivo:</strong> Incluye agua o gaseosa<br>
            • <strong>Menú degustación:</strong> Incluye copa de vino de la casa<br>
            • <strong>Menú infantil:</strong> Incluye jugo o gaseosa<br>
            • <strong>Carta regular:</strong> Las bebidas se piden por separado<br>
            También tenemos carta de vinos, cervezas artesanales y tragos.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen mesas afuera/terraza?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Sí! Tenemos una hermosa terraza climatizada con:<br>
            • 12 mesas con vista al jardín<br>
            • Calefacción en invierno<br>
            • Ventiladores y toldos en verano<br>
            • Pet-friendly (podés venir con tu mascota)<br>
            Las mesas de terraza son muy solicitadas, te recomendamos reservar con anticipación.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuál es la especialidad de la casa?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Nuestras especialidades más pedidas son:<br>
            1. <strong>Bife de chorizo a las brasas</strong> (400g) - $12.500<br>
            2. <strong>Risotto de mariscos</strong> - $9.800<br>
            3. <strong>Pasta casera con salsa a elección</strong> - $7.500<br>
            4. <strong>Salmón grillado con vegetales</strong> - $11.200<br>
            El chef recomienda nuestro menú degustación de 5 pasos ($15.000).</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo pedir para llevar?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Claro! Tenemos servicio take away con 15% de descuento:<br>
            • Pedí por teléfono o WhatsApp<br>
            • Tu pedido estará listo en 20-30 minutos<br>
            • Packaging ecológico biodegradable<br>
            • Pagás al retirar o por transferencia<br>
            También podés pedir por las apps de delivery sin descuento.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen menú infantil?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Sí! Nuestro menú kids ($4.500) incluye:<br>
            <strong>A elegir:</strong><br>
            • Milanesas con papas fritas<br>
            • Pasta con manteca o tuco<br>
            • Hamburguesa mini con papas<br>
            • Nuggets de pollo caseros<br>
            <strong>Incluye:</strong> Jugo o gaseosa + helado de postre<br>
            También tenemos sillitas para bebés y zona de juegos.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen eventos privados?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Sí! Tenemos salón privado para eventos:<br>
            • <strong>Capacidad:</strong> 25-50 personas<br>
            • <strong>Ideal para:</strong> Cumpleaños, aniversarios, reuniones empresariales<br>
            • <strong>Incluye:</strong> Menú personalizado, decoración básica, wifi<br>
            • <strong>Precio:</strong> Desde $180.000 (menú + salón)<br>
            También hacemos catering externo. ¿Te paso el contacto del área de eventos?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Dónde están ubicados?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Estamos en Av. Santa Fe 2450, Palermo.<br>
            <strong>Cómo llegar:</strong><br>
            • Subte D (estación Bulnes) - 2 cuadras<br>
            • Colectivos: 12, 39, 55, 110, 152<br>
            • Estacionamiento público a 50 metros<br>
            <strong>Contacto:</strong><br>
            • WhatsApp: +54 9 11 1234-5678<br>
            • Instagram: @restaurante<br>
            • www.restaurante.com</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Necesito reservar o puedo ir directamente?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Depende del día y horario:<br>
            • <strong>Sin reserva:</strong> Lunes a miércoles al mediodía (baja ocupación)<br>
            • <strong>Recomendamos reservar:</strong> Jueves y viernes (alta demanda)<br>
            • <strong>Obligatorio reservar:</strong> Fines de semana y feriados<br>
            Si venís sin reserva, podés esperar en nuestro bar con entrada y tragos mientras se libera mesa.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen estacionamiento?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Tenemos convenio con estacionamiento a 50 metros:<br>
            • <strong>Precio:</strong> $1.500 por 3 horas<br>
            • <strong>Beneficio:</strong> 50% descuento validando ticket en el restaurant<br>
            • <strong>Ubicación:</strong> Av. Santa Fe 2380<br>
            También hay zona de estacionamiento medido en la cuadra (app Telepase). No contamos con servicio de valet parking.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿El servicio de mesa está incluido?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">El servicio de mesa (cubierto) está incluido en todos nuestros platos. La propina es opcional y sugerida al 10%, pero completamente voluntaria.<br>
            <strong>Incluye:</strong><br>
            • Pan de la casa<br>
            • Manteca saborizada<br>
            • Agua con o sin gas<br>
            Si tenés alguna preferencia alimentaria, avisanos al sentarte.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen promociones?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Sí! Nuestras promos vigentes:<br>
            • <strong>Happy Hour:</strong> Lun-Vie 18-20hs - 2x1 en tragos seleccionados<br>
            • <strong>Martes de Pasta:</strong> 30% off en todas las pastas<br>
            • <strong>Jueves Gourmet:</strong> Menú degustación $12.000 (precio regular $15.000)<br>
            • <strong>Cumpleañeros:</strong> Postre gratis presentando DNI<br>
            Seguinos en Instagram para promos exclusivas!</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo ver la carta online?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Claro! Podés ver nuestra carta completa en:<br>
            • <strong>Web:</strong> www.restaurante.com/menu<br>
            • <strong>Instagram:</strong> @restaurante (destacadas)<br>
            • <strong>Código QR:</strong> En nuestras mesas<br>
            La carta incluye fotos de todos los platos, ingredientes, alérgenos y precios actualizados. También tenemos carta de vinos y tragos.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen catering para eventos?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Sí! Ofrecemos servicio de catering completo:<br>
            • <strong>Menú personalizado:</strong> Adaptado a tu presupuesto<br>
            • <strong>Incluye:</strong> Comida, bebidas, mozos, vajilla, mantelería<br>
            • <strong>Desde:</strong> $8.000 por persona (mínimo 30 personas)<br>
            • <strong>Tipos:</strong> Finger food, platos emplatados, buffet<br>
            Te pasamos presupuesto sin cargo. ¿Para cuántas personas sería?</div>
        </div>
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
    height: 120px;
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
    background: #f6f7fb;
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
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="{BASE_URL}Asistenteecommerce.png" alt="Ecommerce">
        <h1>Asistente de Ecommerce</h1>
        <p>Demo interactivo - Tienda Online</p>
    </div>
    
    <div class="demo-chat">
        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen stock de zapatillas Nike Air Max talle 42?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Las Nike Air Max están disponibles en talle 42:<br>
            • <strong>Air Max 90:</strong> $89.999 - Stock: 5 unidades<br>
            • <strong>Air Max 270:</strong> $119.999 - Stock: 3 unidades<br>
            • <strong>Air Max Plus:</strong> $109.999 - Stock: 7 unidades<br>
            Envío gratis en compras superiores a $80.000. ¿Cuál te interesa?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuánto tarda el envío a Córdoba Capital?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Los tiempos de envío a Córdoba Capital son:<br>
            • <strong>Envío estándar:</strong> 5-7 días hábiles - $2.500<br>
            • <strong>Envío express:</strong> 2-3 días hábiles - $4.800<br>
            • <strong>Envío prioritario:</strong> 24-48 hs - $8.000<br>
            <strong>Envío GRATIS</strong> en compras mayores a $80.000 (estándar)<br>
            Todos los envíos incluyen seguro y tracking.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo pagar en cuotas?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Tenemos varias opciones de financiación:<br>
            • <strong>Tarjetas de crédito:</strong> Hasta 12 cuotas sin interés<br>
            • <strong>Mercado Pago:</strong> Hasta 18 cuotas (con interés)<br>
            • <strong>Naranja/Visa/Mastercard:</strong> 3, 6, 9 o 12 cuotas<br>
            • <strong>Efectivo/Transferencia:</strong> 10% descuento adicional<br>
            También aceptamos débito y billeteras digitales.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo hago para cambiar un producto?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">El proceso de cambio es muy simple:<br>
            1. <strong>Tenés 30 días</strong> desde la compra<br>
            2. <strong>El producto debe estar:</strong> Sin uso, con etiquetas, en embalaje original<br>
            3. <strong>Iniciá el cambio:</strong> Desde tu cuenta o por WhatsApp<br>
            4. <strong>Te enviamos:</strong> Etiqueta de devolución prepaga<br>
            5. <strong>Recibimos y validamos:</strong> 2-3 días hábiles<br>
            6. <strong>Enviamos el nuevo:</strong> Sin cargo adicional<br>
            Los cambios son GRATIS.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Dónde está mi pedido #12345?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Tu pedido #12345 está en camino! 📦<br>
            • <strong>Estado:</strong> En distribución<br>
            • <strong>Courier:</strong> Andreani<br>
            • <strong>Código de seguimiento:</strong> AN123456789AR<br>
            • <strong>Entrega estimada:</strong> Mañana antes de las 18hs<br>
            Podés rastrearlo en tiempo real en: www.andreani.com/tracking<br>
            Recibirás un SMS cuando esté a 2 horas de llegar.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen buzos oversize?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Tenemos una colección completa de buzos oversize:<br>
            • <strong>Buzo básico liso:</strong> $12.999 (S/M/L/XL)<br>
            • <strong>Buzo con capucha:</strong> $15.999 (S/M/L/XL)<br>
            • <strong>Buzo estampado:</strong> $17.999 (S/M/L/XL)<br>
            • <strong>Colores:</strong> Negro, gris, blanco, beige, verde militar<br>
            <strong>Promo:</strong> Comprá 2 buzos y llevá 25% OFF. ¿Te paso el link de la colección?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo sé mi talle?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Tenemos una guía de talles completa:<br>
            📏 <strong>Para ropa:</strong><br>
            • Medí tu busto/pecho, cintura y cadera<br>
            • Compará con nuestra tabla de talles<br>
            👟 <strong>Para calzado:</strong><br>
            • Medí tu pie en cm (del talón a la punta)<br>
            • Usá nuestro conversor de tallas<br>
            <strong>Tip:</strong> En cada producto hay una guía específica con medidas exactas.<br>
            ¿Querés que te ayude con un producto en particular?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen tienda física?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Tenemos 3 locales:<br>
            📍 <strong>Palermo:</strong> Av. Santa Fe 3500<br>
            &nbsp;&nbsp;&nbsp;Lun-Sáb 10-20hs, Dom 12-19hs<br>
            📍 <strong>Belgrano:</strong> Av. Cabildo 2200<br>
            &nbsp;&nbsp;&nbsp;Lun-Sáb 10-20hs, Dom 12-19hs<br>
            📍 <strong>Unicenter:</strong> Local 234, 1er piso<br>
            &nbsp;&nbsp;&nbsp;Todos los días 10-22hs<br>
            Podés comprar online y retirar en cualquier local SIN CARGO.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo retirar en local?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">¡Claro! Retiro en tienda es GRATIS:<br>
            1. <strong>Comprás online</strong> y elegís "Retiro en tienda"<br>
            2. <strong>Elegís el local</strong> más cercano<br>
            3. <strong>Te llega un email</strong> cuando está listo (24-48hs)<br>
            4. <strong>Retirás</strong> presentando DNI y número de orden<br>
            <strong>Ventajas:</strong><br>
            ✓ Sin costo de envío<br>
            ✓ Podés probarte en el local<br>
            ✓ Cambio inmediato si no te queda<br>
            Horarios: Lun-Sáb 10-20hs</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Hacen envíos al interior?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Enviamos a todo el país:<br>
            <strong>CABA y GBA:</strong><br>
            • Estándar: 3-5 días - $1.800<br>
            • Express: 24-48hs - $3.500<br>
            <strong>Interior del país:</strong><br>
            • Córdoba, Rosario, Mendoza: 5-7 días - $2.500<br>
            • Resto del país: 7-10 días - $3.200<br>
            • Patagonia: 10-15 días - $4.500<br>
            <strong>ENVÍO GRATIS</strong> en compras +$80.000 a todo el país!</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cuándo hay restock de las Jordan?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Las Air Jordan 1 Retro High están agotadas actualmente.<br>
            📅 <strong>Próximo restock:</strong> 15 de febrero<br>
            👟 <strong>Talles disponibles:</strong> Del 38 al 44<br>
            💰 <strong>Precio:</strong> $149.999<br>
            <strong>¿Querés que te avisemos?</strong><br>
            Dejá tu email y te notificamos 24hs antes del lanzamiento. Además, tenés acceso prioritario por 2 horas antes de la venta pública.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen descuentos por cantidad?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Tenemos descuentos progresivos:<br>
            • <strong>2 productos:</strong> 10% OFF<br>
            • <strong>3 productos:</strong> 15% OFF<br>
            • <strong>4 o más productos:</strong> 20% OFF<br>
            <strong>Además:</strong><br>
            • Comprá $100.000 o más: 25% OFF adicional<br>
            • Primera compra: 15% OFF con código BIENVENIDO<br>
            • Suscribite al newsletter: 10% OFF permanente<br>
            Los descuentos se aplican automáticamente en el carrito.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Qué pasa si el producto llega defectuoso?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Si recibís un producto con defecto:<br>
            1. <strong>Contactanos inmediatamente</strong> con fotos del defecto<br>
            2. <strong>Te enviamos</strong> etiqueta de devolución prepaga<br>
            3. <strong>Opciones:</strong><br>
            &nbsp;&nbsp;&nbsp;• Cambio por uno nuevo<br>
            &nbsp;&nbsp;&nbsp;• Reintegro del 100% del dinero<br>
            &nbsp;&nbsp;&nbsp;• Crédito en la tienda con 10% extra<br>
            4. <strong>Tiempo de resolución:</strong> 48-72hs<br>
            Todos los productos tienen garantía de 90 días contra defectos de fábrica.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen programa de puntos?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Nuestro programa VIP Club:<br>
            💎 <strong>Cómo funciona:</strong><br>
            • Por cada $100 gastados = 1 punto<br>
            • 100 puntos = $500 de descuento<br>
            <strong>Beneficios por nivel:</strong><br>
            🥉 <strong>Bronce</strong> (0-500 puntos): 5% descuento permanente<br>
            🥈 <strong>Plata</strong> (501-1000): 10% + envíos gratis<br>
            🥇 <strong>Oro</strong> (1001+): 15% + acceso anticipado a lanzamientos<br>
            Registrate gratis y empezá a acumular puntos hoy!</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Aceptan mercadería usada como parte de pago?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Tenemos nuestro programa "Trade-In":<br>
            👟 <strong>Productos aceptados:</strong><br>
            • Zapatillas de marca (buen estado)<br>
            • Ropa deportiva premium<br>
            • Accesorios originales<br>
            <strong>Proceso:</strong><br>
            1. Envianos fotos del producto<br>
            2. Nuestro equipo lo evalúa (24hs)<br>
            3. Te damos un valor de canje<br>
            4. Lo usás como crédito en tu próxima compra<br>
            <strong>Bonificación:</strong> Hasta 40% del valor original.</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Puedo cancelar mi pedido?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí, podés cancelar tu pedido:<br>
            ✅ <strong>ANTES del envío:</strong><br>
            • Cancelación 100% gratis<br>
            • Reembolso inmediato (2-5 días hábiles)<br>
            • Desde tu cuenta o por WhatsApp<br>
            ⚠️ <strong>DESPUÉS del envío:</strong><br>
            • Ya no se puede cancelar<br>
            • Podés rechazar el paquete al recibirlo<br>
            • O iniciá una devolución dentro de los 30 días<br>
            ¿Cuál es el número de tu pedido?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen gift cards?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Nuestras tarjetas regalo son perfectas:<br>
            🎁 <strong>Valores disponibles:</strong><br>
            • $10.000 / $20.000 / $50.000 / $100.000<br>
            • O elegí el monto que quieras (mín. $5.000)<br>
            <strong>Características:</strong><br>
            • Válidas por 12 meses<br>
            • Usables online y en tiendas<br>
            • Entrega inmediata por email<br>
            • Podés personalizarla con mensaje<br>
            • Sin cargo adicional<br>
            ¿Para quién sería el regalo?</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Cómo me registro en la web?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Registrarte es súper fácil:<br>
            1. <strong>Hacé click</strong> en "Crear cuenta"<br>
            2. <strong>Completá:</strong> Email y contraseña<br>
            3. <strong>Verificá</strong> tu email (te llega un link)<br>
            4. <strong>¡Listo!</strong> Ya podés comprar<br>
            <strong>Beneficios de tener cuenta:</strong><br>
            ✓ 15% OFF en tu primera compra<br>
            ✓ Guardás tus datos para comprar más rápido<br>
            ✓ Seguimiento de pedidos<br>
            ✓ Acceso a ventas exclusivas<br>
            ✓ Acumulás puntos VIP</div>
        </div>

        <div class="demo-message">
            <div class="demo-label">Cliente</div>
            <div class="demo-bubble demo-user">¿Tienen app móvil?</div>
        </div>
        <div class="demo-message">
            <div class="demo-label">Asistente IA</div>
            <div class="demo-bubble demo-bot">Sí! Descargá nuestra app:<br>
            📱 <strong>iOS:</strong> App Store - "Tienda Online"<br>
            🤖 <strong>Android:</strong> Google Play - "Tienda Online"<br>
            <strong>Beneficios exclusivos de la app:</strong><br>
            • 10% OFF adicional en tu primera compra<br>
            • Notificaciones de ofertas y lanzamientos<br>
            • Escaneo de productos en tienda<br>
            • Acceso a descuentos exclusivos<br>
            • Compra más rápida con 1 click<br>
            ¡Descargala gratis ahora!</div>
        </div>
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
    height: 120px;
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
    background: #f6f7fb;
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
</style>

<div class="demo-container">
    <div class="demo-header">
        <img src="{BASE_URL}Asistentefinanzas.png" alt="Finanzas">
        <h1>Asistente de Finanzas</h1>
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
            📈 <strong>Bonos:</strong><br>
            • Compra/venta: 0.3% por operación<br>
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
            • Desde Argentina<br>
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
            🛡️ <strong>Custodia segregada:</strong><br>
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
    
    <div class="demo-back">
        <a href="?vista=asistentes">← Volver a Asistentes</a>
    </div>
</div>

{FOOTER}
"""

# =========================
# RENDER - Usar st.html() sin iframes
# =========================
if vista == "demo":
    # Obtener el tipo de asistente del query param
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
    else:
        st.html(HTML_HOME)
elif vista == "asistentes":
    st.html(HTML_ASISTENTES)
elif vista == "precios":
    st.html(HTML_PRECIOS)
else:
    st.html(HTML_HOME)
