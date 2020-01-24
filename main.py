import platform
import subprocess
import sys
import os

print("####################################")
print("#                                  #")
print("#   Notch Hider by LR(yymin1022)   #")
print("#                                  #")
print("####################################")

strOS = platform.system()
if strOS == "Windows":
    print("PC의 운영체제는 Windows입니다.")
    print("Current OS is Windows.\n")
    adb_path = os.path.join(sys._MEIPASS, "adb.exe")
elif strOS == "Linux":
    print("PC의 운영체제는 Linux입니다.")
    print("Current OS is Linux.\n")
    adb_path = os.path.join(sys._MEIPASS, "adb")

while(True):
    print("USB 디버깅을 활성화한 뒤 USB 케이블로 기기를 연결해주세요.")
    print("Enable USB Debugging and connect device with USB Cable.\n")

    print("/* 계속하려면 아무키나 누르십시오. */")
    input("/* Press any key to continue. */\n")
    if "product" in str(subprocess.check_output([adb_path, 'devices', '-l'])):
        print("기기가 확인되었습니다.")
        print("Device Found.\n")
        break
    else:
        print("기기가 확인되지 않습니다. 다시시도해주세요.")
        print("Device Not Found. Try Again.\n")
        continue

while(True):
    print("원하시는 항목의 숫자를 입력해주세요.")
    print("Select what you want to do.")
    print("1. 노치가리기 활성화\n   Enable Notch Hiding")
    print("2. 노치가리기 비활성화(순정상태로 되돌리기)\n   Disable Notch Hiding(Back to Stock)")
    selectNum = input()
    if selectNum == "1":
        applyValue = "0,90,0,0"
        appCommand = [adb_path, 'install', os.path.join(sys._MEIPASS, "app.apk")]
        break
    elif selectNum == "2":
        applyValue = "reset"
        appCommand = [adb_path, 'shell', 'pm', 'uninstall', 'com.yong.notchhider']
        break
    else:
        print("잘못 선택하셨습니다. 다시시도해주세요.")
        print("Something went wrong. Please try again.")
        continue

print("UI 조작 커맨드가 실행됩니다. 기기의 연결을 해제하지 말고 잠시만 기다려주세요.")
print("Overscan Command will run. Please wait a moment, and DO NOT DISCONNECT DEVICE.\n")
print("/* 계속하려면 아무키나 누르십시오. */")
input("/* Press any key to continue. */\n")
failCount = 0
while(True):
    if failCount >= 3:
        print("여러번 작업을 시도하였으나, 실패하였습니다. 기기가 지원되지 않는 것 같습니다. 개발자에게 리포트해주세요.")
        print("Failed too many time. Device might be unsupported. Please contact developer.")
        print("Email : yymin1022@gmail.com\n")
        break
    else:
        try:
            subprocess.check_output([adb_path, 'shell', 'wm', 'overscan', applyValue])
        except subprocess.CalledProcessError:
            print("작업에 실패하였습니다. 다시시도합니다.")
            print("Failed. Trying again.\n")
            failCount += 1
            continue
        try:
            subprocess.check_output(appCommand)
        except subprocess.CalledProcessError:
            print("작업에 실패하였습니다. 다시시도합니다.")
            print("Failed. Trying again.\n")
            failCount += 1
            continue
        print("성공적으로 적용되었습니다. 기기가 재부팅됩니다.")
        print("Successfully applied. Device will be rebooted.\n")
        subprocess.check_output([adb_path, 'reboot'])
        break
subprocess.check_output([adb_path, 'kill-server'])

print("/* 계속하려면 아무키나 누르십시오. */")
input("/* Press any key to continue. */\n")
