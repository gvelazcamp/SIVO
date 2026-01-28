import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Demo Viajes - MercadoBot",
    page_icon="✈️",
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
    
    /* Estilos del chat */
    .stChatMessage {
        max-width: 800px;
        margin: 0 auto;
    }
    
    .stChatFloatingInputContainer {
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Header personalizado - más profesional */
    .custom-header {
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
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
    
    /* Botones más profesionales */
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
        background: #0f3460;
        border-color: #0f3460;
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(15, 52, 96, 0.2);
    }
    
    /* Mejorar los caption de ejemplos */
    .stCaption {
        color: #6b7280 !important;
        font-size: 14px !important;
        line-height: 1.8 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header personalizado
st.markdown("""
<div class="custom-header">
    <h1>🌍 Asistente de Viajes Inteligente</h1>
    <p>Encontrá tu próximo destino ideal. Preguntame lo que necesites.</p>
</div>
""", unsafe_allow_html=True)

# Inicializar el chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": """¡Hola! 👋 Soy tu asistente de viajes.

**¿Qué tipo de viaje te interesa?**""",
            "show_buttons": "inicial"
        }
    ]

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

# Función para agregar mensaje y ocultar botones
def add_message_and_hide_buttons(user_msg, bot_response, next_buttons=None):
    st.session_state.messages.append({"role": "user", "content": user_msg})
    st.session_state.messages.append({
        "role": "assistant", 
        "content": bot_response,
        "show_buttons": next_buttons
    })
    st.session_state.button_clicked = True

# Función para obtener respuesta del bot
def get_bot_response(prompt):
    p = prompt.lower()
    
    # Respuestas basadas en el flujo
    if any(word in p for word in ["playa", "relax", "marzo", "verano"]):
        return {
            "content": """¡Perfecto! 🏖️ Te recomiendo estas opciones:""",
            "buttons": "destinos_playa"
        }
    
    elif "cancun" in p or "cancún" in p or "opción 1" in p:
        return {
            "content": """¡Excelente elección! 🇲🇽

**Paquete Cancún Premium incluye:**
✅ Vuelos directos Buenos Aires → Cancún
✅ Hotel 5★ frente al mar (7 noches)
✅ All inclusive (desayuno, almuerzo, cena, bar)
✅ Traslados aeropuerto ↔ hotel
✅ Excursión a Chichén Itzá GRATIS
✅ Snorkel en cenotes GRATIS

**Precio:** USD 1.200/persona

🎁 **Reservando HOY:** $50 USD descuento + upgrade de habitación""",
            "buttons": "acciones_cancun"
        }
    
    elif "punta cana" in p or "opción 2" in p:
        return {
            "content": """¡Gran elección! 🇩🇴

**Paquete Punta Cana Premium:**
✅ Vuelos directos Buenos Aires → Punta Cana
✅ Resort 5★ all inclusive (7 noches)
✅ Playa Bávaro (mejor zona)
✅ Excursiones incluidas (Isla Saona)
✅ Deportes acuáticos ilimitados

**Precio:** USD 1.350/persona

🎁 **Bonus:** Masaje en el spa incluido""",
            "buttons": "acciones_punta_cana"
        }
    
    elif "florianopolis" in p or "florianópolis" in p or "opción 3" in p:
        return {
            "content": """¡Excelente! 🇧🇷

**Paquete Florianópolis:**
✅ Vuelos Buenos Aires → Florianópolis
✅ Hotel boutique cerca de la playa (5 noches)
✅ Desayuno incluido
✅ Traslados aeropuerto ↔ hotel
✅ Tour por las mejores playas

**Precio:** USD 800/persona

🎁 **Ventaja:** Más económico y cerca, español muy parecido""",
            "buttons": "acciones_floripa"
        }
    
    elif "montaña" in p or "nieve" in p or "esqui" in p:
        return {
            "content": """¡Genial! ❄️ Te muestro las mejores opciones de montaña:""",
            "buttons": "destinos_montana"
        }
    
    elif "aventura" in p:
        return {
            "content": """¡Perfecto para aventureros! 🎒 Mirá estas opciones:""",
            "buttons": "destinos_aventura"
        }
    
    elif any(word in p for word in ["personas", "2", "dos", "3", "tres"]):
        return {
            "content": """Perfecto! Para 2 personas: **USD 2.400 total** ✈️

**¿Querés agregar experiencias VIP?**""",
            "buttons": "experiencias"
        }
    
    elif any(word in p for word in ["cuotas", "pago", "financ", "tarjeta"]):
        return {
            "content": """¡Claro! 💳

**Formas de pago disponibles:**
💵 **Efectivo/Transferencia:** 5% descuento adicional
💳 **Tarjeta de crédito:**
   • 3 cuotas sin interés
   • 6 cuotas sin interés
   • 12 cuotas (TNA 48%)
🌎 **Mercado Pago:** Hasta 18 cuotas

**Ejemplo para 2 personas (USD 2.400):**
→ 6 cuotas de **USD 400** sin interés
→ 12 cuotas de **USD 220** c/interés""",
            "buttons": "pago_opciones"
        }
    
    elif "reservar" in p or "comprar" in p or "quiero" in p or "sí" in p:
        return {
            "content": """¡GENIAAAL! 🎉

**Para confirmar necesito:**
📝 Datos de los pasajeros (nombre completo, DNI, fecha nac.)
📧 Email de contacto
📱 WhatsApp

**Opciones para continuar:**""",
            "buttons": "contacto"
        }
    
    else:
        return {
            "content": """Puedo ayudarte con muchas cosas! 😊

**¿Qué te gustaría saber?**""",
            "buttons": "ayuda"
        }

# Mostrar historial de mensajes
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
        # Mostrar botones solo si es el último mensaje del asistente
        is_last_assistant = (i == len(st.session_state.messages) - 1 and msg["role"] == "assistant")
        
        if is_last_assistant and "show_buttons" in msg and msg["show_buttons"]:
            button_type = msg["show_buttons"]
            
            # Botones iniciales
            if button_type == "inicial":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🏖️ Playa", key=f"btn_playa_{i}", use_container_width=True):
                        response = get_bot_response("playa")
                        add_message_and_hide_buttons("🏖️ Playa", response["content"], response["buttons"])
                        st.rerun()
                
                with col2:
                    if st.button("⛰️ Montaña", key=f"btn_montana_{i}", use_container_width=True):
                        response = get_bot_response("montaña")
                        add_message_and_hide_buttons("⛰️ Montaña", response["content"], response["buttons"])
                        st.rerun()
                
                with col3:
                    if st.button("🎒 Aventura", key=f"btn_aventura_{i}", use_container_width=True):
                        response = get_bot_response("aventura")
                        add_message_and_hide_buttons("🎒 Aventura", response["content"], response["buttons"])
                        st.rerun()
            
            # Botones de destinos playa
            elif button_type == "destinos_playa":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🇲🇽 Cancún\nUSD 1.200", key=f"btn_cancun_{i}", use_container_width=True):
                        response = get_bot_response("cancun")
                        add_message_and_hide_buttons("Opción 1 - Cancún", response["content"], response["buttons"])
                        st.rerun()
                
                with col2:
                    if st.button("🇩🇴 Punta Cana\nUSD 1.350", key=f"btn_punta_{i}", use_container_width=True):
                        response = get_bot_response("punta cana")
                        add_message_and_hide_buttons("Opción 2 - Punta Cana", response["content"], response["buttons"])
                        st.rerun()
                
                with col3:
                    if st.button("🇧🇷 Florianópolis\nUSD 800", key=f"btn_floripa_{i}", use_container_width=True):
                        response = get_bot_response("florianopolis")
                        add_message_and_hide_buttons("Opción 3 - Florianópolis", response["content"], response["buttons"])
                        st.rerun()
            
            # Botones de acciones Cancún
            elif button_type == "acciones_cancun":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("👥 ¿Para cuántos?", key=f"btn_personas_{i}", use_container_width=True):
                        response = get_bot_response("2 personas")
                        add_message_and_hide_buttons("¿Cuánto para 2 personas?", response["content"], response["buttons"])
                        st.rerun()
                
                with col2:
                    if st.button("💳 Formas de pago", key=f"btn_pago_{i}", use_container_width=True):
                        response = get_bot_response("formas de pago")
                        add_message_and_hide_buttons("💳 ¿Cómo puedo pagar?", response["content"], response["buttons"])
                        st.rerun()
                
                with col3:
                    if st.button("✅ ¡Lo quiero!", key=f"btn_reservar_{i}", use_container_width=True):
                        response = get_bot_response("quiero reservar")
                        add_message_and_hide_buttons("✅ Quiero reservar", response["content"], response["buttons"])
                        st.rerun()
            
            # Botones de acciones Punta Cana
            elif button_type == "acciones_punta_cana":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("👥 ¿Para cuántos?", key=f"btn_personas_pc_{i}", use_container_width=True):
                        response = get_bot_response("2 personas")
                        add_message_and_hide_buttons("¿Cuánto para 2 personas?", response["content"], response["buttons"])
                        st.rerun()
                
                with col2:
                    if st.button("💳 Formas de pago", key=f"btn_pago_pc_{i}", use_container_width=True):
                        response = get_bot_response("formas de pago")
                        add_message_and_hide_buttons("💳 ¿Cómo puedo pagar?", response["content"], response["buttons"])
                        st.rerun()
                
                with col3:
                    if st.button("✅ ¡Lo quiero!", key=f"btn_reservar_pc_{i}", use_container_width=True):
                        response = get_bot_response("quiero reservar")
                        add_message_and_hide_buttons("✅ Quiero reservar", response["content"], response["buttons"])
                        st.rerun()
            
            # Botones de acciones Floripa
            elif button_type == "acciones_floripa":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("👥 ¿Para cuántos?", key=f"btn_personas_fl_{i}", use_container_width=True):
                        response = get_bot_response("2 personas")
                        add_message_and_hide_buttons("¿Cuánto para 2 personas?", response["content"], response["buttons"])
                        st.rerun()
                
                with col2:
                    if st.button("💳 Formas de pago", key=f"btn_pago_fl_{i}", use_container_width=True):
                        response = get_bot_response("formas de pago")
                        add_message_and_hide_buttons("💳 ¿Cómo puedo pagar?", response["content"], response["buttons"])
                        st.rerun()
                
                with col3:
                    if st.button("✅ ¡Lo quiero!", key=f"btn_reservar_fl_{i}", use_container_width=True):
                        response = get_bot_response("quiero reservar")
                        add_message_and_hide_buttons("✅ Quiero reservar", response["content"], response["buttons"])
                        st.rerun()
            
            # Botones de experiencias
            elif button_type == "experiencias":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🌊 Nado con delfines\n+USD 120", key=f"btn_delfines_{i}", use_container_width=True):
                        add_message_and_hide_buttons("🌊 Agregar nado con delfines", "¡Agregado! 🐬 Experiencia increíble incluida.\n\n**Total:** USD 2.640\n\n¿Querés agregar algo más?", "experiencias_mas")
                        st.rerun()
                
                with col2:
                    if st.button("🏛️ Tour Tulum privado\n+USD 150", key=f"btn_tulum_{i}", use_container_width=True):
                        add_message_and_hide_buttons("🏛️ Agregar tour a Tulum", "¡Agregado! 🏛️ Tour privado confirmado.\n\n**Total:** USD 2.700\n\n¿Querés agregar algo más?", "experiencias_mas")
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🍽️ Cena romántica\n+USD 80", key=f"btn_cena_{i}", use_container_width=True):
                        add_message_and_hide_buttons("🍽️ Agregar cena romántica", "¡Agregado! 🍽️ Cena en la playa incluida.\n\n**Total:** USD 2.480\n\n¿Querés agregar algo más?", "experiencias_mas")
                        st.rerun()
                
                with col2:
                    if st.button("❌ No, seguir sin extras", key=f"btn_sin_extras_{i}", use_container_width=True):
                        add_message_and_hide_buttons("No agregar extras", "Perfecto! Mantenemos el paquete básico.\n\n**Total:** USD 2.400\n\n¿Cómo querés pagar?", "pago_opciones")
                        st.rerun()
            
            # Botones de pago
            elif button_type == "pago_opciones":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("💵 Efectivo\n5% OFF", key=f"btn_efectivo_{i}", use_container_width=True):
                        add_message_and_hide_buttons("💵 Pagar en efectivo", "¡Excelente! Con el descuento del 5%:\n\n**Total final:** USD 2.280\n\n¿Confirmamos la reserva?", "contacto")
                        st.rerun()
                
                with col2:
                    if st.button("💳 6 cuotas\nSin interés", key=f"btn_6cuotas_{i}", use_container_width=True):
                        add_message_and_hide_buttons("💳 Pagar en 6 cuotas", "Perfecto! Plan de pago:\n\n**6 cuotas de USD 400** sin interés\n\n¿Confirmamos la reserva?", "contacto")
                        st.rerun()
                
                with col3:
                    if st.button("💳 12 cuotas\nCon interés", key=f"btn_12cuotas_{i}", use_container_width=True):
                        add_message_and_hide_buttons("💳 Pagar en 12 cuotas", "Entendido! Plan de pago:\n\n**12 cuotas de USD 220** c/interés\n\n¿Confirmamos la reserva?", "contacto")
                        st.rerun()
            
            # Botones de contacto
            elif button_type == "contacto":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("💬 WhatsApp", key=f"btn_whatsapp_{i}", use_container_width=True):
                        add_message_and_hide_buttons("💬 Seguir por WhatsApp", "Perfecto! 📱\n\n**Continuá en:** +54 9 11 1234-5678\n\nTe enviamos el formulario y link de pago.\n\n¡Gracias por confiar en nosotros! ✈️", None)
                        st.rerun()
                
                with col2:
                    if st.button("📞 Llamada", key=f"btn_llamar_{i}", use_container_width=True):
                        add_message_and_hide_buttons("📞 Prefiero llamada", "¡Dale! 📞\n\nTe llamamos en 5 minutos al número que nos dejes.\n\n**Dejanos tu teléfono en el chat o contactanos:**\n+54 9 11 1234-5678\n\n¡Gracias por elegir viajar con nosotros! ✈️", None)
                        st.rerun()
                
                with col3:
                    if st.button("📧 Email", key=f"btn_email_{i}", use_container_width=True):
                        add_message_and_hide_buttons("📧 Enviar por email", "Listo! 📧\n\n**Enviamos toda la info a tu email.**\n\nDejanos tu email en el chat o escribinos a:\nviajes@mercadobot.com\n\n¡Nos vemos en Cancún! 🏖️", None)
                        st.rerun()
            
            # Botones de ayuda
            elif button_type == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏖️ Ver destinos", key=f"btn_destinos_{i}", use_container_width=True):
                        response = get_bot_response("playa")
                        add_message_and_hide_buttons("Mostrame destinos", response["content"], response["buttons"])
                        st.rerun()
                
                with col2:
                    if st.button("💳 Formas de pago", key=f"btn_pago_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("formas de pago")
                        add_message_and_hide_buttons("¿Cómo puedo pagar?", response["content"], response["buttons"])
                        st.rerun()
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📋 Requisitos", key=f"btn_requisitos_{i}", use_container_width=True):
                        add_message_and_hide_buttons("¿Qué necesito?", "Para viajar a México necesitás:\n\n✅ Pasaporte válido (mín. 6 meses)\n✅ Formulario migratorio\n✅ Seguro de viaje (incluido)\n\n❌ NO necesitas visa\n\n¿Tenés tu pasaporte al día?", "requisitos_opciones")
                        st.rerun()
                
                with col2:
                    if st.button("🛡️ Seguros", key=f"btn_seguros_{i}", use_container_width=True):
                        add_message_and_hide_buttons("Info sobre seguros", "**Seguro Básico (incluido):**\n✅ Gastos médicos USD 50.000\n✅ Equipaje perdido USD 1.000\n\n**Seguro Premium (+USD 80):**\n✅ Gastos médicos USD 150.000\n✅ COVID cubierto 100%\n✅ Deportes extremos\n\n¿Querés el Premium?", "seguro_opciones")
                        st.rerun()

# Mostrar sugerencias de preguntas al final (SIEMPRE visible)
st.markdown("---")
st.markdown("**💬 Ejemplos de consultas que podés hacer:**")
col1, col2 = st.columns(2)
with col1:
    st.caption("• Quiero ir a la playa en marzo con $1500 USD")
    st.caption("• ¿Qué opciones hay para viajar con 2 niños?")
    st.caption("• Buscamos algo romántico para luna de miel")
    st.caption("• ¿Cuánto sale Punta Cana todo incluido?")
    st.caption("• Viajo solo, 25 años, busco aventura")
with col2:
    st.caption("• ¿Puedo pagar en 6 cuotas sin interés?")
    st.caption("• ¿Necesito tramitar visa para Brasil?")
    st.caption("• ¿Qué está incluido en el paquete a Cancún?")
    st.caption("• Tengo $800 USD, ¿a dónde puedo ir?")
    st.caption("• Quiero algo tranquilo, tipo spa y relax")

# Procesar input del usuario o botón de sugerencia
if "temp_input" in st.session_state:
    prompt = st.session_state.temp_input
    del st.session_state.temp_input
    
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Obtener respuesta
    response = get_bot_response(prompt)
    
    # Agregar respuesta del bot
    st.session_state.messages.append({
        "role": "assistant", 
        "content": response["content"],
        "show_buttons": response["buttons"]
    })
    
    st.rerun()

# Input del chat
if prompt := st.chat_input("Escribí tu pregunta o hacé click en las opciones..."):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Obtener respuesta del bot
    response = get_bot_response(prompt)
    
    # Agregar respuesta del bot
    st.session_state.messages.append({
        "role": "assistant", 
        "content": response["content"],
        "show_buttons": response.get("buttons")
    })
    
    with st.chat_message("assistant"):
        st.markdown(response["content"])

# Footer
st.divider()
st.caption("💡 **Este es un demo interactivo.** El bot responde con información de ejemplo.")
st.caption("🔌 En producción conecta con tu base de datos real y APIs de viajes.")

# Botón para resetear conversación
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar chat"):
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": """¡Hola! 👋 Soy tu asistente de viajes.

**¿Qué tipo de viaje te interesa?**""",
                "show_buttons": "inicial"
            }
        ]
        st.session_state.button_clicked = False
        st.rerun()
