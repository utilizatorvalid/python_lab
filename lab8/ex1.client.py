# 1b. Sa se implementeze un client pentru serverul implementat la 1a: un script care primeste de la linia de
# comanda un string addr si un integer port si se conecteaza prin TCP la adresa addr, la portul port.
import socket
import sys

if __name__=="__main__":
    args = sys.argv
    ip = args[1]
    port = int(args[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    s.close()