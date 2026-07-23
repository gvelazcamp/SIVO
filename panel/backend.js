// ============================================================
// SIVO Web — backend.js
// Imita el puente Python (window.pywebview.api) en el navegador.
// Datos locales -> localStorage. Chat/generación -> API_URL (o demo).
// El index.html NO se modifica: es el mismo de la app de escritorio.
// ============================================================

(function () {
  const CFG = window.SIVO_CONFIG || { API_URL: "", DEMO_LIMITE_MENSAJES: 10 };

  // ---------------- almacenamiento ----------------
  const DB = {
    leer(k, def) {
      try { return JSON.parse(localStorage.getItem("sivo_" + k)) ?? def; }
      catch { return def; }
    },
    escribir(k, v) { localStorage.setItem("sivo_" + k, JSON.stringify(v)); }
  };
  const uid = () => Math.random().toString(16).slice(2, 14);
  const ahora = () => new Date().toISOString().slice(0, 19);

  // ---------------- agentes (mismos de la app) ----------------
  const AGENTES_BASE = [
    { id:"general", nombre:"SIVO", icono:"💬", comando:"/sivo", prompt:"", descripcion:"Asistente general de automatización." },
    { id:"python", nombre:"Python Expert", icono:"🐍", comando:"/python",
      prompt:"Actuá como desarrollador Python senior. Entregá código completo, listo para ejecutar, con buenas prácticas. Sin explicaciones de más.",
      descripcion:"Scripts, automatización y desarrollo en Python." },
    { id:"html", nombre:"HTML Expert", icono:"🌐", comando:"/html",
      prompt:"Actuá como desarrollador front-end. Entregá HTML/CSS/JS completo en un solo archivo, moderno y responsivo. Devolvé el archivo entero.",
      descripcion:"Páginas, componentes y diseño web." },
    { id:"sql", nombre:"SQL Expert", icono:"🗄", comando:"/sql",
      prompt:"Actuá como experto en bases de datos. Entregá consultas SQL claras, optimizadas y comentadas.",
      descripcion:"Consultas, esquemas y optimización de bases de datos." },
    { id:"excel", nombre:"Excel Expert", icono:"📊", comando:"/excel",
      prompt:"Actuá como analista de datos experto en Excel. Entregá fórmulas, macros o pasos concretos, listos para aplicar.",
      descripcion:"Fórmulas, macros y análisis de planillas." },
    { id:"mail", nombre:"Redactor", icono:"✉", comando:"/mail",
      prompt:"Actuá como redactor profesional de correos laborales. Entregá el correo listo para enviar, con asunto y cuerpo.",
      descripcion:"Redacción de correos y comunicaciones laborales." },
    { id:"playwright", nombre:"Automatización Web", icono:"⚡", comando:"/playwright",
      prompt:"Actuá como experto en automatización con Playwright en Python. Entregá scripts completos y robustos.",
      descripcion:"Automatización de navegador con Playwright/Selenium." },
    { id:"laboratorio", nombre:"Laboratorio", icono:"🧪", comando:"/lab",
      prompt:"Actuá como asistente de gestión de laboratorio clínico. Enfocate en stock de reactivos, inventario y procesos.",
      descripcion:"Gestión de reactivos, stock e inventario de laboratorio." },
    { id:"compras", nombre:"Compras", icono:"📦", comando:"/compras",
      prompt:"Actuá como analista de compras y abastecimiento. Enfocate en pedidos, proveedores y planificación.",
      descripcion:"Pedidos, proveedores y planificación de compras." }
  ];

  const PLANTILLAS = [
    { id:"python", nombre:"Python", icono:"🐍", categoria:"python",
      prompt:"Generá un script Python completo y listo para ejecutar que haga lo siguiente. Devolvé ÚNICAMENTE el código:\n\n" },
    { id:"playwright", nombre:"Playwright", icono:"🌐", categoria:"playwright",
      prompt:"Generá un script Python con Playwright completo y robusto que haga lo siguiente. Devolvé ÚNICAMENTE el código:\n\n" },
    { id:"excel", nombre:"Excel", icono:"📊", categoria:"excel",
      prompt:"Generá un script Python con openpyxl que haga lo siguiente sobre archivos Excel. Devolvé ÚNICAMENTE el código:\n\n" },
    { id:"sql", nombre:"SQL", icono:"🗄", categoria:"sql",
      prompt:"Generá un script Python con sqlite3 para lo siguiente. Devolvé ÚNICAMENTE el código:\n\n" },
    { id:"html", nombre:"HTML", icono:"🌍", categoria:"html",
      prompt:"Generá un script Python que cree un archivo HTML completo según lo siguiente. Devolvé ÚNICAMENTE el código:\n\n" },
    { id:"correo", nombre:"Outlook/Correo", icono:"📧", categoria:"correo",
      prompt:"Generá un script Python que redacte o procese correos según lo siguiente. Devolvé ÚNICAMENTE el código:\n\n" }
  ];

  const CATS_AUTOS = [
    { id:"python", nombre:"Python", icono:"🐍" },
    { id:"playwright", nombre:"Playwright", icono:"🌐" },
    { id:"excel", nombre:"Excel", icono:"📊" },
    { id:"sql", nombre:"SQL", icono:"🗄" },
    { id:"html", nombre:"HTML", icono:"🌍" },
    { id:"correo", nombre:"Outlook/Correo", icono:"📧" },
    { id:"web", nombre:"Automatizaciones Web", icono:"⚡" }
  ];

  const CATS_BIBLIO = [
    { id:"python", nombre:"Python", icono:"🐍" },
    { id:"sql", nombre:"SQL", icono:"🗄" },
    { id:"html", nombre:"HTML", icono:"🌐" },
    { id:"excel", nombre:"Excel", icono:"📊" },
    { id:"playwright", nombre:"Playwright", icono:"⚡" },
    { id:"automatizaciones", nombre:"Automatizaciones", icono:"🔧" },
    { id:"prompts", nombre:"Prompts", icono:"💡" },
    { id:"otros", nombre:"Otros", icono:"📁" }
  ];

  let agenteActivoId = null;

  function agentesConCustom() {
    const custom = DB.leer("agentes_custom", {});
    return AGENTES_BASE.map(a => ({ ...a, ...(custom[a.id] || {}) }));
  }

  function detectarComando(msg) {
    if (!msg.startsWith("/")) return [null, msg];
    const [cmd, ...resto] = msg.split(/\s+/);
    const ag = agentesConCustom().find(a => a.comando === cmd.toLowerCase());
    return ag ? [ag, resto.join(" ")] : [null, msg];
  }

  function limpiarCodigo(t) {
    t = (t || "").trim();
    if (t.startsWith("```")) {
      const i = t.indexOf("\n");
      if (i !== -1) t = t.slice(i + 1);
      if (t.trimEnd().endsWith("```")) t = t.trimEnd().slice(0, -3);
    }
    return t.trim();
  }

  // ---------------- llamada a la IA (API o demo) ----------------
  async function llamarIA(mensaje) {
    if (CFG.API_URL) {
      const resp = await fetch(CFG.API_URL.replace(/\/$/, "") + "/consultar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensaje })
      });
      if (!resp.ok) throw new Error("El servicio no está disponible (" + resp.status + ")");
      const data = await resp.json();
      return data.texto || "(sin respuesta)";
    }

    // --- modo demo ---
    const usados = DB.leer("demo_usados", 0);
    if (usados >= CFG.DEMO_LIMITE_MENSAJES) {
      return "Alcanzaste el límite de la demo. Para uso completo, contactanos y llevá SIVO a tu negocio: contacto@sivoia.store";
    }
    DB.escribir("demo_usados", usados + 1);
    await new Promise(r => setTimeout(r, 1400));
    return "🔧 DEMO — Esta es una respuesta de prueba de SIVO Web.\n\n" +
           "Recibí tu consulta: \u201C" + mensaje.slice(0, 120) + "\u201D\n\n" +
           "En la versión completa, acá va la respuesta real de la IA con la solución lista para usar. " +
           "Quedan " + (CFG.DEMO_LIMITE_MENSAJES - usados - 1) + " mensajes de demo.";
  }

  // ---------------- API que la UI espera ----------------
  const api = {

    // ---- adjuntos (en web: solo informativo) ----
    elegir_archivo: async () => {
      return new Promise(res => {
        const inp = document.createElement("input");
        inp.type = "file";
        inp.onchange = () => res(inp.files[0] ? { ok: true, nombre: inp.files[0].name } : { ok: false });
        inp.click();
      });
    },
    quitar_archivo: async () => ({ ok: true }),

    // ---- chat ----
    enviar: async (mensaje) => {
      (async () => {
        const t0 = Date.now();
        try {
          window.setEstado?.("🟡 Analizando...", "#e5b567");
          window.setProgreso?.("Analizando solicitud...", 15);

          let [ag, resto] = detectarComando(mensaje);
          if (!ag && agenteActivoId) ag = agentesConCustom().find(a => a.id === agenteActivoId);
          const final = ag && ag.prompt ? ag.prompt + "\n\n" + resto : (ag ? resto : mensaje);

          if (ag && ag.id !== agenteActivoId) {
            agenteActivoId = ag.id;
            window.setAgenteActivo?.(ag.id, ag.nombre);
          }

          window.setEstado?.("🟠 Generando solución...", "#e58a4e");
          window.setProgreso?.("Construyendo solución...", 60);

          const texto = await llamarIA(final);
          const dur = Math.round((Date.now() - t0) / 1000);
          const hora = new Date().toTimeString().slice(0, 5);

          // guardar en historial local
          const hist = DB.leer("historial", []);
          hist.unshift({ id: uid(), fecha: ahora(), pregunta: ag ? resto : mensaje,
                         respuesta: texto, duracion: dur, proveedor: CFG.API_URL ? "api" : "demo",
                         contexto: ag ? { agente: ag.id } : {} });
          DB.escribir("historial", hist.slice(0, 500));

          window.setMeta?.("Tiempo: " + dur + " s", "Última ejecución: " + hora);
          window.agregarRespuesta?.(texto, "IA: SIVO Engine · Tiempo: " + dur + " s · " + hora);
        } catch (e) {
          window.agregarRespuesta?.("Ocurrió un error: " + e.message, "");
        } finally {
          window.setProgreso?.("", 100);
          window.setEstado?.("🟢 IA lista", "#4caf50");
        }
      })();
      return { ok: true };
    },

    // ---- historial ----
    historial_listar: async (filtro) => {
      let items = DB.leer("historial", []);
      if (filtro && filtro.trim()) {
        const t = filtro.toLowerCase();
        items = items.filter(i => (i.pregunta || "").toLowerCase().includes(t) ||
                                  (i.respuesta || "").toLowerCase().includes(t));
      }
      return { ok: true, items, favoritos: DB.leer("favoritos", []).map(f => f.id) };
    },
    historial_limpiar: async () => { DB.escribir("historial", []); return { ok: true }; },
    historial_eliminar: async (id) => {
      DB.escribir("historial", DB.leer("historial", []).filter(i => i.id !== id));
      return { ok: true };
    },
    estadisticas: async () => {
      const h = DB.leer("historial", []);
      const hoy = new Date().toISOString().slice(0, 10);
      return { ok: true, stats: { total: h.length,
        hoy: h.filter(i => (i.fecha || "").startsWith(hoy)).length,
        favoritos: DB.leer("favoritos", []).length } };
    },

    // ---- favoritos ----
    favoritos_listar: async () => ({ ok: true, items: DB.leer("favoritos", []) }),
    favoritos_alternar: async (id) => {
      let favs = DB.leer("favoritos", []);
      const ya = favs.some(f => f.id === id);
      if (ya) favs = favs.filter(f => f.id !== id);
      else {
        const item = DB.leer("historial", []).find(i => i.id === id);
        if (item) favs.unshift({ ...item, marcado: ahora() });
      }
      DB.escribir("favoritos", favs);
      return { ok: true, items: favs, marcado: !ya };
    },

    // ---- agentes ----
    agentes_listar: async () => ({ ok: true, agentes: agentesConCustom(), activo: agenteActivoId }),
    agente_seleccionar: async (id) => {
      agenteActivoId = (!id || id === "general") ? null : id;
      const a = agenteActivoId ? agentesConCustom().find(x => x.id === agenteActivoId) : null;
      return { ok: true, activo: agenteActivoId, nombre: a ? a.nombre : "SIVO" };
    },
    agente_editar_prompt: async (id, prompt) => {
      const c = DB.leer("agentes_custom", {});
      c[id] = { ...(c[id] || {}), prompt };
      DB.escribir("agentes_custom", c);
      return { ok: true, agente: agentesConCustom().find(a => a.id === id) };
    },
    agente_restaurar: async (id) => {
      const c = DB.leer("agentes_custom", {});
      delete c[id];
      DB.escribir("agentes_custom", c);
      return { ok: true, agente: agentesConCustom().find(a => a.id === id) };
    },

    // ---- biblioteca ----
    biblioteca_categorias: async () => {
      const conteo = {};
      DB.leer("biblioteca", []).forEach(i => { conteo[i.categoria] = (conteo[i.categoria] || 0) + 1; });
      return { ok: true, categorias: CATS_BIBLIO, conteo };
    },
    biblioteca_listar: async (categoria, filtro) => {
      let items = DB.leer("biblioteca", []);
      if (categoria && categoria !== "todas") items = items.filter(i => i.categoria === categoria);
      if (filtro && filtro.trim()) {
        const t = filtro.toLowerCase();
        items = items.filter(i => (i.titulo || "").toLowerCase().includes(t) ||
                                  (i.pregunta || "").toLowerCase().includes(t) ||
                                  (i.respuesta || "").toLowerCase().includes(t));
      }
      return { ok: true, items };
    },
    biblioteca_guardar: async (id, categoria) => {
      const item = DB.leer("historial", []).find(i => i.id === id);
      if (!item) return { ok: false, error: "No encontré ese elemento." };
      const b = DB.leer("biblioteca", []);
      if (!b.some(x => x.id === id)) {
        b.unshift({ ...item, categoria, titulo: (item.pregunta || "").slice(0, 60),
                    guardado: ahora() });
        DB.escribir("biblioteca", b);
      }
      return { ok: true };
    },
    biblioteca_eliminar: async (id) => {
      DB.escribir("biblioteca", DB.leer("biblioteca", []).filter(i => i.id !== id));
      return { ok: true };
    },

    // ---- automatizaciones ----
    autos_listar: async (categoria, filtro) => {
      let items = DB.leer("autos", []);
      if (categoria && categoria !== "todas") items = items.filter(a => a.categoria === categoria);
      if (filtro && filtro.trim()) {
        const t = filtro.toLowerCase();
        items = items.filter(a => (a.nombre || "").toLowerCase().includes(t) ||
                                  (a.descripcion || "").toLowerCase().includes(t) ||
                                  (a.categoria || "").toLowerCase().includes(t));
      }
      const conteo = {};
      DB.leer("autos", []).forEach(a => { conteo[a.categoria] = (conteo[a.categoria] || 0) + 1; });
      return { ok: true, items, categorias: CATS_AUTOS, conteo };
    },
    autos_obtener: async (id) => {
      const a = DB.leer("autos", []).find(x => x.id === id);
      return { ok: !!a, auto: a };
    },
    autos_plantillas: async () => ({ ok: true, plantillas: PLANTILLAS }),
    autos_generar: async (plantillaId, descripcion) => {
      (async () => {
        try {
          window.setEstado?.("🟠 Generando automatización...", "#e58a4e");
          const p = PLANTILLAS.find(x => x.id === plantillaId);
          const codigo = limpiarCodigo(await llamarIA(p.prompt + descripcion));
          window.autoGenerada?.({ ok: true, codigo, categoria: p.categoria });
        } catch (e) {
          window.autoGenerada?.({ ok: false, error: e.message });
        } finally {
          window.setEstado?.("🟢 IA lista", "#4caf50");
        }
      })();
      return { ok: true };
    },
    autos_crear: async (nombre, descripcion, categoria, script) => {
      if (!nombre.trim()) return { ok: false, error: "El nombre es obligatorio." };
      const items = DB.leer("autos", []);
      const auto = { id: uid(), nombre: nombre.trim(), descripcion: (descripcion || "").trim(),
                     categoria: categoria || "python", script, activa: true,
                     creada: ahora(), ejecuciones: 0, ultima_ejecucion: null };
      items.unshift(auto);
      DB.escribir("autos", items);
      return { ok: true, auto };
    },
    autos_editar: async (id, nombre, descripcion, categoria, script, activa) => {
      const items = DB.leer("autos", []);
      const a = items.find(x => x.id === id);
      if (!a) return { ok: false, error: "No encontré esa automatización." };
      if (nombre) a.nombre = nombre;
      a.descripcion = descripcion ?? a.descripcion;
      a.categoria = categoria ?? a.categoria;
      if (script && script.trim()) a.script = script;
      a.activa = !!activa;
      DB.escribir("autos", items);
      return { ok: true, auto: a };
    },
    autos_duplicar: async (id) => {
      const a = DB.leer("autos", []).find(x => x.id === id);
      if (!a) return { ok: false, error: "No encontré esa automatización." };
      return api.autos_crear(a.nombre + " (copia)", a.descripcion, a.categoria, a.script);
    },
    autos_eliminar: async (id) => {
      DB.escribir("autos", DB.leer("autos", []).filter(a => a.id !== id));
      return { ok: true };
    },
    autos_ejecutar: async (id) => {
      setTimeout(() => {
        window.autoEjecutada?.(id, {
          ok: false, salida: "",
          error: "La ejecución de scripts corre en tu PC y está disponible en la " +
                 "versión instalada de SIVO. Esta demo online permite crear, editar " +
                 "y organizar automatizaciones, pero no ejecutarlas."
        });
      }, 600);
      return { ok: true };
    },

    // ---- usuarios ----
    listar_usuarios: async () => ({ ok: true, usuarios: DB.leer("usuarios", []) }),
    registrar_usuario: async (nombre, whatsapp) => {
      nombre = (nombre || "").trim();
      whatsapp = (whatsapp || "").replace(/\D/g, "");
      if (!nombre || !whatsapp) return { ok: false, error: "Nombre y WhatsApp son obligatorios." };
      const us = DB.leer("usuarios", []);
      if (us.some(u => u.whatsapp === whatsapp)) return { ok: false, error: "Ese número ya está registrado." };
      us.push({ nombre, whatsapp, rol: "cliente" });
      DB.escribir("usuarios", us);
      return { ok: true, usuarios: us };
    },
    eliminar_usuario: async (whatsapp) => {
      const us = DB.leer("usuarios", []).filter(u => u.whatsapp !== whatsapp);
      DB.escribir("usuarios", us);
      return { ok: true, usuarios: us };
    }
  };

  window.pywebview = { api };
})();
