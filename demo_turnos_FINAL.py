import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Demo Turnos - AppointmentBot",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS mejorado
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stChatMessage { max-width: 900px; margin: 0 auto; }
    .stChatFloatingInputContainer { max-width: 900px; margin: 0 auto; }
    .custom-header {
        text-align: center; padding: 25px;
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        border-radius: 12px; margin-bottom: 30px; color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .custom-header h1 { margin: 0; font-size: 28px; font-weight: 600; }
    .custom-header p { margin: 10px 0 0 0; opacity: 0.9; font-size: 15px; }
    div[data-testid="column"] > div > div > button {
        width: 100%; border-radius: 10px; padding: 16px 24px; font-weight: 600;
        font-size: 15px; transition: all 0.3s ease; border: 2px solid #e5e7eb;
        background: white; color: #374151; box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    div[data-testid="column"] > div > div > button:hover {
        background: #4a90e2; border-color: #4a90e2; color: white;
        transform: translateY(-2px); box-shadow: 0 6px 16px rgba(74, 144, 226, 0.3);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 15px;">
    <span style="display: inline-block; background: linear-gradient(135deg, #4a90e2 0%, #5ba3f5 100%);
        color: white; padding: 10px 24px; border-radius: 25px; font-weight: 600; font-size: 14px;
        box-shadow: 0 2px 8px rgba(74, 144, 226, 0.4);">
        🎯 Imaginate este demo con tus datos - Tu agenda, tus servicios, tus reglas
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="custom-header">
    <h1>📅 AppointmentBot - Reservá tu Turno</h1>
    <p>Sistema inteligente de gestión de turnos - Simple, rápido y efectivo</p>
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

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": """¡Hola! 👋 Soy tu asistente de turnos

**Reservá en 3 pasos:**
1️⃣ Elegí el día
2️⃣ Seleccioná el horario  
3️⃣ Confirmá tus datos

¿Empezamos?""",
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

def get_response(prompt):
    p = (prompt or "").lower().strip()
    
    # VER CALENDARIO
    if any(k in p for k in ["calendario", "disponible", "turno", "reserva", "agenda", "ver"]):
        return {
            "content": """📅 **Calendario Visual - Próximos 14 Días**

╔════════════════════════════════════════════════════════╗
║           📅 SEMANA 1 (Ene-Feb 2024)                  ║
╚════════════════════════════════════════════════════════╝

```
┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
│   LUN   │   MAR   │   MIÉ   │   JUE   │   VIE   │   SÁB   │   DOM   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│   29    │   30    │   31    │    1    │    2    │    3    │    4    │
│   Ene   │   Ene   │   Ene   │   Feb   │   Feb   │   Feb   │   Feb   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  🟢 8   │  🟢 9   │  🔵 7   │  🟢 8   │  🟡 6   │  🟡 3   │  ⚫ 0   │
│ turnos  │ turnos  │ turnos  │ turnos  │ turnos  │ turnos  │ Cerrado │
└─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

╔════════════════════════════════════════════════════════╗
║           📅 SEMANA 2 (Feb 2024)                      ║
╚════════════════════════════════════════════════════════╝

```
┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
│   LUN   │   MAR   │   MIÉ   │   JUE   │   VIE   │   SÁB   │   DOM   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│    5    │    6    │    7    │    8    │    9    │   10    │   11    │
│   Feb   │   Feb   │   Feb   │   Feb   │   Feb   │   Feb   │   Feb   │
├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
│  🟢 8   │  🟢 9   │  🔵 7   │  🟢 8   │  🟡 6   │  🟡 3   │  ⚫ 0   │
│ turnos  │ turnos  │ turnos  │ turnos  │ turnos  │ turnos  │ Cerrado │
└─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

**LEYENDA:**
🟢 Verde = Muchos turnos (6-9)  
🔵 Azul = Disponible (5-7)  
🟡 Amarillo = Pocos turnos (2-4)  
⚫ Negro = Cerrado

**💡 RECOMENDACIONES:**
• **Más disponibilidad:** Martes, Miércoles, Jueves
• **Se llenan rápido:** Sábados (reservá con anticipación)
• **Menos espera:** Lunes mañana, Miércoles tarde

**🎯 PARA RESERVAR:**
Usá los botones o escribí:
• "Quiero el martes 30"
• "Dame turno jueves 1"
• "El viernes 2"

👇 **Días más pedidos**""",
            "buttons": "fecha_rapida",
            "bonus_once": True
        }
    
    # SELECCIÓN DE DÍA
    if any(k in p for k in ["lunes", "martes", "miercoles", "miércoles", "jueves", "viernes", "sabado", "sábado"]) or any(k in p for k in ["30", "31", "1", "2"]):
        
        if "martes" in p or "30" in p:
            fecha = "Martes 30 de Enero"
            emoji = "🟢"
        elif "miercoles" in p or "miércoles" in p or "31" in p:
            fecha = "Miércoles 31 de Enero"
            emoji = "🔵"
        elif "jueves" in p or "1" in p:
            fecha = "Jueves 1 de Febrero"
            emoji = "🟢"
        elif "viernes" in p or "2" in p:
            fecha = "Viernes 2 de Febrero"
            emoji = "🟡"
        else:
            fecha = "Martes 30 de Enero"
            emoji = "🟢"
        
        st.session_state.selected_date = fecha
        
        return {
            "content": f"""✅ **¡Perfecto! {emoji} {fecha}**

⏰ **Horarios Disponibles**

╔════════════════════════════════════════════════════════╗
║         🌅 TURNO MAÑANA (9:00 - 13:00)                ║
╚════════════════════════════════════════════════════════╝

```
┌─────────┬─────────┬─────────┬─────────┐
│  09:00  │  09:30  │  10:00  │  10:30  │
│   ✅    │   ✅    │   ❌    │   ✅    │
├─────────┼─────────┼─────────┼─────────┤
│  11:00  │  11:30  │  12:00  │  12:30  │
│   ✅    │   ✅    │   ✅    │   ✅    │
└─────────┴─────────┴─────────┴─────────┘
```

╔════════════════════════════════════════════════════════╗
║         🌇 TURNO TARDE (14:00 - 19:00)                ║
╚════════════════════════════════════════════════════════╝

```
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│  14:00  │  14:30  │  15:00  │  15:30  │  16:00  │
│   ✅    │   ✅    │   ❌    │   ✅    │   ✅    │
├─────────┼─────────┼─────────┼─────────┼─────────┤
│  16:30  │  17:00  │  17:30  │  18:00  │         │
│   ✅    │   ❌    │   ✅    │   ✅    │         │
└─────────┴─────────┴─────────┴─────────┴─────────┘
```

✅ = Disponible | ❌ = Ocupado

**💡 MENOS ESPERA:**
• Mañana: 9:00, 9:30, 11:00, 11:30
• Tarde: 14:00, 14:30, 16:00, 18:00

**🎯 PARA ELEGIR HORARIO:**
Usá los botones o escribí:
• "Quiero a las 9:30"
• "El de las 14:00"
• "15:30 está bien"

👇 **Horarios populares**""",
            "buttons": "horario_rapido"
        }
    
    # SELECCIÓN HORARIO
    if any(h in p for h in ["9:", "10:", "11:", "12:", "14:", "15:", "16:", "17:", "18:"]):
        if "9:30" in p or "930" in p:
            hora = "09:30"
        elif "14:00" in p or "1400" in p or "14" in p:
            hora = "14:00"
        elif "15:30" in p:
            hora = "15:30"
        elif "11" in p:
            hora = "11:00"
        else:
            hora = "14:00"
        
        st.session_state.selected_time = hora
        fecha = st.session_state.selected_date or "Martes 30 de Enero"
        
        return {
            "content": f"""🎉 **¡Turno Pre-Reservado!**

╔════════════════════════════════════════════════════════╗
║           📋 RESUMEN DE TU TURNO                      ║
╚════════════════════════════════════════════════════════╝

```
  📅 Fecha:     {fecha}
  🕐 Hora:      {hora}
  ⏱️  Duración:  30-45 minutos
  📍 Lugar:     Av. 18 de Julio 1850
```

**✅ PARA CONFIRMAR DAME TUS DATOS:**

Formato: `Nombre, Teléfono, Email`

**Ejemplo:**
`Juan Pérez, 099123456, juan@email.com`

---

**🔔 AL CONFIRMAR RECIBIRÁS:**

```
┌────────────────────────────────────────┐
│ ✅ Email confirmación → Inmediato     │
│ 📅 Google Calendar   → Inmediato     │
│ 📱 WhatsApp 24hs     → Programado     │
│ 💬 SMS 2 horas       → Programado     │
└────────────────────────────────────────┘
```

**📋 RECORDÁ TRAER:**
• Documento de identidad
• Credencial (si tenés)
• Estudios previos

💬 **Escribí tus datos para confirmar**""",
            "buttons": "confirmar_directo"
        }
    
    # CONFIRMACIÓN
    if (any(k in p for k in ["confirmo", "confirmar", "ok"]) and ("@" in p or "099" in p or "098" in p)):
        return {
            "content": """✅ **¡TURNO CONFIRMADO!** 🎉

╔════════════════════════════════════════════════════════╗
║                                                        ║
║              ✓  TU TURNO ESTÁ CONFIRMADO              ║
║         Código: #TURNO-300124-1400                    ║
║                                                        ║
╚════════════════════════════════════════════════════════╝

**📋 DETALLES:**

```
╔══════════════════════════════════════════════════╗
║ FECHA Y HORA                                     ║
║ Martes 30 de Enero 2024 - 14:00hs              ║
╠══════════════════════════════════════════════════╣
║ PACIENTE                                         ║
║ Juan Pérez                                       ║
╠══════════════════════════════════════════════════╣
║ CONTACTO                                         ║
║ 📱 099 123 456 | ✉️ juan@email.com              ║
╠══════════════════════════════════════════════════╣
║ UBICACIÓN                                        ║
║ Av. 18 de Julio 1850, Montevideo                ║
╚══════════════════════════════════════════════════╝
```

**📨 YA TE ENVIAMOS:**

```
┌─────────┬─────────┬─────────┬─────────┐
│   📧    │   📅    │   📱    │   💬    │
│  Email  │Calendar │WhatsApp │   SMS   │
│   ✅    │   ✅    │   ⏰    │   ⏰    │
│ Enviado │ Enviado │24hs ant │ 2hs ant │
└─────────┴─────────┴─────────┴─────────┘
```

**🗺️ CÓMO LLEGAR:**

• 🚇 Metro Tres Cruces (3 cuadras)
• 🚌 Ómnibus 64, 180, 187, 121
• 🚗 Estacionamiento en la puerta

**📋 QUÉ TRAER:**

✓ Documento de identidad
✓ Credencial mutual (si tenés)
✓ Estudios previos
✓ Lista de medicamentos

---

**¿Necesitás cambiar o cancelar?**
📱 Avisá con 24hs: 099 123 456

**¡Nos vemos el martes 30 a las 14:00! 😊**""",
            "buttons": "post_confirmacion"
        }
    
    # CANCELAR/CAMBIAR
    if any(k in p for k in ["cancelar", "cambiar", "modificar", "no puedo"]):
        return {
            "content": """🔄 **Gestión de Turnos**

**Dame estos datos:**
• Tu nombre
• Fecha del turno
• Hora del turno

**Si es cambio:**
• Nueva fecha preferida

**Ejemplo:**
"Juan Pérez, turno martes 30/1 a las 14:00, quiero cambiar al jueves 1/2"

---

**📋 POLÍTICAS:**

```
┌──────────────────────────────────────┐
│ +48hs → Sin cargo, cambio libre     │
│ 24-48hs → Sin problema              │
│ -24hs → Avisá igual                 │
└──────────────────────────────────────┘
```

**📱 CONTACTO RÁPIDO:**
• WhatsApp: 099 123 456
• Tel: 2908 5555""",
            "buttons": "gestion_turno"
        }
    
    # INFO
    if any(k in p for k in ["horario", "donde", "dónde", "ubicacion", "ubicación", "info"]):
        return {
            "content": """ℹ️ **Información del Consultorio**

**⏰ HORARIOS:**

```
┌─────────────────────────────┐
│ Lun-Vie                     │
│ • Mañana: 9:00 - 13:00     │
│ • Tarde: 14:30 - 19:00     │
├─────────────────────────────┤
│ Sábados                     │
│ • Mañana: 9:00 - 13:00     │
│ • Tarde: Cerrado            │
├─────────────────────────────┤
│ Domingos y Feriados         │
│ • Cerrado                   │
└─────────────────────────────┘
```

**📍 UBICACIÓN:**
Av. 18 de Julio 1850, Montevideo

**🚇 CÓMO LLEGAR:**
• Metro Tres Cruces (3 cuadras)
• Ómnibus 64, 180, 187

**📞 CONTACTO:**
• Tel: 2908 5555
• WhatsApp: 099 123 456

¿Querés reservar un turno?""",
            "buttons": "info_acciones"
        }
    
    # DEFAULT
    return {
        "content": """❓ **¿Qué necesitás?**

**Elegí una opción:**

📅 **Ver calendario** - Todos los días
🔄 **Gestionar turno** - Cambiar/cancelar
ℹ️ **Información** - Horarios/ubicación

**O escribí:**
• "Ver calendario"
• "Cambiar turno"
• "Información"

¿Qué hacemos?""",
        "buttons": "ayuda"
    }

# Mostrar mensajes
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
        if msg.get("show_buttons"):
            bt = msg["show_buttons"]
            
            if bt == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Ver Calendario", key=f"cal_{i}", use_container_width=True):
                        r = get_response("calendario")
                        add_msg("Ver calendario", r["content"], r.get("buttons"), r.get("bonus_once"))
                        st.rerun()
                with col2:
                    if st.button("ℹ️ Información", key=f"info_{i}", use_container_width=True):
                        r = get_response("informacion")
                        add_msg("Ver información", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "fecha_rapida":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🟢 Mar 30 - 9 turnos", key=f"mar_{i}", use_container_width=True):
                        r = get_response("martes 30")
                        add_msg("Martes 30 de Enero", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🔵 Mié 31 - 7 turnos", key=f"mie_{i}", use_container_width=True):
                        r = get_response("miércoles 31")
                        add_msg("Miércoles 31 de Enero", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🟢 Jue 1 - 8 turnos", key=f"jue_{i}", use_container_width=True):
                        r = get_response("jueves 1")
                        add_msg("Jueves 1 de Febrero", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🟡 Vie 2 - 6 turnos", key=f"vie_{i}", use_container_width=True):
                        r = get_response("viernes 2")
                        add_msg("Viernes 2 de Febrero", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "horario_rapido":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🌅 09:30", key=f"h1_{i}", use_container_width=True):
                        r = get_response("9:30")
                        add_msg("09:30", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🌅 11:00", key=f"h2_{i}", use_container_width=True):
                        r = get_response("11:00")
                        add_msg("11:00", r["content"], r.get("buttons"))
                        st.rerun()
                with col3:
                    if st.button("🌇 14:00", key=f"h3_{i}", use_container_width=True):
                        r = get_response("14:00")
                        add_msg("14:00", r["content"], r.get("buttons"))
                        st.rerun()
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🌇 15:30", key=f"h4_{i}", use_container_width=True):
                        r = get_response("15:30")
                        add_msg("15:30", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🌇 16:00", key=f"h5_{i}", use_container_width=True):
                        r = get_response("16:00")
                        add_msg("16:00", r["content"], r.get("buttons"))
                        st.rerun()
                with col3:
                    if st.button("🌇 18:00", key=f"h6_{i}", use_container_width=True):
                        r = get_response("18:00")
                        add_msg("18:00", r["content"], r.get("buttons"))
                        st.rerun()
            
            elif bt == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Calendario", key=f"cal_h_{i}", use_container_width=True):
                        r = get_response("calendario")
                        add_msg("Ver calendario", r["content"], r.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("ℹ️ Info", key=f"info_h_{i}", use_container_width=True):
                        r = get_response("informacion")
                        add_msg("Info", r["content"], r.get("buttons"))
                        st.rerun()

# EJEMPLOS SÚPER ATRACTIVOS
st.markdown("---")

# Header llamativo
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h3 style="margin: 0; color: #1f2937; font-size: 22px; font-weight: 700;">
        💬 Probá el Asistente - Ejemplos en Vivo
    </h3>
    <p style="margin: 5px 0 0 0; color: #6b7280; font-size: 14px;">
        Escribí cualquiera de estas frases y el asistente responde al instante
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); 
                padding: 20px; border-radius: 12px; height: 280px;
                border: 2px solid #3b82f6; box-shadow: 0 4px 12px rgba(59, 130, 246, 0.15);">
        <div style="text-align: center; margin-bottom: 15px;">
            <span style="font-size: 32px;">📅</span>
            <h4 style="margin: 8px 0 0 0; color: #1e40af; font-weight: 700;">Reservar Turno</h4>
        </div>
        <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; font-size: 13px; color: #374151;">💬 "Ver calendario completo"</p>
        </div>
        <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; font-size: 13px; color: #374151;">💬 "Quiero el martes a las 14:00"</p>
        </div>
        <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; font-size: 13px; color: #374151;">💬 "Reservar para mañana"</p>
        </div>
        <div style="text-align: center; margin-top: 12px;">
            <span style="background: #1e40af; color: white; padding: 6px 16px; 
                         border-radius: 20px; font-size: 12px; font-weight: 600;">
                ⚡ Reserva en 30 segundos
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); 
                padding: 20px; border-radius: 12px; height: 280px;
                border: 2px solid #f59e0b; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.15);">
        <div style="text-align: center; margin-bottom: 15px;">
            <span style="font-size: 32px;">🔄</span>
            <h4 style="margin: 8px 0 0 0; color: #92400e; font-weight: 700;">Gestionar Turnos</h4>
        </div>
        <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; font-size: 13px; color: #374151;">💬 "Cambiar mi turno del viernes"</p>
        </div>
        <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; font-size: 13px; color: #374151;">💬 "No puedo ir, cancelar"</p>
        </div>
        <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; font-size: 13px; color: #374151;">💬 "Reprogramar para el jueves"</p>
        </div>
        <div style="text-align: center; margin-top: 12px;">
            <span style="background: #92400e; color: white; padding: 6px 16px; 
                         border-radius: 20px; font-size: 12px; font-weight: 600;">
                ✨ Flexibilidad total
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e9d5ff 0%, #d8b4fe 100%); 
                padding: 20px; border-radius: 12px; height: 280px;
                border: 2px solid #a855f7; box-shadow: 0 4px 12px rgba(168, 85, 247, 0.15);">
        <div style="text-align: center; margin-bottom: 15px;">
            <span style="font-size: 32px;">ℹ️</span>
            <h4 style="margin: 8px 0 0 0; color: #6b21a8; font-weight: 700;">Info & Soporte</h4>
        </div>
        <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; font-size: 13px; color: #374151;">💬 "Dónde queda el consultorio"</p>
        </div>
        <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; font-size: 13px; color: #374151;">💬 "Horarios de atención"</p>
        </div>
        <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px;">
            <p style="margin: 0; font-size: 13px; color: #374151;">💬 "Activar recordatorios"</p>
        </div>
        <div style="text-align: center; margin-top: 12px;">
            <span style="background: #6b21a8; color: white; padding: 6px 16px; 
                         border-radius: 20px; font-size: 12px; font-weight: 600;">
                💡 Respuestas instantáneas
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")
st.markdown("""
<div style="text-align: center; background: linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%); 
            padding: 16px 24px; border-radius: 12px; margin-top: 20px;
            border: 2px solid #22c55e; box-shadow: 0 4px 12px rgba(34, 197, 94, 0.15);">
    <p style="margin: 0; font-size: 15px; color: #166534; font-weight: 600;">
        ✨ <strong>¡Escribí cualquier pregunta arriba!</strong> El asistente entiende lenguaje natural y responde con información completa
    </p>
</div>
""", unsafe_allow_html=True)

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
st.caption("💡 Demo con calendario ASCII visual - Sistema profesional de turnos")
st.caption("🔌 En producción sincroniza con tu agenda, WhatsApp API y sistema de pagos")

# Reset
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
