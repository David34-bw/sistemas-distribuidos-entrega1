import socket
import threading

SERVER_IP = "10.0.2.4"
PORT = 5000

def recibir(s):
    while True:
        data = s.recv(1024)
        if not data:
            print("\n[Conexión cerrada]")
            break
        print(f"\n[vm2]: {data.decode()}")
        print("[vm1]: ", end="", flush=True)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, PORT))
        print(f"Conectado con {SERVER_IP}")
        threading.Thread(target=recibir, args=(s,), daemon=True).start()
        while True:
            msg = input("[vm1]: ")
            if msg.lower() == "salir":
                break
            s.sendall(msg.encode())

main()
