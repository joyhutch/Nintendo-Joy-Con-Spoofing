# Nintendo-Joy-Con-Spoofing

## Referenced Repositories
- https://github.com/dekuNukem/Nintendo_Switch_Reverse_Engineering
- https://github.com/JSnowden33/Wii-Bluetooth-Replacement
- https://github.com/ricardoquesada/bluepad32
- https://github.com/mart1nro/joycontrol
- https://github.com/Poohl/joycontrol
- https://github.com/lowlevel-1989/joytransfer

## bstack 
### connectivity in both bluepad & Wii-Bluetooth-Replacement use Btstack
- https://github.com/bluekitchen/btstack

## Neccessary Hardware
* ESP32 Board (not a newer model like ESP32-Sx)
* Switch Console with Joycon controllers


## Installation / Dependencies

$ sudo apt install python3 python3-dbus libhidapi-hidraw0 libbluetooth-dev 
$ sudo apt install pip
$ sudo pip3 install aioconsole hid dbus-python crc8 hidapi

$ git clone https://github.com/Poohl/joycontrol
$ pip install -e ./joycontrol
- '-e' parameter allows the joycontrol source code to be editing without needing to reinstall 

$ sudo -E env PATH=$PATH python joytransfer.py

