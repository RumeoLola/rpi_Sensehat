from sense_hat import SenseHat
import time

sense = SenseHat()

while 1:
    sense.clear()
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    for i in range(int(t) - 23):
        if i < 8:
            sense.set_pixel(1, 7-1, [255, 0, 0])
            print(int(t)-23)

    for i in range(int(p/2) - 500):
        if i < 8:
            sense.set_pixel(3, 7-1, [0, 255, 0])
            print(int(p/2)-500)

    for i in range(int(h) - 35):
        if i < 8:
            sense.set_pixel(5, 7-1, [0, 0, 255])
            print(int(h)-35)

    time.sleep(10)
