import subprocess
import sys
import os

print("####################################")
print("#                                  #")
print("#   Notch Hider by LR(yymin1022)   #")
print("#                                  #")
print("####################################")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

while(True):
    print("Conntect Device with USB Debugging Enabled")
    input("/* Press Any Key to Continue */")
    if "product" in str(subprocess.check_output([resource_path('bin/adb'), 'devices', '-l'])):
        print("Device Found.\n")
        break
    else:
        print("Device Not Found. Try Again.\n")
        continue

print("Overscan Command will run. Please wait a moment, and DO NOT DISCONNECT DEVICE.")
input("/* Press Any Key to Continue */")
failCount = 0
while(True):
    if failCount >= 3:
        print("Failed too many time. Device might be unsupported. Please contact developer.")
        print("Email : yymin1022@gmail.com")
        break
    else:
        try:
            subprocess.check_output(['bin/adb', 'shell', 'wm', 'overscan', '0,0,0,0'])
        except subprocess.CalledProcessError:
            print("Failed. Trying again.")
            failCount += 1
            continue
        print("Successfully applied. Device will be rebooted.")
        subprocess.check_output(['bin/adb', 'reboot'])
        break


