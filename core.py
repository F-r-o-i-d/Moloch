import random
import socket
class Generate:
    def __init__(self):
        pass
    def Ipv4(self):
        ipv1 = random.randint(10,255)
        ipv2 = random.randint(0,255)
        ipv3 = random.randint(0,255)
        ipv4 = random.randint(0,255)
        ipComplete = f"{ipv1}.{ipv2}.{ipv3}.{ipv4}"
        return ipComplete
