import socket
from AlphaBot import AlphaBot

IP_SERVER = "0.0.0.0"
PORTA_SERVER = 10000
BUFFER = 4096

def main():
    a = AlphaBot()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP_SERVER, PORTA_SERVER))
    s.listen(10)
    print("connesso")

    conn, _ = s.accept()

    while True:
        comando = conn.recv(BUFFER).decode().strip()
        
        print(f"Comando ricevuto: {comando}")
        if comando == "avanti":
            a.forward()
            conn.send("avanti".encode())
        elif comando == "indietro":
            a.backward()
            conn.send("indietro".encode())
        elif comando == "sinistra":
            a.left()
            conn.send("sinistra".encode())
        elif comando == "destra":
            a.right()
            conn.send("destra".encode())
        elif comando == "stop":
            a.stop()
            conn.send("stop".encode())
            conn.close()
            s.close()
            break

if __name__ == "__main__":
    main()
