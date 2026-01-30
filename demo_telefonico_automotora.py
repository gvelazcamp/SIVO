import streamlit as st

st.set_page_config(
    page_title="Demo Asistente Telefónico - MercadoBot",
    page_icon="📞",
    layout="centered"
)

# CSS limpio y profesional - estilo MercadoBot
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fondo blanco limpio */
    .stApp {
        background: #f8f9fa;
    }
    
    .main .block-container {
        padding: 2rem 1rem;
        max-width: 900px;
    }
    
    /* Mejorar métricas */
    div[data-testid="stMetricValue"] {
        font-size: 2.5rem !important;
        color: #ff6b00 !important;
        font-weight: bold !important;
    }
    
    /* Botones con gradiente naranja */
    .stButton > button, .stLinkButton > a {
        background: linear-gradient(135deg, #f4b400, #ff6b00) !important;
        color: white !important;
        border: none !important;
        padding: 1rem 2.5rem !important;
        font-size: 1.3rem !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(255, 107, 0, 0.3) !important;
        transition: all 0.3s !important;
    }
    
    .stButton > button:hover, .stLinkButton > a:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 107, 0, 0.4) !important;
    }
    
    /* Success boxes naranjas */
    .element-container div[data-testid="stMarkdownContainer"] div[data-baseweb="notification"] {
        background-color: #fff3e0 !important;
        border-left: 4px solid #ff6b00 !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER PROFESIONAL
# ==========================================
st.markdown("""
<div style="background: linear-gradient(135deg, #f4b400, #ff6b00); padding: 50px 30px; border-radius: 15px; text-align: center; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    <h1 style="margin: 0; font-size: 48px; font-weight: 700; color: white;">
        📞 Asistente Telefónico con IA
    </h1>
    <p style="margin: 20px 0 0 0; color: white; font-size: 20px; opacity: 0.95;">
        Conversá con nuestro vendedor virtual. Atiende 24/7 como una persona real.
    </p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# NÚMERO DE TELÉFONO - DESTACADO
# ==========================================
st.markdown("""
<div style="background: white; padding: 60px 40px; border-radius: 15px; text-align: center; margin: 30px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.08);">
    <h2 style="color: #333; font-size: 32px; margin-bottom: 15px; font-weight: 700;">
        🎙️ Probalo Ahora
    </h2>
    <p style="color: #666; font-size: 18px; margin-bottom: 40px; line-height: 1.6;">
        Llamá desde tu celular y conversá con el asistente.<br>
        Te va a sorprender lo natural que suena.
    </p>
    
    <div style="background: linear-gradient(135deg, #f4b400, #ff6b00); padding: 50px 30px; border-radius: 15px; margin: 30px auto; max-width: 500px;">
        <div style="font-size: 80px; margin-bottom: 20px;">📞</div>
        <div style="font-size: 48px; font-weight: bold; color: white; letter-spacing: 2px; margin: 20px 0;">
            <a href="tel:+5981234567" style="color: white; text-decoration: none;">+598 1234 5678</a>
        </div>
        <p style="color: white; opacity: 0.95; font-size: 16px; margin-top: 15px; font-weight: 500;">
            👆 Tap para llamar desde móvil
        </p>
    </div>
    
    <div style="background: #e8f5e9; padding: 15px 30px; border-radius: 50px; display: inline-block; margin: 25px 0; font-weight: 600; color: #2e7d32;">
        <span style="display: inline-block; width: 12px; height: 12px; background: #4caf50; border-radius: 50%; margin-right: 10px;"></span>
        Disponible 24/7 · Llamá cuando quieras
    </div>
    
    <p style="margin-top: 30px; font-size: 15px; color: #888;">
        💡 Es un demo gratuito. Probá todas las funciones sin costo.
    </p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# CARACTERÍSTICAS
# ==========================================
st.markdown("""
<div style="margin: 40px 0 30px 0;">
    <h2 style="text-align: center; color: #333; font-size: 36px; font-weight: 700;">
        ✨ Qué Puede Hacer
    </h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #ff6b00;">
        <div style="font-size: 40px; margin-bottom: 15px;">🗣️</div>
        <h3 style="color: #333; font-size: 20px; font-weight: 700; margin-bottom: 10px;">Conversación Natural</h3>
        <p style="color: #666; font-size: 15px; line-height: 1.6; margin: 0;">
            Habla como una persona real. Entiende español argentino perfectamente con todas sus expresiones.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #ff6b00;">
        <div style="font-size: 40px; margin-bottom: 15px;">💳</div>
        <h3 style="color: #333; font-size: 20px; font-weight: 700; margin-bottom: 10px;">Explica Financiación</h3>
        <p style="color: #666; font-size: 15px; line-height: 1.6; margin: 0;">
            Detalla cuotas, tasas, anticipo y todas las formas de pago disponibles. Calcula en el momento.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #ff6b00;">
        <div style="font-size: 40px; margin-bottom: 15px;">🔄</div>
        <h3 style="color: #333; font-size: 20px; font-weight: 700; margin-bottom: 10px;">Tasa Usado</h3>
        <p style="color: #666; font-size: 15px; line-height: 1.6; margin: 0;">
            Pregunta por tu auto usado y coordina la tasación sin cargo. Toma marca, modelo, año y km.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #ff6b00;">
        <div style="font-size: 40px; margin-bottom: 15px;">📝</div>
        <h3 style="color: #333; font-size: 20px; font-weight: 700; margin-bottom: 10px;">Califica Leads</h3>
        <p style="color: #666; font-size: 15px; line-height: 1.6; margin: 0;">
            Identifica clientes reales preguntando presupuesto, urgencia y necesidades. Filtra curiosos.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #ff6b00;">
        <div style="font-size: 40px; margin-bottom: 15px;">🚗</div>
        <h3 style="color: #333; font-size: 20px; font-weight: 700; margin-bottom: 10px;">Conoce el Stock</h3>
        <p style="color: #666; font-size: 15px; line-height: 1.6; margin: 0;">
            Sabe todos los autos disponibles, precios y características al detalle. Nunca se confunde.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #ff6b00;">
        <div style="font-size: 40px; margin-bottom: 15px;">📅</div>
        <h3 style="color: #333; font-size: 20px; font-weight: 700; margin-bottom: 10px;">Agenda Test Drives</h3>
        <p style="color: #666; font-size: 15px; line-height: 1.6; margin: 0;">
            Toma tus datos y coordina visitas o pruebas de manejo automáticamente. Confirma fechas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #ff6b00;">
        <div style="font-size: 40px; margin-bottom: 15px;">⏰</div>
        <h3 style="color: #333; font-size: 20px; font-weight: 700; margin-bottom: 10px;">24/7 Disponible</h3>
        <p style="color: #666; font-size: 15px; line-height: 1.6; margin: 0;">
            Nunca pierde una llamada. Atiende de madrugada, fines de semana, feriados. Siempre profesional.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #ff6b00;">
        <div style="font-size: 40px; margin-bottom: 15px;">🎯</div>
        <h3 style="color: #333; font-size: 20px; font-weight: 700; margin-bottom: 10px;">Sin Errores</h3>
        <p style="color: #666; font-size: 15px; line-height: 1.6; margin: 0;">
            Siempre profesional, nunca se olvida información, nunca tiene un mal día. Consistencia garantizada.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# CONVERSACIÓN DE EJEMPLO
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="margin: 40px 0 30px 0;">
    <h2 style="text-align: center; color: #333; font-size: 36px; font-weight: 700;">
        💬 Conversación Real
    </h2>
    <p style="text-align: center; color: #666; font-size: 16px; margin-top: 10px;">
        Así suena una llamada típica con el asistente
    </p>
</div>
""", unsafe_allow_html=True)

with st.chat_message("assistant", avatar="🤖"):
    st.write("¡Hola! Bienvenido a AutoCenter. ¿En qué puedo ayudarte hoy?")

with st.chat_message("user", avatar="👤"):
    st.write("Busco un auto usado")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Dale, perfecto. ¿Qué presupuesto tenés más o menos?")

with st.chat_message("user", avatar="👤"):
    st.write("Unos 10 millones")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Genial. Tengo 2 opciones excelentes: un **Gol Trend 2020** a **$9.8 millones** con 55 mil km, único dueño, service al día. O un **Focus 2019** a **$12.9 millones** con 65 mil km. ¿Cuál te copa más?")

with st.chat_message("user", avatar="👤"):
    st.write("El Gol. ¿Puedo hacer un test drive?")

with st.chat_message("assistant", avatar="🤖"):
    st.write("¡Claro que sí! Te agendo el test drive del Gol Trend. ¿Cuál es tu nombre completo?")

with st.chat_message("user", avatar="👤"):
    st.write("Juan Pérez")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Perfecto Juan. ¿Y tu número de teléfono?")

with st.chat_message("user", avatar="👤"):
    st.write("099 123 456")

with st.chat_message("assistant", avatar="🤖"):
    st.write("Listo Juan, confirmo: **cero nueve nueve, uno dos tres, cuatro cinco seis**. Agendé tu test drive del Gol Trend 2020. Un vendedor te va a contactar en los próximos 10 minutos para confirmar el día y horario que mejor te venga. ¡Muchas gracias por comunicarte con AutoCenter!")

# ==========================================
# ESTADÍSTICAS
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="margin: 40px 0 30px 0;">
    <h2 style="text-align: center; color: #333; font-size: 36px; font-weight: 700;">
        📊 Resultados Comprobados
    </h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Disponibilidad", value="24/7")

with col2:
    st.metric(label="Llamadas Atendidas", value="100%", delta="vs. humanos 70%")

with col3:
    st.metric(label="Tiempo Promedio", value="3 min", delta="-5 min vs. humanos")

with col4:
    st.metric(label="Leads Calificados", value="85%", delta="+40% vs. humanos")

# ==========================================
# CTA FINAL
# ==========================================
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="background: white; padding: 60px 40px; border-radius: 15px; text-align: center; margin: 30px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.08);">
    <h2 style="color: #333; font-size: 40px; font-weight: 700; margin-bottom: 20px;">
        ¿Listo para Probarlo?
    </h2>
    <p style="color: #666; font-size: 20px; margin-bottom: 40px; line-height: 1.6;">
        Llamá ahora y conversá con el asistente.<br>
        Es completamente <strong>gratis</strong> y podés probar todas las funciones.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.link_button("📞 Llamar +598 1234 5678", "tel:+5981234567", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# FOOTER
st.divider()
st.caption("💡 **Nota:** Este es un demo funcional. El asistente está configurado para una automotora de ejemplo. En producción se personaliza 100% con tu negocio, stock real y precios actualizados.")
st.caption("🔒 Todas las llamadas son procesadas con IA de última generación (GPT-4 + ElevenLabs). Funcionamiento garantizado 24/7. Integración con CRM disponible.")
st.caption("⚡ **ROI Promedio:** El sistema se paga solo en 30 días. Clientes reportan aumento del 40% en conversión de llamadas.")
