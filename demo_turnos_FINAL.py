import streamlit as st

st.set_page_config(
    page_title="Demo Turnos - AppointmentBot",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stChatMessage { max-width: 800px; margin: 0 auto; }
    .stChatFloatingInputContainer { max-width: 800px; margin: 0 auto; }
    .custom-header {
        text-align: center; padding: 25px;
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        border-radius: 12px; margin-bottom: 30px; color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .custom-header h1 { margin: 0; font-size: 28px; font-weight: 600; }
    .custom-header p { margin: 10px 0 0 0; opacity: 0.9; font-size: 15px; }
    div[data-testid="column"] > div > div > button {
        width: 100%; border-radius: 8px; padding: 14px 20px; font-weight: 500;
        font-size: 15px; transition: all 0.2s ease; border: 1.5px solid #e5e7eb;
        background: white; color: #374151; box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    div[data-testid="column"] > div > div > button:hover {
        background: #4a90e2; border-color: #4a90e2; color: white;
        transform: translateY(-1px); box-shadow: 0 4px 8px rgba(74, 144, 226, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Badge
st.markdown("""
<div style="text-align: center; margin-bottom: 15px;">
    <span style="display: inline-block; background: linear-gradient(135deg, #4a90e2 0%, #5ba3f5 100%);
        color: white; padding: 10px 24px; border-radius: 25px; font-weight: 600; font-size: 14px;
        box-shadow: 0 2px 8px rgba(74, 144, 226, 0.4);">
        🎯 Imaginate este demo con tus datos - Tu agenda, tus servicios, tus reglas
    </span>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="custom-header">
    <h1>📅 AppointmentBot - Gestión de Turnos Inteligente</h1>
    <p>Reservas automáticas, recordatorios y administración de agenda 24/7</p>
</div>
""", unsafe_allow_html=True)

BONUS = "Este asistente gestiona tu agenda automáticamente, envía recordatorios y reduce inasistencias hasta un 60%."

def maybe_bonus():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({"role": "assistant", "content": f"💡 **{BONUS}**", "show_buttons": None})
        st.session_state.bonus_shown = True

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": """¡Hola! Soy tu asistente de turnos 📅

Puedo ayudarte con:
- 📅 Reservar turnos
- 🔍 Consultar disponibilidad
- ⏰ Ver horarios disponibles
- 📝 Confirmar o cancelar turnos
- 💬 Recibir recordatorios

¿Qué necesitás?""",
        "show_buttons": "inicial"
    }]

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if "bonus_shown" not in st.session_state:
    st.session_state.bonus_shown = False

def add_msg(user, bot, btns=None, bonus=False):
    st.session_state.messages.append({"role": "user", "content": user})
    st.session_state.messages.append({"role": "assistant", "content": bot, "show_buttons": btns})
    if bonus:
        maybe_bonus()
    st.session_state.button_clicked = True

def get_response(prompt):
    p = (prompt or "").lower().strip()
    
    # TURNOS
    if any(k in p for k in ["turno", "reserva", "disponible", "agenda", "horario", "cuando", "cuándo"]):
        return {
            "content": """📅 **Agenda Disponible - Próximos 7 Días**

**HOY - Lunes 29/01** ⚡
- 14:00, 16:00, 17:30 ✅

**Martes 30/01** 🌟
- 09:00, 10:00, 11:00 ✅
- 14:30, 15:30, 16:30, 17:30, 18:00 ✅

**Miércoles 31/01**
- 09:30, 11:00, 12:00, 15:00, 16:00, 17:00 ✅

**Jueves 1/02**
- 09:00, 10:30, 11:30, 14:00, 15:00, 16:00, 17:30 ✅

**Viernes 2/02** 😊
- 09:00-12:00, 14:30, 15:30 ✅

**Sábado 3/02** ⚠️
- 09:00, 10:00, 11:00 ✅

**💡 Tips:**
- Miércoles: Más opciones
- Sábados: Se llenan rápido
- Mañanas: Menos espera

¿Qué día te viene bien?""",
            "buttons": "turno_opciones",
            "bonus_once": True
        }
    
    # CANCELAR
    if any(k in p for k in ["cancelar", "cambiar", "modificar", "no puedo"]):
        return {
            "content": """🔄 **Gestión de Turnos**

Para cancelar o cambiar, dame:
1. Tu nombre
2. Fecha actual del turno
3. Nueva fecha (si es cambio)

**Políticas:**
✅ +48hs: Sin cargo
✅ 24-48hs: Sin problema
⚠️ -24hs: Avisá igual
🔴 Inasistencia: Afecta próximos turnos

**Formas:**
📱 WhatsApp: +598 99 123 456
📞 Tel: +598 2908 5555
💬 Este chat

¿Qué turno querés modificar?""",
            "buttons": "cancelar_opciones"
        }
    
    # RECORDATORIOS
    if any(k in p for k in ["recordatorio", "aviso", "notificacion", "notificación", "mensaje"]):
        return {
            "content": """🔔 **Recordatorios Automáticos**

**Enviamos:**
- 48hs antes: Email con confirmación
- 24hs antes: WhatsApp
- 2hs antes: SMS recordatorio

**Canales:**
📱 WhatsApp (más efectivo)
📧 Email (detallado)
💬 SMS (backup)

**Impacto:**
✅ 60% menos inasistencias
✅ 85% confirmaciones
✅ Mejor organización

**Activar:**
Dame tu número y listo!

¿Querés activar recordatorios?""",
            "buttons": "recordatorios"
        }
    
    # HORARIOS
    if any(k in p for k in ["horario", "atienden", "abierto", "cierran"]):
        return {
            "content": """⏰ **Horarios de Atención**

**Lunes a Viernes:**
🕐 Mañana: 9:00-13:00
🕒 Tarde: 14:30-19:00

**Sábados:**
🕐 9:00-13:00 (solo mañana)

**Domingos:** Cerrado

**Ubicación:**
📍 Av. 18 de Julio 1850, MVD
📞 +598 2908 5555
📱 WhatsApp: +598 99 123 456

**Llegar:**
- Ómnibus: 64, 180, 187
- Metro: Tres Cruces (3 cuadras)

¿Necesitás reservar un turno?""",
            "buttons": "horarios_acciones"
        }
    
    # DEFAULT
    return {
        "content": """❓ No entendí, pero puedo ayudarte con:

**📅 TURNOS**
• Reservar turno
• Ver disponibilidad
• Confirmar asistencia
• Cancelar/cambiar

**ℹ️ INFO**
• Horarios
• Servicios
• Ubicación
• Recordatorios

**Ejemplos:**
- "Quiero turno para esta semana"
- "Necesito cambiar mi turno"
- "Qué horarios hay"
- "Activar recordatorios"

¡Preguntame! 📅""",
        "buttons": "ayuda"
    }

# Mostrar mensajes
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
        if msg.get("show_buttons"):
            bt = msg["show_buttons"]
            
            if bt == "inicial":
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("📅 Reservar", key=f"b1_{i}", use_container_width=True):
                        r = get_response("turno")
                        add_msg("Reservar turno", r["content"], r.get("buttons"))
                        st.rerun()
                with c2:
                    if st.button("🔍 Disponibilidad", key=f"b2_{i}", use_container_width=True):
                        r = get_response("disponibilidad")
                        add_msg("Ver disponibilidad", r["content"], r.get("buttons"))
                        st.rerun()
                
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("✅ Confirmar", key=f"b3_{i}", use_container_width=True):
                        r = get_response("confirmar")
                        add_msg("Confirmar turno", r["content"], r.get("buttons"))
                        st.rerun()
                with c2:
                    if st.button("🔄 Cambiar", key=f"b4_{i}", use_container_width=True):
                        r = get_response("cancelar")
                        add_msg("Cambiar turno", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "ayuda":
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("📅 Reservar", key=f"bh1_{i}", use_container_width=True):
                        r = get_response("turno")
                        add_msg("Reservar", r["content"], r.get("buttons"))
                        st.rerun()
                with c2:
                    if st.button("ℹ️ Info", key=f"bh2_{i}", use_container_width=True):
                        r = get_response("horarios")
                        add_msg("Info", r["content"], r.get("buttons"))
                        st.rerun()

# Ejemplos
st.markdown("---")
st.markdown("**💬 Ejemplos:**")
c1, c2 = st.columns(2)
with c1:
    st.caption("• Quiero turno esta semana")
    st.caption("• Cambiar mi turno del jueves")
    st.caption("• Qué horarios hay")
with c2:
    st.caption("• Activar recordatorios")
    st.caption("• Dónde queda")
    st.caption("• Confirmar asistencia")

# Input
if prompt := st.chat_input("Escribí tu consulta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    r = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": r["content"], "show_buttons": r.get("buttons")})
    if r.get("bonus_once"):
        maybe_bonus()
    st.rerun()

# Footer
st.divider()
st.caption("💡 Demo interactivo - Sistema de turnos profesional")
st.caption("🔌 En producción sincroniza con Google Calendar y WhatsApp API")

# Reset
c1, c2 = st.columns([3, 1])
with c2:
    if st.button("🔄 Reiniciar"):
        st.session_state.messages = [{
            "role": "assistant",
            "content": """¡Hola! Soy tu asistente de turnos 📅

Puedo ayudarte con:
- 📅 Reservar turnos
- 🔍 Consultar disponibilidad
- ⏰ Ver horarios disponibles
- 📝 Confirmar o cancelar turnos
- 💬 Recibir recordatorios

¿Qué necesitás?""",
            "show_buttons": "inicial"
        }]
        st.session_state.button_clicked = False
        st.session_state.bonus_shown = False
        st.rerun()
