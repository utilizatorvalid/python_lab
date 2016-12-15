# 2a. Sa se implementeze folosind modulul socket (peste UDP), un server care atunci cand primeste un pachet UDP
# (datagrama), scrie intr-un fisier text urmatoarele informatii: ora si data, adresa, port, lungime,
# hash-ul md5 pe continut in format hex, hash-ul sha256 pe continut in format hex.
import socket
import hashlib
import time
def get_hash_sha256(data):
    m = hashlib.sha256()
    m.update(data)
    return m.hexdigest()
def get_hash_md5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()
def get_info_about(data, addr):
    info = ''''
    ___________________________________
    Time:   {time}
    IP:     {ip}
    PORT:   {port}
    length: {len}
    sha256: {sha256}
    md5:    {md5}

    '''
    timeObj = time.localtime()
    timestr = time.strftime("%H:%M:%S - %d %m %Y",timeObj)
    sha256 = get_hash_sha256(data)
    md5 = get_hash_md5(data)
    length = len(data)
    return info.format(time = timestr,
                       ip = addr[0],
                       port = addr[1],
                       len = length,
                       sha256 = sha256,
                       md5 = md5)



ip = '127.0.0.1'
port = 6970


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip, port))
print('serving at:',(ip,port))
while True:
    data, addr = s.recvfrom(1024)
    print("received message:",data, " from", addr)
    info = get_info_about(data, addr)
    with open('log2.txt','a')as log:
        log.write(info)
