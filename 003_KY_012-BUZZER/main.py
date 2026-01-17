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
        time.sleep(0.3)

    ultimo_valor = valor

    # Simula beep mantenido
    if estado_buzzer == 1:
        buzzer.value(1)
        time.sleep(0.1)
        buzzer.value(0)
        time.sleep(0.1)
    else:
        buzzer.value(0)
        time.sleep(0.1)


