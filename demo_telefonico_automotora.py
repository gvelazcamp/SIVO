import streamlit as st

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(
    page_title="Demo Asistente Telefónico IA - MercadoBot",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# CSS GLOBAL
# =========================
st.markdown("""
<style>
#MainMenu, footer, header {display: none;}

.stApp {
    background: #ffffff;
    font-family: Inter, sans-serif;
}

/* -------- HERO -------- */
.hero {
    text-align: center;
    padding: 60px 30px 40px;
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    color: #111;
    margin-bottom: 15px;
}

.hero p {
    font-size: 20px;
    color: #555;
    max-width: 720px;
    margin: auto;
}

/* -------- PHONE CARD -------- */
.phone-card {
    background: linear-gradient(135deg, #ff7a18, #ff9f43);
    color: white;
    border-radius: 28px;
    padding: 45px 35px;
    text-align: center;
    margin: 40px 0;
    box-shadow: 0 20px 50px rgba(255,122,24,0.35);
}

.phone-card h2 {
    font-size: 30px;
    margin-bottom: 15px;
}

.phone-number {
    font-size: 46px;
    font-weight: 800;
    letter-spacing: 2px;
    margin: 20px 0;
}

.phone-number a {
    color: white;
    text-decoration: none;
}

.badge {
    display: inline-block;
    background: rgba(255,255,255,0.2);
    padding: 10px 18px;
    border-radius: 999px;
    font-weight: 600;
    margin-top: 15px;
}

/* -------- FEATURES -------- */
.section {
    padding: 60px 20px;
    max-width: 1100px;
    margin: auto;
}

.section h2 {
    text-align: center;
    font-size: 32px;
    margin-bottom: 40px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 25px;
}

.card {
    background: #fff;
    border-radius: 22px;
    padding: 30px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.08);
    transition: all .25s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 45px rgba(0,0,0,0.12);
}

.card span {
    font-size: 36px;
}

.card h3 {
    margin: 15px 0 10px;
}

.card p {
    color: #555;
    line-height: 1.6;
}

/* -------- CHAT DEMO -------- */
.chat-box {
    background: #fafafa;
    border-radius: 22px;
    padding: 35px;
    max-width: 850px;
    margin: auto;
}

.msg {
    margin-bottom: 18px;
    max-width: 80%;
    padding: 15px 20px;
    border-radius: 18px;
}

.bot {
    background: #ffe8d6;
}

.user {
    background: #eaeaea;
    margin-left: auto;
}

/* -------- CTA -------- */
.cta {
    background: #111;
    color: white;
    border-radius: 28px;
    padding: 60px 30px;
    text-align: center;
    margin: 70px 0;
}

.cta h2 {
    font-size: 34px;
    margin-bottom: 15px;
}

.cta p {
    font-size: 20px;
    opacity: .9;
}

/* -------- BUTTON -------- */
.stButton > button {
    background: #ff7a18;
    color: white;
    border-radius: 999px;
    padding: 16px 26px;
    font-size: 18px;
    font-weight: 700;
    border: none;
}

.stButton > button:hover {
    background: #ff8f3d;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <h1>Asistente Telefónico con IA</h1>
    <p>
        Un asistente que atiende llamadas reales, conversa como una persona
        y vende usando la información de tu negocio.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# PHONE DEMO
# =========================
st.markdown("""
<div class="phone-card">
    <h2>Probá el Asistente en Vivo</h2>
    <p>Llamá ahora y hablá con el asistente como si fuera un vendedor real.</p>
    <div class="phone-number">
        <a href="tel:+5981234567">+598 1234 5678</a>
    </div>
    <div class="badge">Disponible 24/7 · Demo gratuita</div>
</div>
""", unsafe_allow_html=True)

# =========================
# FEATURES
# =========================
st.markdown("""
<div class="section">
<h2>Qué hace este asistente</h2>

<div class="grid">
    <div class="card">
        <span>🗣️</span>
        <h3>Habla natural</h3>
        <p>Conversación fluida, humana y clara en español.</p>
    </div>
    <div class="card">
        <span>📦</span>
        <h3>Conoce tu negocio</h3>
        <p>Responde con precios, stock y condiciones reales.</p>
    </div>
    <div class="card">
        <span>📞</span>
        <h3>No pierde llamadas</h3>
        <p>Atiende clientes incluso fuera de horario.</p>
    </div>
    <div class="card">
        <span>🎯</span>
        <h3>Califica leads</h3>
        <p>Detecta clientes reales y toma datos.</p>
    </div>
    <div class="card">
        <span>📅</span>
        <h3>Agenda acciones</h3>
        <p>Coordina visitas, pruebas o seguimientos.</p>
    </div>
    <div class="card">
        <span>⚙️</span>
        <h3>Personalizable</h3>
        <p>Se adapta 100% a tu rubro y tus datos.</p>
    </div>
</div>
</div>
""", unsafe_allow_html=True)

# =========================
# CHAT DEMO
# =========================
st.markdown("""
<div class="section">
<h2>Ejemplo de conversación</h2>

<div class="chat-box">
    <div class="msg bot">Hola, bienvenido. ¿En qué puedo ayudarte?</div>
    <div class="msg user">Estoy buscando un auto usado</div>
    <div class="msg bot">Perfecto. ¿Tenés un presupuesto aproximado?</div>
    <div class="msg user">Hasta 10 millones</div>
    <div class="msg bot">
        Genial. Tengo dos opciones disponibles y puedo coordinar un test drive.
    </div>
</div>
</div>
""", unsafe_allow_html=True)

# =========================
# CTA
# =========================
st.markdown("""
<div class="cta">
    <h2>Esto no es un chatbot genérico</h2>
    <p>
        Es un asistente entrenado con datos reales,
        listo para atender, vender y escalar tu negocio.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# BOTÓN LLAMAR
# =========================
if st.button("📞 Llamar y probar ahora"):
    st.markdown("""
    <script>
    window.location.href = "tel:+5981234567";
    </script>
    """, unsafe_allow_html=True)

st.caption("Demo visual · El asistente se adapta a cualquier rubro.")
