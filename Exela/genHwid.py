import subprocess


class Gen:
    def __init__(self) -> None:
        self.get_hwid_number()
    def get_hwid_number(self) -> None:
        command = "wmic csproduct get uuid"
        run = str(subprocess.check_output(command).decode('utf-8').split("\n")[1].strip())
        return run
    