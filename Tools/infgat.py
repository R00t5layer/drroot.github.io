#pip3 install argparse

import argparse

def clearer () :
    import os
    import platform
    so = platform.system()
    print(so)
    if so == "Windows" :
        os.system("cls")
    elif so == "Linux" :
        os.system("clear")

def menu() :
    clearer()

    title = '''
    ██████╗ ██████╗    ██████╗  ██████╗  ██████╗ ████████╗██╗███╗   ██╗███████╗ ██████╗  █████╗ ████████╗
    ██╔══██╗██╔══██╗   ██╔══██╗██╔═████╗██╔═████╗╚══██╔══╝██║████╗  ██║██╔════╝██╔════╝ ██╔══██╗╚══██╔══╝
    ██║  ██║██████╔╝   ██████╔╝██║██╔██║██║██╔██║   ██║   ██║██╔██╗ ██║█████╗  ██║  ███╗███████║   ██║   
    ██║  ██║██╔══██╗   ██╔══██╗████╔╝██║████╔╝██║   ██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██║   ██║   
    ██████╔╝██║  ██║██╗██║  ██║╚██████╔╝╚██████╔╝   ██║██╗██║██║ ╚████║██║     ╚██████╔╝██║  ██║   ██║   
    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝╚═╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                                                                                    
    '''
    print(title)
    
    parser = argparse.ArgumentParser()
    #ip, domain, url
    parser.add_argument('-ip', '--ip', type=str, help='IP address of target', required=False)
    parser.add_argument('-d', '--d', type=str, help='Domain address of target', required=False)
    parser.add_argument('-u', '--u', type=str, help='Url of target', required=False)
    parser.add_argument('-mode', '--mode',
                        type=str,
                        choices=['services', 'directory', 'subdomain'],
                        help='Scanner mode')

    args = parser.parse_args()

    if args.mode == 'services':
        executer(1, args)
    elif args.mode == 'directory':
        executer(2, args)
    elif args.mode == 'subdomain':
        executer(3, args)

def executer(d, argf) :
    #scan ports & services => IP
    args = argf
    commands = ["nmap -sV -sS {0}".format(args.ip), 
                "nmap -A {0}".format(args.ip), 
                "nmap -sU -sV -sC --top-ports=20 {0}".format(args.ip), 
                "nmap -sU --min-rate 7500 -F  {0}".format(args.ip),
                "whatweb {0}".format(args.ip)]

    #scan directory list => url
    commands2 = ["gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -u {0}".format(args.u),
                "ffuf -c -u {0} -H 'Host:FUZZ.{1}' -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -mc 200".format(args.u, args.d)
                ]

    #scan domain names => dominio, ip
    commands3 = ["dig axfr @{0} {1}".format(args.ip, args.d)
                ]

    fileNames = ["services", "directory", "subdomain"]

    results = [] #all the results will stored here, before write into a file
    signal = [] #signal if thread finish

    fileName = ""
    
    def init_command (command) :
        import subprocess
        print("Running {}".format(command))
        subprocess = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
        subprocess_return = subprocess.stdout.read()
        response = subprocess_return.decode("utf-8")
        results.append(command + "\n" + response)
        print("Finish {}".format(command))
        signal.append(True)

    def executeThread (commandsList):
        import threading
        for v in range (len(commandsList)) :
            t = threading.Thread(target = init_command, args = (commandsList[v], ))
            t.start()
        print("\n\n")
    def writer () :
        file = open(str(args.mode) + ".txt" , "w")
        for v in results :
            file.write(v)
            file.write("\n\n\n")
        file.close()
    commandsList = []
    if d == 1 :
        commandsList = commands
        executeThread(commands)
    elif d == 2 :
        commandsList = commands2
        executeThread(commands2)
    elif d == 3 :
        commandsList = commands3
        executeThread(commands3)

    semaphore = True
    while semaphore :
        if len(signal) == len(commandsList) :
            writer()
            semaphore = False
menu()
