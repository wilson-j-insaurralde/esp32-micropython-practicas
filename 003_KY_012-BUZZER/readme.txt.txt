📌 Toggle Buzzer con ESP32 (KY-012)

Descripción:
Este proyecto utiliza un ESP32 y un buzzer KY-012 para crear un sistema toggle con botón:

Un toque del botón → el buzzer comienza a sonar 

Otro toque → el buzzer se apaga

Anti-rebote incluido para evitar pulsaciones múltiples accidentales

Es ideal para aprender entradas y salidas digitales, lógica de toggle y control de actuadores en MicroPython.

🔧 Materiales necesarios

ESP32 (ESP32-WROOM-32)

Buzzer KY-012 (activo)

Botón pulsador

Cables de conexión

Protoboard (opcional)

🛠️ Conexiones
1️⃣ Botón
ESP32 GPIO15 (P15) → un lado del botón
ESP32 GND         → otro lado del botón


Configurado con Pin.IN, Pin.PULL_UP en MicroPython

Permite leer cuando se presiona el botón (0) y cuando no (1)

2️⃣ Buzzer KY-012
ESP32 GPIO2 (P2) → S (control del buzzer)
ESP32 5V        → + (alimentación)
ESP32 GND       → - (común con ESP32 y botón)


GPIO2 controla el encendido/apagado del buzzer

5V alimenta el buzzer de manera segura

GND compartido con el ESP32 y botón para referencia común

💻 Código en MicroPython
from machine import Pin
import time

boton = Pin(15, Pin.IN, Pin.PULL_UP)
buzzer = Pin(2, Pin.OUT)

estado_buzzer = 0
ultimo_valor = 1

while True:
    valor = boton.value()
    
    if valor == 0 and ultimo_valor == 1:
        estado_buzzer = 1 - estado_buzzer
        ultimo_valor = valor
        time.sleep(0.3)  # anti-rebote

    ultimo_valor = valor

    # Simula beep sostenido con el buzzer activo
    if estado_buzzer == 1:
        buzzer.value(1)
        time.sleep(0.1)
        buzzer.value(0)
        time.sleep(0.1)
    else:
        buzzer.value(0)
        time.sleep(0.1)

🧠 Cómo funciona el código

Se lee constantemente el botón con boton.value()

Se detecta el momento exacto que se presiona (flanco 1→0)

Se cambia el estado del buzzer (0 → 1 o 1 → 0)

Se aplica anti-rebote con time.sleep(0.3) para no contar múltiples pulsaciones

Mientras está activado, un loop rápido ON/OFF simula un sonido sostenido
