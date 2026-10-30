import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

def recibir(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            print("\n[Conexión cerrada]")
            break
        print(f"\n[vm1]: {data.decode()}")
        print("[vm2]: ", end="", flush=True)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Esperando conexión en el puerto {PORT}...")
        conn, addr = s.accept()
        print(f"Conectado con {addr[0]}")
        threading.Thread(target=recibir, args=(conn,), daemon=True).start()
        while True:
            msg = input("[vm2]: ")
            if msg.lower() == "salir":
                break
            conn.sendall(msg.encode())
        conn.close()

main()
