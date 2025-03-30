#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

ev3 = EV3Brick()

motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)
fator = 0.6  

try:
    while True:
         for i in range(2):

          motor_esquerdo.run(200)
          motor_direito.run(200)
          wait(2000)
          motor_direito.run_time(200 * (1 - fator), 850, wait=False)
          motor_esquerdo.run_time(200 * (1 + fator), 850)
          wait(850)
        
          motor_esquerdo.hold()
          motor_direito.hold()
          wait(100)
        
          motor_esquerdo.run(200)
          motor_direito.run(200)
          wait(2000)
          motor_direito.run_time(200 * (1 - fator), 850, wait=False)
          motor_esquerdo.run_time(200 * (1 + fator), 850)
          wait(850)
        
          motor_esquerdo.hold()
          motor_direito.hold()
          wait(100)

except KeyboardInterrupt:
      motor_esquerdo.stop()
      motor_direito.stop()