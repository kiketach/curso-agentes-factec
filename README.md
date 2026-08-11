# Construye tu primer agente de IA: de la idea a un asistente funcional

**Curso oficial de la Séptima Escuela de Temporada FACTEC 2026 · Facultad Tecnológica, Universidad de Santiago de Chile (USACH)**

🌐 **Sitio del curso:** https://kiketach.github.io/curso-agentes-factec/
👤 **Relator:** [Enrique Abril Contreras](https://www.linkedin.com/in/enrique-abril-contreras) — AI Engineer & Software Architect
📅 **Agosto 2026** · 6 sesiones en vivo · **51 participantes inscritos**

---

## 🎯 La misión

La mayoría de los cursos de IA enseñan a *usar* un chatbot. Este enseña a **construir**: en 6 sesiones prácticas, profesionales sin experiencia en programación ven nacer un **agente de IA real, pieza por pieza** — desde la primera instrucción hasta un asistente que razona, ejecuta acciones y se conecta con herramientas del mundo real.

> La brecha ya no es de acceso a la tecnología — es de **criterio para construir con ella**.

## 📚 El programa (12 horas · 6 sesiones)

| # | Sesión | Qué se construye |
|---|--------|------------------|
| 1 | **El nuevo paradigma: programar con IA** | Demo en vivo: una app funcional desde un prompt en lenguaje natural |
| 2 | **Claude Code como copiloto** | Cada participante automatiza una tarea real de su trabajo |
| 3 | **Anatomía de un agente** | Primer agente conversacional en Python (modelo + instrucciones + memoria) |
| 4 | **Dale manos a tu agente** | Herramientas propias: el agente deja de inventar y consulta datos reales |
| 5 | **MCP: conecta tu agente al mundo** | Conexión a servidores MCP: capacidades nuevas sin escribir integraciones |
| 6 | **Tu agente funcional + qué sigue** | Integración, límites de autonomía, seguridad y costos |

**Modalidad:** 100% online sincrónico · 19:00–21:00 (hora de Chile)

## 🧭 Decisiones de diseño instruccional

- **Demo-led:** cada concepto se construye **en vivo**, incluso cuando algo falla — un error real enseña más que una diapositiva.
- **Dos niveles de participación:** 🟢 *construyo en vivo* (replicas con tu entorno) o 🔵 *observo y diseño*. Ambos certifican; nadie queda fuera por no tener el entorno listo.
- **100% realizable con herramientas gratuitas.** El relator demuestra con herramientas líderes, pero cada paso tiene una vía sin costo (Gemini API, AI Studio, modelos locales). El código del curso es **agnóstico al proveedor**: cambiar de modelo es una línea.
- **Interacción diseñada, no improvisada:** quiz diagnóstico al inicio y de cierre al final (para medir el progreso real del grupo), retos por chat y la audiencia decidiendo los inputs de las demos.

## 🛠️ La ingeniería detrás del curso

Además del contenido, la operación del curso está **automatizada de punta a punta**. Todo construido para este curso:

| Pieza | Cómo funciona |
|---|---|
| **Sitio del curso** | Slides generadas con [Marp](https://marp.app/) (Markdown → HTML) con tema propio; hub estático en GitHub Pages con despliegue por GitHub Actions |
| **Publicación progresiva** | Un script (`publicar.sh N`) copia el deck de la sesión, inyecta la navegación, regenera el índice y despliega — las slides aparecen el día de cada clase |
| **Registro de asistencia** | Formulario con correo verificado + **Apps Script** que cruza las respuestas contra la lista oficial y genera la matriz de asistencia, el % y quién certifica |
| **Apertura/cierre automático** | 12 disparadores programados abren el formulario en los últimos minutos de cada clase y lo cierran después — sin intervención manual |
| **Comunicación** | Los 51 correos de bienvenida enviados como mensajes individuales personalizados vía Apps Script, no como lista oculta |

> El curso enseña a automatizar con IA — y su propia operación es un ejemplo de ello.

## 🗂️ Este repositorio

Contiene el **sitio público** del curso. Las slides de cada sesión se publican progresivamente.

```
├── index.html        # Hub: accesos del curso + estado de las 6 sesiones
├── sesionN.html      # Slides de cada sesión (aparecen al publicarse)
├── gen_index.py      # Regenera el índice según las sesiones publicadas
├── publicar.sh       # Publica una sesión: bash publicar.sh N
└── .github/workflows # Despliegue automático a GitHub Pages
```

**Stack del sitio:** Marp · HTML/CSS (glassmorphism, responsive, tema claro) · Python · Bash · GitHub Actions.
Las presentaciones se navegan con las flechas del teclado.

---

## 👨‍🏫 Sobre el relator

**Enrique Abril Contreras** — AI Engineer & Software Architect

- **AI Engineer en MimeIA** — sistemas multi-agente en producción para clientes de LATAM.
- **Ex-CTO de Rentoso** — plataforma de agentes sobre Google Cloud (ADK + Vertex AI + Gemini) con **11+ agencias operando** bajo arquitectura multi-tenant.
- **Agentes de voz en tiempo real** sobre Google Cloud (Gemini Live API + Cloud Run).
- **RAG empresarial** sobre documentos corporativos.
- Certificado **Microsoft Azure AI-900** y **DP-900**.

> *"La IA no se aprende viéndola — se aprende construyendo un agente que trabaje para ti."*

📧 [LinkedIn](https://www.linkedin.com/in/enrique-abril-contreras) · 🌐 [Fyllu](https://fyllu.net)

---

*Séptima Escuela de Temporada FACTEC 2026 — iniciativa de vinculación con el medio de la [Facultad Tecnológica de la USACH](https://www.usach.cl/facultad-tecnologica).*
