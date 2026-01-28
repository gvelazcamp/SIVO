import os
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Demo Ecommerce - TechStore Bot",
    page_icon="🛒",
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

    /* Header personalizado - tema tech/ecommerce */
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
        background: #667eea;
        border-color: #667eea;
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(102, 126, 234, 0.2);
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
    <h1>🛒 TechStore - Asistente de Compras IA</h1>
    <p>Tu tienda de tecnología con atención inteligente 24/7</p>
</div>
""", unsafe_allow_html=True)

BONUS_TEXTO = (
    "Este asistente busca productos, compara precios, verifica stock y procesa pedidos en tiempo real.\n"
    "No es un catálogo estático."
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
            "content": """¡Hola! 👋 Bienvenido a TechStore.

Soy tu asistente de compras y estoy para ayudarte.

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
        texto += f"{idx}. {item['item']} - ${item['precio']:,}\n"
    texto += f"\n**Subtotal: ${st.session_state.total_carrito:,}**"
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

    # 1) Búsqueda de productos - Notebooks
    if any(word in p for word in ["notebook", "laptop", "portatil", "portátil", "computadora"]):
        return {
            "content": """💻 **Notebooks disponibles (stock actualizado)**

**GAMA ALTA - Profesional**
🔥 **MacBook Air M3** (2024)
• 15" · 16GB RAM · 512GB SSD · Chip M3
• **$1.899.000** - ⚡ Quedan 3 unidades
• ⭐⭐⭐⭐⭐ (487 reseñas)

**GAMA MEDIA - Mejor relación precio/calidad**
💎 **Lenovo IdeaPad 5 Pro**
• 14" · Ryzen 7 · 16GB · 512GB SSD
• **$799.000** - ✅ Stock: 12 unidades
• ⭐⭐⭐⭐½ (234 reseñas)

**GAMA ECONÓMICA - Estudiantes**
✅ **HP 15-dy**
• 15.6" · Intel i5 · 8GB · 256GB SSD
• **$549.000** - ✅ Stock: 8 unidades
• ⭐⭐⭐⭐ (156 reseñas)

¿Cuál te interesa o querés que te ayude a elegir según tu uso?""",
            "buttons": "notebook_opciones",
            "bonus_once": True
        }

    # 2) Búsqueda de productos - Celulares
    if any(word in p for word in ["celular", "telefono", "teléfono", "smartphone", "iphone", "samsung"]):
        return {
            "content": """📱 **Smartphones más vendidos**

**FLAGSHIP - Lo mejor**
🔝 **iPhone 15 Pro Max**
• 256GB · A17 Pro · Titanio
• **$1.599.000** - ⚠️ Últimas 2 unidades
• ⭐⭐⭐⭐⭐ (892 reseñas)

🔝 **Samsung Galaxy S24 Ultra**
• 256GB · Snapdragon 8 Gen 3 · S Pen
• **$1.399.000** - ✅ Stock: 5 unidades
• ⭐⭐⭐⭐⭐ (654 reseñas)

**GAMA MEDIA - Best seller**
💚 **Motorola Edge 40**
• 256GB · Snapdragon 7s · 144Hz
• **$449.000** - ✅ Stock: 15 unidades
• ⭐⭐⭐⭐½ (423 reseñas)

**ECONÓMICO - Más vendido**
✅ **Xiaomi Redmi Note 13**
• 128GB · 5G · 120Hz · 5000mAh
• **$269.000** - ✅ Stock: 20+ unidades
• ⭐⭐⭐⭐ (789 reseñas)

¿Cuál se ajusta a tu presupuesto?""",
            "buttons": "celular_opciones"
        }

    # 3) Comparación de productos
    if ("compar" in p) and any(word in p for word in ["iphone", "samsung", "celular", "telefono"]):
        return {
            "content": """📊 **Comparación: iPhone 15 Pro Max vs Samsung S24 Ultra**

| Característica | iPhone 15 Pro Max | Samsung S24 Ultra |
|---|---|---|
| **Precio** | $1.599.000 | $1.399.000 ✅ |
| **Procesador** | A17 Pro ✅ | Snapdragon 8 Gen 3 |
| **Cámara** | 48MP | 200MP ✅ |
| **Batería** | 4.441 mAh | 5.000 mAh ✅ |
| **Pantalla** | 6.7" 120Hz | 6.8" 120Hz ✅ |
| **S Pen** | ❌ | ✅ Incluido |
| **Ecosistema** | iOS ✅ | Android |
| **Peso** | 221g ✅ | 232g |

**Resumen:**
• **iPhone:** Mejor rendimiento puro, ecosistema Apple
• **Samsung:** Mejor cámara, batería, S Pen, $200K menos

¿Querés agregar alguno al carrito o necesitás más info?""",
            "buttons": "comparacion_acciones"
        }

    # 4) Consulta de stock específico
    if ("stock" in p or "hay" in p or "quedan" in p) and any(word in p for word in ["macbook", "iphone", "samsung", "notebook"]):
        if "macbook" in p:
            return {
                "content": """📦 **Stock MacBook Air M3 15" - Actualizado HOY**

✅ **Color Space Gray:** 2 unidades
✅ **Color Silver:** 1 unidad  
❌ **Color Midnight:** AGOTADO (llega en 5 días)
❌ **Color Starlight:** AGOTADO (llega en 5 días)

**⚠️ ALERTA:** Este modelo se está vendiendo rápido.

💡 **Tip:** Si lo comprás hoy, te lo enviamos mañana mismo con envío gratis.

¿Lo agregamos al carrito?""",
                "buttons": "stock_acciones"
            }
        elif "iphone" in p:
            return {
                "content": """📦 **Stock iPhone 15 Pro Max 256GB**

⚠️ **Últimas 2 unidades disponibles**

✅ **Color Titanio Natural:** 1 unidad
✅ **Color Titanio Azul:** 1 unidad
❌ **Otros colores:** Próximo stock en 7-10 días

🔥 **Muy demandado:** 8 personas lo compraron esta semana.

¿Lo reservamos ahora antes de que se agote?""",
                "buttons": "stock_acciones"
            }

    # 5) Consulta de precio específico
    if ("cuanto" in p or "cuánto" in p or "precio" in p) and any(word in p for word in ["cuesta", "sale", "vale"]):
        if "iphone" in p:
            return {
                "content": """💰 **Precios iPhone 15 Pro Max**

**256GB** - $1.599.000 (⚠️ Últimas 2 unidades)
**512GB** - $1.849.000 (✅ Stock disponible)
**1TB** - $2.199.000 (✅ Stock disponible)

**💳 Formas de pago:**
• Contado: 5% descuento adicional
• 3 cuotas sin interés
• 6 cuotas sin interés con tarjetas seleccionadas
• 12 cuotas con interés

🚚 **Envío GRATIS** a todo el país

¿Querés agregarlo al carrito?""",
                "buttons": "precio_acciones"
            }

    # 6) Formas de pago
    if any(word in p for word in ["pago", "cuotas", "tarjeta", "efectivo", "transferencia"]):
        return {
            "content": """💳 **Formas de pago disponibles**

**EFECTIVO / TRANSFERENCIA**
✅ 5% descuento adicional
✅ Precio final en el momento

**TARJETAS DE DÉBITO**
✅ Sin recargo
✅ Acreditación inmediata

**TARJETAS DE CRÉDITO**
✅ **3 cuotas sin interés** (todas las tarjetas)
✅ **6 cuotas sin interés** (Visa, Mastercard, Amex)
✅ **12 cuotas con interés** (23% TEA)

**MERCADO PAGO**
✅ Hasta 12 cuotas
✅ Protección al comprador

**CRYPTO**
✅ USDT, BTC, ETH
✅ 3% descuento

¿Querés seguir comprando o ir al checkout?""",
            "buttons": "pago_acciones"
        }

    # 7) Envíos
    if any(word in p for word in ["envio", "envío", "entrega", "delivery", "demora"]):
        return {
            "content": """🚚 **Opciones de envío**

**ENVÍO EXPRESS (24-48hs)**
• CABA y GBA: GRATIS en compras +$200.000
• Interior: GRATIS en compras +$300.000
• Seguimiento en tiempo real

**ENVÍO ESTÁNDAR (3-5 días)**
• Todo el país: $5.000
• Compras +$150.000: GRATIS

**RETIRO EN SUCURSAL**
• GRATIS
• Disponible en 2-4hs en CABA
• Locales: Palermo, Belgrano, Microcentro

**📍 Tu ubicación:** Montevideo, Uruguay
• Envío internacional: 7-12 días
• Costo: $15.000 (GRATIS en compras +$500.000)
• Incluye tracking y seguro

¿Querés calcular el envío para tu pedido?""",
            "buttons": "envio_acciones"
        }

    # 8) Ofertas y promociones
    if any(word in p for word in ["oferta", "promo", "promocion", "promoción", "descuento", "rebaja"]):
        return {
            "content": """🔥 **OFERTAS ACTIVAS - Válidas HOY**

**⚡ FLASH SALE (próximas 6 horas)**
💻 MacBook Air M2 - ~~$1.299.000~~ **$999.000** (23% OFF)
📱 Xiaomi 13T Pro - ~~$549.000~~ **$429.000** (22% OFF)

**🎯 HOT DEALS**
🎧 AirPods Pro (2da Gen) - ~~$349.000~~ **$289.000**
⌚ Apple Watch SE - ~~$449.000~~ **$379.000**
🖱️ Magic Mouse - ~~$129.000~~ **$99.000**

**💳 COMBO OFERTAS**
📱 Celular + Auriculares: 15% OFF adicional
💻 Notebook + Mochila: Regalo mochila premium
🖥️ iMac + Magic Keyboard: 10% OFF adicional

**📅 CYBER WEEK (toda la semana)**
✅ 3 cuotas sin interés en TODO
✅ Envío gratis sin mínimo
✅ 15% OFF en accesorios

¿Qué oferta te interesa?""",
            "buttons": "ofertas_acciones"
        }

    # 9) Seguimiento de pedido
    if any(word in p for word in ["seguimiento", "pedido", "orden", "track", "donde esta", "dónde está", "envio", "envío"]):
        if any(word in p for word in ["seguimiento", "track", "donde", "dónde"]):
            return {
                "content": """📦 **Seguimiento de pedido**

Para rastrear tu pedido necesito:

**Opción 1:** Número de orden (ej: #TK-2024-45678)

**Opción 2:** Email de compra

**Opción 3:** DNI del comprador

Escribí cualquiera de estos datos y te digo exactamente dónde está tu pedido.

O si todavía no compraste, ¿te ayudo a buscar productos?""",
                "buttons": "ayuda"
            }

    # 10) Garantía
    if any(word in p for word in ["garantia", "garantía", "devolucion", "devolución", "cambio"]):
        return {
            "content": """🛡️ **Garantía y devoluciones**

**GARANTÍA OFICIAL**
✅ 12 meses en todos los productos
✅ Cobertura de fábrica
✅ Service oficial autorizado
✅ Sin costo adicional

**DEVOLUCIÓN (30 días)**
✅ Cambio sin preguntas
✅ Reembolso total
✅ Retiro gratuito a domicilio
✅ Producto sin usar, caja original

**CAMBIO POR DEFECTO**
✅ Cambio inmediato
✅ Sin costo
✅ Hasta 12 meses

**GARANTÍA EXTENDIDA (+$)**
• +1 año: 15% del precio
• +2 años: 25% del precio
• Cubre accidentes, líquidos, caídas

¿Necesitás más info sobre alguna compra?""",
            "buttons": "garantia_acciones"
        }

    # 11) Ayuda para elegir
    if any(word in p for word in ["ayuda", "ayudame", "ayúdame", "cual", "cuál", "elegir", "recomend", "mejor"]):
        return {
            "content": """🤔 **Te ayudo a elegir el producto ideal**

Decime:

**1. ¿Qué vas a usar principalmente?**
• Gaming
• Trabajo / estudio
• Multimedia / streaming
• Uso básico / navegación

**2. ¿Cuál es tu presupuesto?**
• Hasta $300.000
• $300.000 - $600.000
• $600.000 - $1.000.000
• Más de $1.000.000

**3. ¿Qué es más importante para vos?**
• Rendimiento
• Batería
• Cámara
• Pantalla

O si preferís, escribí directamente tu caso (ej: "necesito notebook para programar con presupuesto de $800mil")""",
            "buttons": "ayuda_elegir"
        }

    # Respuesta por defecto
    return {
        "content": """No estoy seguro de entender bien 🤔

**¿Querés que te ayude con alguna de estas opciones?**

• 💻 Ver notebooks disponibles
• 📱 Ver smartphones más vendidos
• 🔥 Ver ofertas del día
• 🚚 Consultar envíos
• 💳 Formas de pago
• 📦 Seguimiento de pedido
• 🛒 Ver mi carrito

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
                    if st.button("💻 Ver notebooks", key=f"btn_notebooks_{i}", use_container_width=True):
                        response = get_bot_response("notebooks")
                        add_message_and_hide_buttons(
                            "Quiero ver notebooks",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("📱 Ver celulares", key=f"btn_celulares_{i}", use_container_width=True):
                        response = get_bot_response("celulares")
                        add_message_and_hide_buttons(
                            "Quiero ver celulares",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🔥 Ver ofertas", key=f"btn_ofertas_{i}", use_container_width=True):
                        response = get_bot_response("ofertas")
                        add_message_and_hide_buttons(
                            "¿Qué ofertas tienen?",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

                with col2:
                    if st.button("🤔 Ayuda para elegir", key=f"btn_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("ayudame a elegir")
                        add_message_and_hide_buttons(
                            "Ayúdame a elegir",
                            response["content"],
                            response.get("buttons")
                        )
                        st.rerun()

            # Opciones de notebooks
            elif button_type == "notebook_opciones":
                if st.button("💻 MacBook Air M3 ($1.899.000)", key=f"btn_macbook_{i}", use_container_width=True):
                    agregar_al_carrito("MacBook Air M3 15\" (16GB/512GB)", 1899000)
                    add_message_and_hide_buttons(
                        "Agregar MacBook Air M3",
                        """✅ **¡Agregado al carrito!**

{}

**💡 Clientes que compraron esto también llevaron:**
• Magic Mouse ($99.000) - 30% OFF
• USB-C Hub 7 en 1 ($45.000)
• Funda premium ($35.000)

¿Querés agregar algo más o finalizar la compra?""".format(get_carrito_text()),
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("💎 Lenovo IdeaPad 5 Pro ($799.000)", key=f"btn_lenovo_{i}", use_container_width=True):
                    agregar_al_carrito("Lenovo IdeaPad 5 Pro (Ryzen 7/16GB/512GB)", 799000)
                    add_message_and_hide_buttons(
                        "Agregar Lenovo IdeaPad 5 Pro",
                        f"""✅ **¡Agregado al carrito!**

{get_carrito_text()}

**💡 Clientes que compraron esto también llevaron:**
• Mouse inalámbrico Logitech ($25.000)
• Mochila para notebook 15" ($18.000)
• Mousepad XXL ($12.000)

¿Querés agregar algo más o finalizar la compra?""",
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("✅ HP 15-dy ($549.000)", key=f"btn_hp_{i}", use_container_width=True):
                    agregar_al_carrito("HP 15-dy (Intel i5/8GB/256GB)", 549000)
                    add_message_and_hide_buttons(
                        "Agregar HP 15-dy",
                        """✅ **¡Agregado al carrito!**

{}

**💡 Te recomendamos agregar:**
• Memoria RAM 8GB extra ($35.000) - Mejorá el rendimiento
• Mouse óptico USB ($8.000)
• Mochila básica ($12.000)

¿Querés agregar algo o finalizar?""".format(get_carrito_text()),
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("🔍 Comparar modelos", key=f"btn_comparar_nb_{i}", use_container_width=True):
                    add_message_and_hide_buttons(
                        "Comparar notebooks",
                        """📊 **Comparación de notebooks**

| Modelo | Procesador | RAM | Precio | Mejor para |
|---|---|---|---|---|
| MacBook Air M3 | M3 ⚡ | 16GB | $1.899K | Profesionales |
| Lenovo IdeaPad | Ryzen 7 | 16GB | $799K | Relación calidad/precio |
| HP 15-dy | Intel i5 | 8GB | $549K | Estudiantes |

**Mi recomendación:**
• **Trabajo pesado:** MacBook (rendering, edición)
• **Uso general:** Lenovo (mejor valor)
• **Estudiante:** HP (cumple bien, buen precio)

¿Cuál te convence?""",
                        "notebook_opciones"
                    )
                    st.rerun()

            # Opciones de celulares
            elif button_type == "celular_opciones":
                if st.button("📱 iPhone 15 Pro Max ($1.599.000)", key=f"btn_iphone_{i}", use_container_width=True):
                    agregar_al_carrito("iPhone 15 Pro Max 256GB Titanio", 1599000)
                    add_message_and_hide_buttons(
                        "Agregar iPhone 15 Pro Max",
                        """✅ **¡Agregado al carrito!**

{}

**🔥 COMBO PACK SUGERIDO:**
• AirPods Pro 2da Gen ($289.000) - ~~$349.000~~
• Funda MagSafe ($49.000)
• Protector de pantalla ($15.000)
**Total combo:** $353.000 (ahorrás $60.000)

¿Agregamos el combo?""".format(get_carrito_text()),
                        "carrito_combo"
                    )
                    st.rerun()

                if st.button("📱 Samsung S24 Ultra ($1.399.000)", key=f"btn_samsung_{i}", use_container_width=True):
                    agregar_al_carrito("Samsung Galaxy S24 Ultra 256GB", 1399000)
                    add_message_and_hide_buttons(
                        "Agregar Samsung S24 Ultra",
                        """✅ **¡Agregado al carrito!**

{}

**🎁 REGALO incluido:** Funda S Pen ($35.000)

**💡 Recomendado:**
• Galaxy Buds2 Pro ($179.000)
• Cargador super rápido 45W ($45.000)

¿Querés agregar algo más?""".format(get_carrito_text()),
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("📱 Motorola Edge 40 ($449.000)", key=f"btn_moto_{i}", use_container_width=True):
                    agregar_al_carrito("Motorola Edge 40 256GB", 449000)
                    add_message_and_hide_buttons(
                        "Agregar Motorola Edge 40",
                        """✅ **¡Agregado al carrito!**

{}

**🎯 Best seller del mes** - Excelente elección

**💡 Combo ideal:**
• Auriculares Moto Buds ($89.000)
• Funda transparente ($15.000)

¿Agregamos algo más?""".format(get_carrito_text()),
                        "carrito_acciones"
                    )
                    st.rerun()

                if st.button("🔍 Comparar iPhone vs Samsung", key=f"btn_comparar_cel_{i}", use_container_width=True):
                    response = get_bot_response("comparar iphone samsung")
                    add_message_and_hide_buttons(
                        "Comparar iPhone vs Samsung",
                        response["content"],
                        response.get("buttons")
                    )
                    st.rerun()

            # Acciones del carrito
            elif button_type == "carrito_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("➕ Seguir comprando", key=f"btn_seguir_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Seguir comprando",
                            """¿Qué más necesitás?

• 💻 Ver notebooks
• 📱 Ver celulares  
• 🎧 Ver accesorios
• 🔥 Ver ofertas

O escribí lo que buscás!""",
                            "inicial"
                        )
                        st.rerun()

                with col2:
                    if st.button("✅ Finalizar compra", key=f"btn_checkout_{i}", use_container_width=True):
                        envio_gratis = "GRATIS" if st.session_state.total_carrito >= 200000 else "$5.000"
                        total_final = st.session_state.total_carrito if st.session_state.total_carrito >= 200000 else st.session_state.total_carrito + 5000
                        
                        mensaje_envio = '✅ Envío gratis por compra mayor a $200.000' if st.session_state.total_carrito >= 200000 else '💡 Agregá $' + str(200000 - st.session_state.total_carrito) + ' para envío gratis'
                        
                        mensaje = """🛒 **Resumen de tu compra**

{}

**📦 Envío:** {}
{}

**💰 TOTAL: ${:,}**

**¿Cómo querés pagar?**
• 💳 Tarjeta (hasta 12 cuotas)
• 💵 Transferencia (5% OFF extra)
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

            # Combo sugerido
            elif button_type == "carrito_combo":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Sí, agregar combo", key=f"btn_combo_si_{i}", use_container_width=True):
                        agregar_al_carrito("AirPods Pro 2da Gen", 289000)
                        agregar_al_carrito("Funda MagSafe", 49000)
                        agregar_al_carrito("Protector pantalla", 15000)
                        add_message_and_hide_buttons(
                            "Agregar combo completo",
                            """✅ **¡Combo agregado!**

{}

🎉 **Ahorraste $60.000** con este combo

¿Listo para finalizar la compra?""".format(get_carrito_text()),
                            "carrito_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("❌ No, solo el celular", key=f"btn_combo_no_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Solo el celular",
                            """👍 Perfecto

{}

¿Querés seguir comprando o finalizamos?""".format(get_carrito_text()),
                            "carrito_acciones"
                        )
                        st.rerun()

            # Checkout - Forma de pago
            elif button_type == "checkout_pago":
                if st.button("💳 Tarjeta de crédito", key=f"btn_tarjeta_{i}", use_container_width=True):
                    descuento = 0
                    total_con_descuento = st.session_state.total_carrito + (0 if st.session_state.total_carrito >= 200000 else 5000)
                    
                    mensaje = """💳 **Pago con tarjeta de crédito**

**Total:** ${:,}

**Cuotas disponibles:**
• 1 pago: ${:,}
• 3 cuotas sin interés: ${:,}/mes
• 6 cuotas sin interés: ${:,}/mes
• 12 cuotas: ${:,}/mes

Para finalizar necesito:
1. Email de contacto
2. Dirección de envío
3. Teléfono

Escribí todo junto, ej: 'juan@mail.com, Av. Italia 1234, 099123456' """.format(
                        total_con_descuento,
                        total_con_descuento,
                        total_con_descuento // 3,
                        total_con_descuento // 6,
                        int(total_con_descuento * 1.23 / 12)
                    )
                    
                    add_message_and_hide_buttons(
                        "Pagar con tarjeta",
                        mensaje,
                        "confirmar_compra"
                    )
                    st.rerun()

                if st.button("💵 Transferencia (5% OFF)", key=f"btn_transfer_{i}", use_container_width=True):
                    total_base = st.session_state.total_carrito + (0 if st.session_state.total_carrito >= 200000 else 5000)
                    descuento = int(total_base * 0.05)
                    total_con_descuento = total_base - descuento
                    
                    mensaje = """💵 **Pago por transferencia bancaria**

**Subtotal:** ${:,}
**Envío:** ${}
**Descuento 5%:** -${:,} 🎉

**TOTAL FINAL:** ${:,}

**Datos bancarios:**
🏦 Banco: Santander
👤 Titular: TechStore SRL
💳 CBU: 0720123456789012345678
💰 Alias: techstore.uy

Para confirmar necesito:
1. Email
2. Dirección de envío  
3. Teléfono
4. Comprobante de pago

Escribilo todo junto!""".format(
                        st.session_state.total_carrito,
                        0 if st.session_state.total_carrito >= 200000 else 5000,
                        descuento,
                        total_con_descuento
                    )
                    
                    add_message_and_hide_buttons(
                        "Pagar con transferencia",
                        mensaje,
                        "confirmar_compra"
                    )
                    st.rerun()

                if st.button("🪙 MercadoPago", key=f"btn_mp_{i}", use_container_width=True):
                    total = st.session_state.total_carrito + (0 if st.session_state.total_carrito >= 200000 else 5000)
                    mensaje = """🪙 **Pago con MercadoPago**

**Total:** ${:,}

**Cuotas disponibles:**
• 1 pago
• Hasta 12 cuotas (según tu tarjeta)

🔐 **Protección al comprador incluida**

Para finalizar necesito:
1. Email
2. Dirección  
3. Teléfono

Y te genero el link de pago!""".format(total)
                    
                    add_message_and_hide_buttons(
                        "Pagar con MercadoPago",
                        mensaje,
                        "confirmar_compra"
                    )
                    st.rerun()

            # Opciones de comparación
            elif button_type == "comparacion_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📱 Agregar iPhone", key=f"btn_add_iphone_{i}", use_container_width=True):
                        agregar_al_carrito("iPhone 15 Pro Max 256GB", 1599000)
                        add_message_and_hide_buttons(
                            "Agregar iPhone 15 Pro Max",
                            """✅ **iPhone agregado al carrito**

{}

¿Seguimos comprando?""".format(get_carrito_text()),
                            "carrito_acciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("📱 Agregar Samsung", key=f"btn_add_samsung_{i}", use_container_width=True):
                        agregar_al_carrito("Samsung S24 Ultra 256GB", 1399000)
                        add_message_and_hide_buttons(
                            "Agregar Samsung S24 Ultra",
                            """✅ **Samsung agregado al carrito**

{}

🎁 Regalo: Funda S Pen incluida

¿Seguimos comprando?""".format(get_carrito_text()),
                            "carrito_acciones"
                        )
                        st.rerun()

            # Stock acciones
            elif button_type == "stock_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Sí, lo quiero", key=f"btn_stock_si_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Quiero reservarlo",
                            """Perfecto! Para reservar tu unidad necesito que:

1. Lo agregues al carrito
2. Completes la compra en las próximas 2 horas
3. Te lo enviamos mañana mismo

¿Volvemos a ver el producto para agregarlo?""",
                            "inicial"
                        )
                        st.rerun()

                with col2:
                    if st.button("🔔 Avisarme cuando llegue", key=f"btn_avisar_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Avisarme de stock",
                            """📧 **Te avisamos cuando llegue**

Dejame tu email y te notificamos apenas tengamos stock.

Escribí tu email, ej: tu@email.com""",
                            None
                        )
                        st.rerun()

            # Ofertas acciones
            elif button_type == "ofertas_acciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("⚡ Ver Flash Sale", key=f"btn_flash_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Ver flash sale",
                            """⚡ **FLASH SALE - Termina en 5:47:23**

💻 **MacBook Air M2** 
~~$1.299.000~~ **$999.000** (23% OFF)
• 13" · M2 · 8GB · 256GB
• ⚠️ Quedan 4 unidades

📱 **Xiaomi 13T Pro**
~~$549.000~~ **$429.000** (22% OFF)
• 256GB · 144Hz · 5000mAh
• ✅ Stock: 8 unidades

⏰ **Apurate!** Estas ofertas se agotan rápido.

¿Cuál te interesa?""",
                            "flash_opciones"
                        )
                        st.rerun()

                with col2:
                    if st.button("💳 Ver combos", key=f"btn_combos_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Ver combos",
                            """🎯 **COMBOS CON DESCUENTO**

📱 **COMBO CELULAR**
iPhone 15 + AirPods + Funda
~~$1.997.000~~ **$1.799.000**
Ahorrás: $198.000

💻 **COMBO NOTEBOOK**
MacBook Air + Magic Mouse + Funda
~~$2.127.000~~ **$1.949.000**
Ahorrás: $178.000

🎮 **COMBO GAMER**
Notebook gaming + Mouse + Auriculares
~~$1.349.000~~ **$1.199.000**
Ahorrás: $150.000

¿Te interesa algún combo?""",
                            None
                        )
                        st.rerun()

            # Ayuda general
            elif button_type == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💻 Ver productos", key=f"btn_productos_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Ver productos",
                            """¿Qué categoría te interesa?

• 💻 Notebooks
• 📱 Celulares
• 🎧 Auriculares
• ⌚ Smartwatches
• 🖱️ Accesorios
• 🎮 Gaming

Escribí la categoría o elegí una opción""",
                            "inicial"
                        )
                        st.rerun()

                with col2:
                    if st.button("🛒 Ver carrito", key=f"btn_ver_carrito_{i}", use_container_width=True):
                        if st.session_state.carrito:
                            add_message_and_hide_buttons(
                                "Ver mi carrito",
                                """{}

¿Querés finalizar la compra?""".format(get_carrito_text()),
                                "carrito_acciones"
                            )
                        else:
                            add_message_and_hide_buttons(
                                "Ver mi carrito",
                                """🛒 Tu carrito está vacío

¿Querés ver productos?""",
                                "inicial"
                            )
                        st.rerun()

# Mostrar sugerencias de preguntas al final
st.markdown("---")
st.markdown("**💬 Ejemplos de consultas que podés hacer:**")
col1, col2 = st.columns(2)
with col1:
    st.caption("• Busco notebook para programar, hasta $800 mil")
    st.caption("• ¿Cuál es el mejor celular por menos de $500 mil?")
    st.caption("• Compará el iPhone 15 con el Samsung S24")
    st.caption("• ¿Tienen stock del MacBook Air M3?")
    st.caption("• Quiero ver las ofertas del día")
with col2:
    st.caption("• ¿Puedo pagar en 6 cuotas sin interés?")
    st.caption("• ¿Cuánto sale el envío a Montevideo?")
    st.caption("• Dame opciones de notebooks gamer")
    st.caption("• ¿Qué incluye la garantía?")
    st.caption("• Necesito ayuda para elegir un celular")

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
st.caption("💡 **Este es un demo interactivo.** El bot responde con datos de ejemplo.")
st.caption("🔌 En producción conecta con tu inventario real, sistema de pagos y logística.")

# Botón para resetear conversación y carrito
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """¡Hola! 👋 Bienvenido a TechStore.

Soy tu asistente de compras y estoy para ayudarte.

**¿Qué estás buscando hoy?**""",
                "show_buttons": "inicial"
            }
        ]
        st.session_state.button_clicked = False
        st.session_state.bonus_shown = False
        st.session_state.carrito = []
        st.session_state.total_carrito = 0
        st.rerun()
