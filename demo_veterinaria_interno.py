import os
import time
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="SIVO Interno",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background: linear-gradient(180deg, #f0f7ff 0%, #ffffff 100%);
    }

    /* Estilos del chat */
    .stChatMessage {
        max-width: 800px;
        margin: 0 auto 4px auto;
    }

    .stChatFloatingInputContainer {
        max-width: 800px;
        margin: 0 auto;
    }

    [data-testid="stChatMessage"] {
        border-radius: 18px;
        padding: 4px 6px;
        animation: fadeInUp 0.35s ease-out;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(8px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Header personalizado - tema SIVO Interno */
    .custom-header {
        text-align: center;
        padding: 32px 24px;
        background: linear-gradient(135deg, #1e3a5f 0%, #1e40af 45%, #3b82f6 100%);
        border-radius: 20px;
        margin-bottom: 24px;
        color: white;
        box-shadow: 0 10px 30px rgba(30, 64, 175, 0.25);
        position: relative;
        overflow: hidden;
    }

    .custom-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 60%);
        animation: pulse 4s ease-in-out infinite;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.6; }
        50% { transform: scale(1.1); opacity: 1; }
    }

    .custom-header-badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        padding: 5px 14px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 12px;
        position: relative;
        z-index: 1;
    }

    .custom-header h1 {
        margin: 0;
        font-size: 30px;
        font-weight: 800;
        letter-spacing: -0.5px;
        position: relative;
        z-index: 1;
    }

    .custom-header p {
        margin: 10px 0 0 0;
        opacity: 0.95;
        font-size: 15px;
        font-weight: 500;
        position: relative;
        z-index: 1;
    }

    .custom-header .status-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        background: #4ade80;
        border-radius: 50%;
        margin-right: 6px;
        box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7);
        animation: dotPulse 2s infinite;
    }

    @keyframes dotPulse {
        0% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.6); }
        70% { box-shadow: 0 0 0 6px rgba(74, 222, 128, 0); }
        100% { box-shadow: 0 0 0 0 rgba(74, 222, 128, 0); }
    }

    /* Resumen flotante (KPI rápido) */
    .resumen-flotante {
        position: fixed;
        top: 18px;
        right: 18px;
        background: linear-gradient(135deg, #1e40af, #3b82f6);
        color: white;
        padding: 10px 18px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 14px;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.35);
        z-index: 999999;
        display: flex;
        align-items: center;
        gap: 8px;
        animation: bounceIn 0.4s ease-out;
    }

    @keyframes bounceIn {
        0% { transform: scale(0.7); opacity: 0; }
        60% { transform: scale(1.08); }
        100% { transform: scale(1); opacity: 1; }
    }

    @media (max-width: 768px) {
        .resumen-flotante {
            top: auto;
            bottom: 80px;
            right: 14px;
            padding: 8px 14px;
            font-size: 12px;
        }
    }

    /* Botones más profesionales */
    div[data-testid="column"] > div > div > button {
        width: 100%;
        border-radius: 12px;
        padding: 15px 20px;
        font-weight: 600;
        font-size: 15px;
        transition: all 0.2s ease;
        border: 1.5px solid #dbeafe;
        background: white;
        color: #374151;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }

    div[data-testid="column"] > div > div > button:hover {
        background: linear-gradient(135deg, #1e40af, #3b82f6);
        border-color: #3b82f6;
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(59, 130, 246, 0.3);
    }

    div[data-testid="column"] > div > div > button:active {
        transform: translateY(0) scale(0.98);
    }

    /* Mejorar los caption de ejemplos */
    .stCaption {
        color: #6b7280 !important;
        font-size: 14px !important;
        line-height: 1.9 !important;
    }

    .ejemplos-header {
        font-weight: 700;
        font-size: 15px;
        color: #111827;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Indicador "escribiendo..." */
    .typing-indicator {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 8px 4px;
    }

    .typing-indicator span {
        width: 7px;
        height: 7px;
        background: #3b82f6;
        border-radius: 50%;
        animation: typingBounce 1.2s infinite ease-in-out;
    }

    .typing-indicator span:nth-child(2) { animation-delay: 0.15s; }
    .typing-indicator span:nth-child(3) { animation-delay: 0.3s; }

    @keyframes typingBounce {
        0%, 60%, 100% { transform: translateY(0); opacity: 0.5; }
        30% { transform: translateY(-6px); opacity: 1; }
    }

    /* Tabla de datos estilizada dentro del chat */
    .tabla-datos {
        width: 100%;
        border-collapse: collapse;
        font-size: 13px;
        margin: 10px 0;
    }
    .tabla-datos th {
        background: #eff6ff;
        color: #1e3a5f;
        padding: 8px 10px;
        text-align: left;
        font-weight: 700;
        border-bottom: 2px solid #dbeafe;
    }
    .tabla-datos td {
        padding: 8px 10px;
        border-bottom: 1px solid #f0f0f0;
    }

    /* Botón flotante "Volver a SIVO" */
    .volver-flotante {
        position: fixed;
        bottom: 18px;
        left: 18px;
        background: #1e3a5f;
        color: white;
        padding: 12px 18px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 13px;
        box-shadow: 0 8px 22px rgba(30, 58, 95, 0.4);
        z-index: 999999;
        display: flex;
        align-items: center;
        gap: 8px;
        text-decoration: none;
        transition: transform 0.2s;
    }

    .volver-flotante:hover {
        transform: translateY(-2px) scale(1.03);
        color: white;
    }

    @media (max-width: 768px) {
        .volver-flotante {
            bottom: 80px;
            padding: 10px 14px;
            font-size: 12px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header personalizado
st.markdown("""
<div class="custom-header">
    <div class="custom-header-badge"><span class="status-dot"></span>EN VIVO · DEMO INTERACTIVO</div>
    <h1>📊 SIVO Interno</h1>
    <p>Le preguntás a tus propios datos como si le hablaras a un empleado. Veterinaria San Roque · Datos de ejemplo.</p>
</div>
""", unsafe_allow_html=True)

# Botón flotante para volver a sivoia.store
st.markdown("""
<a href="https://sivoia.store/?vista=home" target="_blank" class="volver-flotante">
    ← Volver a SIVO
</a>
""", unsafe_allow_html=True)

BONUS_TEXTO = (
    "Esto no es un chatbot de atención al cliente — es un asistente interno.\n"
    "Le preguntás por tu facturación, tu stock o tus reportes y te responde con tus datos reales, al instante."
)

def maybe_append_bonus_once():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"💡 **{BONUS_TEXTO}**",
            "show_buttons": None
        })
        st.session_state.bonus_shown = True

# Inicializar el chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """¡Hola! 👋 Soy SIVO, el asistente interno de **Veterinaria San Roque**.

No atiendo clientes — te ayudo a vos, el dueño, a entender qué está pasando en tu negocio sin tener que abrir ninguna planilla.

**¿Qué querés saber hoy?**""",
            "show_buttons": "inicial"
        }
    ]

if "bonus_shown" not in st.session_state:
    st.session_state.bonus_shown = False

# Función para agregar mensaje con typing simulado
def add_message_and_hide_buttons(user_msg, bot_response, next_buttons=None, show_bonus_once=False):
    st.session_state.messages.append({"role": "user", "content": user_msg})

    with st.chat_message("assistant", avatar="📊"):
        placeholder = st.empty()
        placeholder.markdown("""
        <div class="typing-indicator">
            <span></span><span></span><span></span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.7)
        placeholder.empty()

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response,
        "show_buttons": next_buttons
    })

    if show_bonus_once:
        maybe_append_bonus_once()

# =========================
# Función para obtener respuesta del bot (datos ficticios internos)
# =========================
def get_bot_response(prompt):
    p = (prompt or "").lower()

    # 1) Facturación / ventas del mes
    if any(w in p for w in ["facturacion", "facturación", "factur", "vendi", "vendí", "ventas del mes", "cuanto vendi"]):
        return {
            "content": """💰 **Facturación de este mes (enero 2026)**

<table class="tabla-datos">
<tr><th>Categoría</th><th>Monto</th><th>vs. mes anterior</th></tr>
<tr><td>Consultas</td><td>$412.000</td><td>📈 +12%</td></tr>
<tr><td>Vacunas</td><td>$298.500</td><td>📈 +8%</td></tr>
<tr><td>Medicamentos</td><td>$185.300</td><td>📉 -4%</td></tr>
<tr><td>Peluquería / Baño</td><td>$96.200</td><td>📈 +21%</td></tr>
</table>

**Total facturado: $992.000** — un **+9% más** que el mes pasado ($910.500).

¿Querés que te mande el desglose por día o por veterinario?""",
            "buttons": "facturacion_opciones",
            "bonus_once": True
        }

    # 2) Stock crítico / inventario
    if any(w in p for w in ["stock", "inventario", "queda", "falta", "se esta acabando", "se está acabando"]):
        return {
            "content": """📦 **Stock con alerta crítica**

<table class="tabla-datos">
<tr><th>Producto</th><th>Stock actual</th><th>Dura aprox.</th></tr>
<tr><td>Vacuna antirrábica</td><td>4 dosis</td><td>~3 días</td></tr>
<tr><td>Antiparasitario Bravecto</td><td>2 unidades</td><td>~2 días</td></tr>
<tr><td>Alimento balanceado Premium</td><td>6 bolsas</td><td>~5 días</td></tr>
</table>

⚠️ 3 productos están por agotarse esta semana.

¿Querés que genere la orden de compra y la envíe al proveedor?""",
            "buttons": "stock_accion"
        }

    # 3) Producto / servicio más vendido
    if any(w in p for w in ["mas vendido", "más vendido", "top", "ranking", "mejor producto", "que mas se vende"]):
        return {
            "content": """🏆 **Top 5 servicios más solicitados este mes**

<table class="tabla-datos">
<tr><th>#</th><th>Servicio</th><th>Cantidad</th></tr>
<tr><td>1</td><td>Consulta general</td><td>142</td></tr>
<tr><td>2</td><td>Vacuna antirrábica</td><td>89</td></tr>
<tr><td>3</td><td>Baño y peluquería</td><td>76</td></tr>
<tr><td>4</td><td>Desparasitación</td><td>61</td></tr>
<tr><td>5</td><td>Castración</td><td>34</td></tr>
</table>

La consulta general sigue siendo tu servicio más fuerte, seguido de cerca por vacunación.

¿Te interesa ver la evolución de algún servicio en particular?""",
            "buttons": "ranking_opciones"
        }

    # 4) Comparativa de meses
    if any(w in p for w in ["compara", "comparar", "mes anterior", "mes pasado", "evolucion", "evolución", "crecimiento"]):
        return {
            "content": """📈 **Comparativa: este mes vs. mes anterior**

<table class="tabla-datos">
<tr><th>Indicador</th><th>Enero</th><th>Diciembre</th><th>Variación</th></tr>
<tr><td>Facturación total</td><td>$992.000</td><td>$910.500</td><td>📈 +9%</td></tr>
<tr><td>Cantidad de turnos</td><td>312</td><td>289</td><td>📈 +8%</td></tr>
<tr><td>Ticket promedio</td><td>$3.179</td><td>$3.151</td><td>📈 +1%</td></tr>
<tr><td>Clientes nuevos</td><td>47</td><td>38</td><td>📈 +24%</td></tr>
</table>

Buen mes: crecieron tanto la facturación como la cantidad de clientes nuevos.

¿Querés que prepare un reporte con estos datos para enviar por mail?""",
            "buttons": "reporte_opciones"
        }

    # 5) Reportes / enviar por mail
    if any(w in p for w in ["reporte", "informe", "mandame", "envia", "envíame", "mail", "excel"]):
        return {
            "content": """📧 **Reporte generado**

He armado el reporte mensual con:
✅ Facturación detallada por categoría
✅ Stock crítico y sugerencias de compra
✅ Top servicios y evolución vs. mes anterior
✅ Gráficos de tendencia

El archivo Excel está listo y se envió a **gerencia@vetsanroque.com**

¿Querés que también lo programe para que se genere y envíe automáticamente todos los meses?""",
            "buttons": "automatizar_opciones"
        }

    # 6) Clientes / turnos
    if any(w in p for w in ["clientes", "turnos", "agenda", "cuantos pacientes", "cuántos pacientes"]):
        return {
            "content": """🐾 **Pacientes y turnos**

<table class="tabla-datos">
<tr><th>Indicador</th><th>Este mes</th></tr>
<tr><td>Turnos atendidos</td><td>312</td></tr>
<tr><td>Clientes nuevos</td><td>47</td></tr>
<tr><td>Clientes recurrentes</td><td>265</td></tr>
<tr><td>Cancelaciones</td><td>9 (2.8%)</td></tr>
</table>

Tu tasa de cancelación está muy baja (2.8%), eso es excelente para el rubro.

¿Querés ver el detalle de turnos por veterinario?""",
            "buttons": "ayuda"
        }

    # Respuesta por defecto
    return {
        "content": """No estoy seguro de entender bien tu consulta 🤔

**¿Querés que te ayude con alguno de estos temas?**

• 💰 Facturación del mes
• 📦 Stock crítico e inventario
• 🏆 Servicios más vendidos
• 📈 Comparar con el mes anterior
• 📧 Generar y enviar un reporte
• 🐾 Turnos y clientes

O preguntame directamente lo que necesitás saber sobre tu negocio.""",
        "buttons": "ayuda"
    }

# =========================
# Resumen flotante (KPI rápido siempre visible)
# =========================
st.markdown("""
<div class="resumen-flotante">
    💰 $992.000 este mes
</div>
""", unsafe_allow_html=True)

# =========================
# Mostrar mensajes del chat
# =========================
BOT_AVATAR = "📊"

for i, message in enumerate(st.session_state.messages):
    avatar = BOT_AVATAR if message["role"] == "assistant" else None
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"], unsafe_allow_html=True)

        if message.get("show_buttons"):
            button_type = message["show_buttons"]

            if button_type == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💰 Facturación del mes", key=f"btn_fact_{i}", use_container_width=True):
                        response = get_bot_response("facturacion")
                        add_message_and_hide_buttons("¿Cuánto facturé este mes?", response["content"], response.get("buttons"), response.get("bonus_once"))
                        st.rerun()
                with col2:
                    if st.button("📦 Stock crítico", key=f"btn_stock_{i}", use_container_width=True):
                        response = get_bot_response("stock")
                        add_message_and_hide_buttons("¿Qué stock está en alerta?", response["content"], response.get("buttons"))
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🏆 Servicios más vendidos", key=f"btn_top_{i}", use_container_width=True):
                        response = get_bot_response("mas vendido")
                        add_message_and_hide_buttons("¿Cuál es mi servicio más vendido?", response["content"], response.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("📈 Comparar con mes anterior", key=f"btn_comp_{i}", use_container_width=True):
                        response = get_bot_response("comparar")
                        add_message_and_hide_buttons("Comparame este mes con el anterior", response["content"], response.get("buttons"))
                        st.rerun()

            elif button_type == "facturacion_opciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📧 Enviar reporte", key=f"btn_rep_fact_{i}", use_container_width=True):
                        response = get_bot_response("reporte")
                        add_message_and_hide_buttons("Mandame el reporte por mail", response["content"], response.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("📈 Comparar meses", key=f"btn_comp_fact_{i}", use_container_width=True):
                        response = get_bot_response("comparar")
                        add_message_and_hide_buttons("Comparame con el mes anterior", response["content"], response.get("buttons"))
                        st.rerun()

            elif button_type == "stock_accion":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Generar orden de compra", key=f"btn_orden_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Sí, generá la orden y enviala",
                            """✅ **Orden de compra generada**

Se solicitaron:
• Vacuna antirrábica × 20 dosis
• Antiparasitario Bravecto × 15 unidades
• Alimento balanceado Premium × 30 bolsas

**Total estimado:** $186.400

La orden fue enviada al proveedor habitual. Te aviso cuando confirmen la recepción.""",
                            "ayuda"
                        )
                        st.rerun()
                with col2:
                    if st.button("🏆 Ver más vendidos", key=f"btn_top_stock_{i}", use_container_width=True):
                        response = get_bot_response("mas vendido")
                        add_message_and_hide_buttons("¿Cuál es mi servicio más vendido?", response["content"], response.get("buttons"))
                        st.rerun()

            elif button_type == "ranking_opciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💰 Ver facturación", key=f"btn_fact_rank_{i}", use_container_width=True):
                        response = get_bot_response("facturacion")
                        add_message_and_hide_buttons("¿Cuánto facturé este mes?", response["content"], response.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("🐾 Ver turnos y clientes", key=f"btn_turnos_rank_{i}", use_container_width=True):
                        response = get_bot_response("turnos")
                        add_message_and_hide_buttons("¿Cuántos pacientes atendí?", response["content"], response.get("buttons"))
                        st.rerun()

            elif button_type == "reporte_opciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📧 Mandalo ahora", key=f"btn_mandar_{i}", use_container_width=True):
                        response = get_bot_response("reporte")
                        add_message_and_hide_buttons("Sí, mandalo por mail", response["content"], response.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("📦 Ver stock crítico", key=f"btn_stock_rep_{i}", use_container_width=True):
                        response = get_bot_response("stock")
                        add_message_and_hide_buttons("¿Qué stock está en alerta?", response["content"], response.get("buttons"))
                        st.rerun()

            elif button_type == "automatizar_opciones":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Sí, automatizalo", key=f"btn_auto_{i}", use_container_width=True):
                        add_message_and_hide_buttons(
                            "Sí, programalo todos los meses",
                            """✅ **Reporte automático configurado**

A partir de hoy, este reporte se va a generar y enviar **automáticamente el día 1 de cada mes** a gerencia@vetsanroque.com, sin que tengas que pedirlo de nuevo.

Esto es exactamente lo que hace SIVO en producción: una vez configurado, el trabajo queda hecho solo. 🙌""",
                            "ayuda"
                        )
                        st.rerun()
                with col2:
                    if st.button("🐾 Ver turnos y clientes", key=f"btn_turnos_auto_{i}", use_container_width=True):
                        response = get_bot_response("turnos")
                        add_message_and_hide_buttons("¿Cuántos pacientes atendí?", response["content"], response.get("buttons"))
                        st.rerun()

            elif button_type == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💰 Facturación", key=f"btn_fact_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("facturacion")
                        add_message_and_hide_buttons("¿Cuánto facturé este mes?", response["content"], response.get("buttons"))
                        st.rerun()
                with col2:
                    if st.button("📦 Stock", key=f"btn_stock_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("stock")
                        add_message_and_hide_buttons("¿Qué stock está en alerta?", response["content"], response.get("buttons"))
                        st.rerun()

# Mostrar sugerencias de preguntas al final (SIEMPRE visible)
st.markdown("---")
st.markdown('<div class="ejemplos-header">✨ Probá escribiendo cosas como estas:</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.caption("💬 ¿Cuánto facturé este mes?")
    st.caption("💬 ¿Qué stock está por agotarse?")
    st.caption("💬 ¿Cuál es mi servicio más vendido?")
with col2:
    st.caption("💬 Comparame este mes con el anterior")
    st.caption("💬 Mandame el reporte por mail")
    st.caption("💬 ¿Cuántos pacientes atendí este mes?")

# INPUT DEL CHAT
if prompt := st.chat_input("Preguntale algo a tus datos..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_bot_response(prompt)

    with st.chat_message("assistant", avatar="📊"):
        placeholder = st.empty()
        placeholder.markdown("""
        <div class="typing-indicator">
            <span></span><span></span><span></span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.7)
        placeholder.empty()

    st.session_state.messages.append({
        "role": "assistant",
        "content": response["content"],
        "show_buttons": response.get("buttons")
    })

    if response.get("bonus_once"):
        maybe_append_bonus_once()

    st.rerun()

# Footer
st.divider()
st.caption("💡 **Este es un demo interactivo.** Los datos son de ejemplo (Veterinaria San Roque, ficticia).")
st.caption("🔌 En producción, SIVO se conecta a tu Excel, tu sistema de gestión o tu base de datos real.")

# Botón para resetear conversación
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """¡Hola! 👋 Soy SIVO, el asistente interno de **Veterinaria San Roque**.

No atiendo clientes — te ayudo a vos, el dueño, a entender qué está pasando en tu negocio sin tener que abrir ninguna planilla.

**¿Qué querés saber hoy?**""",
                "show_buttons": "inicial"
            }
        ]
        st.session_state.bonus_shown = False
        st.rerun()
