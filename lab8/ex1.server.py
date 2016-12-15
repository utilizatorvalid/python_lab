import socket
import time


# 1a. Sa se implementeze folosind modulul socket (peste TCP), un server care atunci cand un client se conecteaza,
# scrie intr-un fisier text : timpul conexiunii (in format human-readable), adresa si portul clientului.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 6969
s.bind((ip, port))
s.listen(1)
print("listening on:", (ip,port))
while True:
    (connection, address) = s.accept()
    with open("log.txt",'a') as f:
        timeObj = time.localtime()
        f.write("{addr} | {time}\n".format(addr=address,
                                         time = time.strftime("%H:%M:%S - %Y-%m-%d",timeObj)
                                         ))
    print(address)
    connection.close()
