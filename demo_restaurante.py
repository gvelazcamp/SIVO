import os
import json
import time
import re
import unicodedata
import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="SIVO Ferretería",
    page_icon="🔧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================
# CARGA DE DATOS
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def cargar_datos():
    with open(os.path.join(BASE_DIR, "productos.json"), "r", encoding="utf-8") as f:
        productos = json.load(f)
    with open(os.path.join(BASE_DIR, "ventas.json"), "r", encoding="utf-8") as f:
        ventas = json.load(f)
    df_prod = pd.DataFrame(productos)
    df_ventas = pd.DataFrame(ventas)
    df_ventas["fecha"] = pd.to_datetime(df_ventas["fecha"])
    return df_prod, df_ventas

df_prod, df_ventas = cargar_datos()

MESES_NOMBRE = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio"}
MESES_NUM = {v: k for k, v in MESES_NOMBRE.items()}

# =========================
# CSS personalizado
# =========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background: linear-gradient(180deg, #f0f7ff 0%, #ffffff 100%);
    }

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

    .custom-header {
        text-align: center;
        padding: 32px 24px;
        background: linear-gradient(135deg, #1e3a5f 0%, #1e40af 45%, #3b82f6 100%);
        border-radius: 20px;
        margin-bottom: 20px;
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

    /* Dashboard de métricas (KPIs) */
    .kpi-row {
        display: flex;
        gap: 12px;
        margin-bottom: 20px;
    }

    .kpi-card {
        flex: 1;
        background: white;
        border-radius: 16px;
        padding: 16px 14px;
        text-align: center;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        border: 1px solid #e2e8f0;
    }

    .kpi-card .kpi-val {
        font-size: 22px;
        font-weight: 800;
        color: #1e3a5f;
        line-height: 1.2;
    }

    .kpi-card .kpi-lbl {
        font-size: 11px;
        color: #6b7280;
        font-weight: 600;
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 0.3px;
    }

    /* Tabla de datos preview */
    .data-preview-wrap {
        background: white;
        border-radius: 16px;
        padding: 16px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        border: 1px solid #e2e8f0;
        margin-bottom: 24px;
    }

    .data-preview-wrap h4 {
        font-size: 13px;
        font-weight: 800;
        color: #374151;
        margin: 0 0 10px 0;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }

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
    }

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

    .volver-flotante {
        position: fixed;
        top: 14px;
        left: 14px;
        background: #1e3a5f;
        color: white;
        padding: 10px 18px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 13px;
        box-shadow: 0 4px 14px rgba(30, 58, 95, 0.35);
        z-index: 999999;
        display: flex;
        align-items: center;
        gap: 8px;
        text-decoration: none;
        transition: transform 0.2s;
    }

    .volver-flotante .volver-texto {
        display: inline;
    }

    .volver-flotante:hover {
        transform: scale(1.05);
        color: white;
    }

    @media (max-width: 768px) {
        .volver-flotante {
            top: 10px;
            left: 10px;
            width: 34px;
            height: 34px;
            padding: 0;
            border-radius: 50%;
            font-size: 15px;
            justify-content: center;
        }
        .volver-flotante .volver-texto {
            display: none;
        }
        .kpi-row {
            flex-wrap: wrap;
        }
        .kpi-card {
            min-width: 45%;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="custom-header">
    <div class="custom-header-badge"><span class="status-dot"></span>EN VIVO · DATOS REALES, NO SIMULADOS</div>
    <h1>🔧 SIVO Ferretería</h1>
    <p>Preguntale a tu negocio. Esto consulta una base de datos real de 6 meses de ventas.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<a href="https://sivoia.store/?vista=home" target="_blank" class="volver-flotante" title="Volver a SIVO">
    ← <span class="volver-texto">Volver a SIVO</span>
</a>
""", unsafe_allow_html=True)

# =========================
# DASHBOARD DE DATOS (vista previa, antes del chat)
# =========================
total_facturado = df_ventas["monto"].sum()
total_ventas = len(df_ventas)
total_productos = len(df_prod)
ticket_promedio = df_ventas["monto"].mean()

st.markdown(f"""
<div class="kpi-row">
    <div class="kpi-card">
        <div class="kpi-val">${total_facturado:,.0f}</div>
        <div class="kpi-lbl">Facturado (6 meses)</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-val">{total_ventas:,}</div>
        <div class="kpi-lbl">Ventas registradas</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-val">{total_productos}</div>
        <div class="kpi-lbl">Productos en catálogo</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-val">${ticket_promedio:,.0f}</div>
        <div class="kpi-lbl">Ticket promedio</div>
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("📊 Ver muestra de los datos reales (productos y ventas)"):
    st.markdown("**Catálogo de productos (muestra):**")
    st.dataframe(df_prod.sample(8, random_state=1)[["nombre", "categoria", "precio", "stock"]], hide_index=True, use_container_width=True)
    st.markdown("**Registros de ventas (muestra):**")
    st.dataframe(
        df_ventas.sample(8, random_state=2)[["fecha", "producto_nombre", "cantidad", "monto", "cliente"]],
        hide_index=True, use_container_width=True
    )
    st.caption(f"Base completa: {len(df_prod)} productos · {len(df_ventas)} registros de ventas de enero a junio 2026.")

# =========================
# UTILIDADES DE NORMALIZACIÓN
# =========================
def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return texto

def encontrar_productos_multiples(pregunta_norm):
    """Busca TODOS los productos cuyo nombre comparta al menos 1 palabra clave con la pregunta.
    Útil para términos genéricos en plural (ej: "martillos" -> todos los martillos)."""
    candidatos = []
    for _, row in df_prod.iterrows():
        nombre_norm = normalizar(row["nombre"])
        palabras_prod = set(re.findall(r"[a-z0-9]+", nombre_norm))
        palabras_prod -= {"de", "x", "1", "2", "3", "4", "para"}
        score = sum(1 for palabra in palabras_prod if len(palabra) > 3 and palabra in pregunta_norm)
        if score >= 1:
            candidatos.append((score, row))
    if not candidatos:
        return None
    candidatos.sort(key=lambda x: -x[0])
    mejor_score = candidatos[0][0]
    # Devolver todos los que igualan al mejor score (ej: ambos modelos de martillo)
    ids_coincidentes = [row["id"] for score, row in candidatos if score == mejor_score]
    return df_prod[df_prod["id"].isin(ids_coincidentes)]

def encontrar_categoria(pregunta_norm):
    categorias = df_prod["categoria"].unique()
    for cat in categorias:
        cat_norm = normalizar(cat)
        palabras_cat = re.findall(r"[a-z]+", cat_norm)
        if any(p in pregunta_norm for p in palabras_cat if len(p) > 4):
            return cat
    # Sinónimos comunes
    sinonimos = {
        "tornillo": "Tornillería", "tornillos": "Tornillería",
        "pintura": "Pintura", "pinturas": "Pintura",
        "electric": "Electricidad",
        "plomeria": "Plomería", "plomería": "Plomería", "cano": "Plomería",
        "seguridad": "Seguridad",
        "cerrajeria": "Cerrajería", "cerrajería": "Cerrajería",
    }
    for k, v in sinonimos.items():
        if k in pregunta_norm:
            return v
    return None

def encontrar_meses(pregunta_norm):
    encontrados = []
    for nombre, num in MESES_NUM.items():
        if nombre in pregunta_norm:
            encontrados.append(num)
    return encontrados

# =========================
# MOTOR DE RESPUESTAS (consulta REAL sobre los datos)
# =========================
def responder(pregunta):
    p = normalizar(pregunta)
    meses_mencionados = encontrar_meses(p)
    productos_match = encontrar_productos_multiples(p)
    categoria = encontrar_categoria(p) if productos_match is None else None

    es_comparacion = any(w in p for w in ["compara", "comparar", "versus", "vs", "diferencia entre"])
    es_ranking = any(w in p for w in ["mas vendido", "más vendido", "top", "ranking", "mejor producto", "que mas se vende", "cual vendo mas"])
    es_stock = any(w in p for w in ["stock", "queda", "quedan", "inventario", "disponible", "hay de"])
    es_facturacion = any(w in p for w in ["factur", "vendi", "vendí", "venta", "ventas", "cuanto vendi", "ingreso"])

    # ===== 1) COMPARACIÓN ENTRE MESES =====
    if es_comparacion and len(meses_mencionados) >= 2:
        m1, m2 = meses_mencionados[0], meses_mencionados[1]
        v1 = df_ventas[df_ventas["mes"] == m1]["monto"].sum()
        v2 = df_ventas[df_ventas["mes"] == m2]["monto"].sum()
        diff_pct = ((v1 - v2) / v2 * 100) if v2 else 0
        signo = "📈" if diff_pct >= 0 else "📉"
        return (
            f"📊 **Comparativa {MESES_NOMBRE[m1].capitalize()} vs {MESES_NOMBRE[m2].capitalize()}:**\n\n"
            f"<table class='tabla-datos'>"
            f"<tr><th>Mes</th><th>Facturación</th></tr>"
            f"<tr><td>{MESES_NOMBRE[m1].capitalize()}</td><td>${v1:,.0f}</td></tr>"
            f"<tr><td>{MESES_NOMBRE[m2].capitalize()}</td><td>${v2:,.0f}</td></tr>"
            f"</table>\n\n"
            f"{signo} Variación: **{diff_pct:+.1f}%**"
        )

    # ===== 2) STOCK de producto(s) específico(s) =====
    if es_stock and productos_match is not None:
        if len(productos_match) == 1:
            producto = productos_match.iloc[0]
            return (
                f"📦 **Stock de {producto['nombre']}:**\n\n"
                f"Quedan **{producto['stock']} unidades** disponibles.\n"
                f"Precio unitario: ${producto['precio']:,.0f}\n"
                f"Categoría: {producto['categoria']}"
            )
        else:
            filas = "".join(
                f"<tr><td>{r['nombre']}</td><td>{r['stock']}</td></tr>"
                for _, r in productos_match.iterrows()
            )
            total_stock = productos_match["stock"].sum()
            return (
                f"📦 **Stock encontrado ({len(productos_match)} variantes):**\n\n"
                f"<table class='tabla-datos'><tr><th>Producto</th><th>Stock</th></tr>{filas}</table>\n\n"
                f"Total combinado: **{int(total_stock)} unidades**"
            )

    # ===== 3) STOCK de una categoría =====
    if es_stock and categoria is not None:
        sub = df_prod[df_prod["categoria"] == categoria].sort_values("stock")
        filas = "".join(
            f"<tr><td>{r['nombre']}</td><td>{r['stock']}</td></tr>"
            for _, r in sub.head(8).iterrows()
        )
        return (
            f"📦 **Stock en categoría {categoria}:**\n\n"
            f"<table class='tabla-datos'><tr><th>Producto</th><th>Stock</th></tr>{filas}</table>"
        )

    # ===== 4) RANKING (producto más vendido) =====
    if es_ranking:
        df_filtro = df_ventas
        periodo_txt = "en todo el período"
        if meses_mencionados:
            df_filtro = df_ventas[df_ventas["mes"].isin(meses_mencionados)]
            nombres_meses = " y ".join(MESES_NOMBRE[m].capitalize() for m in meses_mencionados)
            periodo_txt = f"en {nombres_meses}"
        if categoria:
            df_filtro = df_filtro[df_filtro["categoria"] == categoria]

        ranking = (
            df_filtro.groupby("producto_nombre")
            .agg(cantidad=("cantidad", "sum"), monto=("monto", "sum"))
            .sort_values("cantidad", ascending=False)
            .head(5)
        )
        if ranking.empty:
            return f"No encontré ventas {periodo_txt} con esos filtros. Probá con otro mes o categoría."

        filas = "".join(
            f"<tr><td>{i+1}</td><td>{nombre}</td><td>{int(row['cantidad'])}</td><td>${row['monto']:,.0f}</td></tr>"
            for i, (nombre, row) in enumerate(ranking.iterrows())
        )
        return (
            f"🏆 **Top 5 productos más vendidos {periodo_txt}:**\n\n"
            f"<table class='tabla-datos'><tr><th>#</th><th>Producto</th><th>Unidades</th><th>Facturado</th></tr>{filas}</table>"
        )

    # ===== 5) Venta/facturación de producto(s) específico(s) =====
    if productos_match is not None and (es_facturacion or meses_mencionados or not (es_stock or es_ranking)):
        ids_prod = productos_match["id"].tolist()
        df_filtro = df_ventas[df_ventas["producto_id"].isin(ids_prod)]
        periodo_txt = "en todo el período (6 meses)"
        if meses_mencionados:
            df_filtro = df_filtro[df_filtro["mes"].isin(meses_mencionados)]
            nombres_meses = " y ".join(MESES_NOMBRE[m].capitalize() for m in meses_mencionados)
            periodo_txt = f"en {nombres_meses}"

        cantidad_total = df_filtro["cantidad"].sum()
        monto_total = df_filtro["monto"].sum()
        num_operaciones = len(df_filtro)

        nombre_ref = productos_match.iloc[0]["nombre"] if len(productos_match) == 1 else f"{len(productos_match)} variantes encontradas"

        if num_operaciones == 0:
            return f"No registré ventas de **{nombre_ref}** {periodo_txt}."

        detalle_variantes = ""
        if len(productos_match) > 1:
            por_producto = df_filtro.groupby("producto_nombre").agg(cantidad=("cantidad","sum"), monto=("monto","sum"))
            filas = "".join(
                f"<tr><td>{nombre}</td><td>{int(row['cantidad'])}</td><td>${row['monto']:,.0f}</td></tr>"
                for nombre, row in por_producto.iterrows()
            )
            detalle_variantes = f"<table class='tabla-datos'><tr><th>Variante</th><th>Unidades</th><th>Facturado</th></tr>{filas}</table>\n\n"

        return (
            f"🔧 **{nombre_ref}** {periodo_txt}:\n\n"
            f"{detalle_variantes}"
            f"• Unidades vendidas (total): **{int(cantidad_total)}**\n"
            f"• Facturado: **${monto_total:,.0f}**\n"
            f"• Operaciones: {num_operaciones}"
        )

    # ===== 6) Facturación general (con o sin mes/categoría) =====
    if es_facturacion or meses_mencionados or categoria:
        df_filtro = df_ventas
        periodo_txt = "en los 6 meses registrados"
        if meses_mencionados:
            df_filtro = df_filtro[df_filtro["mes"].isin(meses_mencionados)]
            nombres_meses = " y ".join(MESES_NOMBRE[m].capitalize() for m in meses_mencionados)
            periodo_txt = f"en {nombres_meses}"
        if categoria:
            df_filtro = df_filtro[df_filtro["categoria"] == categoria]
            periodo_txt += f" (categoría {categoria})"

        if df_filtro.empty:
            return f"No encontré ventas {periodo_txt}."

        monto_total = df_filtro["monto"].sum()
        cantidad_ops = len(df_filtro)
        return (
            f"💰 **Facturación {periodo_txt}:**\n\n"
            f"• Total facturado: **${monto_total:,.0f}**\n"
            f"• Cantidad de ventas: {cantidad_ops}\n"
            f"• Ticket promedio: ${(monto_total/cantidad_ops if cantidad_ops else 0):,.0f}"
        )

    # ===== Sin match =====
    return None

def get_bot_response(prompt):
    resultado = responder(prompt)
    if resultado:
        return {"content": resultado, "buttons": "ayuda"}
    return {
        "content": (
            "No encontré esa información con precisión 🤔. Podés preguntarme cosas como:\n\n"
            "• ¿Cuánto facturé en marzo?\n"
            "• ¿Cuántos martillos vendí en abril?\n"
            "• ¿Cuál es mi producto más vendido?\n"
            "• ¿Qué stock tengo de tornillos?\n"
            "• Comparame marzo con abril\n\n"
            "Tip: mencioná el nombre del producto, la categoría o el mes para que pueda buscarlo en los datos reales."
        ),
        "buttons": "ayuda"
    }

# =========================
# CHAT
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """¡Hola! 👋 Soy SIVO, conectado a la base de datos real de esta ferretería.

Tengo **6 meses de ventas reales** (959 operaciones, 84 productos). No tengo respuestas preparadas: calculo todo en el momento sobre los datos.

**Probá preguntarme algo:**""",
            "show_buttons": "inicial"
        }
    ]

BOT_AVATAR = "🔧"

def add_message_and_hide_buttons(user_msg, bot_response, next_buttons=None):
    st.session_state.messages.append({"role": "user", "content": user_msg})

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        placeholder = st.empty()
        placeholder.markdown("""
        <div class="typing-indicator">
            <span></span><span></span><span></span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.6)
        placeholder.empty()

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response,
        "show_buttons": next_buttons
    })

for i, message in enumerate(st.session_state.messages):
    avatar = BOT_AVATAR if message["role"] == "assistant" else None
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"], unsafe_allow_html=True)

        if message.get("show_buttons") == "inicial":
            col1, col2 = st.columns(2)
            with col1:
                if st.button("💰 ¿Cuánto facturé en marzo?", key=f"btn1_{i}", use_container_width=True):
                    r = get_bot_response("¿Cuánto facturé en marzo?")
                    add_message_and_hide_buttons("¿Cuánto facturé en marzo?", r["content"], r.get("buttons"))
                    st.rerun()
            with col2:
                if st.button("🏆 ¿Mi producto más vendido?", key=f"btn2_{i}", use_container_width=True):
                    r = get_bot_response("¿Cuál es mi producto más vendido?")
                    add_message_and_hide_buttons("¿Cuál es mi producto más vendido?", r["content"], r.get("buttons"))
                    st.rerun()
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📦 Stock de tornillos", key=f"btn3_{i}", use_container_width=True):
                    r = get_bot_response("¿Qué stock tengo de tornillos?")
                    add_message_and_hide_buttons("¿Qué stock tengo de tornillos?", r["content"], r.get("buttons"))
                    st.rerun()
            with col2:
                if st.button("📈 Comparar marzo vs abril", key=f"btn4_{i}", use_container_width=True):
                    r = get_bot_response("Comparame marzo con abril")
                    add_message_and_hide_buttons("Comparame marzo con abril", r["content"], r.get("buttons"))
                    st.rerun()

# Ejemplos
st.markdown("---")
st.markdown('<div class="ejemplos-header">✨ Esto es una base de datos real — probá preguntar lo que quieras:</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.caption("💬 ¿Cuántos martillos vendí en enero?")
    st.caption("💬 ¿Cuánto facturé en pintura?")
    st.caption("💬 Top 5 productos más vendidos en mayo")
with col2:
    st.caption("💬 ¿Qué stock tengo de taladros?")
    st.caption("💬 Comparame enero con junio")
    st.caption("💬 ¿Cuánto vendí de cable eléctrico?")

# Input
if prompt := st.chat_input("Preguntale algo a los datos reales..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    r = get_bot_response(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        placeholder = st.empty()
        placeholder.markdown("""
        <div class="typing-indicator">
            <span></span><span></span><span></span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.6)
        placeholder.empty()

    st.session_state.messages.append({
        "role": "assistant",
        "content": r["content"],
        "show_buttons": r.get("buttons")
    })

    st.rerun()

st.divider()
st.caption("💡 **Esto NO es una demo con respuestas preparadas.** Los números se calculan en vivo sobre una base de datos real de ejemplo (84 productos, 959 ventas, 6 meses).")
st.caption("🔌 En tu negocio real, SIVO se conecta a tu propio Excel, sistema de gestión o base de datos.")

col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """¡Hola! 👋 Soy SIVO, conectado a la base de datos real de esta ferretería.

Tengo **6 meses de ventas reales** (959 operaciones, 84 productos). No tengo respuestas preparadas: calculo todo en el momento sobre los datos.

**Probá preguntarme algo:**""",
                "show_buttons": "inicial"
            }
        ]
        st.rerun()
