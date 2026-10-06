# Eetu Kyrönlahti
# 07.10.2026
# Tehtävä 6.2

# Lisätään laitteen pinnit
from machine import Pin, PWM

# Lisätään aikamoduulista sleep
from time import sleep

# Moottori A pinnien lisääminen
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B pinnien lisääminen
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# Määritellään liikkumisen funktiot

def eteenpain(nopeus = 49181, aika = 4):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika) 
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(1)

def taaksepain(nopeus = 49181, aika = 4):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika) 
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(1)
    
def vasemmalle(nopeus = 49181, aika = 3):
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika) 
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(1)

def oikealle(nopeus = 49181, aika = 3):
    m1.value(0)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika) 
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(1)

# 5 sekunnin tauko
sleep(5)

with open("focarin_reitti.txt", "r") as file:
    for komento in file:
        komento = komento.strip()
        if komento == "eteenpain":
            eteenpain()
        elif komento == "taaksepain":
            taaksepain()
        elif komento == "vasemmalle":
            vasemmalle()
        elif komento == "oikealle":
            oikealle()