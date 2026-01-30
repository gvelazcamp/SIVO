import streamlit as st

st.set_page_config(
    page_title="Demo Asistente Telefónico",
    page_icon="📞",
    layout="centered"
)

# CSS mínimo para colores naranjas
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
}

.stButton > button {
    background: linear-gradient(135deg, #f4b400, #ff6b00) !important;
    color: white !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    padding: 0.8rem 2rem !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.title("📞 Asistente Telefónico con IA")
st.subheader("Conversá con nuestro vendedor virtual. Atiende 24/7 como una persona real.")

st.divider()

# NÚMERO
st.header("🎙️ Probalo Ahora")
st.write("Llamá desde tu celular y conversá con el asistente. Te va a sorprender lo natural que suena.")

st.markdown("## 📞")
st.markdown("# **+598 1234 5678**")
st.caption("👆 Tap para llamar desde móvil")

st.success("✅ **Disponible 24/7** · Llamá cuando quieras")
st.info("💡 Es un demo gratuito. Probá todas las funciones sin costo.")

st.divider()

# CARACTERÍSTICAS
st.header("✨ Qué Puede Hacer")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🗣️ Conversación Natural")
    st.write("Habla como una persona real. Entiende español argentino perfectamente.")
    
    st.subheader("💳 Explica Financiación")
    st.write("Detalla cuotas, tasas, anticipo y formas de pago. Calcula en el momento.")
    
    st.subheader("🔄 Tasa Usado")
    st.write("Pregunta por tu auto y coordina tasación sin cargo.")
    
    st.subheader("📝 Califica Leads")
    st.write("Identifica clientes reales. Pregunta presupuesto, urgencia, necesidades.")

with col2:
    st.subheader("🚗 Conoce el Stock")
    st.write("Sabe todos los autos disponibles, precios y características al detalle.")
    
    st.subheader("📅 Agenda Test Drives")
    st.write("Toma tus datos y coordina visitas o pruebas de manejo automáticamente.")
    
    st.subheader("⏰ 24/7 Disponible")
    st.write("Nunca pierde una llamada. Atiende de madrugada, fines de semana, feriados.")
    
    st.subheader("🎯 Sin Errores")
    st.write("Siempre profesional. Nunca se olvida información. Consistencia garantizada.")

st.divider()

# CONVERSACIÓN
st.header("💬 Conversación Real")
st.caption("Así suena una llamada típica con el asistente")

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

st.divider()

# MÉTRICAS
st.header("📊 Resultados Comprobados")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Disponibilidad", "24/7")

with col2:
    st.metric("Llamadas", "100%", delta="+30%")

with col3:
    st.metric("Tiempo", "3 min", delta="-5 min")

with col4:
    st.metric("Leads", "85%", delta="+40%")

st.divider()

# CTA
st.header("¿Listo para Probarlo?")
st.write("Llamá ahora y conversá con el asistente. Es completamente **gratis** y podés probar todas las funciones.")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button("📞 Llamar +598 1234 5678", "tel:+5981234567", use_container_width=True)

st.divider()

# FOOTER
st.caption("💡 Demo funcional. En producción se personaliza 100% con tu negocio.")
st.caption("🔒 IA última generación (GPT-4 + ElevenLabs). Funcionamiento 24/7.")
st.caption("⚡ ROI: Se paga solo en 30 días. +40% conversión.")
