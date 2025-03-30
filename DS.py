from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Color, Button
from pybricks.tools import wait
import math

ev3 = EV3Brick()

motor_esq = Motor(Port.B)
motor_dir = Motor(Port.C)
sensor_distancia = UltrasonicSensor(Port.S1)
sensor_cor = ColorSensor(Port.S2)


DIAMETRO_RODA = 6.0  
DIST_ENTRE_RODAS = 13.5  
DISTANCIA_ALVO = 15  
GP = 2.5  # ganho proporcional

def anda_reto(distancia_cm):
    
    graus_motor = (distancia_cm * 360) / (DIAMETRO_RODA * math.pi)
    
    motor_esq.reset_angle(0)
    motor_dir.reset_angle(0)
    
    while (motor_esq.angle() + motor_dir.angle())/2 < graus_motor:
        motor_esq.run(200)
        motor_dir.run(200)
    
    motor_esq.hold()
    motor_dir.hold()

def curva(graus):
   
    graus_motor = graus * (DIST_ENTRE_RODAS / DIAMETRO_RODA)
    
    motor_esq.reset_angle(0)
    motor_dir.reset_angle(0)
    
    while (motor_esq.angle() - motor_dir.angle())/2 < graus_motor:
        motor_esq.run(200)
        motor_dir.run(-200)
    
    motor_esq.hold()
    motor_dir.hold()

def seguir_parede():
  
    try:
        while True:
           
            distancia = sensor_distancia.distance() / 10  
            erro = DISTANCIA_ALVO - distancia
            
          
            motor_esq.run(200 + GP * erro)
            motor_dir.run(200 - GP * erro)
            
            
            cor = sensor_cor.color()
            
            if cor == Color.RED:
               
                curva(90)
                anda_reto(10)  
                
            elif cor == Color.YELLOW:
              
                motor_esq.stop()
                motor_dir.stop()
                ev3.screen.print("Pressione um botão!")
                while not any(ev3.buttons.pressed()):
                    wait(10)
                ev3.screen.clear()
                
            elif cor == Color.GREEN:
                
                motor_esq.stop()
                motor_dir.stop()
                ev3.screen.print("PARADA FINAL!")
                break
            
            wait(50)
            
    except KeyboardInterrupt:
        motor_esq.stop()
        motor_dir.stop()


if __name__ == '__main__':
    seguir_parede()