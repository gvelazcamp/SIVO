import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Demo Asistente Telefónico - MercadoBot",
    page_icon="📞",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
<style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilos generales */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Header personalizado */
    .custom-header {
        text-align: center;
        padding: 40px 25px;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    .custom-header h1 {
        margin: 0;
        font-size: 42px;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .custom-header p {
        margin: 15px 0 0 0;
        color: #666;
        font-size: 18px;
        font-weight: 400;
    }
    
    /* Tarjeta principal */
    .phone-card {
        background: white;
        padding: 50px 40px;
        border-radius: 25px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 15px 50px rgba(0,0,0,0.15);
    }
    
    .phone-display {
        background: linear-gradient(135deg, #667eea, #764ba2);
        padding: 50px 30px;
        border-radius: 20px;
        margin: 30px 0;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .phone-icon {
        font-size: 80px;
        margin-bottom: 20px;
    }
    
    .phone-number {
        font-size: 48px;
        font-weight: bold;
        color: white;
        letter-spacing: 3px;
        margin: 20px 0;
        text-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    .phone-number a {
        color: white;
        text-decoration: none;
    }
    
    .availability {
        background: #e8f5e9;
        padding: 15px 25px;
        border-radius: 50px;
        display: inline-block;
        margin: 20px 0;
        font-weight: 600;
        color: #2e7d32;
    }
    
    .availability-dot {
        display: inline-block;
        width: 10px;
        height: 10px;
        background: #4caf50;
        border-radius: 50%;
        margin-right: 10px;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.4; }
    }
    
    /* Features */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        margin: 30px 0;
    }
    
    .feature-item {
        background: #f8f9ff;
        padding: 25px;
        border-radius: 15px;
        text-align: left;
        transition: all 0.3s;
    }
    
    .feature-item:hover {
        background: #e8ecff;
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.2);
    }
    
    .feature-icon {
        font-size: 36px;
        margin-bottom: 15px;
    }
    
    .feature-title {
        font-size: 18px;
        font-weight: 700;
        color: #333;
        margin-bottom: 10px;
    }
    
    .feature-desc {
        font-size: 14px;
        color: #666;
        line-height: 1.6;
    }
    
    /* Conversation example */
    .conversation-example {
        background: white;
        padding: 30px;
        border-radius: 20px;
        margin: 30px 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
    
    .conv-title {
        font-size: 24px;
        font-weight: 700;
        color: #333;
        margin-bottom: 25px;
        text-align: center;
    }
    
    .message {
        margin: 15px 0;
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
        font-weight: 600;
        color: #888;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .message-bubble {
        padding: 15px 20px;
        border-radius: 18px;
        max-width: 75%;
        font-size: 15px;
        line-height: 1.5;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .message-user .message-bubble {
        background: #667eea;
        color: white;
        border-bottom-right-radius: 5px;
    }
    
    .message-bot .message-bubble {
        background: #f0f0f0;
        color: #333;
        border-bottom-left-radius: 5px;
    }
    
    /* Stats */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 15px;
        margin: 30px 0;
    }
    
    .stat-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .stat-number {
        font-size: 42px;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 8px;
    }
    
    .stat-label {
        font-size: 13px;
        color: #666;
        font-weight: 600;
    }
    
    /* CTA Section */
    .cta-section {
        background: white;
        padding: 50px 40px;
        border-radius: 25px;
        text-align: center;
        margin: 40px 0;
        box-shadow: 0 15px 50px rgba(0,0,0,0.15);
    }
    
    .cta-title {
        font-size: 32px;
        font-weight: 700;
        color: #333;
        margin-bottom: 15px;
    }
    
    .cta-text {
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    
    /* Botones de Streamlit personalizados */
    div[data-testid="column"] > div > div > button {
        width: 100%;
        border-radius: 50px;
        padding: 18px 20px;
        font-weight: 600;
        font-size: 16px;
        transition: all 0.3s ease;
        border: 2px solid #667eea;
        background: white;
        color: #667eea;
    }
    
    div[data-testid="column"] > div > div > button:hover {
        background: #667eea;
        border-color: #667eea;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .feature-grid {
            grid-template-columns: 1fr;
        }
        
        .stats-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .phone-number {
            font-size: 32px;
        }
        
        .custom-header h1 {
            font-size: 32px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header personalizado
st.markdown("""
<div class="custom-header">
    <h1>📞 Asistente Telefónico con IA</h1>
    <p>Conversá con nuestro vendedor virtual. Atiende 24/7 como una persona real.</p>
</div>
""", unsafe_allow_html=True)

# TARJETA PRINCIPAL - NÚMERO DE TELÉFONO
st.markdown("""
<div class="phone-card">
    <h2 style="font-size: 32px; color: #333; margin-bottom: 15px;">🎙️ Probalo Ahora</h2>
    <p style="font-size: 18px; color: #666; margin-bottom: 30px;">
        Llamá desde tu celular y conversá con el asistente.<br>
        Te va a sorprender lo natural que suena.
    </p>
    
    <div class="phone-display">
        <div class="phone-icon">📞</div>
        <div class="phone-number">
            <a href="tel:+5981234567">+598 1234 5678</a>
        </div>
        <p style="color: white; opacity: 0.9; font-size: 16px; margin-top: 15px;">
            Tap para llamar desde móvil
        </p>
    </div>
    
    <div class="availability">
        <span class="availability-dot"></span>
        Disponible 24/7 · Llamá cuando quieras
    </div>
    
    <p style="margin-top: 30px; font-size: 14px; color: #888;">
        💡 Es un demo gratuito. Probá todas las funciones sin costo.
    </p>
</div>
""", unsafe_allow_html=True)

# CARACTERÍSTICAS
st.markdown("""
<div style="background: white; padding: 40px; border-radius: 25px; margin: 30px 0; box-shadow: 0 15px 50px rgba(0,0,0,0.15);">
    <h2 style="font-size: 28px; color: #333; margin-bottom: 30px; text-align: center;">
        ✨ Qué Puede Hacer
    </h2>
    
    <div class="feature-grid">
        <div class="feature-item">
            <div class="feature-icon">🗣️</div>
            <div class="feature-title">Conversación Natural</div>
            <div class="feature-desc">
                Habla como una persona real. Entiende español argentino perfectamente.
            </div>
        </div>
        
        <div class="feature-item">
            <div class="feature-icon">🚗</div>
            <div class="feature-title">Conoce el Stock</div>
            <div class="feature-desc">
                Sabe todos los autos disponibles, precios y características al detalle.
            </div>
        </div>
        
        <div class="feature-item">
            <div class="feature-icon">💳</div>
            <div class="feature-title">Explica Financiación</div>
            <div class="feature-desc">
                Detalla cuotas, tasas, anticipo y todas las formas de pago disponibles.
            </div>
        </div>
        
        <div class="feature-item">
            <div class="feature-icon">📅</div>
            <div class="feature-title">Agenda Test Drives</div>
            <div class="feature-desc">
                Toma tus datos y coordina visitas o pruebas de manejo automáticamente.
            </div>
        </div>
        
        <div class="feature-item">
            <div class="feature-icon">🔄</div>
            <div class="feature-title">Tasa Usado</div>
            <div class="feature-desc">
                Pregunta por tu auto usado y coordina la tasación sin cargo.
            </div>
        </div>
        
        <div class="feature-item">
            <div class="feature-icon">⏰</div>
            <div class="feature-title">24/7 Disponible</div>
            <div class="feature-desc">
                Nunca pierde una llamada. Atiende de madrugada, fines de semana, feriados.
            </div>
        </div>
        
        <div class="feature-item">
            <div class="feature-icon">📝</div>
            <div class="feature-title">Califica Leads</div>
            <div class="feature-desc">
                Identifica clientes reales y toma sus datos para que cierres la venta.
            </div>
        </div>
        
        <div class="feature-item">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Sin Errores</div>
            <div class="feature-desc">
                Siempre profesional, nunca se olvida información, nunca tiene un mal día.
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# EJEMPLO DE CONVERSACIÓN
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
            Listo Juan, cero nueve nueve, uno dos tres, cuatro cinco seis. Agendé tu test drive 
            del Gol Trend. Un vendedor te contacta en 10 minutos para confirmar día y horario. 
            ¡Gracias por llamar!
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ESTADÍSTICAS
st.markdown("""
<div style="background: white; padding: 40px; border-radius: 25px; margin: 30px 0; box-shadow: 0 15px 50px rgba(0,0,0,0.15);">
    <h2 style="font-size: 28px; color: #333; margin-bottom: 30px; text-align: center;">
        📊 Resultados Reales
    </h2>
    
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Disponibilidad</div>
        </div>
        
        <div class="stat-card">
            <div class="stat-number">100%</div>
            <div class="stat-label">Llamadas Atendidas</div>
        </div>
        
        <div class="stat-card">
            <div class="stat-number">3 min</div>
            <div class="stat-label">Tiempo Promedio</div>
        </div>
        
        <div class="stat-card">
            <div class="stat-number">85%</div>
            <div class="stat-label">Leads Calificados</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# CTA FINAL
st.markdown("""
<div class="cta-section">
    <div class="cta-title">¿Listo para Probarlo?</div>
    <div class="cta-text">
        Llamá ahora y conversá con el asistente. Es completamente gratis y podés probar todas las funciones.
    </div>
</div>
""", unsafe_allow_html=True)

# Botones de acción
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("📞 Llamar +598 1234 5678", use_container_width=True):
        st.markdown("""
        <script>
        window.location.href = "tel:+5981234567";
        </script>
        """, unsafe_allow_html=True)

st.divider()

# Footer
st.caption("💡 **Nota:** Este es un demo funcional. El asistente está configurado para una automotora de ejemplo. En producción se personaliza 100% con tu negocio.")
st.caption("🔒 Todas las llamadas son procesadas con IA de última generación. Funcionamiento garantizado 24/7.")

# Opcional: Botón de reset o volver
st.divider()
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("← Volver a Demos", use_container_width=True):
        st.markdown('<meta http-equiv="refresh" content="0; url=/" />', unsafe_allow_html=True)
