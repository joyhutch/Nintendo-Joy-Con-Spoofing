# Updates

## Feb 13th

Met with the professor to confirm goals and get a better understanding of resources and hardware which may be necessary for the project

## March 18th
- Clone https://github.com/JSnowden33/Wii-Bluetooth-Replacement 
- Clone https://github.com/bluekitchen/btstack.git 
- In VSCode, we added an ESP-IDF extension called "PlatformIO IDE".
- Following instructions from https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/get-started-legacy/index.html to setup ESP32 (Note: platform we are using from Wii-Bluetooth-Replacement repo uses a legacy system of esp-idf, so we are doing the same)   
    - Step 1: Following instructions from https://docs.espressif.com/projects/esp-idf/en/v4.4/esp32/get-started-legacy/linux-setup.html, set up linux toolchain for 64-bit linux 
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
        -  

                