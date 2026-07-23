# SIVO Web

La misma interfaz de SIVO Enterprise, adaptada para correr online.

## Qué funciona online
- Chat con IA (modo demo con respuestas simuladas hasta conectar la API)
- Agentes y comandos (/python, /sql, /html, ...)
- Historial, Favoritos y Biblioteca (se guardan en el navegador del visitante)
- Crear automatizaciones con plantillas (la ejecución de scripts es solo de la versión instalada)
- Registro de usuarios de WhatsApp (local del navegador)

## Publicado en GitHub Pages
Este panel vive en la carpeta `panel/` del repo `gvelazcamp/SIVO`
(GitHub Pages ya está activo en ese repo, sirviendo desde `main` / raíz).
URL: https://gvelazcamp.github.io/SIVO/panel/

## Conectar la API (cuando quieras que responda de verdad)
1. Subí la carpeta `backend/` a un repo (puede ser otro).
2. En Render: New Web Service sobre ese repo.
   - Build:  pip install -r requirements.txt
   - Start:  uvicorn main:app --host 0.0.0.0 --port $PORT
3. Variables de entorno del servicio:
   - ANTHROPIC_API_KEY = tu key de console.anthropic.com
4. Poné un límite de gasto a esa key desde la consola de Anthropic.
5. Copiá la URL del servicio (ej: https://sivo-api.onrender.com)
   y pegala en `config.js` -> API_URL. Subí el cambio. Fin.

IMPORTANTE: la API key nunca va en el código ni en git. Solo en la
variable de entorno del servidor.
