import os
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Demo Tienda Ropa - StyleBot",
    page_icon="👗",
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

    /* Header personalizado - tema fashion */
    .custom-header {
        text-align: center;
        padding: 25px;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
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
        background: #f5576c;
        border-color: #f5576c;
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(245, 87, 108, 0.2);
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
    <h1>👗 StyleHub - Tu Asesor de Moda IA</h1>
    <p>Encuentra tu estilo perfecto con recomendaciones personalizadas</p>
</div>
""", unsafe_allow_html=True)

BONUS_TEXTO = (
    "Este asistente recomienda outfits, verifica tallas, combina prendas y procesa pedidos.\n"
    "No es un catálogo genérico."
)

def maybe_append_bonus_once():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "💡 **{}**".format(BONUS_TEXTO),
            "show_buttons": None
        })
        st.session_state.bonus_shown = True

# Inicializar el chat y carrito
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """¡Hola! 👋 Bienvenida a StyleHub.

Soy tu asesora de moda personal y estoy para ayudarte.

**¿Qué estás buscando hoy?**""",
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
    
    texto = "🛒 **Tu carrito:**\n\n"
    for idx, item in enumerate(st.session_state.carrito, 1):
        texto += "{}. {} - ${:,}\n".format(idx, item['item'], item['precio'])
    texto += "\n**Subtotal: ${:,}**".format(st.session_state.total_carrito)
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

    # 1) Búsqueda por estilo - Casual
    if any(word in p for word in ["casual", "comodo", "cómodo", "diario", "informal"]):
        return {
            "content": """👕 **Colección Casual - Uso diario**

**LO MÁS VENDIDO**
💙 **Jeans Mom Fit**
• Tiro alto · Azul claro
• Tallas: XS a XL
• **$12.990** - ✅ Stock todas las tallas
• ⭐⭐⭐⭐⭐ (842 reseñas)

🤍 **Remera Oversize Algodón**
• 100% algodón · 5 colores
• Tallas: XS a XXL
• **$4.990** - ✅ Stock completo
• ⭐⭐⭐⭐½ (1.234 reseñas)

**OUTFITS ARMADOS**
✨ **Look Casual Completo**
Jeans + Remera + Zapatillas blancas
~~$25.980~~ **$19.990** (23% OFF)

¿Cuál te interesa o querés ver más opciones?""",
            "buttons": "casual_opciones",
            "bonus_once": True
        }

    # 2) Búsqueda por estilo - Formal/Oficina
    if any(word in p for word in ["formal", "trabajo", "oficina", "elegante", "profesional"]):
        return {
            "content": """💼 **Colección Formal - Office & Elegante**

**BESTSELLERS**
🖤 **Blazer Entallado**
• Corte moderno · Negro/Beige
• Tallas: XS a XL
• **$24.990** - ⚠️ Pocas unidades en M y L
• ⭐⭐⭐⭐⭐ (567 reseñas)

👗 **Vestido Midi Liso**
• Manga 3/4 · 4 colores
• Tallas: S a XXL
• **$18.990** - ✅ Stock disponible
• ⭐⭐⭐⭐⭐ (892 reseñas)

👔 **Pantalón Recto Pinzado**
• Cintura alta · Negro/Gris
• Tallas: XS a XL
• **$15.990** - ✅ Stock completo
• ⭐⭐⭐⭐ (445 reseñas)

**COMBO OFICINA**
Blazer + Pantalón + Blusa
~~$59.970~~ **$49.990** (ahorrás $9.980)

¿Te armo un look completo?""",
            "buttons": "formal_opciones"
        }

    # 3) Búsqueda por estilo - Fiesta/Noche
    if any(word in p for word in ["fiesta", "noche", "salir", "evento", "boda", "casamiento"]):
        return {
            "content": """✨ **Colección Fiesta & Noche**

**DESTACADOS DE LA TEMPORADA**
💃 **Vestido Satinado Largo**
• Escote V · Negro/Bordo/Verde
• Tallas: XS a L
• **$34.990** - ⚠️ Solo quedan 2 en talla S
• ⭐⭐⭐⭐⭐ (234 reseñas)

🌟 **Vestido Corto Lentejuelas**
• Espalda abierta · Dorado/Plata
• Tallas: S a XL
• **$29.990** - ✅ Stock disponible
• ⭐⭐⭐⭐½ (189 reseñas)

👠 **Jumpsuit Elegante**
• Pierna recta · Negro
• Tallas: XS a XXL
• **$27.990** - ✅ Stock completo
• ⭐⭐⭐⭐⭐ (312 reseñas)

**💡 TIP DE ESTILO:** ¿Qué tipo de evento es? (boda, cena, fiesta) Te recomiendo según el dress code.

¿Para qué ocasión lo necesitás?""",
            "buttons": "fiesta_opciones"
        }

    # 4) Consulta de tallas
    if any(word in p for word in ["talla", "talle", "medida", "tamaño", "me queda", "calza"]):
        return {
            "content": """📏 **Guía de Tallas**

**TABLA DE MEDIDAS (CM)**

| Talla | Busto | Cintura | Cadera |
|-------|-------|---------|--------|
| **XS** | 80-84 | 60-64 | 88-92 |
| **S** | 84-88 | 64-68 | 92-96 |
| **M** | 88-92 | 68-72 | 96-100 |
| **L** | 92-98 | 72-78 | 100-106 |
| **XL** | 98-104 | 78-84 | 106-112 |
| **XXL** | 104-110 | 84-90 | 112-118 |

**¿Cómo medir?**
• **Busto:** Parte más ancha del pecho
• **Cintura:** Parte más estrecha del torso
• **Cadera:** Parte más ancha de la cadera

**💡 CONSEJO:** Si estás entre dos tallas, te recomendamos la mayor para mayor comodidad.

**🔄 CAMBIOS GRATIS** - Si no te queda, lo cambiamos sin costo.

¿Necesitás ayuda con alguna prenda específica?""",
            "buttons": "tallas_acciones"
        }

    # 5) Nuevos ingresos / Novedades
    if any(word in p for word in ["nuevo", "novedades", "tendencia", "moda", "temporada", "llegadas"]):
        return {
            "content": """🆕 **Nuevos Ingresos - Temporada Verano 2026**

**RECIÉN LLEGADOS (esta semana)**

🔥 **Top Crop Tejido**
• Estilo boho · 6 colores
• **$6.990** - ✅ Todas las tallas
• 🔥 145 personas lo vieron hoy

☀️ **Short Jean Tiro Alto**
• Rotos · Denim stretch
• **$9.990** - ✅ Stock completo
• 🔥 89 personas lo compraron esta semana

👗 **Vestido Midi Flores**
• Print exclusivo · Fluido
• **$16.990** - ⚠️ Se está agotando rápido
• 🔥 Solo quedan 8 unidades

🕶️ **Conjunto 2 Piezas Lino**
• Top + Pantalón · Beige/Blanco
• **$22.990** - ✅ Stock disponible

**📸 INSPIRACIÓN:** Seguinos en @stylehub.uy para ver cómo combinarlos

¿Cuál te gusta más?""",
            "buttons": "novedades_acciones"
        }

    # 6) Ofertas y descuentos
    if any(word in p for word in ["oferta", "descuento", "promo", "promocion", "rebaja", "sale", "barato"]):
        return {
            "content": """🏷️ **OFERTAS ACTIVAS - Hasta 50% OFF**

**⚡ FLASH SALE (termina en 8 horas)**
• Remeras lisas - **$2.990** (antes $5.990)
• Calzas deportivas - **$4.990** (antes $9.990)
• Medias pack x3 - **$1.990** (antes $3.990)

**💥 OUTLET - Última temporada**
• Vestidos - Hasta 50% OFF
• Pantalones - Hasta 40% OFF
• Abrigos - Hasta 45% OFF

**🎯 COMBOS ESPECIALES**
👗 **Combo Verano**
3 Remeras + 1 Short = **$19.990**
(Ahorrás $8.000)

👔 **Combo Trabajo**
2 Blusas + 1 Pantalón = **$24.990**
(Ahorrás $6.000)

**📱 DESCUENTO EXTRA**
Código: STYLE15
15% OFF adicional en tu primera compra

¿Qué oferta te interesa?""",
            "buttons": "ofertas_acciones"
        }

    # 7) Consulta sobre envíos
    if any(word in p for word in ["envio", "envío", "entrega", "delivery", "llega", "demora"]):
        return {
            "content": """🚚 **Opciones de Envío**

**ENVÍO EXPRESS (24-48hs)**
• Montevideo: **GRATIS** en compras +$15.000
• Interior: **GRATIS** en compras +$25.000
• Seguimiento en tiempo real

**ENVÍO ESTÁNDAR (3-5 días)**
• Todo Uruguay: $350
• Compras +$10.000: **GRATIS**

**RETIRO EN TIENDA**
• **GRATIS** - Listo en 2-4 horas
• Locales: Pocitos, Punta Carretas, Centro

**📍 Tu ubicación detectada:** Montevideo
• Envío gratis en compras +$15.000
• Retiro disponible hoy mismo

**📦 EMPAQUE REGALO**
• Gratis en compras +$20.000
• Incluye tarjeta personalizada

¿Necesitás calcular el costo para tu pedido?""",
            "buttons": "envio_acciones"
        }

    # 8) Formas de pago
    if any(word in p for word in ["pago", "pagar", "cuotas", "tarjeta", "efectivo", "transferencia"]):
        return {
            "content": """💳 **Formas de Pago**

**TARJETAS DE CRÉDITO**
✅ Todas las tarjetas
✅ **3 cuotas sin interés** (compras +$10.000)
✅ **6 cuotas sin interés** (compras +$20.000)
✅ Hasta 12 cuotas con interés

**TARJETAS DE DÉBITO**
✅ Sin recargo
✅ Acreditación inmediata

**TRANSFERENCIA / EFECTIVO**
✅ **10% descuento adicional**
✅ Precio final al momento

**MERCADO PAGO**
✅ Hasta 12 cuotas
✅ Protección al comprador

**PROGRAMAS DE PUNTOS**
✅ OCA Azul
✅ Prex
✅ Santander Recompensas

¿Querés seguir comprando o ir al checkout?""",
            "buttons": "pago_acciones"
        }

    # 9) Programa de fidelidad
    if any(word in p for word in ["puntos", "descuento", "beneficio", "cliente", "vip", "fidelidad"]):
        return {
            "content": """⭐ **StyleClub - Programa de Fidelidad**

**ACUMULÁ PUNTOS**
• 1 punto por cada $10 gastados
• 1.000 puntos = $100 de descuento

**NIVELES VIP**
🥉 **Bronce** (0-5.000 pts)
• 5% OFF permanente
• Acceso a preventa

🥈 **Plata** (5.000-15.000 pts)
• 10% OFF permanente
• Envíos gratis siempre
• Regalos de cumpleaños

🥇 **Oro** (15.000+ pts)
• 15% OFF permanente
• Envíos express gratis
• Acceso VIP a lanzamientos
• Personal shopper

**🎁 BONO DE BIENVENIDA**
Registrate hoy y recibí **500 puntos gratis**

¿Querés registrarte en StyleClub?""",
            "buttons": "fidelidad_acciones"
        }

    # 10) Asesoramiento personalizado
    if any(word in p for word in ["ayuda", "ayudame", "ayúdame", "recomend", "consejo", "outfit", "combinar"]):
        return {
            "content": """💁 **Asesoramiento de Estilo Personalizado**

Para darte las mejores recomendaciones, contame:

**1. ¿Para qué ocasión?**
• Uso diario / trabajo
• Salir / fiesta
• Evento especial
• Deporte / gym

**2. ¿Qué estilo te gusta?**
• Casual y cómodo
• Elegante / formal
• Trendy / moderno
• Clásico / atemporal

**3. ¿Cuál es tu presupuesto?**
• Hasta $10.000
• $10.000 - $25.000
• $25.000 - $50.000
• Más de $50.000

O escribí directamente tu consulta, ej: "necesito outfit para una boda en verano, presupuesto $40.000"

**📸 También podés enviarnos foto** de alguna prenda que tengas y te armamos el look completo!""",
            "buttons": "ayuda_estilo"
        }

    # Respuesta por defecto
    return {
        "content": """No estoy segura de entender 🤔

**¿Querés que te ayude con alguna de estas opciones?**

• 👕 Ver ropa casual
• 💼 Ver ropa formal/trabajo
• ✨ Ver ropa de fiesta
• 🆕 Ver novedades
• 🏷️ Ver ofertas
• 📏 Guía de tallas
• 🛒 Ver mi carrito

O escribime directamente lo que buscás!""",
        "buttons": "ayuda"
    }

# =========================
# Mostrar mensajes del chat
# =========================
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if "image" in message and message["image"]:
            st.image(message["image"], use_container_width=True)

        if message.get("show_buttons"):
            button_type = message["show_buttons"]

            # Botones iniciales
            if button_type == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("👕 Casual", key="btn_casual_{}".format(i), use_container_width=True):
                        response = get_bot_response("casual")
                        add_message_and_hide_buttons(
                            "Quiero ver ropa casual",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("💼 Formal", key="btn_formal_{}".format(i), use_container_width=True):
                        response = get_bot_response("formal")
                        add_message_and_hide_buttons(
                            "Quiero ver ropa formal",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✨ Fiesta", key="btn_fiesta_{}".format(i), use_container_width=True):
                        response = get_bot_response("fiesta")
                        add_message_and_hide_buttons(
                            "Busco algo para fiesta",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("🆕 Novedades", key="btn_novedades_{}".format(i), use_container_width=True):
                        response = get_bot_response("novedades")
                        add_message_and_hide_buttons(
                            "Qué novedades tienen",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

            # Opciones casual
            elif button_type == "casual_opciones":
                if st.button("💙 Jeans Mom Fit ($12.990)", key="btn_jeans_{}".format(i), use_container_width=True):
                    add_message_and_hide_buttons(
                        "Quiero ver el jeans",
                        """💙 **Jeans Mom Fit - Tiro Alto**

**Detalles:**
• Color: Azul claro
• Material: 98% algodón, 2% elastano
• Tiro: Alto
• Fit: Mom (relajado en piernas)

**Tallas disponibles:**
• XS - ✅ Stock: 8 unidades
• S - ✅ Stock: 12 unidades
• M - ✅ Stock: 15 unidades
• L - ✅ Stock: 10 unidades
• XL - ✅ Stock: 6 unidades

**$12.990** - Envío gratis

💡 **Se combina perfecto con:**
• Remera oversize blanca ($4.990)
• Zapatillas blancas ($18.990)
• Bolso tote ($8.990)

¿Qué talla necesitás?""",
                        "jeans_tallas"
                    )
                    st.rerun()

                if st.button("🤍 Remera Oversize ($4.990)", key="btn_remera_{}".format(i), use_container_width=True):
                    agregar_al_carrito("Remera Oversize Algodón - Blanca M", 4990)
                    mensaje = """✅ **Agregado al carrito**

{}

💡 **Clientes que compraron esto también llevaron:**
• Jeans Mom Fit ($12.990)
• Short jean ($9.990)

¿Querés agregar algo más?""".format(get_carrito_text())
                    
                    add_message_and_hide_buttons(
                        "Agregar remera oversize",
                        mensaje,
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("✨ Look Casual Completo ($19.990)", key="btn_look_casual_{}".format(i), use_container_width=True):
                    add_message_and_hide_buttons(
                        "Ver look completo",
                        """✨ **Look Casual Completo - $19.990**

**Incluye:**
• Jeans Mom Fit azul claro
• Remera oversize blanca
• Zapatillas deportivas blancas

~~$25.980~~ **$19.990** (ahorrás $5.990)

**Elegí tu talla de jean:**
XS · S · M · L · XL

Escribí tu talla, ej: "Talla M" """,
                        None
                    )
                    st.rerun()

            # Opciones formales
            elif button_type == "formal_opciones":
                if st.button("🖤 Blazer Entallado ($24.990)", key="btn_blazer_{}".format(i), use_container_width=True):
                    add_message_and_hide_buttons(
                        "Ver blazer",
                        """🖤 **Blazer Entallado - Corte Moderno**

**Colores disponibles:**
• Negro - ⚠️ Solo quedan 3 en M, 2 en L
• Beige - ✅ Stock completo

**Tallas y stock:**
• XS - ✅ 8 unidades (ambos colores)
• S - ✅ 12 unidades
• M - ⚠️ Negro: 3 · Beige: 10
• L - ⚠️ Negro: 2 · Beige: 8
• XL - ✅ 6 unidades

**$24.990**

💡 **Outfit completo:**
Blazer + Pantalón + Blusa = $49.990 (ahorrás $9.980)

¿Qué color y talla preferís?""",
                        "blazer_opciones"
                    )
                    st.rerun()

                if st.button("👗 Vestido Midi ($18.990)", key="btn_vestido_midi_{}".format(i), use_container_width=True):
                    agregar_al_carrito("Vestido Midi Manga 3/4 - Negro S", 18990)
                    mensaje = """✅ **Agregado al carrito**

{}

**Este vestido es perfecto para:**
• Oficina / trabajo
• Reuniones importantes
• Eventos formales

¿Querés agregar algo más?""".format(get_carrito_text())
                    
                    add_message_and_hide_buttons(
                        "Agregar vestido midi",
                        mensaje,
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("💼 Combo Oficina ($49.990)", key="btn_combo_oficina_{}".format(i), use_container_width=True):
                    add_message_and_hide_buttons(
                        "Ver combo oficina",
                        """💼 **Combo Oficina Completo**

**Incluye:**
• Blazer entallado (negro o beige)
• Pantalón recto pinzado
• Blusa elegante

~~$59.970~~ **$49.990**
**Ahorrás: $9.980** (17% OFF)

**Seleccioná tu talla:**
• XS · S · M · L · XL

Escribí tu talla y color de blazer, ej: "Talla M, blazer negro" """,
                        None
                    )
                    st.rerun()

            # Selección de tallas para jeans
            elif button_type == "jeans_tallas":
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("Talla S", key="btn_jeans_s_{}".format(i), use_container_width=True):
                        agregar_al_carrito("Jeans Mom Fit Azul - Talla S", 12990)
                        mensaje = """✅ **Jeans Mom Fit Talla S agregado**

{}

¿Querés el outfit completo con 23% OFF?""".format(get_carrito_text())
                        
                        add_message_and_hide_buttons(
                            "Agregar Jeans S",
                            mensaje,
                            "carrito_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("Talla M", key="btn_jeans_m_{}".format(i), use_container_width=True):
                        agregar_al_carrito("Jeans Mom Fit Azul - Talla M", 12990)
                        mensaje = """✅ **Jeans Mom Fit Talla M agregado**

{}

¿Querés el outfit completo con 23% OFF?""".format(get_carrito_text())
                        
                        add_message_and_hide_buttons(
                            "Agregar Jeans M",
                            mensaje,
                            "carrito_acciones"
                        )
                        st.rerun()

                with col3:
                    if st.button("Talla L", key="btn_jeans_l_{}".format(i), use_container_width=True):
                        agregar_al_carrito("Jeans Mom Fit Azul - Talla L", 12990)
                        mensaje = """✅ **Jeans Mom Fit Talla L agregado**

{}

¿Querés el outfit completo con 23% OFF?""".format(get_carrito_text())
                        
                        add_message_and_hide_buttons(
                            "Agregar Jeans L",
                            mensaje,
                            "carrito_acciones"
                        )
                        st.rerun()

            # Acciones del carrito
            elif button_type == "carrito_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("➕ Seguir comprando", key="btn_seguir_{}".format(i), use_container_width=True):
                        add_message_and_hide_buttons(
                            "Seguir comprando",
                            """¿Qué más necesitás?

• 👕 Ropa casual
• 💼 Ropa formal
• ✨ Ropa de fiesta
• 🆕 Novedades
• 🏷️ Ofertas

O escribí lo que buscás!""",
                            "inicial"
                        )
                        st.rerun()

                with col2:
                    if st.button("✅ Finalizar compra", key="btn_checkout_{}".format(i), use_container_width=True):
                        envio_gratis = "GRATIS" if st.session_state.total_carrito >= 15000 else "$350"
                        total_envio = 0 if st.session_state.total_carrito >= 15000 else 350
                        total_final = st.session_state.total_carrito + total_envio
                        mensaje_envio = "✅ Envío gratis por compra mayor a $15.000" if st.session_state.total_carrito >= 15000 else "💡 Agregá ${} para envío gratis".format(15000 - st.session_state.total_carrito)
                        
                        mensaje = """🛒 **Resumen de compra**

{}

**📦 Envío:** {}
{}

**💰 TOTAL: ${:,}**

**Formas de pago:**
• 💳 Tarjeta (hasta 6 cuotas sin interés)
• 💵 Efectivo/Transferencia (10% OFF extra)
• 🪙 MercadoPago

Elegí tu forma de pago:""".format(
                            get_carrito_text(),
                            envio_gratis,
                            mensaje_envio,
                            total_final
                        )
                        
                        add_message_and_hide_buttons(
                            "Ir al checkout",
                            mensaje,
                            "checkout_pago"
                        )
                        st.rerun()

            # Checkout - Formas de pago
            elif button_type == "checkout_pago":
                if st.button("💳 Tarjeta", key="btn_tarjeta_{}".format(i), use_container_width=True):
                    total_envio = 0 if st.session_state.total_carrito >= 15000 else 350
                    total = st.session_state.total_carrito + total_envio
                    cuota_3 = total // 3
                    cuota_6 = total // 6
                    
                    mensaje = """💳 **Pago con Tarjeta**

**Total:** ${:,}

**Cuotas disponibles:**
• 1 pago: ${:,}
• 3 cuotas sin interés: ${:,}/mes
• 6 cuotas sin interés: ${:,}/mes

Para finalizar necesito:
1. Email
2. Dirección de envío
3. Teléfono

Escribí todo junto, ej: 'ana@mail.com, Av. Italia 1234, 099123456' """.format(
                        total, total, cuota_3, cuota_6
                    )
                    
                    add_message_and_hide_buttons(
                        "Pagar con tarjeta",
                        mensaje,
                        "confirmar_compra"
                    )
                    st.rerun()

                if st.button("💵 Efectivo/Transfer (10% OFF)", key="btn_efectivo_{}".format(i), use_container_width=True):
                    total_envio = 0 if st.session_state.total_carrito >= 15000 else 350
                    total_base = st.session_state.total_carrito + total_envio
                    descuento = int(total_base * 0.10)
                    total_final = total_base - descuento
                    
                    mensaje = """💵 **Pago en Efectivo o Transferencia**

**Subtotal:** ${:,}
**Envío:** ${}
**Descuento 10%:** -${:,} 🎉

**TOTAL FINAL:** ${:,}

**Datos para transferencia:**
🏦 Banco: BROU
💳 Cuenta: 001234567-00001
💰 Alias: stylehub.uy

Para confirmar necesito:
1. Email
2. Dirección  
3. Teléfono
4. Comprobante (opcional)

Escribilo todo junto!""".format(
                        st.session_state.total_carrito,
                        total_envio,
                        descuento,
                        total_final
                    )
                    
                    add_message_and_hide_buttons(
                        "Pagar en efectivo",
                        mensaje,
                        "confirmar_compra"
                    )
                    st.rerun()

            # Otros botones
            elif button_type == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("👕 Ver ropa", key="btn_ver_ropa_{}".format(i), use_container_width=True):
                        add_message_and_hide_buttons(
                            "Ver ropa",
                            """¿Qué estilo buscás?

• 👕 Casual
• 💼 Formal
• ✨ Fiesta
• 🆕 Novedades

Elegí una opción""",
                            "inicial"
                        )
                        st.rerun()

                with col2:
                    if st.button("🛒 Mi carrito", key="btn_mi_carrito_{}".format(i), use_container_width=True):
                        if st.session_state.carrito:
                            mensaje_carrito = """{}

¿Querés finalizar la compra?""".format(get_carrito_text())
                            add_message_and_hide_buttons(
                                "Ver carrito",
                                mensaje_carrito,
                                "carrito_acciones"
                            )
                        else:
                            add_message_and_hide_buttons(
                                "Ver carrito",
                                """🛒 Tu carrito está vacío

¿Querés ver productos?""",
                                "inicial"
                            )
                        st.rerun()

# Ejemplos de consultas
st.markdown("---")
st.markdown("**💬 Ejemplos de consultas:**")
col1, col2 = st.columns(2)
with col1:
    st.caption("• Busco jeans cómodos para el día a día")
    st.caption("• Necesito un vestido para una boda")
    st.caption("• Qué outfits tienen para ir a trabajar")
    st.caption("• Cuál es mi talla si mido 90-70-95")
    st.caption("• Qué novedades tienen de esta temporada")
with col2:
    st.caption("• Tienen ofertas en pantalones")
    st.caption("• Cuánto sale el envío a Montevideo")
    st.caption("• Puedo pagar en cuotas sin interés")
    st.caption("• Cómo me registro en el programa de puntos")
    st.caption("• Ayudame a armar un look casual")

# Input del chat
if prompt := st.chat_input("Escribí tu consulta..."):
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
st.caption("💡 **Este es un demo interactivo.** El bot responde con datos de ejemplo.")
st.caption("🔌 En producción conecta con tu inventario real, sistema de tallas y pagos.")

# Botón reset
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """¡Hola! 👋 Bienvenida a StyleHub.

Soy tu asesora de moda personal y estoy para ayudarte.

**¿Qué estás buscando hoy?**""",
                "show_buttons": "inicial"
            }
        ]
        st.session_state.button_clicked = False
        st.session_state.bonus_shown = False
        st.session_state.carrito = []
        st.session_state.total_carrito = 0
        st.rerun()
