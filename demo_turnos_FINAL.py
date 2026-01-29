import streamlit as st
from datetime import datetime, timedelta

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
    
    .stChatMessage {
        max-width: 800px;
        margin: 0 auto;
    }
    
    .stChatFloatingInputContainer {
        max-width: 800px;
        margin: 0 auto;
    }
    
    .custom-header {
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        margin-bottom: 30px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .custom-header h1 {
        margin: 0;
        font-size: 28px;
        font-weight: 600;
        letter-spacing: -0.5px;
    }
    
    .custom-header p {
        margin: 10px 0 0 0;
        opacity: 0.9;
        font-size: 15px;
        font-weight: 400;
    }
    
    div[data-testid="column"] > div > div > button {
        width: 100%;
        border-radius: 8px;
        padding: 14px 20px;
        font-weight: 500;
        font-size: 15px;
        transition: all 0.2s ease;
        border: 1.5px solid #e5e7eb;
        background: white;
        color: #374151;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    div[data-testid="column"] > div > div > button:hover {
        background: #667eea;
        border-color: #667eea;
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(102, 126, 234, 0.2);
    }
    
    .stCaption {
        color: #6b7280 !important;
        font-size: 14px !important;
        line-height: 1.8 !important;
    }
</style>
""", unsafe_allow_html=True)

# Badge impactante
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <span style="display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; padding: 12px 28px; border-radius: 30px; font-weight: 700; font-size: 15px;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4); animation: pulse 2s infinite;">
        🎯 Sistema completo: Agenda + Recordatorios + Estadisticas + Integraciones
    </span>
</div>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="custom-header">
    <h1>📅 AppointmentBot Pro - Gestion Inteligente de Turnos</h1>
    <p>Automatiza tu agenda, reduce inasistencias 60% y ahorra 15 horas/semana</p>
</div>
""", unsafe_allow_html=True)

BONUS_TEXTO = (
    "Sistema profesional que se integra con Google Calendar, WhatsApp API y tu CRM. "
    "Reduce inasistencias hasta 60% con recordatorios automaticos."
)

def maybe_append_bonus_once():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "💡 **{}**".format(BONUS_TEXTO),
            "show_buttons": None
        })
        st.session_state.bonus_shown = True

# Inicializar estado
if "messages" not in st.session_state:
    # Mensaje inicial CON CALENDARIO
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """Hola! Soy tu asistente de turnos 24/7 📅

**📊 ESTADO DE TU AGENDA HOY:**
- Turnos confirmados: 12
- Espacios libres: 8
- Lista de espera: 3 clientes

**Que necesitas?**""",
            "show_buttons": "inicial_con_calendario"
        }
    ]

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if "bonus_shown" not in st.session_state:
    st.session_state.bonus_shown = False

def add_message_and_hide_buttons(user_msg, bot_response, next_buttons=None, show_bonus_once=False):
    st.session_state.messages.append({"role": "user", "content": user_msg})
    bot_msg = {
        "role": "assistant",
        "content": bot_response,
        "show_buttons": next_buttons
    }
    st.session_state.messages.append(bot_msg)
    if show_bonus_once:
        maybe_append_bonus_once()
    st.session_state.button_clicked = True

def get_bot_response(prompt):
    p = (prompt or "").lower()
    
    # 1) Mostrar calendario
    if "calendario" in p or "dias" in p or "disponible" in p or "cuando" in p:
        return {
            "content": """📅 **Calendario Interactivo - Proximos 14 Dias**

**ESTA SEMANA:**

| Dia | Fecha | Turnos Libres | Estado |
|-----|-------|---------------|--------|
| LUN | 29/01 | 3 turnos | ⚠️ Pocos |
| MAR | 30/01 | 12 turnos | ✅ Disponible |
| MIE | 31/01 | 15 turnos | ✅ Disponible |
| JUE | 01/02 | 8 turnos | ✅ Disponible |
| VIE | 02/02 | 4 turnos | ⚠️ Llenandose |
| SAB | 03/02 | 2 turnos | 🔴 Casi lleno |

**PROXIMA SEMANA:**

| Dia | Fecha | Turnos Libres | Estado |
|-----|-------|---------------|--------|
| LUN | 05/02 | 18 turnos | ✅✅ Mucho espacio |
| MAR | 06/02 | 16 turnos | ✅ Disponible |
| MIE | 07/02 | 14 turnos | ✅ Disponible |

**💡 TIPS INTELIGENTES:**
- Miercoles: Mas opciones y flexibilidad
- Sabados: Se llenan rapido, reserva con anticipacion
- Lunes proxima semana: Mejor disponibilidad

Que dia te interesa?""",
            "buttons": "seleccionar_dia",
            "bonus_once": True
        }
    
    # 2) Servicios disponibles
    if "servicio" in p or "corte" in p or "tintura" in p or "tratamiento" in p or "que hacen" in p:
        return {
            "content": """💇 **Servicios Disponibles**

**CORTES**
✂️ Corte Clasico
- Duracion: 30 min
- Precio: $800
- Profesionales: 3 disponibles

✂️ Corte + Barba
- Duracion: 45 min
- Precio: $1.200
- Profesionales: 2 disponibles

**COLOR**
🎨 Tintura Completa
- Duracion: 90 min
- Precio: $2.500
- Profesional: Ana (especialista)

🎨 Mechas/Balayage
- Duracion: 120 min
- Precio: $3.500
- Profesional: Lucia (experta)

**TRATAMIENTOS**
💆 Tratamiento Capilar
- Duracion: 60 min
- Precio: $1.800
- Profesionales: 2 disponibles

💆 Alisado/Botox
- Duracion: 180 min
- Precio: $5.000
- Consultar disponibilidad especial

Que servicio te interesa?""",
            "buttons": "seleccionar_servicio"
        }
    
    # 3) Profesionales
    if "profesional" in p or "quien" in p or "con quien" in p or "peluquer" in p:
        return {
            "content": """👥 **Nuestro Equipo**

**ANA MARTINEZ** ⭐⭐⭐⭐⭐
- Especialidad: Color y mechas
- Experiencia: 12 años
- Valoracion: 4.9/5 (156 reseñas)
- Disponibilidad: Mar, Mie, Jue, Vie

**LUCIA RODRIGUEZ** ⭐⭐⭐⭐⭐
- Especialidad: Cortes y estilo
- Experiencia: 8 años
- Valoracion: 4.8/5 (234 reseñas)
- Disponibilidad: Lun, Mie, Vie, Sab

**CARLOS GOMEZ** ⭐⭐⭐⭐½
- Especialidad: Corte masculino y barba
- Experiencia: 10 años
- Valoracion: 4.7/5 (189 reseñas)
- Disponibilidad: Lun, Mar, Jue, Sab

**SOFIA PEREZ** ⭐⭐⭐⭐⭐
- Especialidad: Tratamientos capilares
- Experiencia: 6 años
- Valoracion: 4.9/5 (98 reseñas)
- Disponibilidad: Mar, Jue, Vie

**💡 TIP:** Si no tenes preferencia, el sistema elige automaticamente segun disponibilidad.

Con quien te gustaria tu turno?""",
            "buttons": "seleccionar_profesional"
        }
    
    # 4) Recordatorios
    if "recordatorio" in p or "aviso" in p or "notificacion" in p or "whatsapp" in p:
        return {
            "content": """📱 **Sistema de Recordatorios Automaticos**

**COMO FUNCIONA:**

**48 HORAS ANTES**
📧 Email con detalles completos:
- Fecha y hora
- Profesional asignado
- Servicio contratado
- Boton de confirmacion
- Opcion de cancelar/reprogramar

**24 HORAS ANTES**
💬 WhatsApp personalizado:
- Mensaje con tu nombre
- Recordatorio amigable
- Link para confirmar
- Ubicacion del local

**2 HORAS ANTES**
📲 SMS de recordatorio:
- Breve y directo
- Hora exacta
- Numero de contacto

**ESTADISTICAS REALES:**
- ✅ 60% menos inasistencias
- ✅ 85% tasa de confirmacion
- ✅ 92% satisfaccion del cliente
- ✅ 40% menos llamadas de consulta

**INTEGRACIONES:**
🔗 Google Calendar (sincroniza automatico)
🔗 WhatsApp Business API
🔗 Twilio SMS
🔗 Mailchimp/SendGrid

Los recordatorios se activan automaticamente al confirmar tu turno!

Queres reservar ahora?""",
            "buttons": "recordatorios_acciones"
        }
    
    # 5) Cancelar/Modificar
    if "cancelar" in p or "cambiar" in p or "modificar" in p or "reprogramar" in p:
        return {
            "content": """🔄 **Gestion de Turnos - Cancelar/Modificar**

**POLITICAS CLARAS:**

✅ **+48 HORAS**
- Cancelacion SIN cargo
- Cambio inmediato sin penalizacion
- Turno vuelve a disponibilidad
- Confirmacion por WhatsApp

✅ **24-48 HORAS**
- Cambio permitido
- Penalizacion: 20% del servicio
- Se ofrece a lista de espera
- Notificacion por email

⚠️ **-24 HORAS**
- Penalizacion: 50% del servicio
- Cambio segun disponibilidad
- Turno ofrecido urgente a otros
- Llamada de confirmacion

🔴 **INASISTENCIA SIN AVISO**
- Cargo: 100% del servicio
- Afecta futuras reservas
- Requiere pago anticipado proxima vez
- Sistema de credito reducido

**COMO HACERLO:**

**Opcion 1:** Por este chat
- "Quiero cancelar mi turno del jueves 15:00"

**Opcion 2:** Por WhatsApp
- +598 99 123 456

**Opcion 3:** Por email
- turnos@salon.com

**Opcion 4:** Portal web
- salon.com/misturnos

Que turno necesitas modificar?""",
            "buttons": "cancelar_opciones"
        }
    
    # 6) Estadisticas
    if "estadistica" in p or "reporte" in p or "cuantos" in p or "numeros" in p:
        return {
            "content": """📊 **Dashboard en Tiempo Real**

**HOY - Lunes 29/01**
- Turnos agendados: 20
- Completados: 12
- Pendientes: 8
- Cancelaciones: 2
- Inasistencias: 0 ✅
- Facturacion: $24.500

**ESTA SEMANA**
- Total turnos: 142
- Tasa ocupacion: 85%
- Tasa confirmacion: 92%
- Clientes nuevos: 18
- Clientes recurrentes: 65
- Facturacion proyectada: $178.000

**ESTE MES**
- Turnos totales: 580
- Profesional top: Ana (156 turnos)
- Servicio mas vendido: Corte clasico
- Dia mas ocupado: Sabados
- Horario pico: 15:00-17:00
- Ingresos: $680.000

**METRICAS CLAVE**
✅ Tasa de ocupacion: 85% (objetivo: 80%)
✅ Tiempo promedio espera: 5 min
✅ Satisfaccion cliente: 4.8/5
⚠️ Tasa cancelacion: 8% (objetivo: 5%)

**PREDICCIONES IA:**
- Sabado proximo: Se llenara 100%
- Lunes 05/02: Solo 60% ocupado
- Recomendacion: Ofrecer promo lunes

El sistema aprende y optimiza tu agenda automaticamente!

Queres ver algo especifico?""",
            "buttons": "estadisticas_acciones"
        }
    
    # 7) Lista de espera
    if "lista" in p or "espera" in p or "completo" in p or "lleno" in p:
        return {
            "content": """⏰ **Sistema de Lista de Espera Inteligente**

**COMO FUNCIONA:**

**1. TURNO COMPLETO**
- Sistema te ofrece automaticamente lista de espera
- Te registras con un click
- Sin costo ni compromiso

**2. SE LIBERA UN TURNO**
- Notificacion INSTANTANEA por WhatsApp
- Tienes 30 minutos para confirmar
- Si no respondes, pasa al siguiente

**3. CONFIRMACION AUTOMATICA**
- Click en el link
- Turno reservado
- Confirmacion por email

**VENTAJAS:**
✅ No perdes tiempo buscando
✅ Notificacion inmediata
✅ Prioridad sobre nuevas reservas
✅ Sistema justo (orden de llegada)

**ACTUALMENTE EN LISTA:**

**Sabado 03/02 - 10:00am**
- 3 personas esperando
- Tu posicion: Proxima
- Probabilidad liberacion: 60%

**Viernes 02/02 - 17:00pm**
- 2 personas esperando
- Tu posicion: Primera
- Probabilidad: 80%

**💡 DATO:** El 45% de los turnos en lista de espera se confirman!

Queres anotarte en alguna lista?""",
            "buttons": "lista_espera_acciones"
        }
    
    # Respuesta por defecto
    return {
        "content": """No estoy seguro de entender 🤔

**PUEDO AYUDARTE CON:**

📅 **RESERVAS**
- Ver calendario disponible
- Seleccionar profesional
- Elegir servicio
- Confirmar turno

📱 **GESTION**
- Cancelar/modificar turnos
- Lista de espera
- Recordatorios automaticos
- Historial de turnos

📊 **INFORMACION**
- Servicios y precios
- Equipo de profesionales
- Horarios de atencion
- Estadisticas y reportes

**EJEMPLOS:**
- "Quiero turno para esta semana"
- "Mostrame el calendario"
- "Que servicios ofrecen"
- "Como funcionan los recordatorios"
- "Ver estadisticas"

Que necesitas?""",
        "buttons": "ayuda"
    }

# Mostrar mensajes del chat
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        if message.get("show_buttons"):
            button_type = message["show_buttons"]
            
            # Botones iniciales con calendario
            if button_type == "inicial_con_calendario":
                # CALENDARIO VISUAL
                st.markdown("### 📅 Selecciona una fecha:")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("📅 HOY Lun 29/01\n⚠️ 3 turnos", key="cal_hoy_{}".format(i), use_container_width=True):
                        response = get_bot_response("calendario")
                        add_message_and_hide_buttons("Ver calendario completo", response["content"], response.get("buttons"))
                        st.rerun()
                
                with col2:
                    if st.button("📅 MAR 30/01\n✅ 12 turnos", key="cal_mar_{}".format(i), use_container_width=True):
                        response = get_bot_response("calendario")
                        add_message_and_hide_buttons("Ver calendario completo", response["content"], response.get("buttons"))
                        st.rerun()
                
                with col3:
                    if st.button("📅 MIE 31/01\n✅ 15 turnos", key="cal_mie_{}".format(i), use_container_width=True):
                        response = get_bot_response("calendario")
                        add_message_and_hide_buttons("Ver calendario completo", response["content"], response.get("buttons"))
                        st.rerun()
                
                st.markdown("---")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💇 Ver servicios", key="btn_serv_{}".format(i), use_container_width=True):
                        response = get_bot_response("servicios")
                        add_message_and_hide_buttons("Que servicios tienen", response["content"], response.get("buttons"))
                        st.rerun()
                
                with col2:
                    if st.button("👥 Ver profesionales", key="btn_prof_{}".format(i), use_container_width=True):
                        response = get_bot_response("profesionales")
                        add_message_and_hide_buttons("Quienes son los profesionales", response["content"], response.get("buttons"))
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📱 Recordatorios", key="btn_rec_{}".format(i), use_container_width=True):
                        response = get_bot_response("recordatorios")
                        add_message_and_hide_buttons("Como funcionan los recordatorios", response["content"], response.get("buttons"))
                        st.rerun()
                
                with col2:
                    if st.button("📊 Estadisticas", key="btn_est_{}".format(i), use_container_width=True):
                        response = get_bot_response("estadisticas")
                        add_message_and_hide_buttons("Ver estadisticas", response["content"], response.get("buttons"))
                        st.rerun()
            
            # Despues de ver calendario
            elif button_type == "seleccionar_dia":
                st.markdown("**Selecciona un dia:**")
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("MAR 30/01", key="dia_mar_{}".format(i), use_container_width=True):
                        add_message_and_hide_buttons(
                            "Martes 30/01",
                            """⏰ **Horarios Disponibles - Martes 30/01**

**MANANA**
- 09:00 ✅ Ana / Lucia
- 10:00 ✅ Carlos / Sofia
- 11:00 ✅ Ana / Lucia / Carlos
- 12:00 ✅ Sofia

**TARDE**
- 14:30 ✅ Ana / Carlos
- 15:30 ✅ Lucia / Sofia
- 16:30 ✅ Ana / Carlos / Sofia
- 17:30 ✅ Todos disponibles
- 18:00 ✅ Lucia / Carlos

Que horario te viene bien?""",
                            "seleccionar_horario"
                        )
                        st.rerun()
                
                with col2:
                    if st.button("MIE 31/01", key="dia_mie_{}".format(i), use_container_width=True):
                        add_message_and_hide_buttons(
                            "Miercoles 31/01",
                            """⏰ **Horarios Disponibles - Miercoles 31/01**

**MANANA**
- 09:30 ✅ Ana / Lucia / Carlos
- 11:00 ✅ Todos disponibles
- 12:00 ✅ Sofia / Ana

**TARDE**
- 15:00 ✅ Lucia / Carlos
- 16:00 ✅ Ana / Sofia
- 17:00 ✅ Todos disponibles

💡 Miercoles: Mejor dia para mas opciones

Que horario prefieres?""",
                            "seleccionar_horario"
                        )
                        st.rerun()
                
                with col3:
                    if st.button("JUE 01/02", key="dia_jue_{}".format(i), use_container_width=True):
                        add_message_and_hide_buttons(
                            "Jueves 01/02",
                            """⏰ **Horarios Disponibles - Jueves 01/02**

**MANANA**
- 09:00 ✅ Carlos / Sofia
- 10:30 ✅ Ana / Lucia
- 11:30 ✅ Carlos

**TARDE**
- 14:00 ✅ Sofia / Ana
- 15:00 ✅ Lucia / Carlos
- 16:00 ✅ Ana / Sofia
- 17:30 ✅ Carlos

Que hora te sirve?""",
                            "seleccionar_horario"
                        )
                        st.rerun()
            
            # Seleccionar servicio
            elif button_type == "seleccionar_servicio":
                if st.button("✂️ Corte Clasico ($800)", key="serv_corte_{}".format(i), use_container_width=True):
                    add_message_and_hide_buttons(
                        "Corte Clasico",
                        """✅ **Servicio seleccionado: Corte Clasico**

- Duracion: 30 minutos
- Precio: $800
- Profesionales disponibles: Ana, Lucia, Carlos

Ahora necesito:
1. Que dia prefieres? (ej: "Martes 30/01")
2. Que horario? (ej: "15:00")
3. Con quien? (o digo "el que este disponible")

O escribi todo junto: "Martes 15:00 con Lucia" """,
                        None
                    )
                    st.rerun()
                
                if st.button("🎨 Tintura Completa ($2.500)", key="serv_tin_{}".format(i), use_container_width=True):
                    add_message_and_hide_buttons(
                        "Tintura Completa",
                        """✅ **Servicio seleccionado: Tintura Completa**

- Duracion: 90 minutos
- Precio: $2.500
- Profesional especialista: Ana Martinez

Necesito tu disponibilidad:
1. Que dia te viene bien?
2. Horario preferido?

💡 Requiere 90min, te sugiero horarios de mañana para mejor resultado.

Escribi: "Miercoles 10:00" """,
                        None
                    )
                    st.rerun()
            
            # Ayuda general
            elif button_type == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Ver calendario", key="btn_cal_ayuda_{}".format(i), use_container_width=True):
                        response = get_bot_response("calendario")
                        add_message_and_hide_buttons("Mostrar calendario", response["content"], response.get("buttons"))
                        st.rerun()
                
                with col2:
                    if st.button("💇 Ver servicios", key="btn_serv_ayuda_{}".format(i), use_container_width=True):
                        response = get_bot_response("servicios")
                        add_message_and_hide_buttons("Ver servicios", response["content"], response.get("buttons"))
                        st.rerun()

# Ejemplos de consultas
st.markdown("---")
st.markdown("**💬 Ejemplos de lo que puedo hacer:**")
col1, col2 = st.columns(2)
with col1:
    st.caption("• Mostrame el calendario disponible")
    st.caption("• Quiero turno para corte el martes")
    st.caption("• Necesito cancelar mi turno del jueves")
    st.caption("• Que servicios tienen y precios")
    st.caption("• Como funcionan los recordatorios")
with col2:
    st.caption("• Ver estadisticas de la semana")
    st.caption("• Quienes son los profesionales")
    st.caption("• Anotarme en lista de espera")
    st.caption("• Ver mi historial de turnos")
    st.caption("• Que horarios atienden")

# Input del chat
if prompt := st.chat_input("Escribi tu consulta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_bot_response(prompt)
    st.session_state.messages.append({
        "role": "assistant",
        "content": response["content"],
        "show_buttons": response.get("buttons")
    })
    if response.get("bonus_once"):
        maybe_append_bonus_once()
    st.rerun()

# Footer impactante
st.divider()
st.caption("💡 **Sistema profesional de gestion de turnos** - Nivel empresarial")
st.caption("🔌 **Integraciones:** Google Calendar, WhatsApp Business API, Twilio SMS, Mailchimp")
st.caption("📊 **ROI comprobado:** -60% inasistencias, +40% eficiencia, 15hs/semana ahorradas")

# Boton reset
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """Hola! Soy tu asistente de turnos 24/7 📅

**📊 ESTADO DE TU AGENDA HOY:**
- Turnos confirmados: 12
- Espacios libres: 8
- Lista de espera: 3 clientes

**Que necesitas?**""",
                "show_buttons": "inicial_con_calendario"
            }
        ]
        st.session_state.button_clicked = False
        st.session_state.bonus_shown = False
        st.rerun()
