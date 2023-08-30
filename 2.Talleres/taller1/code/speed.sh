#!/bin/bash

# Velocidades teóricas (ejemplo - cambiar según velocidad conocida)
TEORICA_DOWN="100"  # 100 Mbps de bajada
TEORICA_UP="50"     # 50 Mbps de subida

# Medir latencia
echo -e "\nMidiendo latencia con ping...\n"
ping -c 4 google.com

# Medir velocidades de subida y bajada
echo -e "\nMidiendo velocidades con speedtest-cli..."
RESULTADO=$(speedtest-cli --simple)

echo -e "\n$RESULTADO"

# Extraer velocidades reales de subida y bajada
REAL_DOWN=$(echo "$RESULTADO" | grep "Download" | awk '{print $2}')
REAL_UP=$(echo "$RESULTADO" | grep "Upload" | awk '{print $2}')

# Comparar velocidades teóricas con reales
echo -e "\nComparación de velocidades:"
echo "Teórica bajada: $TEORICA_DOWN Mbps vs Real bajada: $REAL_DOWN Mbps"
echo "Teórica subida: $TEORICA_UP Mbps vs Real subida: $REAL_UP Mbps"
