# Contador de pulsaciones con botón – ESP32 (MicroPython)

Este proyecto es una práctica básica de **entrada digital** usando un **botón** conectado a un **ESP32** programado con **MicroPython**.

El programa cuenta cuántas veces se presiona un botón y finaliza cuando se alcanzan **15 pulsaciones**.

---

## 🧠 Conceptos utilizados

- Entradas digitales (`Pin.IN`)
- Resistencia interna `PULL_UP`
- Lectura de botones
- Anti-rebote por software
- Funciones
- Bucles `while`
- Contadores
- Control de flujo

---

## 🔌 Conexión del hardware

- **GPIO 15** → un lado del botón  
- **GND** → el otro lado del botón  

No se necesita resistencia externa porque se utiliza `Pin.PULL_UP`.

GPIO 15 ─── BOTÓN ─── GND


---

## ⚙️ Funcionamiento del programa

1. El ESP32 espera a que el botón sea presionado.
2. Detecta una pulsación completa:
   - presionar (1 → 0)
   - soltar (0 → 1)
3. Incrementa un contador.
4. Imprime la cantidad de pulsaciones por consola.
5. Cuando el contador llega a 15, el programa termina.

Se utiliza un pequeño retardo (`sleep`) para evitar el rebote mecánico del botón.

---

## 🧪 Código

```python
from machine import Pin
import time

boton = Pin(15, Pin.IN, Pin.PULL_UP)

def esperar_pulsacion():
    # Esperar a que el botón sea presionado
    while boton.value() == 1:
        time.sleep(0.01)
    time.sleep(0.03)  # anti-rebote al presionar

    # Esperar a que el botón sea soltado
    while boton.value() == 0:
        time.sleep(0.01)
    time.sleep(0.03)  # anti-rebote al soltar

contador = 0
while contador < 15:
    esperar_pulsacion()
    contador += 1
    print("Pulsaciones:", contador)

print("termino")
📌 Notas
El botón funciona con lógica invertida:

1 → no presionado

0 → presionado

El uso de PULL_UP evita valores inestables cuando el botón no está presionado.

El programa está pensado como práctica educativa y base para proyectos más complejos.

