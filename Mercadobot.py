import streamlit as st
import streamlit.components.v1 as components

# =========================
# RESPUESTAS DEL CHATBOT
# =========================
CHATBOT_RESPONSES = {
    'hola': '¡Hola! 👋 Bienvenido a MercadoBot. ¿En qué puedo ayudarte?<br><br>Podés preguntarme sobre:<br>• Precios y planes<br>• Integraciones<br>• Cómo funciona<br>• Agendar demo',
    'precio': 'Nuestros planes:<br><br>💰 <strong>Básico:</strong> $25.000/mes<br>• Hasta 1.000 consultas/mes<br>• 1 asistente<br>• Soporte email<br><br>💎 <strong>Pro:</strong> $50.000/mes<br>• Hasta 5.000 consultas/mes<br>• 3 asistentes<br>• Soporte prioritario<br><br>🚀 <strong>Enterprise:</strong> Personalizado<br>• Consultas ilimitadas<br>• Asistentes ilimitados<br>• Soporte dedicado<br><br>Todos incluyen 7 días de prueba gratis! ✨',
    'costo': 'Nuestros planes:<br><br>💰 <strong>Básico:</strong> $25.000/mes<br>💎 <strong>Pro:</strong> $50.000/mes<br>🚀 <strong>Enterprise:</strong> Personalizado<br><br>¿Querés que te cuente más detalles de algún plan?',
    'cuanto': 'El plan <strong>Básico</strong> arranca en $25.000/mes con 7 días de prueba gratuita. ¿Querés conocer todos los planes?',
    'whatsapp': '¡Sí! Nuestro chatbot se integra con:<br><br>✅ WhatsApp<br>✅ Instagram<br>✅ Web<br>✅ Shopify<br>✅ Mercado Pago<br>✅ Email<br><br>¿Cuál te interesa más?',
    'integra': 'Integramos con WhatsApp, Instagram, tu sitio web, Shopify, Mercado Pago, Email y más plataformas. ¿Qué plataforma usás actualmente?',
    'instagram': '¡Sí! Conectamos tu chatbot con Instagram Direct. Responde automáticamente mensajes y comentarios 24/7. ¿Querés ver cómo funciona?',
    'funciona': 'Es súper simple en 3 pasos:<br><br>🔌 <strong>1. Conectás</strong><br>Vinculás tus datos, productos o servicios<br><br>🧠 <strong>2. Entrenás</strong><br>El asistente aprende sobre tu negocio<br><br>🚀 <strong>3. Lanzás</strong><br>Lo instalamos y empieza a atender clientes<br><br>¿Querés agendar una demo?',
    'demo': '¡Perfecto! Para agendar tu demo gratuita:<br><br>📧 Escribinos a: <strong>hola@mercadobot.com</strong><br>💬 O dejame tu email y te contactamos en 24hs<br><br>¿Cuál preferís?',
    'contacto': 'Podés contactarnos por:<br><br>📧 <strong>Email:</strong> hola@mercadobot.com<br>💬 <strong>Chat:</strong> Estás hablando conmigo! 😊<br><br>Respondemos en menos de 24hs.',
    'gratis': '¡Sí! Tenés <strong>7 días de prueba GRATIS</strong>:<br><br>✅ Sin tarjeta de crédito<br>✅ Acceso completo<br>✅ Sin compromisos<br>✅ Cancelás cuando quieras<br><br>¿Empezamos?',
    'cancelar': 'Podés cancelar cuando quieras:<br><br>✅ Sin permanencia<br>✅ Sin penalizaciones<br>✅ Simple y rápido<br><br>Somos 100% transparentes 💯',
    'programa': '¡NO necesitás saber programar! 🎉<br><br>Nosotros configuramos todo:<br>• Instalación completa<br>• Entrenamiento del bot<br>• Integración con tus sistemas<br>• Soporte continuo<br><br>Vos solo nos pasás tu info y listo!',
    'tiempo': 'Tiempos de implementación:<br><br>⚡ <strong>Casos simples:</strong> 2-3 días<br>Chatbot básico con info estándar<br><br>🔧 <strong>Integraciones complejas:</strong> 1-2 semanas<br>Múltiples sistemas, datos complejos<br><br>Te damos un timeline claro desde el inicio 📅',
    'seguro': 'Tu información está 100% protegida:<br><br>🔒 Encriptación de datos<br>✅ Cumplimos normativas de protección<br>🛡️ Servidores seguros<br>🔐 Acceso restringido<br><br>Tanto tus datos como los de tus clientes están seguros 💯',
    'dato': 'Toda la información está encriptada y protegida con los más altos estándares de seguridad. Cumplimos con GDPR y todas las normativas locales. 🔒',
    'buenos': '¡Hola! 👋 ¿En qué puedo ayudarte hoy?',
    'buenos dias': '¡Buenos días! ☀️ ¿Cómo puedo ayudarte?',
    'buenas': '¡Buenas! 👋 ¿Qué te gustaría saber sobre MercadoBot?',
    'ayuda': 'Claro! Puedo ayudarte con:<br><br>💰 Precios y planes<br>🔌 Integraciones (WhatsApp, Web, etc)<br>⚙️ Cómo funciona<br>📅 Agendar demo<br>🎁 Prueba gratis<br><br>¿Qué te interesa?',
    'gracias': '¡De nada! 😊 ¿Te ayudo con algo más?',
    'chau': '¡Hasta pronto! 👋 Si tenés más dudas, acá estoy 24/7 😊',
    'adios': '¡Nos vemos! Si necesitás algo más, escribime cuando quieras 💬',
    'default': 'Hmm, no tengo info específica sobre eso 🤔<br><br>Pero puedo ayudarte con:<br>• Precios<br>• Integraciones<br>• Cómo funciona<br>• Agendar demo<br><br>O escribinos a <strong>hola@mercadobot.com</strong> para consultas específicas.'
}

def get_chatbot_response(message):
    """Busca respuesta basada en keywords"""
    msg = message.lower()
    for keyword, response in CHATBOT_RESPONSES.items():
        if keyword in msg:
            return response
    return CHATBOT_RESPONSES['default']

# =========================
# API CHATBOT
# =========================
def _qp_get(key: str, default: str = "") -> str:
    try:
        v = st.query_params.get(key, default)
    except:
        v = st.experimental_get_query_params().get(key, [default])
    if isinstance(v, list):
        return v[0] if v else default
    return v if v is not None else default

# Interceptar llamada del chatbot
if _qp_get("api") == "chat":
    msg = _qp_get("msg", "")
    if msg:
        respuesta = get_chatbot_response(msg)
        st.markdown(f'<pre id="mbot-response" style="display:none;">{respuesta}</pre>', unsafe_allow_html=True)
    st.stop()

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

st.markdown("""<style>
.main .block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stAppViewContainer"] { padding: 0 !important; }
header[data-testid="stHeader"], footer, #MainMenu { display: none !important; }
</style>""", unsafe_allow_html=True)

try:
    vista = st.query_params.get("vista", "home")
except:
    vista = st.experimental_get_query_params().get("vista", ["home"])[0]

# Aquí iría todo tu HTML (HOME, FOOTER_CHATBOT, etc)
# Lo simplifico para que quepa:

FOOTER_CHATBOT = """
<div class="footer-section" style="background:#1a1a2e;padding:40px;color:white;text-align:center;">
<p>© 2025 MercadoBot</p>
</div>

<div id="chatbot-wrapper" style="position:fixed;bottom:20px;right:20px;z-index:9999;">
<button id="chatbot-button" onclick="toggleChat()" style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#f4b400,#ff6b00);border:none;cursor:pointer;box-shadow:0 4px 15px rgba(244,180,0,0.5);">
💬
</button>

<div id="chatbot-container" style="display:none;position:absolute;bottom:75px;right:0;width:350px;height:420px;background:white;border-radius:20px;box-shadow:0 10px 40px rgba(0,0,0,0.3);flex-direction:column;overflow:hidden;">
<div style="background:linear-gradient(135deg,#f4b400,#ff6b00);color:white;padding:14px;display:flex;justify-content:space-between;">
<span>🤖 MercadoBot</span>
<button onclick="toggleChat()" style="background:none;border:none;color:white;font-size:24px;cursor:pointer;">×</button>
</div>

<div id="chat-messages" style="flex:1;overflow-y:auto;padding:14px;background:#f8f9fa;">
<div style="margin-bottom:10px;display:flex;gap:8px;">
<div style="width:28px;height:28px;border-radius:50%;background:#e9ecef;display:flex;align-items:center;justify-content:center;">🤖</div>
<div style="max-width:75%;padding:10px;border-radius:14px;background:white;border:1px solid #e9ecef;font-size:13px;">¡Hola! 👋 ¿En qué puedo ayudarte?</div>
</div>
</div>

<div style="padding:10px;background:white;border-top:1px solid #e9ecef;display:flex;gap:8px;">
<input type="text" id="message-input" placeholder="Escribe tu mensaje..." onkeypress="if(event.key==='Enter')sendMessage()" style="flex:1;padding:10px;border:1px solid #e0e0e0;border-radius:20px;font-size:13px;outline:none;">
<button onclick="sendMessage()" style="width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#f4b400,#ff6b00);border:none;cursor:pointer;">📤</button>
</div>
</div>
</div>

<script>
function toggleChat() {
const container = document.getElementById('chatbot-container');
container.style.display = container.style.display === 'none' ? 'flex' : 'none';
}

function addMessage(text, isUser) {
const messages = document.getElementById('chat-messages');
const div = document.createElement('div');
div.style = 'margin-bottom:10px;display:flex;gap:8px;' + (isUser ? 'flex-direction:row-reverse;' : '');
div.innerHTML = '<div style="width:28px;height:28px;border-radius:50%;background:#e9ecef;display:flex;align-items:center;justify-content:center;">' + (isUser ? '👤' : '🤖') + '</div><div style="max-width:75%;padding:10px;border-radius:14px;' + (isUser ? 'background:linear-gradient(135deg,#f4b400,#ff6b00);color:white;' : 'background:white;border:1px solid #e9ecef;') + 'font-size:13px;">' + text + '</div>';
messages.appendChild(div);
messages.scrollTop = messages.scrollHeight;
}

function sendMessage() {
const input = document.getElementById('message-input');
const msg = input.value.trim();
if (!msg) return;

addMessage(msg, true);
input.value = '';

fetch('/?api=chat&msg=' + encodeURIComponent(msg))
.then(res => res.text())
.then(html => {
const doc = new DOMParser().parseFromString(html, 'text/html');
const el = doc.querySelector('#mbot-response');
const response = el ? (el.textContent || el.innerText || '').trim() : 'Error al leer respuesta';
addMessage(response, false);
})
.catch(() => addMessage('Error de conexión', false));
}
</script>
"""

components.html(FOOTER_CHATBOT, height=550)
