#!/usr/bin/python3
# File name   : setup.py
# Author      : Adeept
# Date        : 2020/3/14

import os
import time

os.environ["PIP_ROOT_USER_ACTION"]="ignore"
curpath = os.path.realpath(__file__)
thisPath = "/" + os.path.dirname(curpath)

if not os.popen('uname -n').read().strip() == 'rasptank':
    print("This script can only run on RaspTank OS")
    os.exit()


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
    print("Configuring WiFi WPA2...")
    ssid=input('Enter network name (SSID):\n')
    pwd=input('Enter password:\n')
    content="network={{\nssid=\"{}\"\nproto=WPA2\nkey_mgmt=WPA-PSK\npairwise=CCMP TKIP\nscan_ssid=1\npsk=\"{}\"\npriority=10\n}}".format(ssid, pwd)
    add_file("/etc/wpa_supplicant.conf", content)


print("***********************************************")
print("Installing Adeept RaspTank Software Stack...")


if not os.path.isfile("//.rasptank_wifi"):
    configure_wifi()
    os.system('touch //.rasptank_wifi')
else:
    print("WiFi WPA2 is already configured. Remove the file /.rasptank_wifi to reconfigure it.")


if not os.path.isfile("//etc/init.d/rasptank_service.sh"):
    print("Configuring service... If sucessful, the device will reboot and install the software stack.")
    time.sleep(3)
    try:
        os.system("cp -f "+ thisPath  +"/rasptank_service.sh //etc/init.d/")
        os.system("update-rc.d rasptank_service.sh defaults")
        os.system("reboot")
        os.exit()
    except:
        print("Error: installation service could not be configured.")
else:
    print("RaspTank service is already configured.")
    if not os.path.isfile("//.rasptank_install_in_progress"):
        os.system('touch //.rasptank_install_in_progress')
        print("Rebooting now to finish installation...")
        os.system("reboot")
        os.exit()


try:
    replace_num("/boot/config.txt", '#dtparam=i2c_arm=off','dtparam=i2c_arm=on\nstart_x=1\n')
except:
    print('Error updating boot config to enable i2c. Please try again.')


try: #fix conflict with onboard Raspberry Pi audio
    os.system('touch /etc/modprobe.d/snd-blacklist.conf')
    with open("/etc/modprobe.d/snd-blacklist.conf",'w') as file_to_write:
        file_to_write.write("blacklist snd_bcm2835")
except:
    pass

try:
    os.system("cp -f "+ thisPath  +"/server/config.txt //etc/config.txt")
except:
    pass

# Enable splash screen on boot
try:
    os.system("mv /etc/rcS.d/S00psplash.sh /etc/rcS.d/S40psplash.d")
except:
    pass

# Display IP address on tty
try:
    with open("/etc/issue") as issuef:
       if not 'IP address' in issuef.read():
           os.system("echo \"IP address: \\4\" >> /etc/issue")
except:
    pass

os.system('touch //.rasptank_installed')
os.system('rm //.rasptank_install_in_progress')

print('Update/Installation complete. \nIf not assembled already, you can now power off the Raspberry Pi to install the camera and driver board (Robot HAT). \nAfter turning on again, the Raspberry Pi will automatically run the program to set the servos port signal to turn the servos to the middle position, which is convenient for mechanical assembly.')
print('Restarting...')

time.sleep(3)
os.system("reboot")
os.exit()

