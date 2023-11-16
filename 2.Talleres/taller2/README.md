# Script de Captura y Análisis de Tráfico de Red

## Descripción

Este script de Python utiliza las bibliotecas ```pyshark``` y ```pandas``` para capturar y analizar el tráfico de red. Está diseñado para capturar paquetes Ethernet y, si están presentes, etiquetas MPLS (Multi-Protocol Label Switching). Los datos capturados se almacenan en un archivo CSV para un análisis más detallado.

## Características

- Captura de paquetes Ethernet, incluyendo direcciones MAC de origen y destino.

- Detección y procesamiento de etiquetas MPLS, incluyendo etiquetas, valores de Experiencia (Exp) y Tiempo de Vida (TTL).

- Exportación de datos capturados a un archivo CSV para análisis.

## Requisitos

- Python 3.x
- **Librerías:** ```pyshark``` y ```pandas```

## Uso

- Ejecute el script con Python.
- El script iniciará la captura de paquetes en la interfaz especificada (```wlo1``` por defecto) y procesará los primeros 50 paquetes (configurable).
- Una vez completada la captura, los datos serán guardados en ```network_traffic_analysis.csv```.

## Configuración

- **interface:** Especifica la interfaz de red para la captura. Por defecto es ```wlo1```.
- **packet_count:** Define el número de paquetes a capturar. El valor por defecto es 50.

## Ejemplos de uso

Para ejecutar el script con la configuración por defecto:

```python
  capture_packets()
```

Para ejecutar el script con la configuración por defecto:

```python
  capture_packets(interface='eth0', packet_count=100)
```
