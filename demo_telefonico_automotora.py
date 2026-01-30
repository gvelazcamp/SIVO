import streamlit as st

# =========================
# CONFIGURACIÓN DE PÁGINA
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

/* =========================
   HERO
   ========================= */
.hero {
    text-align: center;
    padding: 70px 30px 40px;
}

.hero h1 {
    font-size: 44px;
    font-weight: 800;
    color: #111;
    margin-bottom: 16px;
}

.hero p {
    font-size: 20px;
    color: #555;
    max-width: 760px;
    margin: auto;
}

/* =========================
   PHONE CARD
   ========================= */
.phone-card {
    background: linear-gradient(135deg, #ff7a18, #ff9f43);
    color: white;
    border-radius: 30px;
    padding: 50px 40px;
    text-align: center;
    margin: 45px 0;
    box-shadow: 0 25px 55px rgba(255,122,24,0.35);
}

.phone-card h2 {
    font-size: 32px;
    margin-bottom: 14px;
}

.phone-card p {
    font-size: 18px;
    opacity: 0.95;
}

.phone-number {
    font-size: 48px;
    font-weight: 800;
    letter-spacing: 2px;
    margin: 24px 0;
}

.phone-number a {
    color: white;
    text-decoration: none;
}

.badge {
    display: inline-block;
    background: rgba(255,255,255,0.25);
    padding: 12px 22px;
    border-radius: 999px;
    font-weight: 600;
    margin-top: 10px;
}

/* =========================
   FEATURES HEADER
   ========================= */
.features-header {
    text-align: center;
    margin: 70px 0 45px;
}

.phone-icon {
    font-size: 54px;
    margin-bottom: 12px;
}

.divider-line {
    width: 90px;
    height: 4px;
    background: linear-gradient(90deg, #ff7a18, #ffb347);
    margin: 0 auto 18px;
    border-radius: 10px;
}

.features-header h2 {
    font-size: 34px;
    font-weight: 800;
    color: #111;
}

/* =========================
   FEATURES GRID
   ========================= */
.section {
    padding: 0 20px 60px;
    max-width: 1100px;
    margin: auto;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 28px;
}

.card {
    background: #ffffff;
    border-radius: 24px;
    padding: 34px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    transition: all .25s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 45px rgba(0,0,0,0.12);
}

.card span {
    font-size: 38px;
}

.card h3 {
    margin: 16px 0 10px;
    font-size: 20px;
}

.card p {
    color: #555;
    line-height: 1.6;
    font-size: 15px;
}

/* =========================
   CONVERSACIÓN
   ========================= */
.conversation-example {
    background: #ffffff;
    padding: 40px;
    border-radius: 28px;
    margin: 60px auto;
    max-width: 900px;
    box-shadow: 0 15px 45px rgba(0,0,0,0.1);
}

.conv-title {
    font-size: 28px;
    font-weight: 800;
    color: #111;
    margin-bottom: 35px;
    text-align: center;
}

.message {
    margin: 16px 0;
    display: flex;
    flex-direction: column;
}

.message-user {
    align-items: flex-end;
}

.message-bot {
    align-items: flex-start;
}

.message-label {
    font-size: 11px;
    font-weight: 700;
    color: #888;
    margin-bottom: 6px;
    text-transform: uppercase;
}

.message-bubble {
    padding: 16px 22px;
    border-radius: 18px;
    max-width: 75%;
    font-size: 15px;
    line-height: 1.6;
}

.message-user .message-bubble {
    background: #eaeaea;
}

.message-bot .message-bubble {
    background: #ffe8d6;
}

/* =========================
   CTA
   ========================= */
.cta {
    background: #111;
    color: white;
    border-radius: 30px;
    padding: 65px 35px;
    text-align: center;
    margin: 80px 0 60px;
}

.cta h2 {
    font-size: 36px;
    margin-bottom: 15px;
}

.cta p {
    font-size: 20px;
    opacity: 0.9;
}

/* =========================
   BUTTON
   ========================= */
.stButton > button {
    background: #ff7a18;
    color: white;
    border-radius: 999px;
    padding: 18px 28px;
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
        Atiende llamadas reales, conversa como una persona
        y responde usando los datos de tu negocio.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# PHONE DEMO
# =========================
st.markdown("""
<div class="phone-card">
    <h2>Probalo en vivo</h2>
    <p>Llamá ahora y hablá con el asistente telefónico</p>
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
<div class="features-header">
    <div class="phone-icon">📞</div>
    <div class="divider-line"></div>
    <h2>Qué hace este asistente</h2>
</div>

<div class="section">
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
        <p>Identifica clientes reales y toma datos útiles.</p>
    </div>
    <div class="card">
        <span>📅</span>
        <h3>Agenda acciones</h3>
        <p>Coordina visitas, pruebas o seguimientos.</p>
    </div>
    <div class="card">
        <span>⚙️</span>
        <h3>Personalizable</h3>
        <p>Se adapta 100% a tu rubro y tu información.</p>
    </div>
</div>
</div>
""", unsafe_allow_html=True)

# =========================
# EJEMPLO DE CONVERSACIÓN
# =========================

st.markdown("""
<div class="conversation-example">
    <div class="conv-title">💬 Ejemplo de Conversación Real</div>

    <div class="message message-bot">
        <div class="message-label">Asistente</div>
        <div class="message-bubble">
            ¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?
        </div>
    </div>

    <div class="message message-user">
        <div class="message-label">Cliente</div>
        <div class="message-bubble">
            Busco un auto usado
        </div>
    </div>

    <div class="message message-bot">
        <div class="message-label">Asistente</div>
        <div class="message-bubble">
            Dale, perfecto. ¿Qué presupuesto tenés más o menos?
        </div>
    </div>

    <div class="message message-user">
        <div class="message-label">Cliente</div>
        <div class="message-bubble">
            Unos 10 millones
        </div>
    </div>

    <div class="message message-bot">
        <div class="message-label">Asistente</div>
        <div class="message-bubble">
            Genial. Tengo 2 opciones excelentes: un Gol Trend 2020 a 9.8 millones con 55 mil km,
            único dueño. O un Focus 2019 a 12.9 millones con 65 mil km y service al día.
            ¿Cuál te copa más?
        </div>
    </div>

    <div class="message message-user">
        <div class="message-label">Cliente</div>
        <div class="message-bubble">
            El Gol. ¿Puedo hacer un test drive?
        </div>
    </div>

    <div class="message message-bot">
        <div class="message-label">Asistente</div>
        <div class="message-bubble">
            ¡Claro! Te agendo el test drive del Gol. ¿Tu nombre completo?
        </div>
    </div>

    <div class="message message-user">
        <div class="message-label">Cliente</div>
        <div class="message-bubble">
            Juan Pérez
        </div>
    </div>

    <div class="message message-bot">
        <div class="message-label">Asistente</div>
        <div class="message-bubble">
            Perfecto Juan. ¿Tu teléfono?
        </div>
    </div>

    <div class="message message-user">
        <div class="message-label">Cliente</div>
        <div class="message-bubble">
            099 123 456
        </div>
    </div>

    <div class="message message-bot">
        <div class="message-label">Asistente</div>
        <div class="message-bubble">
            Listo Juan. Agendé tu test drive del Gol Trend.
            Un vendedor te contacta en 10 minutos para confirmar día y horario.
            ¡Gracias por comunicarte!
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# =========================
# CTA
# =========================
st.markdown("""
<div class="cta">
    <h2>No es un chatbot genérico</h2>
    <p>
        Es un asistente entrenado con datos reales,
        diseñado para atender, vender y escalar tu negocio.
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

st.caption("Demo visual del Asistente Telefónico · MercadoBot")
