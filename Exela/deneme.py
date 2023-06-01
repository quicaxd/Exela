hook = str(input("Enter your webhook URL : "))


file = open(r"C:\Users\anani\OneDrive\Masaüstü\deneme.py", "r")
source = file.read()
updatesource = source.replace("%URL%", hook)
print(updatesource)