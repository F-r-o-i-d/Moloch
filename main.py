from mcstatus import MinecraftServer
import core, socket, threading, requests, bs4
from art import *
gen = core.Generate()
portClass = [21,22,80,443,8080,25565,3306,23,25,5900,3389,111,139, 554]
webPort = [80,443,8080]
gamePort = [25565]
print(text2art("Moloch Security", "rand"))
print("random art because its fun")
aprint("random")
print(" _" + "_"*10)
print("/")
def searching():
    ipCount = 0
    while (1):
        ip = gen.Ipv4()
        ipFormat = ""
        goodport = []
        for port in portClass:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(.5)
            ipCount += 1
            try:
                s.connect((ip, port))
                goodport.append(port)
            except KeyboardInterrupt:
                exit()
            except:
                pass
        ipFormat = f"{ip}:"
        webcheck = False
        for port in goodport:
            ipFormat += " " + str(port)
        for port in goodport:
            for x in webPort:
                if port == x:
                    if(webcheck):
                        pass
                    else:
                        try:
                            r = requests.get(f"http://{ip}:{port}")
                            html = bs4.BeautifulSoup(r.text, 'html.parser')
                            ipFormat += f" {html.find('title').string}"
                            webcheck = True
                        except:
                            pass
            for x in gamePort:
                try:
                    server = MinecraftServer.lookup(f"{ip}:{port}")
                    ipFormat += f" Minecraft server {server.description, server.version}"
                except:
                    pass
        if len(goodport) >= 1:
            print("| - " + ipFormat)
            with open("ip.txt","a") as f:
                f.writelines("\n" + ipFormat)
                f.close()
        if(ipCount >= 70):
            ipCount = 0
for x in range(36):
    threading.Thread(target=searching).start()
searching()
