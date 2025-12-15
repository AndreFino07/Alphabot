import socket
from pynput import keyboard

IP_SERVER = "192.168.1.126"
PORTA_SERVER = 10000
BUFFER = 4096

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP_SERVER, PORTA_SERVER))
    print("Premi W/A/S/D per muovere o Q per uscire.")

    def on_press(key):
        if hasattr(key, "char"):
            comando = None
            if key.char == "w":
                comando = "avanti"
            elif key.char == "s":
                comando = "indietro"
            elif key.char == "a":
                comando = "sinistra"
            elif key.char == "d":
                comando = "destra"
            elif key.char == "q":
                comando = "stop"

            if comando:
                s.send(comando.encode())
                risposta = s.recv(BUFFER).decode()
                print(f"risposta server: {risposta}")
                if comando == "stop":
                    return False 

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    s.close()

if __name__ == "__main__":
    main()
