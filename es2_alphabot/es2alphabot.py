from AlphaBot import AlphaBot
import RPi.GPIO as GPIO
import time

def main():
    DR = 16
    DL = 19
    alphabot = AlphaBot()
    print("connesso")
    

    while True:
        DR_status = GPIO.input(DR)
        time.sleep(0.1)
        DL_status = GPIO.input(DL)
        time.sleep(0.1)
        alphabot.forward()
        if DR_status == 0 or DL_status == 0:
            alphabot.right()   

main()