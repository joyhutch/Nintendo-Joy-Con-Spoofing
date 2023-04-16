# Updates

## Feb 13th

Met with the professor to confirm goals and get a better understanding of resources and hardware which may be necessary for the project

## March 18th

- Clone <https://github.com/JSnowden33/Wii-Bluetooth-Replacement>
- Clone <https://github.com/bluekitchen/btstack.git>
- In VSCode, we added an ESP-IDF extension called "PlatformIO IDE".
- Following instructions from <https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/get-started-legacy/index.html> to setup ESP32 (Note: platform we are using from Wii-Bluetooth-Replacement repo uses a legacy system of esp-idf, so we are doing the same)
  - Step 1: Following instructions from <https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/get-started-legacy/linux-setup.html>, set up linux toolchain for 64-bit linux
    - ran pip install cryptography==2.7
    - downloaded ESP32 toolchain for 64-bit Linux
    - changing PATH variable
    - added current user to dialout group to makesure we don't get permission issues later
            while flashing ESP32
  - Step 2: cloned version 4.4 of esp-idf
  - Step 3 & 4:
    - removed the --user parameter (already in an vir-env)
      - running into
                ERROR: Failed building wheel for gevent
                ERROR: Could not build wheels ofr gevent, which is required to install pyproject.toml-based projects
      - solution steps
        - sudo apt install python2-devel
        - python3.10 -m venv "esp_venv"
                    create & activate a 3.10 virtual_env to run python3.10
        - sudo apt install python3-devel
        - sudo apt install python3.10-devel
      - now running the command in step 4 works
  - Step 5: Copy Wii-Bluetooth-Replacement Repo in
        Note: project directory looks like:
             esp-idf   esp_venv   xtensa-esp32-elf   Wii-Bluetooth-Replacement
  - Step 6: Connect device
    - by plugging and unplugging, we can see the ESP32 board is connected /dev/ttyUSB0
  - Step 7: configure
    - in WBR repo, run 'make menuconig'
    - in menu, navigate to 'Serial flasher config > Default serial port' and enter /dev/ttyUSB0 & save
  - Step 8: make flash
    - running into
            WARNING: Compiler version is not supported: 12.2.0
            Expected to see version(s): 8.4.0
    - solution steps - re do step 2 - 4, check 7
    - running into issues with lc3.h [LEFT OFF]

## March 21st

- Realized the legacy versions of ESP and btstack, specifically the latter, is no longer supported and so we switched to the newest versions of everything. This also required switching from GNUMake to CMake
- forked the Wii-Bluetooth-Replacement repo and isolated the esp32 part
- updated the build system so that everything could build correctly
- now running into issues due to some functionality in the repo being depricated

## March 25th

- uart_controller.c > line 186 uart_driver_install
    lines 187 - 191; commented out for now
    uart_isr_register() is depricated and does not exist
- make and flash to esp board [with error lines commented out]
- timer_group and timer.h depricated
- uart_controller.c seems to be mostly depricated, embarking on a new journey of completely rewriting this file
- fixed issues -- guess is that a config somewhere got messed up -- by copying code into clean repo and building until build ran correctly
- flash and run to board, printed "Joy-Con Connected!"
    [we have alot of code commented out and the code errors right after the print statement]
- fixed some errors & started to replace much of the deprecated code with the newest api

## April 1st

- successfully ran hid_mouse_demo in btstack/example
- switched to using new repo: <https://github.com/mart1nro/joycontrol.git>
- was able to connect controller to switch console, but connect exits everytime we leave
    the 'Change Grip/Order' menu
- joy used: <https://scribles.net/enabling-bluetooth-in-virtualbox/>
    to fix the bluetooth issues she was experiencing in virtualbox vm

## April 8th

- found some additional resources of people running into similar issues we were experiencing with the emulated controller being disconnected for unknown reasons
- ava was able to run new code that was able to reconnect the controller with the console after the connection is dropped
  - does not function reliably
- joy's bluetooth service on her vm has stopped working for some reason

## April 16th

- updating Ubuntu 20.4 to 22.4 to fix error
    `AttributeError: /lib/x86_64-linux-gnu/libhidapi-hidraw.so.0: undefined symbol: hid_get_input_report`
- in server.py in create_hid_server (line 23), requesting input() in async function funky
- **Note: while creating HidDevice, setting up a control and interupt socket, bind those for listening, set the name, set the HidDevice to being powered on and pairable, set HidDevice name, set profile path, set to discoverable, then set_class is called from device.py
  - sets the HidDevice class to '0x002508' which corresponds to a (Gamepad/Joystick)

- setting up vm
  - download 22.04 image
  - add user to sudoers
  - sudo apt-get install openssh-server
  - port forwarding in vm box settings
