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
