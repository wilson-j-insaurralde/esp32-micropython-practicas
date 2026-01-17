Este proyecto usa un ESP32 para controlar un láser KY-008 mediante un botón.

Un toque del botón → el láser se prende

Otro toque → el láser se apaga

El sistema usa lógica toggle y anti-rebote para funcionar de manera confiable.

Es ideal para aprender entradas digitales, salidas digitales y lógica de control en MicroPython.

🔧 Materiales necesarios

ESP32 (ESP32-WROOM-32)

Láser KY-008

Botón pulsador

Cables de conexión

Protoboard (opcional)

🛠️ Conexiones
1️⃣ Botón
ESP32 GPIO15 (P15) → un lado del botón
ESP32 GND         → otro lado del botón


Configurado con Pin.IN y Pin.PULL_UP en MicroPython

Permite leer cuando se presiona el botón (0) y cuando no (1)

2️⃣ Láser KY-008
ESP32 GPIO14 (P14) → S (señal/control)
ESP32 5V           → + (alimentación)
ESP32 GND          → - (GND, compartido con el botón)


GPIO14 controla el encendido/apagado del láser

El 5V alimenta el láser de manera segura

GND compartido con el ESP32 y botón para referencia común

💻 Código en MicroPython
from machine import Pin as p
import time

boton = p(15, p.IN, p.PULL_UP)
laser = p(14, p.OUT)

estado_laser = 0        
ultimo_valor = 1  

while True:
    valor = boton.value()
    if valor == 0 and ultimo_valor == 1:
        estado_laser = 1 - estado_laser
        laser.value(estado_laser)
        time.sleep(0.2)  # anti-rebote

    ultimo_valor = valor
    time.sleep(0.05)

🧠 Cómo funciona el código

Se lee constantemente el botón con boton.value()

Se detecta cuando se presiona (flanco 1→0)

Se cambia el estado del láser (0 → 1 o 1 → 0)

Se aplica anti-rebote con time.sleep(0.2)

Se actualiza la variable ultimo_valor para controlar el toggle

