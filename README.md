# rpi_Sensehat
Raspberry Pi sense hat, monitor the weather in my room. Please refer to the clientSocket.py file to view the sense hat data through a socket using your rpi IP address. Also change port number if necessary.

Raspberry Pi 5                Sense HAT
+-----------------+          +-----------------+
|                 |          |                 |
|     Pin 1 (3.3V)+----------+3.3V Power       |
|                 |          |                 |
|     Pin 2 (5V)  +----------+5V Power         |
|                 |          |                 |
|     Pin 3 (GPIO 2)+--------+I2C SDA          |
|                 |          |                 |
|     Pin 4 (5V)  +----------+5V Power         |
|                 |          |                 |
|     Pin 5 (GPIO 3)+--------+I2C SCL          |
|                 |          |                 |
|     Pin 6 (GND) +----------+Ground           |
|                 |          |                 |
+-----------------+          +-----------------+
