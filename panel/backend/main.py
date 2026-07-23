"""SIVO Web — Backend de la demo online.

Deploy en Render (o Railway):
  1. Subí esta carpeta `backend/` a un repo.
  2. En Render: New Web Service -> ese repo.
     Build:  pip install -r requirements.txt
     Start:  uvicorn main:app --host 0.0.0.0 --port $PORT
  3. En Environment agregá:
     ANTHROPIC_API_KEY = tu key de console.anthropic.com
     (opcional) SIVO_MODELO = claude-sonnet-4-6
  4. Copiá la URL del servicio y pegala en config.js de la web (API_URL).

La key NUNCA va en el código ni en git: vive solo en la variable de entorno.
Poné un límite de gasto a la key desde la consola de Anthropic.
"""

import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="SIVO API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # en producción: tu dominio de GitHub Pages
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

MODELO = os.environ.get("SIVO_MODELO", "claude-sonnet-4-6")
MAX_TOKENS = int(os.environ.get("SIVO_MAX_TOKENS", "2000"))

SYSTEM_PROMPT = (
    "Sos SIVO AI, el asistente inteligente de la plataforma SIVO. "
    "Asistís únicamente en tareas laborales de automatización, programación y "
    "productividad (Python, Playwright, SQL, Excel, HTML, APIs, compras, stock, "
    "inventario, laboratorio, correos laborales). "
    "Si piden algo fuera de ese alcance respondé únicamente: "
    "\"SIVO fue diseñada exclusivamente para asistir en tareas laborales.\" "
    "Si solo saludan, respondé únicamente: \"Soy SIVO, ¿en qué puedo ayudarte?\" "
    "No saludes, no hagas introducciones, entregá directamente la solución. "
    "Cuando generes código, devolvé el archivo completo listo para ejecutar."
)


class Consulta(BaseModel):
    mensaje: str


@app.get("/")
def salud():
    return {"servicio": "SIVO API", "ok": True}


@app.post("/consultar")
def consultar(c: Consulta):
    if not c.mensaje or not c.mensaje.strip():
        raise HTTPException(400, "Mensaje vacío")

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        raise HTTPException(500, "ANTHROPIC_API_KEY no configurada en el servidor")

    try:
        import anthropic
        cliente = anthropic.Anthropic(api_key=api_key)
        r = cliente.messages.create(
            model=MODELO,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": c.mensaje.strip()[:8000]}],
        )
        texto = "".join(b.text for b in r.content if b.type == "text")
        return {"ok": True, "texto": texto}
    except anthropic.APIStatusError as e:
        raise HTTPException(502, f"Error del servicio de IA: {e.status_code}")
    except Exception as e:
        raise HTTPException(500, f"Error interno: {e}")
