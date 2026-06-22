import os
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="SIVO COCINA",
    page_icon="🍽️",
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

    /* Header personalizado - tema restaurante */
    .custom-header {
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #c0392b, #e74c3c, #d35400);
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
        background: #e74c3c;
        border-color: #e74c3c;
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(231, 76, 60, 0.2);
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
    <h1>🍝 SIVO COCINA - Asistente Virtual</h1>
    <p>Tu mesa, tu pedido, tu experiencia. Atendemos 24/7.</p>
</div>
""", unsafe_allow_html=True)

BONUS_TEXTO = (
    "Este asistente toma pedidos, reservas y responde consultas en tiempo real.\n"
    "Funciona como un mesero virtual que nunca descansa."
)

def maybe_append_bonus_once():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"💡 **{BONUS_TEXTO}**",
            "show_buttons": None
        })
        st.session_state.bonus_shown = True

# Inicializar el chat y carrito
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """¡Bienvenido a La Trattoria! 👋

Soy tu asistente virtual y estoy para ayudarte.

**¿Qué necesitás hoy?**""",
            "show_buttons": "inicial"
        }
    ]

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

if "bonus_shown" not in st.session_state:
    st.session_state.bonus_shown = False

if "carrito" not in st.session_state:
    st.session_state.carrito = []

if "total_carrito" not in st.session_state:
    st.session_state.total_carrito = 0

# Función para agregar al carrito
def agregar_al_carrito(item, precio):
    st.session_state.carrito.append({"item": item, "precio": precio})
    st.session_state.total_carrito += precio

# Función para obtener carrito como texto
def get_carrito_text():
    if not st.session_state.carrito:
        return "🛒 **Tu carrito está vacío**"
    
    texto = "🛒 **Tu pedido actual:**\n\n"
    for idx, item in enumerate(st.session_state.carrito, 1):
        texto += f"{idx}. {item['item']} - ${item['precio']:,}\n"
    texto += f"\n**Total: ${st.session_state.total_carrito:,}**"
    return texto

# Función para agregar mensaje y ocultar botones
def add_message_and_hide_buttons(
    user_msg,
    bot_response,
    next_buttons=None,
    image_path=None,
    show_bonus_once=False
):
    st.session_state.messages.append({"role": "user", "content": user_msg})

    bot_msg = {
        "role": "assistant",
        "content": bot_response,
        "show_buttons": next_buttons
    }

    if image_path:
        bot_msg["image"] = image_path

    st.session_state.messages.append(bot_msg)

    if show_bonus_once:
        maybe_append_bonus_once()

    st.session_state.button_clicked = True

# =========================
# Función para obtener respuesta del bot
# =========================
def get_bot_response(prompt):
    p = (prompt or "").lower()

    # 1) Ver menú completo
    if any(word in p for word in ["menu", "menú", "carta", "que tienen", "qué tienen", "comida", "platos"]):
        return {
            "content": """📋 **Nuestro Menú**

**🍝 PASTAS CASERAS**
• Ravioles de ricota y espinaca - $2.800
• Ñoquis con salsa 4 quesos - $2.600
• Fetuccini Alfredo - $2.900
• Lasagna boloñesa - $3.200

**🍕 PIZZAS AL HORNO DE LEÑA**
• Margherita (muzza, tomate, albahaca) - $2.400
• Napolitana (muzza, tomate, ajo, anchoas) - $2.600
• Cuatro quesos - $2.800
• Prosciutto e funghi - $3.000

**🥗 ENSALADAS**
• Caesar con pollo - $2.200
• Caprese (tomate, mozza, albahaca) - $1.900
• Mixta de la casa - $1.600

**🍷 BEBIDAS**
• Vino de la casa (copa) - $800
• Gaseosas - $600
• Agua mineral - $500

¿Querés hacer un pedido o reservar una mesa?""",
            "buttons": "menu_visto",
            "bonus_once": True
        }

    # 2) Hacer pedido / delivery
    if any(word in p for word in ["pedir", "pedido", "delivery", "domicilio", "llevar", "quiero", "ordeno"]):
        return {
            "content": """🛵 **Hacé tu pedido**

**Opciones de entrega:**
• 🏠 **Delivery** (35-45 min) - Envío gratis en pedidos +$3.000
• 🚶 **Take Away** (15-20 min) - Retirás en el local

**🔥 Lo más pedido hoy:**
• Pizza Napolitana + Coca Cola - $3.000
• Ravioles + Ensalada Caesar - $4.200
• Lasagna + Vino - $3.800

¿Querés armar tu pedido o elegir una de estas opciones?""",
            "buttons": "pedido_opciones"
        }

    # 3) Reservar mesa
    if any(word in p for word in ["reservar", "reserva", "mesa", "lugar", "turno", "horario"]):
        return {
            "content": """📅 **Reservá tu mesa**

**Horarios disponibles HOY (Miércoles 28/01):**

⏰ **Almuerzo (12:00 - 15:30)**
• 12:30 hs - ✅ Disponible
• 13:00 hs - ✅ Disponible
• 13:30 hs - ⚠️ Pocas mesas
• 14:00 hs - ✅ Disponible

⏰ **Cena (20:00 - 23:30)**
• 20:00 hs - ✅ Disponible
• 20:30 hs - ✅ Disponible
• 21:00 hs - ⚠️ Pocas mesas
• 21:30 hs - ❌ Completo
• 22:00 hs - ✅ Disponible

¿Para cuántas personas y qué horario preferís?""",
            "buttons": "reserva_opciones"
        }

    # 4) Consultas sobre ingredientes/alérgenos
    if any(word in p for word in ["gluten", "celiaco", "celíaco", "vegano", "vegetariano", "alergia", "alérgico", "sin tacc"]):
        return {
            "content": """🌾 **Opciones para dietas especiales**

**SIN GLUTEN / CELÍACOS:**
✅ Todas nuestras pizzas disponibles con masa sin TACC
✅ Risotto de hongos
✅ Ensaladas (todas)
✅ Pollo a la parrilla con guarnición

**VEGETARIANO:**
✅ Ravioles de ricota y espinaca
✅ Ñoquis con salsa de tomate
✅ Pizza Margherita
✅ Todas las ensaladas

**VEGANO:**
✅ Pizza con vegetales (sin queso)
✅ Ensalada mixta
✅ Pasta con salsa pomodoro

**⚠️ ALÉRGENOS:** Trabajamos con frutos secos, lácteos y mariscos. Consultanos por cada plato.

¿Tenés alguna restricción específica?""",
            "buttons": "especial_opciones"
        }

    # 5) Preguntar por precio específico
    if any(word in p for word in ["cuanto", "cuánto", "precio", "vale", "cuesta", "sale"]) and any(word in p for word in ["pizza", "pasta", "lasagna", "ravioles"]):
        if "pizza" in p:
            return {
                "content": """🍕 **Precios de Pizzas**

• Margherita - $2.400
• Napolitana - $2.600
• Cuatro quesos - $2.800
• Prosciutto e funghi - $3.000
• Especial de la casa - $3.200

**Todas son 8 porciones · Horno de leña**

¿Querés agregar alguna al pedido?""",
                "buttons": "pizza_opciones"
            }
        elif "pasta" in p or "ravioles" in p:
            return {
                "content": """🍝 **Precios de Pastas**

• Ravioles de ricota y espinaca - $2.800
• Ñoquis con salsa 4 quesos - $2.600
• Fetuccini Alfredo - $2.900
• Lasagna boloñesa - $3.200

**Todas incluyen pan de la casa**

¿Querés agregar alguna al pedido?""",
                "buttons": "pasta_opciones"
            }

    # 6) Consulta de horarios
    if any(word in p for word in ["horario", "horarios", "abierto", "abren", "cierran", "atienden"]):
        return {
            "content": """🕐 **Nuestros horarios**

**Lunes a Jueves:**
• 12:00 - 15:30 (almuerzo)
• 20:00 - 23:30 (cena)

**Viernes y Sábado:**
• 12:00 - 16:00 (almuerzo)
• 20:00 - 01:00 (cena)

**Domingo:**
• 12:00 - 16:00 (almuerzo)
• 20:00 - 23:00 (cena)

📍 **Ubicación:** Av. Italia 2345, Montevideo
📞 **Tel:** 2345-6789

¿Querés hacer una reserva?""",
            "buttons": "horarios_accion"
        }

    # 7) Promociones / Descuentos
    if any(word in p for word in ["promo", "promocion", "promoción", "descuento", "oferta", "especial"]):
        return {
            "content": """🎉 **Promociones vigentes**

**🍕 Martes y Miércoles de Pizza**
• 2x1 en pizzas seleccionadas
• Solo para consumo en el local
• No acumulable con otras promos

**💰 Menu ejecutivo (Lun-Vie 12-15hs)**
• Entrada + Plato principal + Postre + Bebida
• $2.500 por persona
• Opciones rotan diariamente

**🍷 Happy Hour (18-20hs)**
• 2x1 en copas de vino
• 30% OFF en tablas de picada

**📱 Seguinos en Instagram @latrattoriamvd** para más promos!

¿Querés aprovechar alguna?""",
            "buttons": "promo_opciones"
        }

    # 8) Formas de pago
    if any(word in p for word in ["pago", "pagar", "tarjeta", "efectivo", "transferencia"]):
        return {
            "content": """💳 **Formas de pago**

**En el local:**
✅ Efectivo (pesos uruguayos)
✅ Tarjetas de débito
✅ Tarjetas de crédito (todas)
✅ Transferencia bancaria
✅ MercadoPago / PedidosYa

**Para delivery:**
✅ Efectivo al recibir
✅ Tarjeta de crédito/débito (por teléfono)
✅ Transferencia previa
✅ MercadoPago

**💡 Aceptamos todas las tarjetas en hasta 6 cuotas sin interés**

¿Querés hacer tu pedido?""",
            "buttons": "pago_accion"
        }

    # Respuesta por defecto
    return {
        "content": """No estoy seguro de entender bien tu consulta 🤔

**¿Querés que te ayude con alguna de estas opciones?**

• 📋 Ver el menú completo
• 🛵 Hacer un pedido (delivery/take away)
• 📅 Reservar una mesa
• 🌾 Consultar opciones sin gluten/veganas
• 💰 Ver promociones vigentes
• 💳 Formas de pago

O escribime directamente lo que necesitás!""",
        "buttons": "ayuda"
    }

# =========================
# Mostrar mensajes del chat
# =========================
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        # Mostrar imagen si existe
        if "image" in message and message["image"]:
            st.image(message["image"], use_container_width=True)

        # Mostrar botones según el tipo
        if message.get("show_buttons"):
            button_type = message["show_buttons"]

            # Botones iniciales
            if button_type == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📋 Ver menú", key=f"btn_menu_{i}", use_container_width=True):
                        response = get_bot_response("menu")
                        add_message_and_hide_buttons(
                            "Ver menú completo",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("🛵 Hacer pedido", key=f"btn_pedido_{i}", use_container_width=True):
                        response = get_bot_response("pedido")
                        add_message_and_hide_buttons(
                            "Quiero hacer un pedido",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Reservar mesa", key=f"btn_reserva_{i}", use_container_width=True):
                        response = get_bot_response("reservar")
                        add_message_and_hide_buttons(
                            "Quiero reservar una mesa",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("🎉 Ver promos", key=f"btn_promo_{i}", use_container_width=True):
                        response = get_bot_response("promociones")
                        add_message_and_hide_buttons(
                            "¿Qué promociones tienen?",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

            # Después de ver el menú
            elif button_type == "menu_visto":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🛵 Hacer pedido", key=f"btn_pedido_menu_{i}", use_container_width=True):
                        response = get_bot_response("pedido")
                        add_message_and_hide_buttons(
                            "Quiero hacer un pedido",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("📅 Reservar mesa", key=f"btn_reserva_menu_{i}", use_container_width=True):
                        response = get_bot_response("reservar")
                        add_message_and_hide_buttons(
                            "Quiero reservar una mesa",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

            # Opciones de pedido
            elif button_type == "pedido_opciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🍕 Pizzas", key=f"btn_pizzas_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Quiero ver pizzas",
                            """🍕 **Nuestras Pizzas** (8 porciones - Horno de leña)

• Margherita (muzza, tomate, albahaca) - $2.400
• Napolitana (muzza, tomate, ajo, anchoas) - $2.600
• Cuatro quesos - $2.800
• Prosciutto e funghi - $3.000
• Especial de la casa - $3.200

¿Cuál querés agregar al pedido?""",
                            "pizza_opciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("🍝 Pastas", key=f"btn_pastas_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Quiero ver pastas",
                            """🍝 **Nuestras Pastas** (Caseras · Con pan de la casa)

• Ravioles de ricota y espinaca - $2.800
• Ñoquis con salsa 4 quesos - $2.600
• Fetuccini Alfredo - $2.900
• Lasagna boloñesa - $3.200

¿Cuál querés agregar al pedido?""",
                            "pasta_opciones"
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🥗 Ensaladas", key=f"btn_ensaladas_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Quiero ver ensaladas",
                            """🥗 **Nuestras Ensaladas**

• Caesar con pollo - $2.200
• Caprese (tomate, mozza, albahaca) - $1.900
• Mixta de la casa - $1.600

¿Cuál querés agregar?""",
                            "ensalada_opciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("📋 Ver menú completo", key=f"btn_menu_completo_{i}", use_container_width=True):
                        response = get_bot_response("menu")
                        add_message_and_hide_buttons(
                            "Ver menú completo",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

            # Opciones de pizzas (para agregar al carrito)
            elif button_type == "pizza_opciones":
                if st.button("🍕 Margherita ($2.400)", key=f"btn_margherita_{i}", use_container_width=True):
                    agregar_al_carrito("Pizza Margherita", 2400)
                    add_message_and_hide_buttons(
                        "Agregar Pizza Margherita",
                        f"""✅ ¡Agregado al pedido!

{get_carrito_text()}

¿Querés agregar algo más o finalizar el pedido?""",
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("🍕 Napolitana ($2.600)", key=f"btn_napolitana_{i}", use_container_width=True):
                    agregar_al_carrito("Pizza Napolitana", 2600)
                    add_message_and_hide_buttons(
                        "Agregar Pizza Napolitana",
                        f"""✅ ¡Agregado al pedido!

{get_carrito_text()}

¿Querés agregar algo más o finalizar el pedido?""",
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("🍕 Cuatro Quesos ($2.800)", key=f"btn_4quesos_{i}", use_container_width=True):
                    agregar_al_carrito("Pizza Cuatro Quesos", 2800)
                    add_message_and_hide_buttons(
                        "Agregar Pizza Cuatro Quesos",
                        f"""✅ ¡Agregado al pedido!

{get_carrito_text()}

¿Querés agregar algo más o finalizar el pedido?""",
                        "carrito_acciones"
                    )
                    st.rerun()

            # Opciones de pastas
            elif button_type == "pasta_opciones":
                if st.button("🍝 Ravioles ($2.800)", key=f"btn_ravioles_{i}", use_container_width=True):
                    agregar_al_carrito("Ravioles de ricota y espinaca", 2800)
                    add_message_and_hide_buttons(
                        "Agregar Ravioles",
                        f"""✅ ¡Agregado al pedido!

{get_carrito_text()}

¿Querés agregar algo más o finalizar el pedido?""",
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("🍝 Ñoquis ($2.600)", key=f"btn_noquis_{i}", use_container_width=True):
                    agregar_al_carrito("Ñoquis con salsa 4 quesos", 2600)
                    add_message_and_hide_buttons(
                        "Agregar Ñoquis",
                        f"""✅ ¡Agregado al pedido!

{get_carrito_text()}

¿Querés agregar algo más o finalizar el pedido?""",
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("🍝 Lasagna ($3.200)", key=f"btn_lasagna_{i}", use_container_width=True):
                    agregar_al_carrito("Lasagna boloñesa", 3200)
                    add_message_and_hide_buttons(
                        "Agregar Lasagna",
                        f"""✅ ¡Agregado al pedido!

{get_carrito_text()}

¿Querés agregar algo más o finalizar el pedido?""",
                        "carrito_acciones"
                    )
                    st.rerun()

            # Acciones del carrito
            elif button_type == "carrito_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("➕ Agregar más", key=f"btn_mas_{i}", use_container_width=True):
                        response = get_bot_response("pedido")
                        add_message_and_hide_buttons(
                            "Agregar más items",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("✅ Finalizar pedido", key=f"btn_finalizar_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Finalizar pedido",
                            f"""{get_carrito_text()}

**¿Cómo lo recibís?**

🏠 **Delivery** (35-45 min) - Envío gratis en pedidos +$3.000
🚶 **Take Away** (15-20 min) - Retirás en el local

Elegí una opción:""",
                            "entrega_opciones"
                        )
                        st.rerun()

            # Opciones de entrega
            elif button_type == "entrega_opciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏠 Delivery", key=f"btn_delivery_{i}", use_container_width=True):
                        envio = "GRATIS" if st.session_state.total_carrito >= 3000 else "$200"
                        add_message_and_hide_buttons(
                            "Quiero delivery",
                            f"""📍 **Delivery seleccionado**

{get_carrito_text()}
• Envío: {envio}

**Total final: ${st.session_state.total_carrito + (0 if st.session_state.total_carrito >= 3000 else 200):,}**

Por favor, confirmame:
1. Tu dirección de entrega
2. Teléfono de contacto
3. Forma de pago

O escribí todo junto, ej: "Av. Italia 1234, Tel: 099123456, pago con tarjeta" """,
                            "confirmar_delivery"
                        )
                        st.rerun()

                with col2:
                    if st.button("🚶 Take Away", key=f"btn_takeaway_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Retiro en el local",
                            f"""🚶 **Retiro en el local**

{get_carrito_text()}

**Tiempo estimado: 15-20 minutos**

📍 Retirás en: Av. Italia 2345, Montevideo

Por favor confirmame:
1. Nombre para el pedido
2. Teléfono de contacto
3. Forma de pago

O escribí todo junto, ej: "Juan Pérez, 099123456, pago en efectivo" """,
                            "confirmar_takeaway"
                        )
                        st.rerun()

            # Opciones de reserva
            elif button_type == "reserva_opciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("⏰ Hoy almuerzo", key=f"btn_almuerzo_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Para hoy al mediodía",
                            """📅 **Horarios disponibles HOY - Almuerzo**

• 12:30 hs - ✅ Disponible
• 13:00 hs - ✅ Disponible
• 13:30 hs - ⚠️ Pocas mesas
• 14:00 hs - ✅ Disponible

¿Para cuántas personas y qué horario preferís?

Ej: "4 personas a las 13:00" """,
                            None
                        )
                        st.rerun()

                with col2:
                    if st.button("🌙 Hoy cena", key=f"btn_cena_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Para hoy a la noche",
                            """📅 **Horarios disponibles HOY - Cena**

• 20:00 hs - ✅ Disponible
• 20:30 hs - ✅ Disponible
• 21:00 hs - ⚠️ Pocas mesas
• 21:30 hs - ❌ Completo
• 22:00 hs - ✅ Disponible

¿Para cuántas personas y qué horario preferís?

Ej: "2 personas a las 20:30" """,
                            None
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📆 Otro día", key=f"btn_otro_dia_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Para otra fecha",
                            """📅 **Reservá para otra fecha**

Decime:
• ¿Qué día?
• ¿Qué horario? (almuerzo 12-15hs / cena 20-23hs)
• ¿Cuántas personas?

Ej: "Viernes 2 de febrero, 21:00hs, 6 personas" """,
                            None
                        )
                        st.rerun()

                with col2:
                    if st.button("🎉 Evento especial", key=f"btn_evento_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Evento o celebración",
                            """🎉 **Eventos y Celebraciones**

¡Perfecto para cumpleaños, aniversarios, despedidas!

**Beneficios:**
✅ Mesa reservada con decoración
✅ Menú especial a convenir
✅ Postre de cortesía
✅ Atención personalizada

Contame:
• ¿Qué festejás?
• ¿Cuántas personas?
• ¿Qué día y horario?

Y armamos algo especial para vos!""",
                            None
                        )
                        st.rerun()

            # Opciones especiales (sin gluten, vegano, etc)
            elif button_type == "especial_opciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📋 Ver opciones", key=f"btn_ver_especial_{i}", use_container_width=True):
                        response = get_bot_response("menu")
                        add_message_and_hide_buttons(
                            "Ver menú completo",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("💬 Consultar chef", key=f"btn_chef_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Hablar con el chef",
                            """👨‍🍳 **Consulta con el Chef**

Para consultas específicas sobre ingredientes, preparación o adaptaciones especiales, podés:

📞 **Llamar:** 2345-6789
📧 **Email:** chef@latrattoria.com.uy
💬 **WhatsApp:** 099 123 456

Contanos tu caso y adaptamos el plato a tu necesidad!

¿Querés que te pase el contacto o preferís hacer tu pedido con las opciones disponibles?""",
                            "menu_visto"
                        )
                        st.rerun()

            # Opciones de promociones
            elif button_type == "promo_opciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🍕 2x1 Pizzas", key=f"btn_2x1_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Quiero el 2x1 de pizzas",
                            """🍕 **2x1 en Pizzas - Martes y Miércoles**

**Pizzas incluidas:**
• Margherita
• Napolitana
• Cuatro quesos

**Solo para consumo en el local**
Válido solo martes y miércoles

¿Querés reservar una mesa para aprovecharla?""",
                            "reserva_opciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("💰 Menú ejecutivo", key=f"btn_ejecutivo_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Info del menú ejecutivo",
                            """💰 **Menú Ejecutivo - $2.500**

**Lunes a Viernes 12:00 - 15:00hs**

Incluye:
• Entrada del día
• Plato principal (rotan 3 opciones)
• Postre
• Bebida

¿Querés reservar para hoy o ver qué hay?""",
                            "reserva_opciones"
                        )
                        st.rerun()

            # Botones de ayuda general
            elif button_type == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📋 Ver menú", key=f"btn_menu_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("menu")
                        add_message_and_hide_buttons(
                            "Ver menú",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("🛵 Hacer pedido", key=f"btn_pedido_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("pedido")
                        add_message_and_hide_buttons(
                            "Hacer pedido",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

            # Después de acciones de horarios/pagos
            elif button_type == "horarios_accion" or button_type == "pago_accion":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Reservar", key=f"btn_reservar_final_{i}", use_container_width=True):
                        response = get_bot_response("reservar")
                        add_message_and_hide_buttons(
                            "Quiero reservar",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("🛵 Pedir", key=f"btn_pedir_final_{i}", use_container_width=True):
                        response = get_bot_response("pedido")
                        add_message_and_hide_buttons(
                            "Quiero pedir",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

# Mostrar sugerencias de preguntas al final (SIEMPRE visible)
st.markdown("---")
st.markdown("**💬 Ejemplos de consultas que podés hacer:**")
col1, col2 = st.columns(2)
with col1:
    st.caption("• Quiero hacer un pedido de pizza para delivery")
    st.caption("• ¿Cuánto sale la lasagna?")
    st.caption("• Reservar mesa para 4 personas hoy a las 21hs")
    st.caption("• ¿Tienen opciones sin gluten?")
    st.caption("• ¿Qué promociones tienen?")
with col2:
    st.caption("• ¿Hasta qué hora atienden?")
    st.caption("• Quiero pedir ravioles para llevar")
    st.caption("• ¿Puedo pagar con tarjeta en cuotas?")
    st.caption("• Necesito una mesa para 10 personas el viernes")
    st.caption("• ¿Tienen menú vegetariano?")

# INPUT DEL CHAT
if prompt := st.chat_input("Escribí tu consulta o hacé click en las opciones..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_bot_response(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response["content"],
        "show_buttons": response.get("buttons"),
        "image": response.get("image")
    })

    if response.get("bonus_once"):
        maybe_append_bonus_once()

    st.rerun()

# Footer
st.divider()
st.caption("💡 **Este es un demo interactivo.** El bot responde con información de ejemplo.")
st.caption("🔌 En producción conecta con tu sistema de reservas, menús y pagos reales.")

# Botón para resetear conversación y carrito
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """¡Bienvenido a La Trattoria! 👋

Soy tu asistente virtual y estoy para ayudarte.

**¿Qué necesitás hoy?**""",
                "show_buttons": "inicial"
            }
        ]
        st.session_state.button_clicked = False
        st.session_state.bonus_shown = False
        st.session_state.carrito = []
        st.session_state.total_carrito = 0
        st.rerun()
