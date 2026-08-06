# Genera index.html del sitio del curso según qué sesiones estén publicadas.
# Una sesión está "publicada" si existe sesionN.html en esta carpeta.
import os

SESIONES = [
    (1, "El nuevo paradigma: programar con IA", "Martes 18 de agosto"),
    (2, "Claude Code como copiloto", "Miércoles 19 de agosto"),
    (3, "Anatomía de un agente", "Jueves 20 de agosto"),
    (4, "Dale manos a tu agente: herramientas (tools)", "Martes 25 de agosto"),
    (5, "MCP: conecta tu agente al mundo", "Miércoles 26 de agosto"),
    (6, "Tu agente funcional + qué sigue", "Jueves 27 de agosto"),
]

items = []
for n, titulo, fecha in SESIONES:
    pub = os.path.exists(f"sesion{n}.html")
    if pub:
        items.append(f'''
      <a class="card item pub" href="sesion{n}.html">
        <div class="num">{n}</div>
        <div class="tx"><b>{titulo}</b><span>{fecha} · 19:00–21:00 (Chile)</span></div>
        <div class="badge ok">Ver slides →</div>
      </a>''')
    else:
        items.append(f'''
      <div class="card item">
        <div class="num off">{n}</div>
        <div class="tx"><b>{titulo}</b><span>{fecha} · 19:00–21:00 (Chile)</span></div>
        <div class="badge">Próximamente</div>
      </div>''')

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Construye tu primer agente de IA — FACTEC 2026</title>
<style>
  :root{{--purple:#7c7ff0;--purple-dark:#5b5fd6;--ink:#1c1c2e;--muted:#6b6f85;--bg:#f7f7fd;--card:#fff;--line:#e4e4f4;--soft:#eeeefc}}
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:'Segoe UI',Inter,system-ui,sans-serif;color:var(--ink);min-height:100vh;
    background:radial-gradient(900px 450px at 85% -5%,rgba(124,127,240,.12),transparent),
      radial-gradient(rgba(124,127,240,.13) 1.5px,transparent 1.5px) 0 0/28px 28px,var(--bg);
    display:flex;flex-direction:column;align-items:center;padding:48px 18px}}
  .kicker{{font-size:11px;letter-spacing:4px;color:var(--purple);font-weight:700;text-transform:uppercase;margin-bottom:10px}}
  h1{{font-size:clamp(26px,5vw,40px);font-weight:800;letter-spacing:-.5px;text-align:center;line-height:1.15}}
  h1 span{{color:var(--purple)}}
  .sub{{color:var(--muted);margin:10px 0 34px;text-align:center;font-size:14px}}
  .list{{width:100%;max-width:680px;display:flex;flex-direction:column;gap:12px}}
  .card{{background:var(--card);border:1px solid var(--line);border-radius:14px;box-shadow:0 4px 18px rgba(60,60,140,.06)}}
  .item{{display:flex;align-items:center;gap:16px;padding:16px 20px;text-decoration:none;color:var(--ink)}}
  a.item.pub:hover{{border-color:var(--purple);transform:translateY(-1px);transition:.15s}}
  .num{{flex:none;width:38px;height:38px;border-radius:11px;background:var(--purple);color:#fff;font-weight:800;font-size:17px;display:flex;align-items:center;justify-content:center}}
  .num.off{{background:var(--soft);color:var(--muted)}}
  .tx{{flex:1;line-height:1.35}}
  .tx b{{font-size:15px}}
  .tx span{{display:block;font-size:12px;color:var(--muted)}}
  .badge{{font-size:11px;font-weight:700;color:var(--muted);background:var(--soft);border:1px solid var(--line);border-radius:20px;padding:5px 12px;white-space:nowrap}}
  .badge.ok{{color:#fff;background:var(--purple);border-color:var(--purple)}}
  .foot{{margin-top:36px;color:var(--muted);font-size:12px;text-align:center;line-height:1.7}}
  .foot b{{color:var(--purple-dark)}}
</style>
</head>
<body>
  <div class="kicker">— &nbsp;Séptima Escuela de Temporada FACTEC 2026 · USACH&nbsp; —</div>
  <h1>Construye tu primer agente de IA:<br><span>de la idea a un asistente funcional</span></h1>
  <p class="sub">Relator: Enrique Abril Contreras · Las slides de cada sesión se publican aquí el día de la clase.</p>
  <div class="list">{"".join(items)}
  </div>
  <p class="foot">💡 Consejo: navega las slides con las flechas del teclado.<br>
  Las grabaciones y el material adicional están en la <b>carpeta compartida del curso</b> (link en el correo de bienvenida).</p>
</body>
</html>
'''
open("index.html", "w", encoding="utf-8", newline="\n").write(html)
print("index.html generado —", sum(1 for n,_,_ in SESIONES if os.path.exists(f"sesion{n}.html")), "sesiones publicadas")
