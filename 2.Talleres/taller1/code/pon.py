### PARA PON

import subprocess
import time

def get_snmp_data(host, community, oid):
    try:
        # Ejecutar el comando snmpwalk y capturar la salida
        result = subprocess.run(['snmpwalk', '-v', '2c', '-c', community, host, oid], capture_output=True, text=True, check=True)
        
        # Procesar la salida (puedes adaptar esto según tus necesidades)
        lines = result.stdout.strip().split("\n")

        if not lines:
          print(f"No se recibieron datos para el OID {oid}.")
          return None

        metrics = {}
        for line in lines:
          parts = line.split(" = ")
          if len(parts) == 2:
            oid, rest = parts
            type_and_value = rest.split(": ")
            if len(type_and_value) == 2:
              type, value = type_and_value
              metrics[oid] = {'type': type, 'value': value}
        ## Retornamos la salida del comando procesada
        return metrics
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar snmpwalk: {e}")
        return None

# Definimos las variables
host = '10.20.180.1'  # IP del dispositivo
community = 'public'  # Comunidad SNMP
oid = '.1.3.6.1.2.1'  # OID raíz

metrics = get_snmp_data(host, community, oid)
if metrics:
    for oid, data in metrics.items():
        print(f"{oid}: {data['type']} = {data['value']}")


def calculate_speed(initial_bytes, final_bytes, initial_time, final_time):
    # Calcula la velocidad en bytes por segundo
    return (final_bytes - initial_bytes) / (final_time - initial_time)

initial_data = get_snmp_data(host, community, '1.3.6.1.2.1.31.1.1.1.6')
# Captura el número inicial de bytes y el tiempo
if initial_data and 'value' in initial_data:
    initial_bytes = initial_data['value']
else:
    print("No se pudo obtener el número inicial de bytes.")
initial_time = time.time()

# Espera un tiempo ( 5 segundos)
time.sleep(5)

# Captura el número final de bytes y el tiempo
if initial_data and 'value' in initial_data:
    final_bytes = initial_data['value']
else:
    print("No se pudo obtener el número inicial de bytes.")
final_time = time.time()

# Calcula la velocidad
if initial_bytes and final_bytes:
  speed = calculate_speed(int(initial_bytes), int(final_bytes), initial_time, final_time)
  print(f"Velocidad: {speed} bytes/s")
else: 
  print("No se pudo obtener el número de bytes.")
  print("No se puede obtener la velocidad.")

