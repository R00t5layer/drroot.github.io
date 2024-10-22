
replacer = { "a" : "4", "e" : "3", "i" : "1", "o" : "0" , "E" : "3", "I" : "1", "O" : "0"}
m = ["AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz", "0123456789", "@%{[}]!¡+*-"]
l = [13, 5, 1]
LENGHT = 20
cant = int(input("Cantidad de contraseñas a crear => "))
toFile = []
import random
for v in range(cant) :
    pwd = ""
    for u in range(len(l)) :
        a = random.sample(m[u], l[u])
        for x in range(len(a)) :
            pwd += a[x]
    pwd += "@"
    toFile.append(pwd)
toWrite = []
for v in range(len(toFile)) :
    a = random.sample(toFile[v], LENGHT)
    b = ""
    for u in a :
        b += u
    toWrite.append(b)
print(toWrite)

f = open("Passwords.txt", "w")
for v in toWrite :
    f.write(v + "\n")

f.close()
    
