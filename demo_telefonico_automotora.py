import streamlit as st

st.set_page_config(
    page_title="Demo Asistente Telefónico",
    page_icon="📞",
    layout="centered"
)

# CSS super simple
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background: #f8f9fa !important;
}

div[data-testid="stMetricValue"] {
    color: #ff6b00 !important;
    font-size: 2rem !important;
}

.stButton > button {
    background: linear-gradient(135deg, #f4b400, #ff6b00) !important;
    color: white !important;
    padding: 1rem 2rem !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================
st.markdown("""
<div style="background: linear-gradient(135deg, #f4b400, #ff6b00); padding: 50px 20px; border-radius: 15px; text-align: center;">
    <h1 style="color: white; margin: 0; font-size: 42px;">📞 Asistente Telefónico con IA</h1>
    <p style="color: white; margin-top: 15px; font-size: 18px; opacity: 0.95;">Conversá con nuestro vendedor virtual. Atiende 24/7 como una persona real.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# NÚMERO DE TELÉFONO
# ==========================================
st.markdown("""
<div style="background: white; padding: 50px 30px; border-radius: 15px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <h2 style="color: #333; margin-bottom: 15px;">🎙️ Probalo Ahora</h2>
    <p style="color: #666; font-size: 16px; margin-bottom: 30px;">Llamá desde tu celular y conversá con el asistente.<br>Te va a sorprender lo natural que suena.</p>
    
    <div style="background: linear-gradient(135deg, #f4b400, #ff6b00); padding: 40px 20px; border-radius: 15px; margin: 20px 0;">
        <div style="font-size: 60px; margin-bottom: 15px;">📞</div>
        <div style="font-size: 36px; font-weight: bold; color: white; margin: 15px 0;">
            <a href="tel:+5981234567" style="color: white; text-decoration: none;">+598 1234 5678</a>
        </div>
        <p style="color: white; font-size: 14px; margin-top: 10px;">👆 Tap para llamar desde móvil</p>
    </div>
    
    <div style="background: #e8f5e9; padding: 12px 20px; border-radius: 25px; display: inline-block; margin-top: 20px;">
        <span style="color: #2e7d32; font-weight: 600;">✅ Disponible 24/7 · Llamá cuando quieras</span>
    </div>
    
    <p style="color: #888; font-size: 14px; margin-top: 20px;">💡 Es un demo gratuito. Probá todas las funciones sin costo.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# CARACTERÍSTICAS
# ==========================================
st.markdown("<h2 style='text-align: center; color: #333;'>✨ Qué Puede Hacer</h2>", unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background: white; padding: 25px; border-radius: 12px; margin-bottom: 15px; border-left: 4px solid #ff6b00; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size: 32px; margin-bottom: 10px;">🗣️</div>
        <h3 style="color: #333; font-size: 18px; margin-bottom: 8px;">Conversación Natural</h3>
        <p style="color: #666; font-size: 14px; margin: 0;">Habla como una persona real. Entiende español argentino perfectamente.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 25px; border-radius: 12px; margin-bottom: 15px; border-left: 4px solid #ff6b00; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size: 32px; margin-bottom: 10px;">💳</div>
        <h3 style="color: #333; font-size: 18px; margin-bottom: 8px;">Explica Financiación</h3>
        <p style="color: #666; font-size: 14px; margin: 0;">Detalla cuotas, tasas, anticipo y formas de pago. Calcula en el momento.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 25px; border-radius: 12px; margin-bottom: 15px; border-left: 4px solid #ff6b00; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size: 32px; margin-bottom: 10px;">🔄</div>
        <h3 style="color: #333; font-size: 18px; margin-bottom: 8px;">Tasa Usado</h3>
        <p style="color: #666; font-size: 14px; margin: 0;">Pregunta por tu auto y coordina tasación sin cargo. Toma marca, modelo, año.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 25px; border-radius: 12px; margin-bottom: 15px; border-left: 4px solid #ff6b00; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size: 32px; margin-bottom: 10px;">📝</div>
        <h3 style="color: #333; font-size: 18px; margin-bottom: 8px;">Califica Leads</h3>
        <p style="color: #666; font-size: 14px; margin: 0;">Identifica clientes reales. Pregunta presupuesto, urgencia y necesidades.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: white; padding: 25px; border-radius: 12px; margin-bottom: 15px; border-left: 4px solid #ff6b00; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size: 32px; margin-bottom: 10px;">🚗</div>
        <h3 style="color: #333; font-size: 18px; margin-bottom: 8px;">Conoce el Stock</h3>
        <p style="color: #666; font-size: 14px; margin: 0;">Sabe todos los autos disponibles, precios y características al detalle.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 25px; border-radius: 12px; margin-bottom: 15px; border-left: 4px solid #ff6b00; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size: 32px; margin-bottom: 10px;">📅</div>
        <h3 style="color: #333; font-size: 18px; margin-bottom: 8px;">Agenda Test Drives</h3>
        <p style="color: #666; font-size: 14px; margin: 0;">Toma tus datos y coordina visitas o pruebas de manejo automáticamente.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 25px; border-radius: 12px; margin-bottom: 15px; border-left: 4px solid #ff6b00; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size: 32px; margin-bottom: 10px;">⏰</div>
        <h3 style="color: #333; font-size: 18px; margin-bottom: 8px;">24/7 Disponible</h3>
        <p style="color: #666; font-size: 14px; margin: 0;">Nunca pierde una llamada. Atiende de madrugada, fines de semana, feriados.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 25px; border-radius: 12px; margin-bottom: 15px; border-left: 4px solid #ff6b00; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size: 32px; margin-bottom: 10px;">🎯</div>
        <h3 style="color: #333; font-size: 18px; margin-bottom: 8px;">Sin Errores</h3>
        <p style="color: #666; font-size: 14px; margin: 0;">Siempre profesional. Nunca se olvida información. Consistencia garantizada.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ==========================================
# CONVERSACIÓN
# ==========================================
st.markdown("<h2 style='text-align: center; color: #333;'>💬 Conversación Real</h2>", unsafe_allow_html=True)
st.caption("Así suena una llamada típica con el asistente")
st.write("")

with st.chat_message("assistant"):
    st.write("¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?")

with st.chat_message("user"):
    st.write("Busco un auto usado")

with st.chat_message("assistant"):
    st.write("Dale, perfecto. ¿Qué presupuesto tenés más o menos?")

with st.chat_message("user"):
    st.write("Unos 10 millones")

with st.chat_message("assistant"):
    st.write("Genial. Tengo 2 opciones: un **Gol Trend 2020** a **$9.8 millones** o un **Focus 2019** a **$12.9 millones**. ¿Cuál te copa más?")

with st.chat_message("user"):
    st.write("El Gol. ¿Puedo hacer un test drive?")

with st.chat_message("assistant"):
    st.write("¡Claro! Te agendo el test drive. ¿Tu nombre completo?")

with st.chat_message("user"):
    st.write("Juan Pérez")

with st.chat_message("assistant"):
    st.write("Listo Juan, **cero nueve nueve, uno dos tres, cuatro cinco seis**. Agendé tu test drive del Gol Trend. Un vendedor te contacta en 10 minutos. ¡Gracias!")

st.write("")
st.write("")

# ==========================================
# ESTADÍSTICAS
# ==========================================
st.markdown("<h2 style='text-align: center; color: #333;'>📊 Resultados Comprobados</h2>", unsafe_allow_html=True)
st.write("")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Disponibilidad", "24/7")

with col2:
    st.metric("Llamadas", "100%", delta="+30%")

with col3:
    st.metric("Tiempo", "3 min", delta="-5 min")

with col4:
    st.metric("Leads", "85%", delta="+40%")

st.write("")
st.write("")

# ==========================================
# CTA FINAL
# ==========================================
st.markdown("""
<div style="background: white; padding: 50px 30px; border-radius: 15px; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <h2 style="color: #333; margin-bottom: 15px;">¿Listo para Probarlo?</h2>
    <p style="color: #666; font-size: 18px; margin-bottom: 30px;">Llamá ahora y conversá con el asistente.<br>Es completamente <strong>gratis</strong> y podés probar todas las funciones.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button("📞 Llamar +598 1234 5678", "tel:+5981234567", use_container_width=True)

st.write("")
st.write("")

# ==========================================
# FOOTER
# ==========================================
st.divider()
st.caption("💡 Este es un demo funcional. En producción se personaliza 100% con tu negocio.")
st.caption("🔒 IA de última generación (GPT-4 + ElevenLabs). Funcionamiento 24/7.")
st.caption("⚡ ROI: Se paga solo en 30 días. +40% conversión en llamadas.")
