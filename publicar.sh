#!/usr/bin/env bash
# Publica las slides de una sesión en GitHub Pages.
# Uso: bash publicar.sh N        (N = 1..6)
# Correr ~1 hora antes de cada clase. Copia el deck, regenera el índice y hace push.
set -e
cd "$(dirname "$0")"
N="$1"
[ -z "$N" ] && { echo "Uso: bash publicar.sh N (1..6)"; exit 1; }

SRC="../material_curso_enrique/slides_marp"
case "$N" in
  1|2|3|4|5) cp "$SRC/clase$N.html" "sesion$N.html" ;;
  6)         cp "$SRC/sesion6_factec.html" "sesion6.html" ;;
  *) echo "Sesión inválida: $N (usa 1..6)"; exit 1 ;;
esac

python gen_index.py
git add -A
git commit -m "Publica sesión $N"
git push
echo "✅ Sesión $N publicada. URL: https://kiketach.github.io/curso-agentes-factec/sesion$N.html"
