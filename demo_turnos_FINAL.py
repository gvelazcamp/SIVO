import streamlit as st
from datetime import datetime, timedelta
import calendar

st.set_page_config(
    page_title="Demo Turnos - AppointmentBot",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS MEJORADO
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
    
    /* Calendario visual */
    .calendar-container {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    
    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 8px;
        margin-top: 15px;
    }
    
    .calendar-day {
        padding: 12px;
        text-align: center;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
        border: 2px solid #e5e7eb;
        background: white;
    }
    
    .calendar-day:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.2);
    }
    
    .day-available {
        background: #e8f4f8;
        border-color: #4a90e2;
    }
    
    .day-few {
        background: #fff4e6;
        border-color: #f59e0b;
    }
    
    .day-full {
        background: #fee;
        border-color: #ef4444;
        opacity: 0.6;
        cursor: not-allowed;
    }
    
    .day-closed {
        background: #f3f4f6;
        border-color: #d1d5db;
        opacity: 0.5;
        cursor: not-allowed;
    }
    
    .time-slot {
        display: inline-block;
        padding: 8px 16px;
        margin: 5px;
        border-radius: 20px;
        border: 2px solid #4a90e2;
        background: white;
        cursor: pointer;
        transition: all 0.2s;
        font-weight: 500;
    }
    
    .time-slot:hover {
        background: #4a90e2;
        color: white;
        transform: scale(1.05);
    }
    
    .time-slot-taken {
        background: #f3f4f6;
        border-color: #d1d5db;
        color: #9ca3af;
        cursor: not-allowed;
    }
    
    div[data-testid="column"] > div > div > button {
        width: 100%; border-radius: 8px; padding: 14px 20px;
        font-weight: 500; font-size: 15px; transition: all 0.2s ease;
        border: 1.5px solid #e5e7eb; background: white; color: #374151;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
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
    <h1>📅 AppointmentBot - Sistema de Turnos Inteligente</h1>
    <p>Reservá tu turno en segundos con nuestro calendario interactivo</p>
</div>
""", unsafe_allow_html=True)

BONUS = "Este asistente gestiona tu agenda automáticamente, envía recordatorios y reduce inasistencias hasta un 60%."

def maybe_bonus():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"💡 **{BONUS}**",
            "show_buttons": None
        })
        st.session_state.bonus_shown = True

# Inicializar
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": """¡Hola! Soy tu asistente de turnos 📅

Seleccioná una opción para comenzar:""",
        "show_buttons": "inicial"
    }]

if "selected_date" not in st.session_state:
    st.session_state.selected_date = None

if "selected_time" not in st.session_state:
    st.session_state.selected_time = None

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if "bonus_shown" not in st.session_state:
    st.session_state.bonus_shown = False

def add_msg(user, bot, btns=None, bonus=False):
    st.session_state.messages.append({"role": "user", "content": user})
    st.session_state.messages.append({"role": "assistant", "content": bot, "show_buttons": btns})
    if bonus:
        maybe_bonus()

def get_calendar_html():
    """Genera un calendario visual para los próximos 14 días"""
    today = datetime.now()
    
    # Disponibilidad simulada (más realista)
    availability = {
        0: 8,  # Lunes: 8 turnos
        1: 9,  # Martes: 9 turnos
        2: 7,  # Miércoles: 7 turnos
        3: 8,  # Jueves: 8 turnos
        4: 6,  # Viernes: 6 turnos
        5: 3,  # Sábado: 3 turnos
        6: 0,  # Domingo: cerrado
    }
    
    html = """
    <div class="calendar-container">
        <h3 style="margin: 0 0 10px 0; color: #1f2937;">📅 Seleccioná un día</h3>
        <p style="margin: 0 0 15px 0; color: #6b7280; font-size: 14px;">
            Próximos 14 días disponibles
        </p>
        <div class="calendar-grid">
    """
    
    for i in range(14):
        date = today + timedelta(days=i)
        day_num = date.day
        day_name = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"][date.weekday()]
        month_name = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"][date.month - 1]
        
        # Determinar disponibilidad
        slots = availability[date.weekday()]
        
        if slots == 0:
            css_class = "day-closed"
            status = "❌ Cerrado"
        elif slots <= 2:
            css_class = "day-few"
            status = f"⚠️ {slots} turnos"
        elif slots <= 5:
            css_class = "day-few"
            status = f"⚡ {slots} turnos"
        else:
            css_class = "day-available"
            status = f"✅ {slots} turnos"
        
        html += f"""
            <div class="calendar-day {css_class}">
                <div style="font-size: 11px; color: #6b7280; font-weight: 600;">{day_name}</div>
                <div style="font-size: 20px; font-weight: 700; margin: 5px 0; color: #1f2937;">{day_num}</div>
                <div style="font-size: 10px; color: #6b7280;">{month_name}</div>
                <div style="font-size: 11px; margin-top: 5px; font-weight: 600;">{status}</div>
            </div>
        """
    
    html += """
        </div>
        <p style="margin: 15px 0 0 0; color: #6b7280; font-size: 13px; text-align: center;">
            💡 Tip: Los miércoles y jueves tienen más disponibilidad
        </p>
    </div>
    """
    
    return html

def get_time_slots_for_date(date_str):
    """Genera horarios disponibles para una fecha"""
    # Horarios base
    morning_slots = ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30"]
    afternoon_slots = ["14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00"]
    
    # Simular algunos ocupados aleatoriamente
    occupied = ["10:00", "15:00", "17:00"]
    
    html = f"""
    <div style="background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
        <h3 style="margin: 0 0 5px 0; color: #1f2937;">⏰ Horarios Disponibles</h3>
        <p style="margin: 0 0 20px 0; color: #6b7280; font-size: 14px;">
            Seleccioná el horario que prefieras
        </p>
        
        <div style="margin-bottom: 20px;">
            <h4 style="color: #4a90e2; margin: 0 0 10px 0;">🌅 Mañana</h4>
    """
    
    for slot in morning_slots:
        if slot in occupied:
            html += f'<span class="time-slot time-slot-taken">{slot} ❌</span>'
        else:
            html += f'<span class="time-slot">{slot}</span>'
    
    html += """
        </div>
        
        <div>
            <h4 style="color: #4a90e2; margin: 0 0 10px 0;">🌇 Tarde</h4>
    """
    
    for slot in afternoon_slots:
        if slot in occupied:
            html += f'<span class="time-slot time-slot-taken">{slot} ❌</span>'
        else:
            html += f'<span class="time-slot">{slot}</span>'
    
    html += """
        </div>
        
        <p style="margin: 20px 0 0 0; padding: 12px; background: #f0f9ff; border-radius: 8px; color: #0369a1; font-size: 13px;">
            💡 <strong>Tip:</strong> Los turnos de mañana (9-11am) suelen tener menos espera
        </p>
    </div>
    """
    
    return html

def get_response(prompt):
    p = (prompt or "").lower().strip()
    
    # VER CALENDARIO
    if any(k in p for k in ["turno", "reserva", "disponible", "agenda", "cuando", "cuándo", "calendario"]):
        calendar_html = get_calendar_html()
        return {
            "content": f"""{calendar_html}

**Para reservar:**
Decime el día que te interesa, por ejemplo:
- "Quiero el martes 30"
- "El viernes que viene"
- "Mañana"
- "El jueves"

O presioná uno de los botones 👇""",
            "buttons": "fecha_rapida",
            "bonus_once": True
        }
    
    # SELECCIÓN DE DÍA ESPECÍFICO
    if any(k in p for k in ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes", "sabado", "sábado"]) or any(k in p for k in ["mañana", "hoy", "pasado"]):
        
        # Determinar qué día eligió
        if "martes" in p or "30" in p:
            fecha = "Martes 30 de Enero"
        elif "miercoles" in p or "miércoles" in p or "31" in p:
            fecha = "Miércoles 31 de Enero"
        elif "jueves" in p:
            fecha = "Jueves 1 de Febrero"
        elif "viernes" in p:
            fecha = "Viernes 2 de Febrero"
        elif "mañana" in p:
            fecha = "Mañana"
        else:
            fecha = "Día seleccionado"
        
        st.session_state.selected_date = fecha
        
        time_slots = get_time_slots_for_date(fecha)
        
        return {
            "content": f"""✅ **Perfecto! {fecha}**

{time_slots}

**Para confirmar tu turno:**
Decime el horario que elegís, por ejemplo:
- "Quiero a las 9:30"
- "El de las 14:00"
- "15:30 está bien"

O seleccioná con los botones 👇""",
            "buttons": "horario_rapido"
        }
    
    # SELECCIÓN DE HORARIO
    if any(k in p for k in ["9", "10", "11", "12", "14", "15", "16", "17", "18"]) and any(k in p for k in [":", "hs", "am", "pm"]):
        # Extraer hora
        if "9:30" in p or "930" in p:
            hora = "09:30"
        elif "14:00" in p or "1400" in p or "14" in p:
            hora = "14:00"
        elif "15:30" in p or "1530" in p:
            hora = "15:30"
        else:
            hora = "14:00"
        
        st.session_state.selected_time = hora
        fecha = st.session_state.selected_date or "Martes 30 de Enero"
        
        return {
            "content": f"""🎉 **¡Excelente! Turno seleccionado**

📅 **Fecha:** {fecha}
🕐 **Hora:** {hora}
⏱️ **Duración:** 30-45 minutos
📍 **Lugar:** Av. 18 de Julio 1850

---

**Para CONFIRMAR necesito:**

1. Tu nombre completo
2. Teléfono / WhatsApp
3. Email

**Ejemplo:**
"Juan Pérez, 099 123 456, juan@email.com"

---

**Recordatorios automáticos:**
✅ Email 24hs antes
✅ WhatsApp 2hs antes  
✅ SMS 30min antes

**Políticas:**
• Cancelación gratis +24hs antes
• Llegá 10min antes
• Consultorio accesible

¿Confirmamos con tus datos?""",
            "buttons": "confirmar_datos"
        }
    
    # CONFIRMACIÓN FINAL
    if any(k in p for k in ["confirmo", "confirmar", "si", "sí", "ok", "dale"]) and ("@" in p or "099" in p or "098" in p):
        return {
            "content": """✅ **¡TURNO CONFIRMADO!**

**Resumen de tu reserva:**

📅 Martes 30 de Enero 2024
🕐 14:00 hs
👤 Juan Pérez
📱 099 123 456
📧 juan@email.com

---

**📨 Te enviamos:**
✅ Confirmación por email ✅ Enviado
✅ Recordatorio WhatsApp ⏳ Pendiente
✅ Link Google Calendar 📆 Enviado

**📍 Cómo llegar:**
Av. 18 de Julio 1850, Montevideo
🚇 Metro Tres Cruces (3 cuadras)
🚌 Ómnibus 64, 180, 187

**Código de confirmación:** #TURNO-30012024-1400

---

**💡 Tips para tu visita:**
• Llegá 10 minutos antes
• Traé documento de identidad
• Si tenés estudios previos, llevalos
• Avisá si vas a llegar tarde

**¿Necesitás cambiar o cancelar?**
Avisá con 24hs de anticipación:
📱 WhatsApp: 099 123 456
📞 Teléfono: 2908 5555

---

**¡Nos vemos el martes! 😊**

¿Necesitás algo más?""",
            "buttons": "turno_confirmado"
        }
    
    # CANCELAR
    if any(k in p for k in ["cancelar", "cambiar", "modificar", "no puedo"]):
        return {
            "content": """🔄 **Gestión de Turnos**

**Para cancelar o cambiar, necesito:**

1. Tu nombre completo
2. Fecha del turno actual
3. Hora del turno actual

**Si es cambio:**
4. Nueva fecha preferida

---

**📋 Políticas:**

✅ **+48hs antes:** Sin cargo, cambio libre
✅ **24-48hs antes:** Sin cargo
⚠️ **-24hs:** Te pedimos que avises
🔴 **Sin aviso:** Afecta próximos turnos

---

**📱 Formas de gestionar:**

1. **Este chat** - Dame los datos
2. **WhatsApp:** 099 123 456
3. **Teléfono:** 2908 5555
4. **Email:** turnos@clinica.uy

**Ejemplo:**
"Juan Pérez, turno martes 30/1 a las 14:00, quiero cambiar al jueves 1/2 a las 10:00"

¿Qué turno querés gestionar?""",
            "buttons": "gestion_turno"
        }
    
    # INFORMACIÓN
    if any(k in p for k in ["horario", "atencion", "atención", "donde", "dónde", "ubicacion", "ubicación"]):
        return {
            "content": """📍 **Información del Consultorio**

**⏰ HORARIOS:**
• Lun-Vie: 9:00-13:00 y 14:30-19:00
• Sábados: 9:00-13:00
• Domingos: Cerrado

**📍 UBICACIÓN:**
Av. 18 de Julio 1850, Montevideo

**🚇 CÓMO LLEGAR:**
• Metro: Tres Cruces (3 cuadras)
• Ómnibus: 64, 180, 187, 121
• Auto: Estacionamiento en la puerta

**📞 CONTACTO:**
• Teléfono: 2908 5555
• WhatsApp: 099 123 456
• Email: info@clinica.uy

**🔔 SERVICIOS:**
• Consultas generales
• Estudios básicos
• Certificados médicos
• Atención familiar

¿Querés reservar un turno?""",
            "buttons": "info_acciones"
        }
    
    # DEFAULT
    return {
        "content": """❓ No entendí bien, pero puedo ayudarte con:

**📅 RESERVAR TURNO**
• Ver calendario interactivo
• Elegir fecha y horario
• Confirmar tu turno

**🔄 GESTIONAR**
• Cambiar turno existente
• Cancelar turno
• Consultar mi turno

**ℹ️ INFORMACIÓN**
• Horarios de atención
• Ubicación y contacto
• Servicios disponibles

**¿Qué necesitás?**""",
        "buttons": "ayuda"
    }

# Mostrar mensajes
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)
        
        if msg.get("show_buttons"):
            bt = msg["show_buttons"]
            
            if bt == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Ver calendario", key=f"cal_{i}", use_container_width=True):
                        r = get_response("calendario")
                        add_msg("Ver calendario disponible", r["content"], r.get("buttons"), r.get("bonus_once"))
                        st.rerun()
                with col2:
                    if st.button("ℹ️ Información", key=f"info_{i}", use_container_width=True):
                        r = get_response("informacion")
                        add_msg("Ver información", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🔄 Gestionar turno", key=f"gest_{i}", use_container_width=True):
                        r = get_response("cancelar")
                        add_msg("Gestionar mi turno", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("⚡ Turno urgente", key=f"urg_{i}", use_container_width=True):
                        r = get_response("hoy")
                        add_msg("Necesito turno urgente", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "fecha_rapida":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Martes 30", key=f"mar_{i}", use_container_width=True):
                        r = get_response("martes 30")
                        add_msg("Martes 30 de Enero", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("Miércoles 31", key=f"mie_{i}", use_container_width=True):
                        r = get_response("miércoles 31")
                        add_msg("Miércoles 31 de Enero", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Jueves 1/2", key=f"jue_{i}", use_container_width=True):
                        r = get_response("jueves")
                        add_msg("Jueves 1 de Febrero", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("Viernes 2/2", key=f"vie_{i}", use_container_width=True):
                        r = get_response("viernes")
                        add_msg("Viernes 2 de Febrero", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "horario_rapido":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("09:30", key=f"h1_{i}", use_container_width=True):
                        r = get_response("9:30")
                        add_msg("Quiero a las 9:30", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("14:00", key=f"h2_{i}", use_container_width=True):
                        r = get_response("14:00")
                        add_msg("Quiero a las 14:00", r["content"], r.get("buttons"))
                        st.rerun()
                with col3:
                    if st.button("15:30", key=f"h3_{i}", use_container_width=True):
                        r = get_response("15:30")
                        add_msg("Quiero a las 15:30", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Ver calendario", key=f"cal_h_{i}", use_container_width=True):
                        r = get_response("calendario")
                        add_msg("Ver calendario", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("ℹ️ Info", key=f"info_h_{i}", use_container_width=True):
                        r = get_response("informacion")
                        add_msg("Ver info", r["content"], r.get("buttons"))
                        st.rerun()

# Ejemplos
st.markdown("---")
st.markdown("**💬 Ejemplos de consultas:**")
col1, col2 = st.columns(2)
with col1:
    st.caption("• Ver calendario")
    st.caption("• Quiero el martes 30")
    st.caption("• A las 14:00")
with col2:
    st.caption("• Cambiar mi turno")
    st.caption("• Dónde queda")
    st.caption("• Confirmo")

# Input
if prompt := st.chat_input("Escribí tu consulta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    r = get_response(prompt)
    st.session_state.messages.append({
        "role": "assistant",
        "content": r["content"],
        "show_buttons": r.get("buttons")
    })
    if r.get("bonus_once"):
        maybe_bonus()
    st.rerun()

# Footer
st.divider()
st.caption("💡 Demo interactivo - Sistema de turnos profesional con calendario visual")
st.caption("🔌 En producción sincroniza con Google Calendar, WhatsApp API y tu sistema")

# Reset
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar"):
        st.session_state.messages = [{
            "role": "assistant",
            "content": """¡Hola! Soy tu asistente de turnos 📅

Seleccioná una opción para comenzar:""",
            "show_buttons": "inicial"
        }]
        st.session_state.selected_date = None
        st.session_state.selected_time = None
        st.session_state.button_clicked = False
        st.session_state.bonus_shown = False
        st.rerun()
