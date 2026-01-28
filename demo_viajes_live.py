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

Encontré opciones ideales para viajar con niños:

**OPCIÓN 1 — Disney Orlando 🇺🇸**
• 7 días parques + hotel: USD 3.200/adulto, USD 2.400/niño
• Entradas 4 parques (Magic Kingdom, Epcot, Hollywood, Animal Kingdom)
• Shuttle gratis a los parques
• Character dining (desayuno con personajes)
• Fast Pass incluido
🎢 **Edad ideal:** 4-12 años

**OPCIÓN 2 — Cancún Familiar 🇲🇽**
• Resort all inclusive con Kids Club: USD 1.400/adulto, USD 700/niño
• Niños menores de 6 años GRATIS
• Parque acuático incluido
• Actividades para niños TODO el día
• Menú infantil especial
🏖️ **Edad ideal:** 2-14 años

**OPCIÓN 3 — Bariloche con Niños 🇦🇷**
• 5 días naturaleza + chocolate: USD 850/adulto, USD 450/niño
• Museo del Chocolate interactivo
• Cerro Campanario (telesilla)
• Paseo en catamarán Victoria
• Mini trekking familiar
🍫 **Edad ideal:** 5-12 años

¿Qué edades tienen tus hijos? Así te personalizo mejor la recomendación.""",
            "buttons": "familia_opciones"
        }
    
    elif any(word in p for word in ["luna de miel", "romántico", "pareja", "casamiento", "boda"]):
        return {
            "content": """¡¡¡FELICITACIONES!!! 💍✨

Opciones ROMÁNTICAS para luna de miel:

**OPCIÓN 1 — Maldivas 🇲🇻**
• 7 noches en villa sobre el agua: USD 4.500/pareja
• Bungalow privado con acceso directo al mar
• Desayuno flotante en la piscina privada
• Cena bajo las estrellas en la playa
• Masaje de pareja al atardecer
• Snorkel en arrecifes de coral
🌴 **El destino más romántico del mundo**

**OPCIÓN 2 — Santorini, Grecia 🇬🇷**
• 6 noches en cave hotel: USD 3.200/pareja
• Cueva tradicional con jacuzzi y vista al volcán
• Tour privado en catamarán al atardecer
• Cena en Oia con la mejor puesta de sol
• Sesión de fotos profesional incluida
• Wine tasting en bodega local
🌅 **Instagram de ensueño**

**OPCIÓN 3 — Punta Cana Luxury 🇩🇴**
• 7 noches en resort adults-only: USD 2.800/pareja
• Suite con jacuzzi privado
• Butler service 24/7
• Cena romántica en la playa (privada)
• Spa couples massage incluido
• Champagne y fresas todos los días
🥂 **Lujo caribeño accesible**

**REGALO ESPECIAL:** 
🎁 Álbum digital profesional de la luna de miel
📸 1 sesión de fotos incluida en el destino

¿Para cuándo es la boda? Te armo un plan perfecto.""",
            "buttons": "luna_miel_opciones"
        }
    
    elif any(word in p for word in ["solo", "sola", "mochilero", "backpacker", "viajo solo"]):
        return {
            "content": """¡Genial! 🎒 Viajes para aventureros solitarios:

**OPCIÓN 1 — Ruta Machu Picchu 🇵🇪**
• 10 días Lima-Cusco-Machu Picchu: USD 1.650
• Grupos pequeños (máx 12 personas)
• Hostels + 1 hotel en Cusco
• Trekking Camino Inca (4 días)
• Valle Sagrado + Maras y Moray
• Guías locales expertos
• Conocés viajeros de todo el mundo
👥 **Edad promedio grupo:** 25-35 años

**OPCIÓN 2 — Colombia Adventure 🇨🇴**
• 12 días ruta completa: USD 1.400
• Cartagena (3 días) + Medellín (3) + Bogotá (2) + Salento (2) + Tayrona (2)
• Alojamiento en hostels top
• Algunas comidas incluidas
• Actividades opcionales (parapente, coffee tour, buceo)
• Transporte entre ciudades
🌴 **Destino económico y seguro**

**OPCIÓN 3 — Europa Interrail 🇪🇺**
• 15 días, 5 países: USD 2.200
• Pase de tren ilimitado
• Barcelona → París → Amsterdam → Berlín → Praga
• Hostels en zona céntrica
• Free walking tours incluidos
• Flexibilidad total de fechas
🚂 **La clásica aventura europea**

Todos los grupos tienen WhatsApp para conocerse antes del viaje.

¿Qué tipo de vibe buscás? ¿Fiesta, cultura, naturaleza?""",
            "buttons": "solo_opciones"
        }
    
    elif any(word in p for word in ["800", "económico", "barato", "poco presupuesto"]) and "usd" in p:
        return {
            "content": """¡Perfecto! Con USD 800 tenés MUY buenas opciones 💰

**OPCIÓN 1 — Florianópolis 🇧🇷**
• 5 días todo incluido: USD 800
• Hotel 3★ cerca de playa
• Desayuno incluido
• Tour por las mejores playas
• Transfer aeropuerto
🏖️ 42 playas + vida nocturna

**OPCIÓN 2 — Mendoza 🇦🇷**
• 4 días vino + montaña: USD 750
• Hotel boutique en Luján de Cuyo
• Tour 2 bodegas premium
• Alta montaña (Aconcagua)
• Rafting día completo
🍷 El mejor vino de Argentina

**OPCIÓN 3 — Iguazú 🇦🇷**
• 3 días cataratas: USD 780
• Hotel 4★ frente a la selva
• Entradas ambos lados (ARG + BRA)
• Paseo en lancha bajo las cataratas
• Traslados incluidos
💦 Una de las 7 maravillas naturales

**OPCIÓN 4 — Salta 🇦🇷**
• 5 días cultura + paisajes: USD 800
• Hotel céntrico
• Tour Cafayate + Quebrada de Humahuaca
• Tren a las Nubes
• Comidas típicas incluidas
🏜️ Paisajes impresionantes

Todas incluyen vuelos desde Buenos Aires. ¿Cuál te cierra más?""",
            "buttons": "economicos_opciones"
        }
    
    elif any(word in p for word in ["spa", "relax", "tranquilo", "descanso", "wellness"]):
        return {
            "content": """Perfecto para desconectar 🧘‍♀️💆‍♂️

**OPCIÓN 1 — Termas de Cacheuta, Mendoza 🇦🇷**
• 3 noches spa resort: USD 950/persona
• Acceso ilimitado a 18 piscinas termales
• 3 masajes incluidos (piedras calientes, aromaterapia, descontracturante)
• Yoga al amanecer con vista a la montaña
• All inclusive (comida orgánica)
• Temazcal andino (ritual ancestral)
🏔️ Relax + montaña

**OPCIÓN 2 — Spa Resort Punta del Este 🇺🇾**
• 4 noches wellness: USD 1.200/persona
• Spa 5 estrellas frente al mar
• Circuito spa diario (sauna, jacuzzi, piscinas)
• 4 tratamientos incluidos
• Clases yoga + meditación
• Alimentación detox
• Masaje shiatsu con vista al océano
🌊 Frente al mar

**OPCIÓN 3 — Entre Ríos Termal 🇦🇷**
• 5 noches en complejo termal: USD 780/persona
• Aguas termales todo el día
• 2 masajes relajantes
• Fangoterapia incluida
• Pileta climatizada
• Comida casera regional
💚 Económico y cerca

**OPCIÓN 4 — Tulum Wellness 🇲🇽**
• 6 noches yoga + playa: USD 1.800/persona
• Hotel boutique eco-friendly
• 2 clases yoga diarias
• 1 temazcal maya
• Meditación guiada
• Alimentación consciente
• Masaje maya ancestral
🌴 Experiencia holística

¿Buscás algo más activo (yoga) o 100% relax (spa)?""",
            "buttons": "relax_opciones"
        }
    
    elif any(word in p for word in ["1500", "1.500"]) and "usd" in p:
        return {
            "content": """¡Excelente presupuesto! Con USD 1.500 accedés a destinos TOP 🌟

**OPCIÓN 1 — Cancún Premium 🇲🇽**
• 7 días all inclusive: USD 1.200
• Hotel 5★ zona hotelera
• TODO incluido (comidas, bebidas, excursiones)
• Te sobran USD 300 para extras
🏖️ Clásico que nunca falla

**OPCIÓN 2 — Río de Janeiro 🇧🇷**
• 6 días completos: USD 1.450
• Hotel en Copacabana
• City tour + Cristo + Pan de Azúcar
• Favela tour con guía local
• Samba show con cena
• 2 días de playa
🎭 Ciudad más vibrante de Brasil

**OPCIÓN 3 — Miami + Crucero Bahamas 🇺🇸🇧🇸**
• 2 días Miami + 3 días crucero: USD 1.500
• Hotel en Miami Beach
• Crucero all inclusive
• Escalas en Nassau + Coco Cay
• Piscinas, casino, shows
🚢 2 destinos en 1

**OPCIÓN 4 — Machu Picchu Comfort 🇵🇪**
• 7 días Cusco + MP: USD 1.480
• Hoteles 4★
• Tren panorámico a Machu Picchu
• Valle Sagrado completo
• Guías en español
• Montaña Arcoíris
🏔️ Experiencia premium

¿Playa, ciudad, aventura o cultura?""",
            "buttons": "rango_medio_opciones"
        }
    
    elif any(word in p for word in ["25", "joven", "20", "30 años"]):
        return {
            "content": """¡Dale! Para tu edad tengo opciones copadas 🎉

**OPCIÓN 1 — Miami Beach 🇺🇸**
• 5 días fiesta + playa: USD 1.350
• Hotel en South Beach
• Pool parties
• Discotecas (Liv, Story)
• Wynwood Walls (arte urbano)
• Everglades tour
🌴 Fiesta + playa USA

**OPCIÓN 2 — Cartagena + San Andrés 🇨🇴**
• 7 días: USD 1.200
• 3 días Cartagena (ciudad amurallada, Getsemaní)
• 4 días San Andrés (mar de 7 colores)
• Hostels con bar en la playa
• Rumba caribeña
• Snorkel + Johnny Cay
🏝️ Caribe económico

**OPCIÓN 3 — Barcelona 🇪🇸**
• 6 días: USD 1.600
• Hostel top en Barrio Gótico
• Sagrada Familia + Park Güell
• Pub crawls (fiesta con otros viajeros)
• Playa Barceloneta
• Montserrat day trip
🎨 Ciudad + playa + cultura

**OPCIÓN 4 — Iguazú + Río 🇦🇷🇧🇷**
• 8 días: USD 1.400
• 3 días Iguazú (cataratas + aventura)
• 5 días Río (playa + samba + Cristo)
• Hostels party
• Vida nocturna en Lapa
• Conocés otros viajeros
💃 Naturaleza + fiesta

¿Solo o con amigos? ¿Más fiesta o más chill?""",
            "buttons": "jovenes_opciones"
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
