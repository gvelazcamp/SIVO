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

    if any(word in p for word in ["1500", "1.500"]) and ("usd" in p or "dolares" in p or "dólares" in p) and any(word in p for word in ["playa", "marzo", "verano"]):
        return {
            "content": """¡Excelente presupuesto! Con USD 1.500 en marzo tenés destinos de playa TOP 🌟""",
            "buttons": "playa_1500"
        }

    elif any(word in p for word in ["playa", "relax", "marzo", "verano"]) and any(word in p for word in ["1500", "1.500"]):
        return {
            "content": """¡Perfecto! 🏖️ Con USD 1.500 para playa en marzo te recomiendo:""",
            "buttons": "playa_1500"
        }

    # Respuestas basadas en el flujo
    elif any(word in p for word in ["playa", "relax", "marzo", "verano"]):
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

    elif "florianopolis" in p or "florianópolis" in p or "opción 3" in p or "floripa" in p:
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

    elif "montaña" in p or "nieve" in p or "esqui" in p or "bariloche" in p:
        return {
            "content": """¡Genial! ❄️ Las mejores opciones de montaña:

**OPCIÓN 1 — Bariloche, Argentina 🇦🇷**
• Hotel 4★ con vista al lago (5 días): USD 950/persona
• Pase de ski Cerro Catedral incluido
• Desayuno buffet + cena
• Excursión Circuito Chico
⛷️ Temporada alta: Julio-Agosto

**OPCIÓN 2 — Valle Nevado, Chile 🇨🇱**
• Resort ski in/ski out (6 días): USD 1.800/persona
• All inclusive (comidas + pases)
• Clases de ski/snowboard incluidas
• La mejor nieve de Sudamérica
❄️ Ideal para esquiadores avanzados

**OPCIÓN 3 — Ushuaia, Argentina 🇦🇷**
• Hotel boutique (4 días): USD 1.100/persona
• Cerro Castor ski resort
• Excursión Canal Beagle
• Cena con centolla fresca
🏔️ El fin del mundo + montaña

¿Cuál te copa más?""",
            "buttons": "montana_opciones"
        }

    elif "aventura" in p:
        return {
            "content": """¡Perfecto para aventureros! 🎒 Mirá estas opciones:

**OPCIÓN 1 — Iguazú Extremo 🇦🇷🇧🇷**
• 4 días lado argentino + brasilero: USD 650/persona
• Rapel en las cataratas
• Kayak en el río Iguazú
• Trekking Macuco Trail
• Vuelo en helicóptero sobre las cataratas
🌊 Adrenalina pura en la selva

**OPCIÓN 2 — Salta Adventure 🇦🇷**
• Ruta 7 días (Salta-Jujuy-Cafayate): USD 980/persona
• Trekking Quebrada de Humahuaca
• Sandboard en dunas de Cafayate
• Cabalgata en los Valles Calchaquíes
• Visita bodegas de altura
🏜️ Paisajes de otro planeta

**OPCIÓN 3 — Mendoza Extremo 🇦🇷**
• 5 días outdoor: USD 1.100/persona
• Rafting clase III-IV en río Mendoza
• Trekking base del Aconcagua
• Canopy en el Valle de Uco
• Tour bodegas + degustación
🏔️ Montaña + vino

¿Qué nivel de adrenalina buscás?""",
            "buttons": "aventura_opciones"
        }

    # NUEVAS RESPUESTAS CONTEXTUALES
    elif any(word in p for word in ["niños", "niño", "hijos", "familia", "chicos"]):
        return {
            "content": """¡Perfecto viaje familiar! 👨‍👩‍👧‍👦

Encontré opciones ideales para viajar con niños:""",
            "buttons": "familia_destinos"
        }

    elif any(word in p for word in ["luna de miel", "romántico", "pareja", "casamiento", "boda"]):
        return {
            "content": """¡¡¡FELICITACIONES!!! 💍✨

Opciones ROMÁNTICAS para luna de miel:""",
            "buttons": "luna_miel_destinos"
        }

    elif any(word in p for word in ["solo", "sola", "mochilero", "backpacker", "viajo solo"]):
        return {
            "content": """¡Genial! 🎒 Viajes para aventureros solitarios:""",
            "buttons": "solo_destinos"
        }

    elif any(word in p for word in ["800", "económico", "barato", "poco presupuesto"]) and ("usd" in p or "dolares" in p or "dólares" in p):
        return {
            "content": """¡Perfecto! Con USD 800 tenés MUY buenas opciones 💰""",
            "buttons": "economicos_destinos"
        }

    elif any(word in p for word in ["spa", "relax", "tranquilo", "descanso", "wellness"]):
        return {
            "content": """Perfecto para desconectar 🧘‍♀️💆‍♂️""",
            "buttons": "spa_destinos"
        }

    elif any(word in p for word in ["1500", "1.500"]) and ("usd" in p or "dolares" in p or "dólares" in p):
        return {
            "content": """¡Excelente presupuesto! Con USD 1.500 accedés a destinos TOP 🌟""",
            "buttons": "rango_medio_destinos"
        }

    elif any(word in p for word in ["25", "joven", "20", "30 años", "jovenes", "jóvenes"]):
        return {
            "content": """¡Dale! Para tu edad tengo opciones copadas 🎉""",
            "buttons": "jovenes_destinos"
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

    elif any(word in p for word in ["visa", "pasaporte", "documento", "requisito"]):
        return {
            "content": """Te cuento los requisitos según destino 📋

**Para MÉXICO (Cancún, Playa del Carmen):**
✅ Pasaporte válido mínimo 6 meses
❌ NO necesita visa
✅ Seguro de viaje (incluido en nuestro paquete)
📝 Formulario migratorio (te lo damos)

**Para BRASIL (Río, Florianópolis):**
✅ DNI argentino actualizado (alcanza)
❌ NO necesita pasaporte ni visa
✅ Seguro de viaje recomendado

**Para USA (Miami, Orlando):**
✅ Pasaporte válido
✅ Visa de turista B1/B2 (tramitada y vigente)
💰 Costo visa: USD 185 (no incluido)
⏰ Turno en embajada: 2-3 semanas

**Para EUROPA (España, Italia, Francia):**
✅ Pasaporte válido mínimo 6 meses
❌ NO necesita visa (hasta 90 días)
✅ Seguro médico obligatorio EUR 30.000
💰 Incluido en nuestros paquetes

**Para COLOMBIA / PERÚ / CHILE:**
✅ DNI o pasaporte
❌ NO necesita visa
✅ Seguro de viaje recomendado

¿A qué destino pensabas ir?""",
            "buttons": None
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

            # Botones familia
            elif button_type == "familia_destinos":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🇺🇸 Disney\nUSD 3.200/adulto", key=f"btn_disney_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Disney Orlando",
                            "**Disney Orlando 🇺🇸**\n• 7 días parques + hotel\n• Entradas 4 parques (Magic Kingdom, Epcot, Hollywood, Animal Kingdom)\n• Character dining incluido\n• Fast Pass\n🎢 **Precio:** USD 3.200/adulto, USD 2.400/niño",
                            "familia_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇲🇽 Cancún Familiar\nUSD 1.400/adulto", key=f"btn_cancun_fam_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Cancún Familiar",
                            "**Cancún Familiar 🇲🇽**\n• Resort all inclusive con Kids Club\n• Niños -6 años GRATIS\n• Parque acuático incluido\n• Menú infantil especial\n🏖️ **Precio:** USD 1.400/adulto, USD 700/niño",
                            "familia_acciones"
                        )
                        st.rerun()

                with col3:
                    if st.button("🇦🇷 Bariloche\nUSD 850/adulto", key=f"btn_bari_fam_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Bariloche con Niños",
                            "**Bariloche con Niños 🇦🇷**\n• 5 días naturaleza + chocolate\n• Museo del Chocolate interactivo\n• Cerro Campanario (telesilla)\n• Catamarán + mini trekking\n🍫 **Precio:** USD 850/adulto, USD 450/niño",
                            "familia_acciones"
                        )
                        st.rerun()

            # Botones luna de miel
            elif button_type == "luna_miel_destinos":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🇲🇻 Maldivas\nUSD 4.500", key=f"btn_maldivas_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Maldivas",
                            "**Maldivas 🇲🇻**\n• 7 noches villa sobre el agua\n• Desayuno flotante\n• Cena bajo las estrellas\n• Masaje de pareja\n🌴 **Precio:** USD 4.500/pareja",
                            "luna_miel_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇬🇷 Santorini\nUSD 3.200", key=f"btn_santorini_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Santorini",
                            "**Santorini 🇬🇷**\n• 6 noches cave hotel con jacuzzi\n• Tour catamarán al atardecer\n• Cena en Oia\n• Sesión fotos profesional\n🌅 **Precio:** USD 3.200/pareja",
                            "luna_miel_acciones"
                        )
                        st.rerun()

                with col3:
                    if st.button("🇩🇴 Punta Cana Luxury\nUSD 2.800", key=f"btn_punta_luxury_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Punta Cana Luxury",
                            "**Punta Cana Luxury 🇩🇴**\n• 7 noches adults-only resort\n• Suite con jacuzzi\n• Butler service 24/7\n• Champagne diario\n🥂 **Precio:** USD 2.800/pareja",
                            "luna_miel_acciones"
                        )
                        st.rerun()

            # Botones viajeros solos
            elif button_type == "solo_destinos":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🇵🇪 Machu Picchu\nUSD 1.650", key=f"btn_machu_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Machu Picchu",
                            "**Machu Picchu 🇵🇪**\n• 10 días Lima-Cusco-MP\n• Grupos 12 personas máx\n• Trekking Camino Inca\n• Valle Sagrado completo\n👥 **Precio:** USD 1.650",
                            "solo_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇨🇴 Colombia\nUSD 1.400", key=f"btn_colombia_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Colombia Adventure",
                            "**Colombia Adventure 🇨🇴**\n• 12 días ruta completa\n• Cartagena + Medellín + Tayrona\n• Hostels top\n• Actividades opcionales\n🌴 **Precio:** USD 1.400",
                            "solo_acciones"
                        )
                        st.rerun()

                with col3:
                    if st.button("🇪🇺 Europa Interrail\nUSD 2.200", key=f"btn_europa_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Europa Interrail",
                            "**Europa Interrail 🇪🇺**\n• 15 días, 5 países\n• Pase de tren ilimitado\n• Barcelona-París-Amsterdam-Berlín-Praga\n• Flexibilidad total\n🚂 **Precio:** USD 2.200",
                            "solo_acciones"
                        )
                        st.rerun()

            # Botones económicos
            elif button_type == "economicos_destinos":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🇧🇷 Florianópolis\nUSD 800", key=f"btn_floripa_eco_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Florianópolis",
                            "**Florianópolis 🇧🇷**\n• 5 días todo incluido\n• 42 playas + vida nocturna\n• Tour mejores playas\n🏖️ **Precio:** USD 800",
                            "economico_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇦🇷 Mendoza\nUSD 750", key=f"btn_mendoza_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Mendoza",
                            "**Mendoza 🇦🇷**\n• 4 días vino + montaña\n• Tour 2 bodegas premium\n• Alta montaña + rafting\n🍷 **Precio:** USD 750",
                            "economico_acciones"
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🇦🇷 Iguazú\nUSD 780", key=f"btn_iguazu_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Iguazú",
                            "**Iguazú 🇦🇷**\n• 3 días cataratas\n• Ambos lados (ARG+BRA)\n• Lancha bajo las cataratas\n💦 **Precio:** USD 780",
                            "economico_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇦🇷 Salta\nUSD 800", key=f"btn_salta_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Salta",
                            "**Salta 🇦🇷**\n• 5 días cultura + paisajes\n• Cafayate + Humahuaca\n• Tren a las Nubes\n🏜️ **Precio:** USD 800",
                            "economico_acciones"
                        )
                        st.rerun()

            # Botones spa/relax
            elif button_type == "spa_destinos":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🇦🇷 Termas Cacheuta\nUSD 950", key=f"btn_cacheuta_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Termas Cacheuta",
                            "**Termas de Cacheuta 🇦🇷**\n• 3 noches spa resort\n• 18 piscinas termales\n• 3 masajes incluidos\n• Yoga + temazcal\n🏔️ **Precio:** USD 950",
                            "spa_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇺🇾 Punta del Este Spa\nUSD 1.200", key=f"btn_punta_spa_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Punta del Este Spa",
                            "**Spa Punta del Este 🇺🇾**\n• 4 noches wellness\n• Spa 5★ frente al mar\n• 4 tratamientos incluidos\n• Alimentación detox\n🌊 **Precio:** USD 1.200",
                            "spa_acciones"
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🇦🇷 Entre Ríos\nUSD 780", key=f"btn_entrerios_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Entre Ríos Termal",
                            "**Entre Ríos Termal 🇦🇷**\n• 5 noches termal\n• Aguas termales todo el día\n• 2 masajes + fangoterapia\n💚 **Precio:** USD 780",
                            "spa_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇲🇽 Tulum Wellness\nUSD 1.800", key=f"btn_tulum_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Tulum Wellness",
                            "**Tulum Wellness 🇲🇽**\n• 6 noches yoga + playa\n• 2 clases yoga diarias\n• Temazcal maya\n• Alimentación consciente\n🌴 **Precio:** USD 1.800",
                            "spa_acciones"
                        )
                        st.rerun()

            # Botones rango medio
            elif button_type == "rango_medio_destinos":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🇲🇽 Cancún\nUSD 1.200", key=f"btn_cancun_medio_{i}", use_container_width=True):
                        response = get_bot_response("cancun")
                        add_message_and_hide_buttons("Cancún Premium", response["content"], response["buttons"])
                        st.rerun()

                with col2:
                    if st.button("🇧🇷 Río de Janeiro\nUSD 1.450", key=f"btn_rio_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Río de Janeiro",
                            "**Río de Janeiro 🇧🇷**\n• 6 días completos\n• Hotel Copacabana\n• Cristo + Pan de Azúcar\n• Samba show + favela tour\n🎭 **Precio:** USD 1.450",
                            "rio_acciones"
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🇺🇸 Miami + Crucero\nUSD 1.500", key=f"btn_miami_crucero_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Miami + Crucero",
                            "**Miami + Crucero Bahamas 🇺🇸🇧🇸**\n• 2 días Miami + 3 días crucero\n• Crucero all inclusive\n• Nassau + Coco Cay\n🚢 **Precio:** USD 1.500",
                            "crucero_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇵🇪 Machu Picchu\nUSD 1.480", key=f"btn_machu_medio_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Machu Picchu Comfort",
                            "**Machu Picchu Comfort 🇵🇪**\n• 7 días Cusco + MP\n• Hoteles 4★\n• Tren panorámico\n• Valle Sagrado + Montaña Arcoíris\n🏔️ **Precio:** USD 1.480",
                            "machu_acciones"
                        )
                        st.rerun()

            # Botones jóvenes
            elif button_type == "jovenes_destinos":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🇺🇸 Miami Beach\nUSD 1.350", key=f"btn_miami_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Miami Beach",
                            "**Miami Beach 🇺🇸**\n• 5 días fiesta + playa\n• South Beach\n• Pool parties + discotecas\n• Wynwood Walls\n🌴 **Precio:** USD 1.350",
                            "jovenes_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇨🇴 Cartagena + San Andrés\nUSD 1.200", key=f"btn_cartagena_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Cartagena + San Andrés",
                            "**Cartagena + San Andrés 🇨🇴**\n• 7 días\n• Ciudad amurallada + mar 7 colores\n• Hostels con bar en playa\n• Rumba caribeña\n🏝️ **Precio:** USD 1.200",
                            "jovenes_acciones"
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🇪🇸 Barcelona\nUSD 1.600", key=f"btn_barcelona_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Barcelona",
                            "**Barcelona 🇪🇸**\n• 6 días\n• Sagrada Familia + Park Güell\n• Pub crawls\n• Playa Barceloneta\n🎨 **Precio:** USD 1.600",
                            "jovenes_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🇦🇷🇧🇷 Iguazú + Río\nUSD 1.400", key=f"btn_iguazu_rio_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Iguazú + Río",
                            "**Iguazú + Río 🇦🇷🇧🇷**\n• 8 días\n• Cataratas + Cristo\n• Hostels party\n• Vida nocturna Lapa\n💃 **Precio:** USD 1.400",
                            "jovenes_acciones"
                        )
                        st.rerun()

            # Botones playa $1500
            elif button_type == "playa_1500":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("🇲🇽 Cancún\nUSD 1.200", key=f"btn_cancun_1500_{i}", use_container_width=True):
                        response = get_bot_response("cancun")
                        add_message_and_hide_buttons("Cancún Premium", response["content"], response["buttons"])
                        st.rerun()

                with col2:
                    if st.button("🇩🇴 Punta Cana\nUSD 1.350", key=f"btn_punta_1500_{i}", use_container_width=True):
                        response = get_bot_response("punta cana")
                        add_message_and_hide_buttons("Punta Cana Premium", response["content"], response["buttons"])
                        st.rerun()

                with col3:
                    if st.button("🇧🇷 Río + Playa\nUSD 1.450", key=f"btn_rio_1500_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Río de Janeiro",
                            "**Río de Janeiro 🇧🇷**\n• 6 días completos\n• Copacabana + Ipanema\n• Cristo + Pan de Azúcar\n• Samba show\n🎭 **Precio:** USD 1.450",
                            "rio_acciones"
                        )
                        st.rerun()

            # Botones de experiencias
            elif button_type == "experiencias":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🌊 Nado con delfines\n+USD 120", key=f"btn_delfines_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "🌊 Agregar nado con delfines",
                            "¡Agregado! 🐬 Experiencia increíble incluida.\n\n**Total:** USD 2.640\n\n¿Querés agregar algo más?",
                            "experiencias_mas"
                        )
                        st.rerun()

                with col2:
                    if st.button("🏛️ Tour Tulum privado\n+USD 150", key=f"btn_tulum_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "🏛️ Agregar tour a Tulum",
                            "¡Agregado! 🏛️ Tour privado confirmado.\n\n**Total:** USD 2.700\n\n¿Querés agregar algo más?",
                            "experiencias_mas"
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🍽️ Cena romántica\n+USD 80", key=f"btn_cena_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "🍽️ Agregar cena romántica",
                            "¡Agregado! 🍽️ Cena en la playa incluida.\n\n**Total:** USD 2.480\n\n¿Querés agregar algo más?",
                            "experiencias_mas"
                        )
                        st.rerun()

                with col2:
                    if st.button("❌ No, seguir sin extras", key=f"btn_sin_extras_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "No agregar extras",
                            "Perfecto! Mantenemos el paquete básico.\n\n**Total:** USD 2.400\n\n¿Cómo querés pagar?",
                            "pago_opciones"
                        )
                        st.rerun()

            # Botones de pago
            elif button_type == "pago_opciones":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("💵 Efectivo\n5% OFF", key=f"btn_efectivo_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "💵 Pagar en efectivo",
                            "¡Excelente! Con el descuento del 5%:\n\n**Total final:** USD 2.280\n\n¿Confirmamos la reserva?",
                            "contacto"
                        )
                        st.rerun()

                with col2:
                    if st.button("💳 6 cuotas\nSin interés", key=f"btn_6cuotas_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "💳 Pagar en 6 cuotas",
                            "Perfecto! Plan de pago:\n\n**6 cuotas de USD 400** sin interés\n\n¿Confirmamos la reserva?",
                            "contacto"
                        )
                        st.rerun()

                with col3:
                    if st.button("💳 12 cuotas\nCon interés", key=f"btn_12cuotas_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "💳 Pagar en 12 cuotas",
                            "Entendido! Plan de pago:\n\n**12 cuotas de USD 220** c/interés\n\n¿Confirmamos la reserva?",
                            "contacto"
                        )
                        st.rerun()

            # Botones de contacto
            elif button_type == "contacto":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("💬 WhatsApp", key=f"btn_whatsapp_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "💬 Seguir por WhatsApp",
                            "Perfecto! 📱\n\n**Continuá en:** +54 9 11 1234-5678\n\nTe enviamos el formulario y link de pago.\n\n¡Gracias por confiar en nosotros! ✈️",
                            None
                        )
                        st.rerun()

                with col2:
                    if st.button("📞 Llamada", key=f"btn_llamar_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "📞 Prefiero llamada",
                            "¡Dale! 📞\n\nTe llamamos en 5 minutos.\n\n**Contactanos:** +54 9 11 1234-5678\n\n¡Gracias por elegir viajar con nosotros! ✈️",
                            None
                        )
                        st.rerun()

                with col3:
                    if st.button("📧 Email", key=f"btn_email_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "📧 Enviar por email",
                            "Listo! 📧\n\n**Enviamos info a tu email.**\n\nviajes@mercadobot.com\n\n¡Nos vemos en el destino! 🏖️",
                            None
                        )
                        st.rerun()

            # Botones de acciones genéricos para todos los destinos
            elif button_type in ["familia_acciones", "luna_miel_acciones", "solo_acciones", "economico_acciones", "spa_acciones", "rio_acciones", "crucero_acciones", "machu_acciones", "jovenes_acciones"]:
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💳 Ver formas de pago", key=f"btn_pago_gen_{i}", use_container_width=True):
                        response = get_bot_response("formas de pago")
                        add_message_and_hide_buttons("💳 ¿Cómo puedo pagar?", response["content"], response["buttons"])
                        st.rerun()

                with col2:
                    if st.button("✅ ¡Lo quiero!", key=f"btn_reservar_gen_{i}", use_container_width=True):
                        response = get_bot_response("quiero reservar")
                        add_message_and_hide_buttons("✅ Quiero reservar", response["content"], response["buttons"])
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
                        add_message_and_hide_buttons(
                            "¿Qué necesito?",
                            "Para viajar a México necesitás:\n\n✅ Pasaporte válido (mín. 6 meses)\n✅ Formulario migratorio\n✅ Seguro de viaje (incluido)\n\n❌ NO necesitas visa\n\n¿Tenés tu pasaporte al día?",
                            "requisitos_opciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🛡️ Seguros", key=f"btn_seguros_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Info sobre seguros",
                            "**Seguro Básico (incluido):**\n✅ Gastos médicos USD 50.000\n✅ Equipaje perdido USD 1.000\n\n**Seguro Premium (+USD 80):**\n✅ Gastos médicos USD 150.000\n✅ COVID cubierto 100%\n✅ Deportes extremos\n\n¿Querés el Premium?",
                            "seguro_opciones"
                        )
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

# =========================
# INPUT DEL CHAT
# =========================
if prompt := st.chat_input("Escribí tu pregunta o hacé click en las opciones..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_bot_response(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response["content"],
        "show_buttons": response.get("buttons")
    })

    st.rerun()

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
