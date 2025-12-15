import socket
from AlphaBot import AlphaBot
import time
import RPi.GPIO as GPIO

IP_SERVER = "0.0.0.0"
PORTA_SERVER = 10000
BUFFER = 4096

DR = 16
DL = 19

def main():
    a = AlphaBot()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DR, GPIO.IN)
    GPIO.setup(DL, GPIO.IN)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP_SERVER, PORTA_SERVER))
    s.listen(10)
    print("connesso")

    conn, _ = s.accept()

    while True:
        sd = GPIO.input(DR)
        ss = GPIO.input(DL)

        if ss == 0:
            a.backward()
            time.sleep(0.1)
            a.right()
            time.sleep(0.1)
            a.stop()
            conn.send("ostacolo".encode())
            continue

        elif sd == 0:
            a.backward()
            time.sleep(0.1)
            a.left()
            time.sleep(0.1)
            a.stop()
            conn.send("ostacolo".encode())
            continue

        comando = conn.recv(BUFFER).decode().strip()
        print(f"Comando ricevuto: {comando}")

        if comando == "avanti":
            a.forward()
            conn.send("ok".encode())
        elif comando == "indietro":
            a.backward()
            conn.send("ok".encode())
        elif comando == "sinistra":
            a.left()
            conn.send("ok".encode())
        elif comando == "destra":
            a.right()
            conn.send("ok".encode())
        elif comando == "stop":
            a.stop()
            conn.send("ok".encode())
            break

    conn.close()
    s.close()
    GPIO.cleanup()
if __name__ == "__main__":
    main()