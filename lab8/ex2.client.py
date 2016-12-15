# Sa se implementeze un client pentru serverul implementat la 2a:
# un script care primeste de la linia de comanda un string addr, un integer port, si un string msg si trimite un
# pachet UDP la adresa addr, la portul port si cu continutul msg.
import socket
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print("please specify address port and message\n\t ex script.py addr port message")
        exit()
    udp_ip = args[1]
    udp_port = int(args[2])
    message = args[3]

    print("udp target IP:", udp_ip)
    print("udp target port:", udp_port)
    print("message", message.encode())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(message.encode(),(udp_ip,udp_port))
    print("message sent")
