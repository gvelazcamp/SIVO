import streamlit as st
import os

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
   HERO COMPACTO
   ========================= */
.hero-compact {
    text-align: center;
    padding: 40px 30px 20px;
    background: white;
    border-radius: 24px;
    margin: 20px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.hero-compact h1 {
    font-size: 48px;
    font-weight: 800;
    color: #111;
    margin-bottom: 10px;
    line-height: 1.1;
}

.hero-compact .sivo-name {
    color: #ff7a18;
}

.hero-compact p {
    font-size: 17px;
    color: #666;
    max-width: 650px;
    margin: 0 auto;
    line-height: 1.5;
}

/* =========================
   AUDIO SECTION - MÁS INTEGRADO
   ========================= */
.audio-section {
    background: linear-gradient(135deg, #ff7a18, #ff9f43);
    color: white;
    border-radius: 24px;
    padding: 35px 30px;
    margin: 30px 0 40px;
    box-shadow: 0 20px 50px rgba(255,122,24,0.25);
}

.audio-section h2 {
    font-size: 26px;
    margin-bottom: 20px;
    font-weight: 700;
    text-align: center;
}

.audio-caption {
    background: white;
    padding: 12px 24px;
    border-radius: 999px;
    margin: 15px auto 0;
    max-width: 350px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.audio-caption p {
    margin: 0;
    font-size: 14px;
    color: #333;
    font-weight: 600;
}

/* =========================
   FEATURES HEADER
   ========================= */
.features-header {
    text-align: center;
    margin: 50px 0 35px;
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
    padding: 0 20px 40px;
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
   CONVERSACIÓN
   ========================= */
.conversation-title {
    text-align: center;
    margin: 50px 0 30px;
}

.conversation-title h3 {
    font-size: 28px;
    font-weight: 800;
    color: #111;
    margin-bottom: 8px;
}

.conversation-title p {
    color: #666;
    font-size: 16px;
}

/* =========================
   CTA SIMPLE
   ========================= */
.cta-simple {
    background: linear-gradient(135deg, #1f2937, #111827);
    color: white;
    border-radius: 24px;
    padding: 45px 35px;
    text-align: center;
    margin: 60px 0 40px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.15);
}

.cta-simple h2 {
    font-size: 28px;
    margin-bottom: 10px;
    font-weight: 700;
}

.cta-simple p {
    font-size: 17px;
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

/* Audio player personalizado */
audio {
    width: 100%;
    outline: none;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-compact h1 {
        font-size: 38px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# HERO COMPACTO
# =========================
st.markdown("""
<div class="hero-compact">
    <h1>Conocé a <span class="sivo-name">SIVO</span></h1>
    <p>
        Tu asistente telefónico con IA que conversa como una persona<br>
        y responde usando los datos reales de tu negocio
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# AUDIO SECTION
# =========================
st.markdown("""
<div class="audio-section">
    <h2>🎧 Escuchá cómo atiende</h2>
""", unsafe_allow_html=True)

# Verificar si existe el archivo de audio
audio_file = "Sivo.mp4"
if os.path.exists(audio_file):
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes, format='audio/mp4')
else:
    st.markdown("""
    <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 12px;">
        <p style="margin: 0; font-size: 15px;">
            🎧 Archivo de audio no encontrado
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="audio-caption">
        <p>Conversación real con un cliente</p>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# FEATURES
# =========================
st.markdown("""
<div class="features-header">
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
# CONVERSACIÓN
# =========================
st.markdown("""
<div class="conversation-title">
    <h3>Ejemplo de conversación</h3>
    <p>Así atiende a tus clientes potenciales</p>
</div>

<div style="max-width: 650px; margin: auto; padding: 0 20px;">
<div style="background: #000; color: white; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px;"><strong>👤</strong> Busco un auto usado</div>

<div style="background: white; color: black; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px; margin-left: auto; border: 1px solid #e0e0e0;"><strong>🤖</strong> ¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?</div>

<div style="background: #000; color: white; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px;"><strong>👤</strong> Unos 10 millones</div>

<div style="background: white; color: black; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px; margin-left: auto; border: 1px solid #e0e0e0;"><strong>🤖</strong> Dale, perfecto. ¿Qué presupuesto tenés más o menos?</div>

<div style="background: #000; color: white; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px;"><strong>👤</strong> El Gol. ¿Puedo hacer un test drive?</div>

<div style="background: white; color: black; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px; margin-left: auto; border: 1px solid #e0e0e0;"><strong>🤖</strong> Genial. Tengo 2 opciones excelentes: un Gol Trend 2020 a 9.8 millones con 55 mil km, único dueño. O un Focus 2019 a 12.9 millones con 65 mil km y service al día. ¿Cuál te copa más?</div>

<div style="background: #000; color: white; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px;"><strong>👤</strong> Juan Pérez</div>

<div style="background: white; color: black; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px; margin-left: auto; border: 1px solid #e0e0e0;"><strong>🤖</strong> ¡Claro! Te agendo el test drive del Gol. ¿Tu nombre completo?</div>

<div style="background: #000; color: white; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px;"><strong>👤</strong> 099 123 456</div>

<div style="background: white; color: black; padding: 16px 20px; border-radius: 18px; max-width: 70%; margin-bottom: 12px; margin-left: auto; border: 1px solid #e0e0e0;"><strong>🤖</strong> Perfecto Juan. ¿Tu teléfono?</div>

<div style="background: white; color: black; padding: 16px 20px; border-radius: 18px; max-width: 75%; margin-bottom: 12px; margin-left: auto; border: 1px solid #e0e0e0;"><strong>🤖</strong> Listo Juan, cero nueve nueve, uno dos tres, cuatro cinco seis. Agendé tu test drive del Gol Trend. Un vendedor te contacta en 10 minutos para confirmar día y horario. ¡Gracias por llamar!</div>
</div>
""", unsafe_allow_html=True)

# =========================
# CTA SIMPLE
# =========================
st.markdown("""
<div class="cta-simple">
    <h2>¿Listo para probar?</h2>
    <p>
        Hablemos de cómo puede ayudar a tu negocio
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# BOTÓN CONTACTAR
# =========================
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("💬 Hablar con Gonzalo", use_container_width=True):
        st.markdown("""
        <script>
        window.open("https://wa.me/59892748175?text=Hola!%20Quiero%20probar%20SIVO%20🤖", "_blank");
        </script>
        """, unsafe_allow_html=True)

st.caption("Demo de SIVO - Asistente Telefónico Inteligente")
