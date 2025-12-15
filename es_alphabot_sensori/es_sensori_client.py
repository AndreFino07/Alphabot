import socket

IP_SERVER = "192.168.1.126"
PORTA_SERVER=10000
BUFFER=4096

def main():

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP_SERVER, PORTA_SERVER))
    while True:
        mov=input("scrivi: avanti, indietro, destra o sinistra ")
        s.send(mov.encode())
        risposta = s.recv(BUFFER).decode()
        print(f"Risposta dal server: {risposta}")
if __name__=="__main__":
    main()