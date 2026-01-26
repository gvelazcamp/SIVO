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
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentecocina.png" alt="Cocina">
                <h3>Asistente de Cocina</h3>
                <p>Recetas rápidas, consejos de cocina y conversiones.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteecommerce.png" alt="Ecommerce">
                <h3>Asistente de Ecommerce</h3>
                <p>Respuestas automáticas sobre productos y pedidos.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentefinanzas.png" alt="Finanzas">
                <h3>Asistente de Finanzas</h3>
                <p>Información financiera y análisis de inversiones.</p>
                <button>Ver asistente</button>
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
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistenteecommerce.png" alt="Ecommerce">
                <h3>Asistente de Ecommerce</h3>
                <p>Soporte para productos y pedidos.</p>
                <button>Ver asistente</button>
            </div>

            <div class="card">
                <img src="{BASE_URL}Asistentefinanzas.png" alt="Finanzas">
                <h3>Asistente de Finanzas</h3>
                <p>Cotizaciones y análisis financiero.</p>
                <button>Ver asistente</button>
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
    else:
        st.html(HTML_HOME)
elif vista == "asistentes":
    st.html(HTML_ASISTENTES)
elif vista == "precios":
    st.html(HTML_PRECIOS)
else:
    st.html(HTML_HOME)
