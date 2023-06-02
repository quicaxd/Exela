import shutil
import os

def zipFile(path):
    if os.path.exists(path + ".zip"):
        os.remove(path + ".zip")
        shutil.make_archive(path, "zip", path)
    else:
        shutil.make_archive(path, "zip", path)
    