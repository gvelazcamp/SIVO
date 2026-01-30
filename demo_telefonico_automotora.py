import streamlit as st

st.set_page_config(
    page_title="Demo Asistente Telefónico",
    page_icon="📞",
    layout="centered"
)

# CSS PROFESIONAL
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    .main .block-container {
        padding: 2rem 1rem !important;
        max-width: 900px !important;
    }
    
    h1 {
        color: white !important;
        text-align: center !important;
        font-size: 3rem !important;
        font-weight: 700 !important;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2) !important;
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        color: #667eea !important;
        font-weight: bold !important;
    }
    
    .stButton > button, .stLinkButton > a {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        padding: 1rem 2rem !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        border-radius: 50px !important;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4) !important;
    }
    
    .stButton > button:hover, .stLinkButton > a:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.6) !important;
    }
    
    hr {
        border: none !important;
        height: 2px !important;
        background: rgba(255,255,255,0.2) !important;
        margin: 2rem 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# HEADER
st.title("📞 Asistente Telefónico con IA")
st.markdown("<p style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 2rem;'>Conversá con nuestro vendedor virtual. Atiende 24/7 como una persona real.</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# NÚMERO DESTACADO
st.markdown("""
<div style='background: white; padding: 3rem 2rem; border-radius: 25px; text-align: center; box-shadow: 0 15px 50px rgba(0,0,0,0.2); margin: 2rem 0;'>
    <h2 style='color: #333; font-size: 2rem; margin-bottom: 1rem;'>🎙️ Probalo Ahora</h2>
    <p style='color: #666; font-size: 1.1rem; margin-bottom: 2rem;'>
        Llamá desde tu celular y conversá con el asistente.<br>
        Te va a sorprender lo natural que suena.
    </p>
    
    <div style='background: linear-gradient(135deg, #667eea, #764ba2); padding: 3rem 2rem; border-radius: 20px; margin: 2rem 0;'>
        <div style='font-size: 5rem; margin-bottom: 1rem;'>📞</div>
        <div style='font-size: 3rem; font-weight: bold; color: white; letter-spacing: 3px; margin: 1rem 0;'>
            <a href='tel:+5981234567' style='color: white; text-decoration: none;'>+598 1234 5678</a>
        </div>
        <p style='color: white; opacity: 0.9; font-size: 1rem; margin-top: 1rem;'>
            👆 Tap para llamar desde móvil
        </p>
    </div>
    
    <div style='background: #e8f5e9; padding: 1rem 2rem; border-radius: 50px; display: inline-block; margin: 1.5rem 0; font-weight: 600; color: #2e7d32;'>
        <span style='display: inline-block; width: 10px; height: 10px; background: #4caf50; border-radius: 50%; margin-right: 10px; animation: pulse 2s infinite;'></span>
        Disponible 24/7 · Llamá cuando quieras
    </div>
    
    <p style='margin-top: 2rem; font-size: 0.9rem; color: #888;'>
        💡 Es un demo gratuito. Probá todas las funciones sin costo.
    </p>
</div>

<style>
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}
</style>
""", unsafe_allow_html=True)

# CARACTERÍSTICAS
st.markdown("<br>", unsafe_allow_html=True)
st.header("✨ Qué Puede Hacer")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🗣️ **Conversación Natural**")
    st.write("Habla como una persona real. Entiende español argentino perfectamente.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 💳 **Explica Financiación**")
    st.write("Detalla cuotas, tasas, anticipo y todas las formas de pago disponibles.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 🔄 **Tasa Usado**")
    st.write("Pregunta por tu auto usado y coordina la tasación sin cargo.")

with col2:
    st.markdown("### 🚗 **Conoce el Stock**")
    st.write("Sabe todos los autos disponibles, precios y características al detalle.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### 📅 **Agenda Test Drives**")
    st.write("Toma tus datos y coordina visitas o pruebas de manejo automáticamente.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("### ⏰ **24/7 Disponible**")
    st.write("Nunca pierde una llamada. Atiende de madrugada, fines de semana, feriados.")

# CONVERSACIÓN
st.markdown("<br><br>", unsafe_allow_html=True)
st.header("💬 Ejemplo de Conversación Real")
st.caption("Así suena una llamada típica con el asistente:")

with st.chat_message("assistant"):
    st.write("¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?")

with st.chat_message("user"):
    st.write("Busco un auto usado")

with st.chat_message("assistant"):
    st.write("Dale, perfecto. ¿Qué presupuesto tenés más o menos?")

with st.chat_message("user"):
    st.write("Unos 10 millones")

with st.chat_message("assistant"):
    st.write("Genial. Tengo 2 opciones: un **Gol Trend 2020** a 9.8 millones o un **Focus 2019** a 12.9 millones. ¿Cuál te copa más?")

with st.chat_message("user"):
    st.write("El Gol. ¿Puedo hacer un test drive?")

with st.chat_message("assistant"):
    st.write("¡Claro! Te agendo el test drive. ¿Tu nombre completo?")

with st.chat_message("user"):
    st.write("Juan Pérez")

with st.chat_message("assistant"):
    st.write("Perfecto Juan. ¿Tu teléfono?")

with st.chat_message("user"):
    st.write("099 123 456")

with st.chat_message("assistant"):
    st.write("Listo Juan, **cero nueve nueve, uno dos tres, cuatro cinco seis**. Agendé tu test drive del Gol Trend. Un vendedor te contacta en 10 minutos para confirmar día y horario. ¡Gracias por llamar!")

# ESTADÍSTICAS
st.markdown("<br><br>", unsafe_allow_html=True)
st.header("📊 Resultados Reales")
st.caption("Métricas de rendimiento del asistente:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Disponibilidad", value="24/7")

with col2:
    st.metric(label="Llamadas", value="100%", delta="Todas atendidas")

with col3:
    st.metric(label="Duración", value="3 min", delta="Promedio")

with col4:
    st.metric(label="Leads", value="85%", delta="Calificados")

# CTA FINAL
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style='background: white; padding: 3rem 2rem; border-radius: 25px; text-align: center; box-shadow: 0 15px 50px rgba(0,0,0,0.2);'>
    <h2 style='color: #333; font-size: 2rem; margin-bottom: 1rem;'>¿Listo para Probarlo?</h2>
    <p style='color: #666; font-size: 1.1rem; margin-bottom: 2rem;'>
        Llamá ahora y conversá con el asistente.<br>
        Es completamente gratis y podés probar todas las funciones.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button("📞 Llamar +598 1234 5678", "tel:+5981234567", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# FOOTER
st.divider()
st.caption("💡 **Nota:** Este es un demo funcional. El asistente está configurado para una automotora de ejemplo. En producción se personaliza 100% con tu negocio.")
st.caption("🔒 Todas las llamadas son procesadas con IA de última generación. Funcionamiento garantizado 24/7.")
st.caption("⚡ Costo aproximado: $0.11 USD/minuto. ROI comprobado en menos de 30 días.")
