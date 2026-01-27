# =========================
# RESPUESTAS DEL CHATBOT
# =========================

CHATBOT_RESPONSES = {
    'hola': '¡Hola! 👋 Bienvenido a MercadoBot. ¿En qué puedo ayudarte?<br><br>Podés preguntarme sobre:<br>• Precios y planes<br>• Integraciones<br>• Cómo funciona<br>• Agendar demo',
    
    'precio': 'Nuestros planes:<br><br>💰 <strong>Básico:</strong> $25.000/mes<br>• Hasta 1.000 consultas/mes<br>• 1 asistente<br>• Soporte email<br><br>💎 <strong>Pro:</strong> $50.000/mes<br>• Hasta 5.000 consultas/mes<br>• 3 asistentes<br>• Soporte prioritario<br><br>🚀 <strong>Enterprise:</strong> Personalizado<br>• Consultas ilimitadas<br>• Asistentes ilimitados<br>• Soporte dedicado<br><br>Todos incluyen 7 días de prueba gratis! ✨',
    
    'costo': 'Nuestros planes:<br><br>💰 <strong>Básico:</strong> $25.000/mes<br>💎 <strong>Pro:</strong> $50.000/mes<br>🚀 <strong>Enterprise:</strong> Personalizado<br><br>¿Querés que te cuente más detalles de algún plan?',
    
    'cuanto': 'El plan <strong>Básico</strong> arranca en $25.000/mes con 7 días de prueba gratuita. ¿Querés conocer todos los planes?',
    
    'whatsapp': '¡Sí! Nuestro chatbot se integra con:<br><br>✅ WhatsApp<br>✅ Instagram<br>✅ Web<br>✅ Shopify<br>✅ Mercado Pago<br>✅ Email<br><br>¿Cuál te interesa más?',
    
    'integra': 'Integramos con WhatsApp, Instagram, tu sitio web, Shopify, Mercado Pago, Email y más plataformas. ¿Qué plataforma usás actualmente?',
    
    'instagram': '¡Sí! Conectamos tu chatbot con Instagram Direct. Responde automáticamente mensajes y comentarios 24/7. ¿Querés ver cómo funciona?',
    
    'funciona': 'Es súper simple en 3 pasos:<br><br>🔌 <strong>1. Conectás</strong><br>Vinculás tus datos, productos o servicios<br><br>🧠 <strong>2. Entrenás</strong><br>El asistente aprende sobre tu negocio<br><br>🚀 <strong>3. Lanzás</strong><br>Lo instalamos y empieza a atender clientes<br><br>¿Querés agendar una demo?',
    
    'demo': '¡Perfecto! Para agendar tu demo gratuita:<br><br>📧 Escribinos a: <strong>hola@mercadobot.com</strong><br>💬 O dejame tu email y te contactamos en 24hs<br><br>¿Cuál preferís?',
    
    'contacto': 'Podés contactarnos por:<br><br>📧 <strong>Email:</strong> hola@mercadobot.com<br>💬 <strong>Chat:</strong> Estás hablando conmigo! 😊<br><br>Respondemos en menos de 24hs.',
    
    'gratis': '¡Sí! Tenés <strong>7 días de prueba GRATIS</strong>:<br><br>✅ Sin tarjeta de crédito<br>✅ Acceso completo<br>✅ Sin compromisos<br>✅ Cancelás cuando quieras<br><br>¿Empezamos?',
    
    'cancelar': 'Podés cancelar cuando quieras:<br><br>✅ Sin permanencia<br>✅ Sin penalizaciones<br>✅ Simple y rápido<br><br>Somos 100% transparentes 💯',
    
    'programa': '¡NO necesitás saber programar! 🎉<br><br>Nosotros configuramos todo:<br>• Instalación completa<br>• Entrenamiento del bot<br>• Integración con tus sistemas<br>• Soporte continuo<br><br>Vos solo nos pasás tu info y listo!',
    
    'tiempo': 'Tiempos de implementación:<br><br>⚡ <strong>Casos simples:</strong> 2-3 días<br>Chatbot básico con info estándar<br><br>🔧 <strong>Integraciones complejas:</strong> 1-2 semanas<br>Múltiples sistemas, datos complejos<br><br>Te damos un timeline claro desde el inicio 📅',
    
    'seguro': 'Tu información está 100% protegida:<br><br>🔒 Encriptación de datos<br>✅ Cumplimos normativas de protección<br>🛡️ Servidores seguros<br>🔐 Acceso restringido<br><br>Tanto tus datos como los de tus clientes están seguros 💯',
    
    'dato': 'Toda la información está encriptada y protegida con los más altos estándares de seguridad. Cumplimos con GDPR y todas las normativas locales. 🔒',
    
    'buenos': '¡Hola! 👋 ¿En qué puedo ayudarte hoy?',
    
    'buenos dias': '¡Buenos días! ☀️ ¿Cómo puedo ayudarte?',
    
    'buenas': '¡Buenas! 👋 ¿Qué te gustaría saber sobre MercadoBot?',
    
    'ayuda': 'Claro! Puedo ayudarte con:<br><br>💰 Precios y planes<br>🔌 Integraciones (WhatsApp, Web, etc)<br>⚙️ Cómo funciona<br>📅 Agendar demo<br>🎁 Prueba gratis<br><br>¿Qué te interesa?',
    
    'gracias': '¡De nada! 😊 ¿Te ayudo con algo más?',
    
    'chau': '¡Hasta pronto! 👋 Si tenés más dudas, acá estoy 24/7 😊',
    
    'adios': '¡Nos vemos! Si necesitás algo más, escribime cuando quieras 💬',
    
    'default': 'Hmm, no tengo info específica sobre eso 🤔<br><br>Pero puedo ayudarte con:<br>• Precios<br>• Integraciones<br>• Cómo funciona<br>• Agendar demo<br><br>O escribinos a <strong>hola@mercadobot.com</strong> para consultas específicas.'
}


def get_chatbot_response(message):
    """
    Busca una respuesta basada en keywords en el mensaje.
    
    Args:
        message (str): Mensaje del usuario
        
    Returns:
        str: Respuesta del bot en HTML
    """
    message_lower = message.lower()
    
    # Buscar keywords en el mensaje
    for keyword, response in CHATBOT_RESPONSES.items():
        if keyword in message_lower:
            return response
    
    # Si no encuentra nada, devolver respuesta por defecto
    return CHATBOT_RESPONSES['default']
