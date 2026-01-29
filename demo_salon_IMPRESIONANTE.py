import os
import streamlit as st

# Configuracion de la pagina
st.set_page_config(
    page_title="Demo Salón - BeautyBot",
    page_icon="💇‍♀️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado
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
        background: linear-gradient(135deg, #ff6b9d 0%, #c06c84 100%);
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
        background: #ff6b9d;
        border-color: #ff6b9d;
        color: white;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(255, 107, 157, 0.3);
    }

    .stCaption {
        color: #6b7280 !important;
        font-size: 14px !important;
        line-height: 1.8 !important;
    }
</style>
""", unsafe_allow_html=True)

# Badge de demo
st.markdown("""
<div style="text-align: center; margin-bottom: 15px;">
    <span style="
        display: inline-block;
        background: linear-gradient(135deg, #ff6b9d 0%, #ff8fab 100%);
        color: white;
        padding: 10px 24px;
        border-radius: 25px;
        font-weight: 600;
        font-size: 14px;
        box-shadow: 0 2px 8px rgba(255, 107, 157, 0.4);
    ">
        ✨ Imaginate este demo con tus datos - Tu salón, tus servicios, tus reglas
    </span>
</div>
""", unsafe_allow_html=True)

# Header personalizado
st.markdown("""
<div class="custom-header">
    <h1>💇‍♀️ BeautyBot - Gestión Inteligente de Salón</h1>
    <p>Reservas, agenda y atención al cliente automatizada 24/7</p>
</div>
""", unsafe_allow_html=True)

BONUS_TEXTO = (
    "Este asistente gestiona turnos en tiempo real, responde consultas sobre servicios y precios, "
    "y coordina la agenda de tus estilistas automáticamente."
)

def maybe_append_bonus_once():
    if not st.session_state.get("bonus_shown", False):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "💡 **{}**".format(BONUS_TEXTO),
            "show_buttons": None
        })
        st.session_state.bonus_shown = True

# Inicializar el chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """¡Hola! Soy tu asistente virtual del salón 💇‍♀️

Puedo ayudarte con:
- 📅 Reservar turnos
- 💰 Consultar servicios y precios
- 👨‍🦱 Ver estilistas disponibles
- ⭐ Promociones vigentes
- 🎁 Paquetes especiales

¿Qué necesitas hoy?""",
            "show_buttons": "inicial"
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

# FUNCION PRINCIPAL - SUPER COMPLETA
def get_bot_response(prompt):
    p = (prompt or "").lower().strip()
    
    # 1) RESERVAR TURNO / AGENDA
    turno_kw = ["turno", "reserva", "reservar", "agendar", "agenda", "cita", "hora", "disponible", 
                "cuando", "cuándo", "libre", "dia", "día", "fecha", "horario", "appointment"]
    
    if any(k in p for k in turno_kw):
        return {
            "content": """📅 **Agenda Disponible - Próximos 7 Días**

**HOY - Sábado 1/2** ⚡ ¡Último momento!
- 10:00am - María (Especialista coloración) ✅
- 14:30pm - Sofía (Corte & styling) ✅
- 16:00pm - Laura (Todo tipo) ✅

**Domingo 2/2** 🌟 Domingo especial
- 09:00am - María ✅
- 11:30am - Sofía ✅
- 15:00pm - Laura ✅
- 17:00pm - María ✅

**Lunes 3/2** 
- 09:00am, 11:00am, 14:00pm, 16:00pm, 18:00pm
- Todas las estilistas disponibles ✅

**Martes 4/2**
- 10:00am, 12:00pm, 15:00pm, 17:00pm ✅

**Miércoles 5/2** 😊 Día tranquilo
- 09:00am, 10:30am, 13:00pm, 15:30pm, 17:30pm ✅

**Jueves 6/2** 🔥 Día popular
- 14:00pm, 16:30pm, 18:00pm (pocos turnos!)

**Viernes 7/2** ⚠️ Casi completo
- 09:00am, 18:30pm (últimos!)

**💡 Tip:** Los sábados y viernes se llenan rápido. 
¡Reservá con anticipación!

¿Qué día te viene bien?""",
            "buttons": "turno_opciones",
            "bonus_once": True
        }
    
    # 2) SERVICIOS Y PRECIOS
    servicio_kw = ["servicio", "servicios", "precio", "precios", "costo", "cuanto", "cuánto", "sale", 
                   "valor", "tarifa", "corte", "color", "tintura", "mechas", "tratamiento", "brushing",
                   "alisado", "permanente", "peinado"]
    
    if any(k in p for k in servicio_kw):
        # Servicios específicos
        if any(k in p for k in ["corte", "cortar", "tijera"]):
            return {
                "content": """✂️ **Servicios de Corte**

**CORTE MUJER**
- Corte + Brushing: $1.200
- Corte + Secado: $900
- Solo Corte: $700
- Flequillo: $300

**CORTE HOMBRE**
- Corte clásico: $600
- Corte + Barba: $850
- Degradé moderno: $750

**CORTE NIÑOS** (hasta 12 años)
- Niños: $500
- Niñas: $550

**SERVICIOS PREMIUM**
- Corte + Tratamiento: $1.800
- Corte + Color: desde $2.500
- Corte + Mechas: desde $3.200

**⏱️ Duración:** 30-60 min
**👨‍🦱 Estilistas:** Todas capacitadas

**🎁 PROMO HOY:**
Corte + Brushing $1.000 (ahorro $200)
Válido solo sábados hasta 14hs

¿Te reservo un turno?""",
                "buttons": "corte_acciones"
            }
        
        elif any(k in p for k in ["color", "tintura", "tinte", "coloracion", "coloración"]):
            return {
                "content": """🎨 **Servicios de Coloración**

**COLOR COMPLETO**
- Raíces (retoque): $1.500
- Color global (pelo corto): $2.200
- Color global (pelo largo): $2.800
- Color fantasía (unicolor): $3.500
- Color fantasía (multicolor): $4.500

**MECHAS & HIGHLIGHTS**
- Mechas californianas: $3.800
- Balayage natural: $4.200
- Babylights: $3.500
- Ombré: $3.900
- Reflejos sutiles: $2.800

**TRATAMIENTOS COLOR**
- Baño de color: $1.200
- Toner/Matizador: $800
- Decapado (por sesión): $2.500

**SERVICIOS PREMIUM**
- Coloración + Corte: desde $3.500
- Mechas + Tratamiento: desde $5.000
- Cambio de look completo: desde $6.000

**⏱️ Duración:** 2-4 horas según servicio
**👩 Especialista:** María (15 años experiencia)

**💝 PACK COLOR:**
Color completo + Corte + Tratamiento: $3.800
(Ahorro de $1.200!)

**⚠️ Importante:** 
- Consulta previa sin cargo
- Test de alergia incluido
- Productos profesionales L'Oréal

¿Querés agendar una consulta?""",
                "buttons": "color_acciones"
            }
        
        elif any(k in p for k in ["mechas", "highlights", "balayage", "ombre", "ombré"]):
            return {
                "content": """✨ **Servicios de Mechas & Highlights**

**TÉCNICAS DISPONIBLES:**

🌟 **Californianas** - $3.800
- Efecto natural degradado
- Ideal pelo castaño/rubio
- Duración: 3 horas
- Mantenimiento cada 3-4 meses

🎨 **Balayage** - $4.200  
- Técnica pintada a mano
- Resultado más personalizado
- Duración: 3.5 horas
- Perfecto para cualquier largo

💫 **Babylights** - $3.500
- Mechas super finas y naturales
- Efecto "iluminado por el sol"
- Duración: 3 horas
- Ideal pelo fino

🌈 **Ombré** - $3.900
- Degradado de raíz a puntas
- Efecto dramático
- Duración: 3.5 horas
- Bajo mantenimiento

💎 **Reflejos Sutiles** - $2.800
- Pocas mechas estratégicas
- Efecto natural y discreto
- Duración: 2 horas

**COMBOS POPULARES:**

🎁 **Mechas + Corte:** $4.500 (ahorro $500)
🎁 **Balayage + Tratamiento:** $5.000
🎁 **Look completo:** Mechas + Corte + Brushing: $5.200

**INCLUYE:**
✅ Consulta previa personalizada
✅ Productos profesionales premium
✅ Tratamiento post-color
✅ Brushing o secado
✅ Consejos de mantenimiento

**👩 Especialista:** María - Experta en colorimetría

**📸 Portfolio:** Podemos mostrarte fotos de trabajos anteriores

¿Te gustaría ver algunas opciones para tu tipo de pelo?""",
                "buttons": "mechas_acciones"
            }
        
        elif any(k in p for k in ["tratamiento", "keratina", "botox", "nutricion", "nutrición", "hidratacion", "hidratación"]):
            return {
                "content": """💆‍♀️ **Tratamientos Capilares**

**TRATAMIENTOS INTENSIVOS:**

✨ **Keratina Brasilera** - $4.500
- Alisado permanente progresivo
- Duración: 3-6 meses
- Reduce 80% del frizz
- Tiempo: 3-4 horas
- Ideal: Pelo rizado/ondulado con frizz

💎 **Botox Capilar** - $2.800
- Reparación profunda instantánea
- Duración: 3-4 semanas
- Brillo y suavidad extrema
- Tiempo: 1.5 horas
- Ideal: Todo tipo de pelo maltratado

🌿 **Nutrición Profunda** - $1.800
- Hidratación intensiva
- Duración: 2-3 semanas
- Productos naturales
- Tiempo: 1 hora
- Ideal: Pelo seco y opaco

🔥 **Reconstrucción Molecular** - $2.200
- Repara daño químico
- Duración: 4 semanas
- Fortalece fibra capilar
- Tiempo: 1.5 horas
- Ideal: Pelo muy dañado

**TRATAMIENTOS RÁPIDOS:**

⚡ **Ampolla Flash** - $800
- Efecto inmediato
- Sin enjuague
- 15 minutos
- Para eventos

💧 **Hidratación Express** - $600
- Mascarilla premium
- 20 minutos
- Brillo instantáneo

**PLANES DE MANTENIMIENTO:**

📦 **Plan 3 Sesiones:** $4.500 (ahorro $900)
- 1 tratamiento mensual
- Seguimiento personalizado
- Productos para casa incluidos

📦 **Plan 6 Sesiones:** $8.000 (ahorro $2.400)
- Tratamiento cada 15 días
- Máximos resultados
- Kit completo de mantenimiento

**🎁 PROMO ESTA SEMANA:**
Botox + Corte + Brushing: $3.500
(Ahorro de $1.500!)

**⚠️ Recomendación:**
Evaluación gratuita del estado de tu cabello
para recomendarte el mejor tratamiento

¿Querés que analicemos tu cabello?""",
                "buttons": "tratamiento_acciones"
            }
        
        # Lista general de servicios
        else:
            return {
                "content": """💅 **Carta Completa de Servicios - Bella Salon**

**✂️ CORTES**
- Mujer (c/brushing): $1.200
- Hombre: $600
- Niños: $500
- Flequillo: $300

**🎨 COLORACIÓN**
- Retoque raíces: $1.500
- Color completo: desde $2.200
- Mechas californianas: $3.800
- Balayage: $4.200
- Ombré: $3.900

**💆‍♀️ TRATAMIENTOS**
- Keratina brasilera: $4.500
- Botox capilar: $2.800
- Nutrición profunda: $1.800
- Hidratación express: $600

**💇‍♀️ PEINADOS & STYLING**
- Brushing: $500
- Peinado social: $1.800
- Peinado novia: $3.500
- Ondas/Rulos: $700
- Planchado: $600

**🌟 SERVICIOS ESPECIALES**
- Alisado permanente: $3.500
- Permanente rizado: $2.800
- Extensiones (consultar): desde $8.000
- Cambio de look completo: desde $6.000

**💝 PAQUETES ESPECIALES**

🎁 **Renovación Total:** $4.900
   Corte + Color + Tratamiento + Brushing
   (Ahorro: $1.500)

🎁 **Express Glam:** $2.200
   Corte + Brushing + Hidratación
   (Ahorro: $500)

🎁 **Transformación Completa:** $7.500
   Mechas + Corte + Keratina + Peinado
   (Ahorro: $2.500)

**⭐ MEMBRESÍA MENSUAL:** $3.500/mes
- 1 corte + brushing
- 1 tratamiento
- 20% desc en otros servicios
- Prioridad en agenda

**🎉 PROMOCIONES VIGENTES:**
- Lunes a miércoles: 15% OFF en todos los servicios
- Cumpleañeras: 20% OFF todo el mes
- Recomienda y gana: $500 de descuento

**⏱️ Horarios:** Lun-Sáb 9am-8pm, Dom 9am-6pm

¿Qué servicio te interesa?""",
                "buttons": "servicios_categorias"
            }
    
    # 3) ESTILISTAS / PROFESIONALES
    estilista_kw = ["estilista", "estilistas", "peluquera", "peluquero", "profesional", "quien", "quién",
                    "maria", "maría", "sofia", "sofía", "laura", "especialista", "mejor"]
    
    if any(k in p for k in estilista_kw):
        return {
            "content": """👩‍🦰 **Nuestro Equipo de Estilistas**

**MARÍA GONZÁLEZ** ⭐⭐⭐⭐⭐ (5.0)
- 🎨 Especialidad: Coloración & Mechas
- 📅 Experiencia: 15 años
- 🏆 Certificaciones: L'Oréal Master, Wella Pro
- 💬 Reseñas: 243 clientes satisfechos
- ⏰ Horarios: Lun-Vie 9am-6pm, Sáb 9am-2pm
- 💰 Servicios estrella:
  • Balayage perfecto: $4.200
  • Color fantasía: $4.500
  • Corrección de color: $3.500

"María es una GENIA! Me hizo unas mechas californianas hermosas, 
super naturales. Explica todo re bien." - Lucía R.

---

**SOFÍA MARTÍNEZ** ⭐⭐⭐⭐⭐ (4.9)
- ✂️ Especialidad: Cortes modernos & Styling
- 📅 Experiencia: 8 años
- 🏆 Certificaciones: Vidal Sassoon, Trends 2024
- 💬 Reseñas: 189 clientes satisfechos
- ⏰ Horarios: Mar-Sáb 10am-7pm, Dom 10am-4pm
- 💰 Servicios estrella:
  • Cortes modernos: $1.200
  • Peinados de novia: $3.500
  • Transformaciones: $2.500

"Sofía tiene un ojo increíble. Me cortó el pelo y quedé 
ENAMORADA del resultado!" - Martina P.

---

**LAURA FERNÁNDEZ** ⭐⭐⭐⭐⭐ (4.8)
- 💆‍♀️ Especialidad: Tratamientos & Recuperación
- 📅 Experiencia: 12 años
- 🏆 Certificaciones: Keratina Expert, Botox Specialist
- 💬 Reseñas: 167 clientes satisfechos
- ⏰ Horarios: Lun-Vie 9am-8pm, Sáb 9am-5pm
- 💰 Servicios estrella:
  • Keratina brasilera: $4.500
  • Reconstrucción capilar: $2.800
  • Botox capilar: $2.800

"Mi pelo estaba MUERTO y Laura lo revivió. Es una maga con 
los tratamientos." - Carolina M.

---

**🎯 CÓMO ELEGIR:**

📌 **Para cambio de color radical:** María
📌 **Para corte moderno/trendy:** Sofía  
📌 **Para reparar cabello dañado:** Laura
📌 **No tenés preferencia:** Cualquiera! Todas son excelentes

**💡 Todas nuestras estilistas:**
✅ Consulta personalizada sin cargo
✅ Productos profesionales premium
✅ Seguimiento post-servicio
✅ Consejos de cuidado en casa

¿Con quién te gustaría agendar?""",
            "buttons": "estilistas_acciones"
        }
    
    # 4) PROMOCIONES Y OFERTAS
    promo_kw = ["promocion", "promoción", "promo", "oferta", "descuento", "rebaja", "especial",
                "paquete", "pack", "combo", "ahorro", "barato"]
    
    if any(k in p for k in promo_kw):
        return {
            "content": """🎁 **Promociones & Ofertas Especiales**

**🔥 PROMOS FLASH - ESTA SEMANA**

⚡ **Martes y Miércoles Mágicos**
- 20% OFF en TODOS los servicios
- Solo turnos de 9am a 2pm
- Incluye cortes, color y tratamientos
- Válido hasta 5/02

⚡ **Sábado Express** (solo hasta 14hs)
- Corte + Brushing: $1.000 (antes $1.200)
- Color raíces: $1.300 (antes $1.500)
- Tratamiento flash: $500 (antes $800)

---

**💝 PAQUETES COMBINADOS**

🎁 **Renovación Total** - $4.900 ⭐ MÁS VENDIDO
   ✨ Corte profesional
   ✨ Color completo O mechas
   ✨ Tratamiento reparador
   ✨ Brushing de regalo
   **Ahorro: $1.800** | Duración: 4hs

🎁 **Glam Express** - $2.200
   ✂️ Corte + Brushing
   💆‍♀️ Hidratación profunda
   **Ahorro: $500** | Duración: 1.5hs

🎁 **Transformación Completa** - $7.500
   🎨 Mechas premium (técnica a elección)
   ✂️ Corte + Diseño personalizado
   💎 Keratina o Botox capilar
   💇‍♀️ Peinado profesional
   **Ahorro: $2.800** | Duración: 5-6hs

---

**⭐ MEMBRESÍA MENSUAL** - $3.500/mes

Incluye TODO ESTO cada mes:
✅ 1 corte profesional + brushing
✅ 1 tratamiento (botox o nutrición)
✅ 20% descuento en servicios adicionales
✅ Prioridad en agenda (reservas con 2 días)
✅ 1 producto profesional gratis por trimestre
✅ Cumpleaños: Servicio adicional sin cargo

**💰 Ahorro anual: $4.800**
Sin permanencia, cancelás cuando quieras

---

**🎉 PROMOS PERMANENTES**

🎂 **Mes de Cumpleaños:** 20% OFF en todo
💑 **Amigas Juntas:** 15% para ambas
👥 **Recomendá y Gana:** $500 de desc c/u
👶 **Primera Vez:** 10% OFF en tu primer visita
🌙 **Turno Tarde:** 10% OFF después de las 17hs (lun-mié)

---

**💎 SERVICIOS PREMIUM CON DESCUENTO**

🌟 Extensiones: Consulta + 15% OFF
🌟 Cambio de look radical: Asesoría gratis + 10% OFF
🌟 Novias: Prueba sin cargo + Pack especial

---

**🎯 PROMO PRÓXIMA SEMANA (6-12 Feb)**

"Semana del Amor" ❤️
- Paquete parejas: $3.800 (2 servicios completos)
- Peinados románticos: desde $1.500
- Tratamiento + Peinado: $2.800

---

**📱 CÓMO APROVECHAR:**

1. Mencioná la promo al reservar
2. Válido solo para nuevas reservas
3. No acumulable entre sí
4. Sujeto a disponibilidad

**💡 TIP:** Las promos de lun-mié son las mejores para
ahorrar sin sacrificar calidad!

¿Querés reservar con alguna promo?""",
            "buttons": "promos_acciones"
        }
    
    # 5) HORARIOS Y UBICACIÓN
    horario_kw = ["horario", "horarios", "abierto", "cierran", "abren", "donde", "dónde", "ubicacion",
                  "ubicación", "direccion", "dirección", "como llegar", "cómo llegar"]
    
    if any(k in p for k in horario_kw):
        return {
            "content": """📍 **Ubicación & Horarios - Bella Salon**

**DIRECCIÓN:**
🏢 Av. 18 de Julio 1234, Montevideo
📍 Entre Yaguarón y Río Branco
🚇 A 2 cuadras del metro Ejido

**HORARIOS DE ATENCIÓN:**

🗓️ **Lunes a Viernes:** 9:00am - 8:00pm
🗓️ **Sábados:** 9:00am - 6:00pm  
🗓️ **Domingos:** 9:00am - 4:00pm
❌ **Feriados:** Cerrado (consultar excepciones)

**⏰ HORARIOS ESPECIALES:**

🌙 **Turnos Noche:** Lun-Jue hasta 8pm
- Ideal para después del trabajo
- 10% descuento después de 17hs

☀️ **Domingo Relax:** 9am-4pm
- Ambiente más tranquilo
- Música suave
- Atención más personalizada

---

**🚗 CÓMO LLEGAR:**

**En Auto:**
- Estacionamiento en la puerta ($)
- Garaje Cordón a 1 cuadra
- Zona azul disponible

**En Ómnibus:**
- Líneas: 64, 180, 187, 121, 187
- Parada: 18 de Julio y Yaguarón

**En Metro:**
- Estación Ejido (2 cuadras)
- Estación Plaza Independencia (5 cuadras)

**A Pie:**
- Centro de la ciudad
- Zona super accesible

---

**☎️ CONTACTO:**

📞 **Teléfono/WhatsApp:** +598 2908 1234
📧 **Email:** hola@bellasalon.uy
📱 **Instagram:** @bellasalon_uy
💬 **Chat:** Estás acá! 😊

**📲 TAMBIÉN PODÉS:**
- Llamar para consultas rápidas
- WhatsApp para fotos/referencias
- Instagram para ver trabajos anteriores

---

**🎯 RECOMENDACIONES:**

💡 **Mejor momento para venir:**
- Lun-Mié por la mañana (más tranquilo)
- Evitar viernes tarde y sábados (lleno)

💡 **Reserva anticipada:**
- Sábados: con 1 semana
- Viernes: con 3-4 días
- Lun-Jue: mismo día OK

💡 **Servicios largos (keratina, mechas):**
- Agendar turno mañana (más tiempo)
- Evitar sábados si es posible

¿Necesitás indicaciones más detalladas?""",
            "buttons": "ubicacion_acciones"
        }
    
    # 6) PEINADOS Y EVENTOS
    peinado_kw = ["peinado", "peinados", "evento", "fiesta", "boda", "casamiento", "15 años", "egresados",
                  "social", "novia", "madrina"]
    
    if any(k in p for k in peinado_kw):
        return {
            "content": """💐 **Peinados para Eventos Especiales**

**👰 NOVIAS** ⭐ Nuestro servicio estrella

💎 **Paquete Novia Completo** - $5.500
✨ Prueba de peinado (incluida)
✨ Peinado el día del evento
✨ Maquillaje profesional
✨ Retoque a domicilio (opcional +$800)
✨ Productos fijación profesional
✨ Tocados/accesorios sugeridos

💫 **Solo Peinado Novia** - $3.500
- Consulta previa sin cargo
- Fotos de referencia incluidas
- Duración: 2 horas
- Garantía de durabilidad
- Productos premium

🎀 **Prueba de Peinado** - $800
- 1 hora de prueba
- Probamos 2-3 estilos
- Fotos para recordar
- Se descuenta del total si contratas

---

**👗 EVENTOS SOCIALES**

🌟 **Madrinas/Invitadas Especiales** - $2.200
- Peinado elaborado
- Asesoramiento de estilo
- Duración: 1.5 horas
- Fijación de larga duración

💃 **Peinado Social Clásico** - $1.800
- Recogidos elegantes
- Semi-recogidos
- Ondas Hollywood
- Trenzas decorativas

⚡ **Peinado Express** - $1.200
- Para eventos informales
- 45 minutos
- Brushing + detalles

---

**🎉 EVENTOS ESPECIALES**

👸 **15 Años** - desde $2.500
- Peinado + Prueba incluida
- Maquillaje opcional: +$1.200
- Retoque en el evento: +$600

🎓 **Egresados** - $1.500
- Peinados juveniles
- Estilos modernos
- Duración: 1 hora

🎭 **Shows/Performances** - Consultar
- Peinados teatrales
- Alta fijación
- Consulta previa necesaria

---

**👥 GRUPOS (3+ personas)**

💝 **Descuentos Grupales:**
- 3-5 personas: 10% OFF
- 6-10 personas: 15% OFF
- +10 personas: 20% OFF

🏠 **Servicio a Domicilio:**
- Grupos 3+: $500 adicional por traslado
- Equipos completos incluidos
- Zona Montevideo y alrededores

---

**📅 AGENDA DE EVENTOS - Próximos Meses**

⚠️ **Temporada Alta (Sep-Dic, Abr-Jun)**
- Reservar con 2-3 meses de anticipación
- Días sábados casi completos
- Precios regulares

✅ **Temporada Baja (Ene-Mar, Jul-Ago)**
- Más disponibilidad
- Posible esperar menos
- Misma calidad

---

**🎨 ESTILOS DISPONIBLES:**

Peinados clásicos:
• Moño francés • Rodete bajo/alto
• Trenzas corona • Semi-recogido romántico

Peinados modernos:
• Ondas texturizadas • Trenza boho
• Twisted bun • Messy elegante

Peinados dramáticos:
• Volumen extremo • Rizado definido
• Peinado estructurado • Up-do editorial

---

**💡 INCLUYE EN TODOS LOS PEINADOS:**

✅ Consulta de estilo
✅ Lavado previo (si necesario)
✅ Productos de fijación profesional
✅ Accesorios básicos (invisibles, horquillas)
✅ Retoque gratis si viene antes del evento

**❌ NO INCLUYE:**
- Tocados decorativos (podés traer los tuyos)
- Maquillaje (servicio aparte)
- Traslado (excepto grupos)

---

**📸 PORTFOLIO:**

Tenemos 200+ fotos de peinados que hicimos!
- Instagram: @bellasalon_uy
- Podemos mostrarte en persona
- O enviarte por WhatsApp

**👰 Testimonios de novias:**
"Sofía me hizo el peinado perfecto! Aguantó toda 
la noche impecable" - Valentina

"El equipo vino a casa y nos peinó a 8 amigas. 
Todas quedamos hermosas!" - Lucía

¿Para qué evento necesitás peinado?""",
            "buttons": "peinados_acciones"
        }
    
    # 7) CANCELAR O CAMBIAR TURNO
    cancelar_kw = ["cancelar", "cambiar", "reprogramar", "mover", "modificar", "anular", "suspender"]
    
    if any(k in p for k in cancelar_kw):
        return {
            "content": """📅 **Gestión de Turnos - Cambios y Cancelaciones**

**🔄 CAMBIAR TURNO:**

Para cambiar tu turno necesitamos:
1. Tu nombre completo
2. Día y hora actual del turno
3. Nueva fecha/hora preferida

**Opciones disponibles:**
- Cambiar por teléfono: +598 2908 1234
- WhatsApp: +598 99 123 456
- Personalmente (si estás cerca)
- Por este chat (dame los datos)

---

**❌ CANCELAR TURNO:**

**Política de cancelación:**

✅ **+48 horas antes:** Cancelación sin cargo
✅ **24-48 horas antes:** Sin problemas
⚠️ **Menos de 24hs:** Cargo del 30%
🔴 **Inasistencia:** Cargo del 50%

**¿Por qué cobramos?**
El turno reservado es tiempo que otra clienta 
podría haber usado. Con aviso, podemos ofrecerlo.

**Excepciones** (sin cargo):
- Emergencias médicas (con comprobante)
- Casos de fuerza mayor
- Primera vez que cancelas

---

**⚡ INASISTENCIAS:**

Si no podés venir, AVISÁ aunque sea tarde!
- Nos ayuda a organizarnos
- Podemos ofrecer el turno a lista de espera
- Evitás cargos

**Lista de espera:**
Si cancelás con tiempo, hay gente esperando:
- Turnos de sábado: ¡siempre hay lista!
- Servicios largos: muchos esperando
- Tu cancelación alegra a alguien 😊

---

**📱 FORMAS DE AVISAR:**

1. **WhatsApp** (más rápido): +598 99 123 456
2. **Teléfono**: +598 2908 1234
3. **Instagram DM**: @bellasalon_uy
4. **Email**: turnos@bellasalon.uy
5. **Este chat**: Dame los datos ahora

---

**🎯 CONSEJOS:**

💡 Si no estás segura del turno:
- Reserva "tentativo"
- Confirmá 48hs antes
- No perdés el lugar

💡 Si llegás tarde:
- Avisá lo antes posible
- Podemos esperarte 15min
- Más que eso, reubicamos

💡 Si te sentís mal:
- ¡No vengas enferma!
- Cancelá sin culpa
- Reagendamos sin problema

---

**🔔 RECORDATORIOS AUTOMÁTICOS:**

Te enviamos recordatorios:
- 48hs antes: Confirmación necesaria
- 24hs antes: "Nos vemos mañana!"
- 2hs antes: "Te esperamos!"

Si no podés, avisá en cualquiera de estos!

---

**¿Necesitás cambiar o cancelar un turno?**
Dame estos datos:
- Nombre y apellido
- Fecha y hora del turno actual
- Qué querés hacer (cambiar/cancelar)
- Si es cambio: nueva fecha preferida""",
            "buttons": "turno_gestion"
        }
    
    # 8) OPINIONES Y RESEÑAS
    opinion_kw = ["opinion", "opinión", "reseña", "reseñas", "review", "comentario", "experiencia",
                  "testimonio", "calificacion", "calificación"]
    
    if any(k in p for k in opinion_kw):
        return {
            "content": """⭐ **Reseñas y Testimonios de Clientes**

**CALIFICACIÓN GENERAL: 4.9/5.0** ⭐⭐⭐⭐⭐
Basado en 243 reseñas verificadas

---

**🌟 DESTACADAS DE ESTA SEMANA:**

⭐⭐⭐⭐⭐ **Lucía Rodríguez** - Hace 2 días
"María es una GENIA! Me hizo unas mechas californianas 
hermosas, super naturales. Explica todo re bien y te 
aconseja sin querer venderte de más. El ambiente del 
salón es súper agradable. 100% recomendable!"
**Servicio:** Mechas + Corte | **Estilista:** María

⭐⭐⭐⭐⭐ **Martina Pérez** - Hace 4 días  
"Sofía tiene un ojo increíble. Me cortó el pelo y quedé 
ENAMORADA del resultado! Además me dio consejos para 
cuidarlo. Ya reservé el próximo turno!"
**Servicio:** Corte moderno | **Estilista:** Sofía

⭐⭐⭐⭐⭐ **Carolina Méndez** - Hace 1 semana
"Mi pelo estaba MUERTO después de años de planchita. 
Laura me hizo una keratina y lo revivió! Es una maga. 
Quedó brillante y manejable. Lo recomiendo 100%"
**Servicio:** Keratina + Tratamiento | **Estilista:** Laura

⭐⭐⭐⭐⭐ **Valentina Sosa** - Hace 2 semanas
"Me peinaron para mi casamiento y fue PERFECTO! Sofía 
vino a casa, nos peinó a 8 amigas, todas quedamos 
hermosas. Mi peinado aguantó TODA la noche. Gracias!"
**Servicio:** Peinado novia + grupo | **Estilista:** Sofía

⭐⭐⭐⭐ **Ana Fernández** - Hace 3 semanas
"Muy buen servicio! María me hizo el color perfecto. 
Solo 4 estrellas porque tuve que esperar 15 min, pero 
por el resultado vale la pena. Vuelvo seguro."
**Servicio:** Color completo | **Estilista:** María

---

**📊 ESTADÍSTICAS:**

**Calidad del servicio:** 4.9/5.0
**Profesionalismo:** 4.9/5.0  
**Puntualidad:** 4.7/5.0
**Relación precio/calidad:** 4.8/5.0
**Ambiente del salón:** 4.9/5.0
**Volvería:** 98% SÍ

---

**🎯 LO QUE MÁS VALORAN:**

✅ Calidad del trabajo (97%)
✅ Atención personalizada (94%)
✅ Asesoramiento honesto (92%)
✅ Ambiente agradable (89%)
✅ Productos de calidad (87%)

---

**💬 COMENTARIOS FRECUENTES:**

"Las chicas son super amables"
"Te explican todo antes de hacer"
"Ambiente relajado, nada pretencioso"
"Buenos precios para la calidad"
"Siempre piden tu opinión"

---

**⚠️ ALGUNAS CRÍTICAS (y cómo las manejamos):**

"Tuve que esperar 20 minutos"
→ Implementamos sistema de recordatorios
→ Bloques de tiempo más realistas

"El café podría ser mejor"
→ ¡Cambiamos a café premium! ☕

"Estacionamiento complicado"
→ Convenio con garaje cercano (desc 30%)

---

**🏆 PREMIOS Y RECONOCIMIENTOS:**

🥇 "Mejor Salón Zona Centro" - Guía Salones UY 2024
⭐ Top 10 Montevideo - TripAdvisor 2023
💎 Certificación L'Oréal Professionnel
👍 4.8/5.0 en Google Reviews (180 reseñas)
📱 4.9/5.0 en Facebook (95 reseñas)

---

**📸 ANTES Y DESPUÉS:**

Tenemos 150+ fotos en Instagram:
- Transformaciones de color
- Cortes dramáticos  
- Rescates de pelo dañado
- Peinados de eventos

**Instagram:** @bellasalon_uy

---

**✍️ DEJANOS TU RESEÑA:**

Después de tu visita:
- Google: búscanos como "Bella Salon MVD"
- Facebook: @BellaSalonMontevideo
- Instagram: mencionanos en stories
- Aquí: contanos tu experiencia!

**🎁 INCENTIVO:**
Reseña en Google con foto = $200 descuento próxima visita!

¿Querés ver más reseñas sobre algún servicio específico?""",
            "buttons": "resenas_acciones"
        }
    
    # 9) PRODUCTOS Y VENTA
    producto_kw = ["producto", "productos", "venta", "venden", "comprar", "shampoo", "champú",
                   "acondicionador", "crema", "serum", "óleo", "oleo", "marca"]
    
    if any(k in p for k in producto_kw):
        return {
            "content": """🛍️ **Productos Profesionales a la Venta**

**💎 MARCAS PREMIUM DISPONIBLES:**

**L'ORÉAL PROFESSIONNEL**
El oro del cuidado capilar

🧴 **Serie Expert:**
- Shampoo + Acondicionador: $1.800/set
- Mascarilla reparadora: $950
- Serum brillo absoluto: $1.200
- Spray termoprotector: $850

🌿 **Líneas Específicas:**
- **Absolut Repair** (pelo dañado): $1.800
- **Liss Unlimited** (anti-frizz): $1.650
- **Vitamino Color** (cabello teñido): $1.900
- **Density Advanced** (volumen): $1.700

---

**WELLA PROFESSIONALS**
Innovación alemana

💆‍♀️ **SP System:**
- Luxe Oil (óleo reparador): $1.400
- Hydrate Shampoo: $900
- Smoothen Mask: $1.100

🎨 **Color Fresh:**
- Mascarilla color: $850
- Champú para cabel teñido: $750

---

**KERASTASE**
Lujo francés para tu pelo

✨ **Tratamientos:**
- Elixir Ultime (aceite precioso): $2.200
- Masque Extentioniste: $1.950
- Bain Satin: $1.100

---

**SCHWARZKOPF PROFESSIONAL**
Calidad y efectividad

🔥 **BC Bonacure:**
- Moisture Kick: $850
- Keratin Smooth Perfect: $980
- Color Freeze: $920

---

**🏠 KITS PARA CASA - SUPER VENTAS**

🎁 **Kit Post-Color** - $2.400
- Shampoo protector
- Acondicionador sellante
- Mascarilla nutritiva
- Serum antidesvanecimiento
**Ahorro:** $600

🎁 **Kit Anti-Frizz** - $2.100
- Shampoo disciplinante
- Acondicionador suavizante
- Crema para peinar
- Serum definidor
**Ahorro:** $500

🎁 **Kit Reparación Intensiva** - $2.600
- Shampoo reparador
- Mascarilla reconstructora
- Ampolla tratamiento
- Aceite nutritivo
**Ahorro:** $700

---

**⚡ PRODUCTOS ESTRELLA:**

⭐ **Óleo Reparador Multi-Uso** - $1.400
- Úsalo en seco o húmedo
- Controla frizz
- Da brillo instantáneo
- Protege del calor
**El más vendido!**

⭐ **Mascarilla Bomba Hidratación** - $950
- Uso semanal
- 5 minutos de acción
- Resultados visibles
- Todo tipo de cabello

⭐ **Serum Anti-Quiebre** - $1.200
- Fortalece fibra capilar
- Reduce caída
- Estimula crecimiento
- Sin enjuague

---

**💡 ASESORAMIENTO PERSONALIZADO:**

¿No sabés qué necesita tu pelo?

📋 **Test Capilar Gratis:**
- Analizamos tu cabello
- Detectamos problemas
- Recomendamos productos exactos
- Sin compromiso de compra

**Reservá tu test:** Solo 15 minutos

---

**🎯 PROMOCIONES EN PRODUCTOS:**

💝 **Comprá 2, Llevá 3:** En productos L'Oréal
💝 **15% OFF:** En tu segundo producto
💝 **Puntos:** Cada $1.000 = 100 puntos
💝 **Canje:** 1000 puntos = $200 descuento

---

**📦 ENVÍOS A DOMICILIO:**

- Montevideo: $200
- Interior: $350
- Gratis en compras +$3.000
- Llega en 24-48hs

---

**🎁 GIFT CARDS:**

Tarjetas de regalo desde $1.000
- Válidas por 1 año
- Para servicios o productos
- Se pueden enviar por email

---

**❓ GARANTÍA:**

✅ Productos originales 100%
✅ Devolución si no te gusta (7 días)
✅ Asesoramiento de uso incluido
✅ Vencimientos de +12 meses

---

**📸 CÓMO USAR NUESTROS PRODUCTOS:**

Te enseñamos:
- Rutina de lavado correcta
- Cantidad a usar
- Frecuencia ideal
- Tips profesionales

**Videos tutoriales:** Instagram @bellasalon_uy

¿Qué tipo de producto necesitás?""",
            "buttons": "productos_acciones"
        }
    
    # 10) COVID / MEDIDAS SANITARIAS
    covid_kw = ["covid", "coronavirus", "barbijo", "sanitario", "higiene", "limpieza", "desinfeccion",
                "desinfección", "protocolo", "seguro", "seguridad"]
    
    if any(k in p for k in covid_kw):
        return {
            "content": """🛡️ **Protocolos de Higiene y Seguridad**

**MEDIDAS PERMANENTES:**

✅ **Limpieza Profunda:**
- Desinfección de superficies cada 2 horas
- Esterilización de herramientas después de cada uso
- Lavado completo de capas entre clientes
- Sanitización de sillas y espejos

✅ **Herramientas:**
- Tijeras, peines, cepillos esterilizados
- Toallas individuales de un solo uso
- Cepas descartables cuando es posible
- Productos en envases con dosificador

✅ **Personal:**
- Uniformes limpios diarios
- Lavado frecuente de manos
- Capacitación en higiene constante

✅ **Espacios:**
- Ventilación cruzada permanente
- Aire acondicionado con filtros HEPA
- Dispensers de alcohol gel disponibles
- Baños higienizados cada hora

---

**🔬 PRODUCTOS DE LIMPIEZA:**

Usamos:
- Desinfectantes grado hospitalario
- Alcohol 70% en todo el salón
- Esterilizador UV para herramientas
- Productos aprobados por MSP

---

**👥 DISTANCIAMIENTO:**

- Sillas separadas 1.5 metros
- Turnos espaciados 15 min extra
- Máximo 4 clientes simultáneos
- Sala de espera con capacidad reducida

---

**📋 TU VISITA SEGURA:**

Cuando vengas:
1. Llegá puntual (evitá esperas)
2. Alcohol gel al entrar
3. Bolso en locker individual
4. Pedí cualquier cosa que necesites

---

**⚕️ SI NO TE SENTÍS BIEN:**

Por favor:
- No vengas si tenés síntomas
- Avisanos para reprogramar
- Sin cargo por cancelación
- Cuidamos entre todos

---

**🎯 CERTIFICACIONES:**

✅ Aprobado por MSP
✅ Certificado LATU
✅ Inspecciones mensuales
✅ Todo en regla siempre

**Tu seguridad es nuestra prioridad** 💚

¿Tenés alguna pregunta sobre nuestros protocolos?""",
            "buttons": None
        }
    
    # RESPUESTA DEFAULT
    return {
        "content": """❓ No entendí tu consulta, pero puedo ayudarte con:

**📅 RESERVAS & TURNOS**
• Agendar turno
• Ver disponibilidad
• Cancelar/cambiar turno

**💰 SERVICIOS**
• Cortes y peinados
• Coloración y mechas
• Tratamientos capilares
• Peinados para eventos

**👩‍🦰 INFORMACIÓN**
• Nuestras estilistas
• Precios y promociones
• Ubicación y horarios
• Reseñas de clientes

**Ejemplos de consultas:**
- "Quiero reservar un turno para el sábado"
- "Cuanto sale un corte con brushing"
- "Tienen promociones esta semana"
- "Quién me puede hacer mechas"

¡Preguntame lo que necesites! 💇‍♀️""",
        "buttons": "ayuda"
    }

# Mostrar mensajes
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("show_buttons"):
            button_type = message["show_buttons"]

            if button_type == "inicial":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Reservar turno", key=f"btn_turno_{i}", use_container_width=True):
                        response = get_bot_response("reservar turno")
                        add_message_and_hide_buttons("Quiero reservar un turno", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("💰 Ver servicios", key=f"btn_serv_{i}", use_container_width=True):
                        response = get_bot_response("servicios y precios")
                        add_message_and_hide_buttons("Ver servicios y precios", response["content"], response.get("buttons"))
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("👩‍🦰 Estilistas", key=f"btn_est_{i}", use_container_width=True):
                        response = get_bot_response("estilistas")
                        add_message_and_hide_buttons("Ver estilistas", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🎁 Promociones", key=f"btn_promo_{i}", use_container_width=True):
                        response = get_bot_response("promociones")
                        add_message_and_hide_buttons("Ver promociones", response["content"], response.get("buttons"))
                        st.rerun()

            elif button_type == "servicios_categorias":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✂️ Cortes", key=f"btn_corte_{i}", use_container_width=True):
                        response = get_bot_response("corte")
                        add_message_and_hide_buttons("Ver servicios de corte", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("🎨 Coloración", key=f"btn_color_{i}", use_container_width=True):
                        response = get_bot_response("color")
                        add_message_and_hide_buttons("Ver servicios de color", response["content"], response.get("buttons"))
                        st.rerun()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💆‍♀️ Tratamientos", key=f"btn_trat_{i}", use_container_width=True):
                        response = get_bot_response("tratamientos")
                        add_message_and_hide_buttons("Ver tratamientos", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("💐 Peinados", key=f"btn_pein_{i}", use_container_width=True):
                        response = get_bot_response("peinados eventos")
                        add_message_and_hide_buttons("Ver peinados para eventos", response["content"], response.get("buttons"))
                        st.rerun()

            elif button_type == "ayuda":
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📅 Reservar", key=f"btn_res_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("turno")
                        add_message_and_hide_buttons("Reservar turno", response["content"], response.get("buttons"))
                        st.rerun()

                with col2:
                    if st.button("💰 Precios", key=f"btn_prec_ayuda_{i}", use_container_width=True):
                        response = get_bot_response("precios")
                        add_message_and_hide_buttons("Ver precios", response["content"], response.get("buttons"))
                        st.rerun()

# Ejemplos
st.markdown("---")
st.markdown("**💬 Ejemplos de consultas:**")
col1, col2 = st.columns(2)
with col1:
    st.caption("• Quiero reservar para el sábado")
    st.caption("• Cuánto sale un corte con brushing")
    st.caption("• Tienen promociones esta semana")
    st.caption("• Quiero hacerme mechas californianas")
    st.caption("• Necesito peinado para casamiento")
with col2:
    st.caption("• Quién es la mejor para coloración")
    st.caption("• Dónde queda el salón")
    st.caption("• Venden productos para casa")
    st.caption("• Qué opinan otras clientas")
    st.caption("• Necesito tratamiento para pelo dañado")

# Input
if prompt := st.chat_input("Escribí tu consulta..."):
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

# Footer
st.divider()
st.caption("💡 **Demo interactivo.** Datos de ejemplo de un salón real.")
st.caption("🔌 En producción conecta con tu agenda, CRM y sistema de pagos.")

# Reset
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🔄 Reiniciar"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": """¡Hola! Soy tu asistente virtual del salón 💇‍♀️

Puedo ayudarte con:
- 📅 Reservar turnos
- 💰 Consultar servicios y precios
- 👨‍🦱 Ver estilistas disponibles
- ⭐ Promociones vigentes
- 🎁 Paquetes especiales

¿Qué necesitas hoy?""",
                "show_buttons": "inicial"
            }
        ]
        st.session_state.button_clicked = False
        st.session_state.bonus_shown = False
        st.rerun()
