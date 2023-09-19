# Nintendo-Joy-Con-Spoofing
Welcome to the Nintendo Joy-Con Spoofing Project! This project, undertaken by Ava Silver and Joy Hutchison for CY4710 Security of Wireless Systems, under the guidance of Prof. Aanjhan Ranganathan, explores the fascinating world of Nintendo Switch controller spoofing. The mission was to understand the intricate communications between the Nintendo Switch console and its controllers, specifically the Joy-Con controllers, and create an emulated controller that could automate complex combos in games like Super Smash Bros. Ultimate.

## Referenced Repositories
- <https://github.com/dekuNukem/Nintendo_Switch_Reverse_Engineering>
<!-- - https://github.com/JSnowden33/Wii-Bluetooth-Replacement -->
<!-- - https://github.com/ricardoquesada/bluepad32 -->
- <https://github.com/mart1nro/joycontrol>
- <https://github.com/Poohl/joycontrol>
- <https://github.com/lowlevel-1989/joytransfer>

## bstack

### connectivity in both bluepad & Wii-Bluetooth-Replacement use Btstack

- <https://github.com/bluekitchen/btstack>

## Neccessary Hardware

- ESP32 Board (not a newer model like ESP32-Sx)

- Switch Console with Joycon controllers

## Installation / Dependencies

$ sudo apt install python3 python3-dbus libhidapi-hidraw0 libbluetooth-dev
$ sudo apt install pip
$ sudo pip3 install aioconsole hid dbus-python crc8 hidapi

$ git clone <https://github.com/Poohl/joycontrol>
$ pip install -e ./joycontrol

- '-e' parameter allows the joycontrol source code to be editing without needing to reinstall

$ sudo -E env PATH=$PATH python joyspoof.py

## Joy-Con Status Data Packet

19 81 03 38 00 92 00 31
0  1  2  3  4  5  6  7  [Bytes 0-8, Fixed Header]

00 00 e9 2e 30 7f 40 00
8  9  10 11 12 13 14 15

00 00 65 f7 81 00 00 00
16 17 18 19 20 21 22 23 [Bytes 16 & 17, Button Status]
                        [Byte 19, Joystick X value]
                        [Byte 20, Joystick Y value]

c0 23 01 e2 ff 3e 10 0a
24 25 26 27 28 29 30 31

00 d6 ff d0 ff 23 01 e1
32 33 34 35 36 37 38 39 [Bytes 33 & 34, Gyroscope Y value]
                        [Bytes 35 & 36, Gyroscope X val]
                        [Bytes 37 & 38, Accelerometer X value]
                        [Bytes 39 & 40, Accelerometer Y value]

ff 37 10 0a 00 d6 ff cf
40 41 42 43 44 45 46 47 [Bytes 41 & 42 Accelerometer Z value]

ff 29 01 dd ff 34 10 0a
48 49 50 51 52 53 54 55

00 d7 ff ce ff
56 57 58 59 60
