#!/usr/bin/env bash
# Publica las slides de una sesión en GitHub Pages.
# Uso: bash scripts/publicar.sh N   (N = 1..6)
# Correr ~1 hora antes de cada clase. Copia el deck, regenera el índice y hace push.
set -e
cd "$(dirname "$0")/.."          # trabajar desde la raíz del repo
N="$1"
[ -z "$N" ] && { echo "Uso: bash publicar.sh N (1..6)"; exit 1; }

SRC="../material_curso/slides_marp"
case "$N" in
  1|2|3|4|5) cp "$SRC/clase$N.html" "sesion$N.html" ;;
  6)         cp "$SRC/sesion6_factec.html" "sesion6.html" ;;
  *) echo "Sesión inválida: $N (usa 1..6)"; exit 1 ;;
esac

# Inyectar botón "← Inicio" para volver al hub (solo en la copia publicada)
python - "sesion$N.html" <<'PYEOF'
import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
BTN = ('<a id="volver-inicio" href="./" title="Volver al inicio" '
       'style="position:fixed;top:12px;right:14px;z-index:99999;'
       "font-family:'Segoe UI',sans-serif;font-size:12px;font-weight:700;"
       'color:#5b5fd6;background:rgba(255,255,255,.92);border:1px solid #e4e4f4;'
       'border-radius:20px;padding:6px 14px;text-decoration:none;'
       'box-shadow:0 2px 10px rgba(60,60,140,.2)">← Inicio</a>')
if 'volver-inicio' not in s:
    s = s.replace('</body>', BTN + '</body>')
    open(p, 'w', encoding='utf-8').write(s)
    print('boton inyectado en', p)
else:
    print('boton ya presente en', p)
PYEOF

python scripts/gen_index.py
git add -A
git commit -m "Publica sesión $N"
git push
echo "✅ Sesión $N publicada. URL: https://kiketach.github.io/curso-agentes-factec/sesion$N.html"
