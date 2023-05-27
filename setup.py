#!/usr/bin/python3
# File name   : setup.py
# Author      : Adeept
# Date        : 2020/3/14

import os
import time

os.environ["ENV PIP_ROOT_USER_ACTION"]="ignore"
curpath = os.path.realpath(__file__)
thisPath = "/" + os.path.dirname(curpath)

def replace_num(file,initial,new_num):
    newline=""
    str_num=str(new_num)
    with open(file,"r") as f:
        for line in f.readlines():
            if(line.find(initial) == 0):
                line = (str_num+'\n')
            newline += line
    with open(file,"w") as f:
        f.writelines(newline)


def add_file(file, atxt):
    str_atxt=str(atxt)
    with open(file,"a") as f:
      f.write("\n"+atxt+"\n")


def configure_wifi():
    print("Configuring WPA2...")
    ssid=input('What is the name of your wifi network (SSID)?\n')
    pwd=input('What is the wifi password?\n')
    content="network={{\nssid=\"{}\"\nproto=WPA2\nkey_mgmt=WPA-PSK\npairwise=CCMP TKIP\nscan_ssid=1\npsk=\"{}\"\npriority=10\n}}".format(ssid, pwd)
    add_file("/etc/wpa_supplicant.conf", content)

    
configure_wifi()

commands_1 = [
    "pip3 install -U pip",
    "pip3 install --upgrade luma.oled",
    "pip3 install adafruit-pca9685",
    "pip3 install rpi_ws281x",
    "pip3 install mpu6050-raspberrypi",
    "pip3 install flask",
    "pip3 install flask_cors",
    "pip3 install websockets",
]

mark_1 = 0
for x in range(3):
    for command in commands_1:
        if os.system(command) != 0:
            print("Error running installation step 1")
            mark_1 = 1
    if mark_1 == 0:
        break


commands_2 = [
    "pip3 install RPi.GPIO",
    "pip3 install -r " + thisPath + "/server/requirements.txt",
    "git clone https://github.com/oblique/create_ap",
    "cd " + thisPath + "/create_ap && sudo make install",
]

mark_2 = 0
for x in range(3):
    for command in commands_2:
        if os.system(command) != 0:
            print("Error running installation step 2")
            mark_2 = 1
    if mark_2 == 0:
        break

commands_3 = [
    "pip3 install numpy",
    #"pip3 install opencv-contrib-python==3.4.11.45",
    "pip3 install opencv-contrib-python",
    "pip3 install imutils zmq pybase64 psutil"
]

mark_3 = 0
for x in range(3):
    for command in commands_3:
        if os.system(command) != 0:
            print("Error running installation step 3")
            mark_3 = 1
    if mark_3 == 0:
        break


#try:
#    replace_num("/boot/config.txt", '#dtparam=i2c_arm=on','dtparam=i2c_arm=on\nstart_x=1\n')
#except:
#    print('Error updating boot config to enable i2c. Please try again.')



try:
    os.system('sudo touch ' + thisPath + '/startup.sh')
    with open(thisPath + "/startup.sh",'w') as file_to_write:
        #you can choose how to control the robot
        file_to_write.write("#!/bin/sh\nifup wlan0\nmodprobe i2c_dev\npython3 " + thisPath + "/server/webServer.py")
except:
    pass


os.system('chmod 777 ' + thisPath + '/startup.sh')

replace_num('/etc/rc.local','fi','fi\n' + thisPath + '/startup.sh start')

try: #fix conflict with onboard Raspberry Pi audio
    os.system('touch /etc/modprobe.d/snd-blacklist.conf')
    with open("/etc/modprobe.d/snd-blacklist.conf",'w') as file_to_write:
        file_to_write.write("blacklist snd_bcm2835")
except:
    pass
try:
    os.system("cp -f "+ thisPath  +"/server/config.txt //etc/config.txt")
except:
    os.system("cp -f "+ thisPath  +"/server/config.txt //etc/config.txt")
print('The program in Raspberry Pi has been installed, disconnected and restarted. \nYou can now power off the Raspberry Pi to install the camera and driver board (Robot HAT). \nAfter turning on again, the Raspberry Pi will automatically run the program to set the servos port signal to turn the servos to the middle position, which is convenient for mechanical assembly.')
print('restarting...')
os.system("reboot")
