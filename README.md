# Adeept RaspTank Software

Example codes for Adeept RaspTank robot intended to work with [RaspTankOS](https://github.com/blkr35/meta-rasptank).

## 1. Install RaspTankOS

Follow instructions from https://github.com/blkr35/meta-rasptank to build the OS and copy the image on a SD card.

At boot, the IP address of the robot will be displayed to allow to connect using the WEB App or SSH.

## 2. WEB App service

In the console, you can check the status of the service with:
```
/etc/init.d/rasptank_service.sh status
```
You can stop/start it with:
```
/etc/init.d/rasptank_service.sh stop
/etc/init.d/rasptank_service.sh start
```

## 3. Controlling Robot via WEB App

- Raspberry Pi will auto run `server/server.py` when booting and run a web UI on the LAN to control the robot.

- When the service is running, the WS2812-LEDs light up with a breathing effect.    

- If the program is not running after boot, you can check the log file in `/var/log/rasptank.log` for more information.

- To connect to the web UI, type in the IP address of the Raspberry Pi port `5000` in you web browser, e.g.   

    > 192.168.3.161:5000  

- If the web UI doesn't show, try stop/start the service and check the logs as described above.  

- If the web UI is shown, check the description for keyboard shortcuts `Instruction` at the bottom and control the robot:   

- `Video` window shows the image captured by the robot's camera in real time.  

- `Move Control` window is to control the basic movements of the robot.   

- `Arm Control` window controls the servo movement. 
    - <kbd>GRAB</kbd>   <kbd>LOOSE</kbd>: Control the claws of the robotic arm to open and close
    - <kbd>HANDUP</kbd> <kbd>HANDDOWN</kbd>: Control the robotic arm to move up and down 
    - <kbd>LEFT</kbd>   <kbd>RIGHT</kbd>: Control the claws rotation of the robotic arm 

- `CVFL Control` window is to control the visual line following function of the robot. Here only an overview for the function is described; more details will be provided in the OpenCV section: 
    - <kbd>START</kbd>: Enable or disable the visual line following function. 
    - <kbd>COLOR</kbd>: Switch between white and black line following. By default the robot follows white lines; click the button to switch to black line following.
    - The line following function analyzes two pixels in parallel and utilizes the information detected; the positions of these two pixels are `L1` and `L2`.
    - `SP` is the threshold of the turning command based on the visual analysis results. A bigger `SP` value means a big deviation; though a particularly small `SP` value may stop the robot from moving as it can't aim the target and find the direction. 
    - When the visual line following function is enabled, the video screen will automatically become binarized results, making the visual analysis clearer.  

- `Hard Ware` window displays CPU temperature, CPU occupancy rate, and memory usage of the Raspberry Pi.  

- `Actions`window control unique functions of the robot: 
    - <kbd>MOTION GET</kbd>: Motion detection function based on OpenCV. When objects move in the view of the camera, the program will circle the part in the `Video` window, and the LED light on the robot will show respective changes. 
    - <kbd>AUTO MATIC</kbd>: Obstacle avoidance function based on ultrasonic. When the ultrasonic module on the robot detects an obstacle, it will automatically turn left, and take a step backward before turning if it's too close to the obstacle. 
    - <kbd>POLICE LIGHT</kbd>: WS2812-LED light control based on multithreading. It makes the WS2812-LED light on the robot blink red and blue alternately.
    - <kbd>TRACK LINE</kbd>: Line tracking function by using the 3-channel infrared module. By default it tracks black lines on a white surface (a white background that reflects infrared, and 1-cm wide black lines that do not reflects infrared). Performance of the line tracking varies from surface and line materials as well as the height of the robot chassis; you may need a cross screwdriver to adjust the potentiometer on the line tracking module.  

- `FC Control` window controls the color lock function of the robot:
    - <kbd>START</kbd>: Enable or disable color searching and tracking function.
    - <kbd>COLOR</kbd>: Select the color to track.
    - When the function is on, the robot will automatically lock one particular color in the camera view. By default it tracks bright yellow objects. You can change the color as you want. When an object is locked, the LED on the robot will turn orange. As the robot's head can only move up and down, the program does not involve tracking colors horizontally. If you have interest in this part, you may add the motor control based on the openCV section to realize effect.   

![webControl](images/webControl.png)

