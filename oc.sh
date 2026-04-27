#!/bin/bash
MODO=$1
PATH_CONFIG="./.opencode"
DESTINO_DOT="$PATH_CONFIG/oh-my-openagent.json"
DESTINO_ROOT="./oh-my-opencode.json"
DEFAULT_ORIGEN="$PATH_CONFIG/oh-my-openagent-default.json"

# 1. Mapear argumentos
case $MODO in
"nogpt") ORIGEN="$PATH_CONFIG/oh-my-opencode-nogpt.json" ;;
"gpt") ORIGEN="$PATH_CONFIG/oh-my-opencode-gpt.json" ;;
"or") ORIGEN="$PATH_CONFIG/oh-my-opencode-openrouter.json" ;;
"orcp") ORIGEN="$PATH_CONFIG/oh-my-opencode-orcp.json" ;;
"nv") ORIGEN="$DEFAULT_ORIGEN"; MODO="nv" ;;
*) ORIGEN="$DEFAULT_ORIGEN"; MODO="default" ;;
esac

# 2. Validar existencia
if [ ! -f "$ORIGEN" ]; then
echo "❌ Error: No existe $ORIGEN"
exit 1
fi

# 3. Copiar a ambos destinos
cp "$ORIGEN" "$DESTINO_DOT"
cp "$ORIGEN" "$DESTINO_ROOT"

# --- BLOQUE DE VERIFICACIÓN ---
echo "------------------------------------------------"
echo "🔍 VERIFICACIÓN DE SESIÓN:"
echo "📂 Archivo fuente: $ORIGEN"
echo "🎯 Archivos activos: $DESTINO_DOT, $DESTINO_ROOT"
MODELO_ACTIVO=$(grep -oP '"model":\s*"\K[^"]+' "$DESTINO_DOT" | head -n 1)
echo "🤖 Modelo principal detectado: $MODELO_ACTIVO"
echo "------------------------------------------------"

# 4. Trap para limpieza
cleanup() {
[ -f "$DEFAULT_ORIGEN" ] && cp "$DEFAULT_ORIGEN" "$DESTINO_DOT"
[ -f "$DEFAULT_ORIGEN" ] && cp "$DEFAULT_ORIGEN" "$DESTINO_ROOT"
echo -e "\n✅ Sesión cerrada. Perfil original restaurado."
}
trap cleanup EXIT INT TERM

# 5. Lanzar
echo "🚀 Iniciando OpenCode..."
opencode
