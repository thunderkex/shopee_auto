import subprocess
# from subprocess import Popen, CREATE_NEW_CONSOLE

n = 10
for i in range(0, n):
            print(i)
            subprocess.Popen(['cmd.exe', '/K', 'main.py'],creationflags=subprocess.CREATE_NEW_CONSOLE)
            subprocess.Popen(['cmd.exe', '/K', 'main_dell.py'],creationflags=subprocess.CREATE_NEW_CONSOLE)
# def go():