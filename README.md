# Construye tu primer agente de IA: de la idea a un asistente funcional

**Curso oficial de la Séptima Escuela de Temporada FACTEC 2026 · Facultad Tecnológica, Universidad de Santiago de Chile (USACH)**

🌐 **Sitio del curso:** https://kiketach.github.io/curso-agentes-factec/

---

## 🎯 La misión

La mayoría de los cursos de IA enseñan a *usar* un chatbot. Este curso enseña a **construir**: en 6 sesiones prácticas, personas sin experiencia en programación ven nacer un **agente de IA real, pieza por pieza** — desde la primera instrucción hasta un asistente que razona, ejecuta acciones y se conecta con herramientas del mundo real.

La brecha ya no es de acceso a la tecnología — es de **criterio para construir con ella**. Este curso cierra esa brecha con un principio simple: *nadie sale sabiendo "de" agentes; sale habiendo visto construir el suyo.*

## 📚 El programa (12 horas · 6 sesiones en vivo)

| # | Sesión | Fecha |
|---|--------|-------|
| 1 | **El nuevo paradigma: programar con IA** — qué es un AI Engineer; demo en vivo de desarrollo asistido por IA (Claude Code); preparación del entorno | Mar 18 ago |
| 2 | **Claude Code como copiloto** — automatizar una tarea real del trabajo de cada participante | Mié 19 ago |
| 3 | **Anatomía de un agente** — modelo + instrucciones + memoria; el ciclo razonar-actuar; primer agente en Python | Jue 20 ago |
| 4 | **Dale manos a tu agente** — function calling: herramientas propias que consultan datos y ejecutan acciones | Mar 25 ago |
| 5 | **MCP: conecta tu agente al mundo** — el estándar Model Context Protocol en vivo | Mié 26 ago |
| 6 | **Tu agente funcional + qué sigue** — integración, buenas prácticas (límites, seguridad, costos), demos de participantes | Jue 27 ago |

**Horario:** 19:00–21:00 (hora de Chile continental) · **Modalidad:** 100% online sincrónico

## 🧭 La metodología

- **Demo-led:** cada concepto se construye **en vivo** frente al grupo — nada pregrabado, incluyendo cuando algo falla (que también enseña).
- **Dos niveles de participación:** 🟢 *construyo en vivo* (replicas con tu entorno) o 🔵 *observo y diseño* (sigues las demos y diseñas en papel). Ambos aprenden; nadie se queda atrás.
- **100% realizable con herramientas gratuitas:** el relator demuestra con herramientas líderes, pero cada paso tiene una vía gratuita (Gemini API, Google AI Studio, modelos locales) guiada en clase.
- **Interactivo por diseño:** Kahoot de diagnóstico y cierre, retos por chat, la audiencia decide los inputs de las demos, y demostraciones de los propios participantes en la sesión final.

## 👨‍🏫 El relator

**Enrique Abril Contreras** — AI Engineer & Software Architect ([LinkedIn](https://www.linkedin.com/in/enrique-abril-contreras))

- **AI Engineer en MimeIA** — diseña y opera **sistemas multi-agente en producción** para clientes reales de LATAM (CRM conversacional y automatización sobre WhatsApp).
- **Ex-CTO de Rentoso** — lideró una plataforma de agentes de IA para el sector inmobiliario sobre Google Cloud (ADK + Vertex AI + Gemini), con **más de 11 agencias operando en producción** bajo arquitectura multi-tenant.
- **Constructor de agentes de voz en tiempo real** sobre Google Cloud (Gemini Live API + Cloud Run), en operación real.
- **Especialista en RAG empresarial** — recuperación semántica sobre documentos corporativos para auditoría y gestión del conocimiento.
- Certificado **Microsoft Azure AI Fundamentals (AI-900)** y **Data Fundamentals (DP-900)**.

> *"La IA no se aprende viéndola — se aprende construyendo un agente que trabaje para ti."*

## 🗂️ Este repositorio

Es el **sitio público del curso** (GitHub Pages). Las slides de cada sesión se publican progresivamente el día de la clase.

```
├── index.html        # Hub del curso: accesos + estado de las 6 sesiones
├── sesionN.html      # Slides de cada sesión (aparecen al publicarse)
├── gen_index.py      # Regenera el índice según las sesiones publicadas
└── publicar.sh       # Publica una sesión: bash publicar.sh N
```

Las presentaciones están construidas con [Marp](https://marp.app/) (Markdown → HTML) con un tema propio, y se navegan con las flechas del teclado.

---

*Séptima Escuela de Temporada FACTEC 2026 — una iniciativa de vinculación con el medio de la Facultad Tecnológica de la USACH.*
