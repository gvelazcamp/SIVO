import streamlit as st

st.set_page_config(layout="wide")

html = """
<style>
/* =========================
   RESET + BASE
========================= */
* {
    box-sizing: border-box;
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

body {
    background: #f6f7fb;
}

/* =========================
   HEADER
========================= */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px 60px;
}

.logo {
    font-size: 22px;
    font-weight: 800;
}

.logo span {
    color: #f4b400;
}

.nav {
    display: flex;
    gap: 32px;
    font-weight: 500;
    color: #555;
}

.btn-login {
    background: #f4b400;
    color: #000;
    padding: 10px 18px;
    border-radius: 12px;
    font-weight: 600;
}

/* =========================
   HERO
========================= */
.hero {
    display: grid;
    grid-template-columns: 1.2fr 1fr;
    gap: 40px;
    padding: 60px;
    align-items: center;
}

.hero h1 {
    font-size: 48px;
    line-height: 1.1;
}

.hero p {
    font-size: 18px;
    color: #555;
    margin: 20px 0;
}

.hero-actions {
    display: flex;
    gap: 20px;
    margin-top: 20px;
}

.btn-primary {
    background: #f4b400;
    padding: 14px 24px;
    border-radius: 14px;
    font-weight: 700;
}

.btn-secondary {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #555;
}

/* =========================
   CATEGORÍAS
========================= */
.categories {
    display: flex;
    justify-content: center;
    gap: 16px;
    margin: 30px 0;
}

.category {
    background: #fff;
    padding: 10px 18px;
    border-radius: 999px;
    font-weight: 600;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
}

/* =========================
   TARJETAS
========================= */
.section {
    padding: 60px;
}

.section h2 {
    text-align: center;
    font-size: 36px;
}

.section p {
    text-align: center;
    color: #666;
    margin-bottom: 40px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
}

.card {
    background: #fff;
    border-radius: 24px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 12px 40px rgba(0,0,0,0.06);
}

.card img {
    width: 100%;
    max-height: 180px;
    object-fit: contain;
}

.card h3 {
    margin-top: 20px;
}

.card p {
    font-size: 14px;
    color: #666;
    min-height: 60px;
}

.card button {
    margin-top: 20px;
    background: #f4b400;
    border: none;
    padding: 10px 18px;
    border-radius: 12px;
    font-weight: 700;
}

/* =========================
   CTA FINAL
========================= */
.cta {
    background: linear-gradient(180deg, #eef2f7, #ffffff);
    padding: 80px;
    text-align: center;
    border-radius: 40px;
    margin: 60px;
}

.cta h2 {
    font-size: 36px;
}

.cta p {
    color: #666;
    margin: 20px 0;
}

.cta button {
    background: #f4b400;
    padding: 16px 30px;
    border-radius: 16px;
    font-weight: 800;
}

/* =========================
   FOOTER
========================= */
.footer {
    padding: 40px;
    display: flex;
    justify-content: space-between;
    color: #888;
    font-size: 14px;
}
</style>

<div class="header">
    <div class="logo">MERCADO<span>BOT</span></div>
    <div class="nav">
        <div>Inicio</div>
        <div>Asistentes</div>
        <div>Precios</div>
        <div>Soporte</div>
    </div>
    <div class="btn-login">Iniciar sesión</div>
</div>

<div class="hero">
    <div>
        <h1>El marketplace<br>de asistentes IA</h1>
        <p>Automatizá tu negocio con asistentes virtuales inteligentes que responden, informan y asisten a tus clientes.</p>
        <div class="hero-actions">
            <div class="btn-primary">Explorar asistentes</div>
            <div class="btn-secondary">▶ Ver demo en vivo</div>
        </div>
    </div>
    <img src="assets/hero.png">
</div>

<div class="categories">
    <div class="category">⚽ Fútbol</div>
    <div class="category">👨‍🍳 Cocina</div>
    <div class="category">🛒 Ecommerce</div>
    <div class="category">💰 Finanzas</div>
</div>

<div class="section">
    <h2>Asistentes IA listos para potenciar tu negocio</h2>
    <p>Explorá, elegí e instalá asistentes inteligentes según tus necesidades.</p>

    <div class="cards">
        <div class="card">
            <img src="assets/futbol.png">
            <h3>Asistente de Fútbol</h3>
            <p>Resultados, noticias y estadísticas del mundo del fútbol.</p>
            <button>Ver asistente</button>
        </div>

        <div class="card">
            <img src="assets/cocina.png">
            <h3>Asistente de Cocina</h3>
            <p>Recetas rápidas, consejos y conversiones al instante.</p>
            <button>Ver asistente</button>
        </div>

        <div class="card">
            <img src="assets/ecommerce.png">
            <h3>Asistente Ecommerce</h3>
            <p>Respuestas automáticas sobre productos, pedidos y envíos.</p>
            <button>Ver asistente</button>
        </div>

        <div class="card">
            <img src="assets/finanzas.png">
            <h3>Asistente de Finanzas</h3>
            <p>Información financiera, cotizaciones y análisis.</p>
            <button>Ver asistente</button>
        </div>
    </div>
</div>

<div class="cta">
    <h2>Integra en minutos</h2>
    <p>Instalá un asistente IA en tu web fácilmente con un simple código.</p>
    <button>Probar gratis</button>
</div>

<div class="footer">
    <div>Política de privacidad · Términos · Contacto</div>
    <div>Facebook · Twitter · LinkedIn</div>
</div>
"""

st.markdown(html, unsafe_allow_html=True)
