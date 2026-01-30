import streamlit as st

# =========================
# CONFIGURACIÓN DE PÁGINA
# =========================
st.set_page_config(
    page_title="SIVO - Asistente Telefónico IA",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# CSS GLOBAL
# =========================
st.markdown("""
<style>
/* Ocultar elementos de Streamlit */
#MainMenu, footer, header {display: none;}

.stApp {
    background: #f9fafb;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* =========================
   HERO
   ========================= */
.hero {
    text-align: center;
    padding: 60px 30px 30px;
    background: white;
    border-radius: 24px;
    margin: 20px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
    color: #111;
    margin-bottom: 16px;
    line-height: 1.2;
}

.hero .sivo-name {
    color: #ff7a18;
    font-size: 48px;
}

.hero p {
    font-size: 19px;
    color: #555;
    max-width: 700px;
    margin: auto;
    line-height: 1.6;
}

/* =========================
   PHONE CARD
   ========================= */
.phone-card {
    background: linear-gradient(135deg, #ff7a18, #ff9f43);
    color: white;
    border-radius: 24px;
    padding: 45px 35px;
    text-align: center;
    margin: 40px 0;
    box-shadow: 0 20px 50px rgba(255,122,24,0.3);
}

.phone-card h2 {
    font-size: 30px;
    margin-bottom: 12px;
    font-weight: 700;
}

.phone-card p {
    font-size: 17px;
    opacity: 0.95;
}

.phone-number {
    font-size: 44px;
    font-weight: 800;
    letter-spacing: 1px;
    margin: 20px 0;
}

.phone-number a {
    color: white;
    text-decoration: none;
    transition: opacity 0.2s;
}

.phone-number a:hover {
    opacity: 0.9;
}

.badge {
    display: inline-block;
    background: rgba(255,255,255,0.25);
    padding: 10px 20px;
    border-radius: 999px;
    font-weight: 600;
    margin-top: 10px;
    font-size: 14px;
}

/* =========================
   FEATURES HEADER
   ========================= */
.features-header {
    text-align: center;
    margin: 60px 0 40px;
}

.phone-icon {
    font-size: 48px;
    margin-bottom: 10px;
}

.divider-line {
    width: 80px;
    height: 4px;
    background: linear-gradient(90deg, #ff7a18, #ffb347);
    margin: 0 auto 16px;
    border-radius: 10px;
}

.features-header h2 {
    font-size: 32px;
    font-weight: 800;
    color: #111;
}

/* =========================
   FEATURES GRID
   ========================= */
.section {
    padding: 0 20px 50px;
    max-width: 1100px;
    margin: auto;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 24px;
}

.card {
    background: #ffffff;
    border-radius: 20px;
    padding: 32px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    transition: all 0.3s ease;
    border: 1px solid #f0f0f0;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 40px rgba(0,0,0,0.1);
}

.card span {
    font-size: 36px;
    display: block;
    margin-bottom: 12px;
}

.card h3 {
    margin: 12px 0 8px;
    font-size: 19px;
    font-weight: 700;
    color: #111;
}

.card p {
    color: #666;
    line-height: 1.6;
    font-size: 15px;
    margin: 0;
}

/* =========================
   CTA
   ========================= */
.cta {
    background: linear-gradient(135deg, #1f2937, #111827);
    color: white;
    border-radius: 24px;
    padding: 55px 35px;
    text-align: center;
    margin: 70px 0 50px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.15);
}

.cta h2 {
    font-size: 32px;
    margin-bottom: 12px;
    font-weight: 700;
}

.cta p {
    font-size: 18px;
    opacity: 0.9;
    line-height: 1.6;
    max-width: 600px;
    margin: auto;
}

/* =========================
   BUTTON
   ========================= */
.stButton > button {
    background: #ff7a18 !important;
    color: white !important;
    border-radius: 999px !important;
    padding: 16px 32px !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    border: none !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 12px rgba(255,122,24,0.3) !important;
}

.stButton > button:hover {
    background: #ff8f3d !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 16px rgba(255,122,24,0.4) !important;
}

/* Caption */
.stCaption {
    text-align: center;
    color: #999;
    font-size: 13px;
    margin-top: 40px;
}

/* Responsive */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 34px;
    }
    
    .hero .sivo-name {
        font-size: 38px;
    }
    
    .phone-number {
        font-size: 36px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<div class="hero">
    <h1>Conocé a <span class="sivo-name">SIVO</span></h1>
    <p>
        Tu asistente telefónico con IA que atiende llamadas reales,
        conversa como una persona y responde usando los datos de tu negocio.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# PHONE DEMO
# =========================
st.markdown("""
<div class="phone-card">
    <h2>Probalo en vivo</h2>
    <p>Llamá ahora y conversá con el asistente</p>
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
    <h2>Qué hace por tu negocio</h2>
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
# CONVERSACIÓN - SIMPLE Y LINDA (usando st.chat_message para simplicidad)
# =========================
st.markdown("### 💬 Ejemplo de conversación real")
st.caption("Así atiende a tus clientes potenciales")

with st.chat_message("assistant", avatar="🤖"):
    st.write("¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?")

with st.chat_message("user", avatar="👤"):
    st.write("Busco un auto usado")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Dale, perfecto. ¿Qué presupuesto tenés más o menos?")

with st.chat_message("user", avatar="👤"):
    st.write("Unos 10 millones")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Genial. Tengo 2 opciones excelentes: un Gol Trend 2020 a 9.8 millones con 55 mil km, único dueño. O un Focus 2019 a 12.9 millones con 65 mil km y service al día. ¿Cuál te copa más?")

with st.chat_message("user", avatar="👤"):
    st.write("El Gol. ¿Puedo hacer un test drive?")

with st.chat_message("assistant", avatar="🤖"):
    st.write("¡Claro! Te agendo el test drive del Gol. ¿Tu nombre completo?")

with st.chat_message("user", avatar="👤"):
    st.write("Juan Pérez")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Perfecto Juan. ¿Tu teléfono?")

with st.chat_message("user", avatar="👤"):
    st.write("099 123 456")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Listo Juan, cero nueve nueve, uno dos tres, cuatro cinco seis. Agendé tu test drive del Gol Trend. Un vendedor te contacta en 10 minutos para confirmar día y horario. ¡Gracias por llamar!")

# =========================
# CTA
# =========================
st.markdown("""
<div class="cta">
    <h2>No es un chatbot genérico</h2>
    <p>
        Es un asistente entrenado con tus datos reales,
        diseñado para atender, vender y escalar tu negocio.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# BOTÓN LLAMAR
# =========================
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("📞 Llamar ahora", use_container_width=True):
        st.markdown("""
        <script>
        window.location.href = "tel:+5981234567";
        </script>
        """, unsafe_allow_html=True)

st.caption("Demo visual de SIVO - Asistente Telefónico Inteligente")
