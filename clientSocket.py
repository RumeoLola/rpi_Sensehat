from flask import Flask, render_template, jsonify
from sense_hat import SenseHat
import threading
import time

app = Flask(__name__)
sense = SenseHat()

sensor_data = {
    'temperature': None,
    'pressure': None,
    'humidity': None
}


def update_sensor_data():
    while True:
        sense.clear()
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()

        for i in range(int(t) - 23):
            if i < 8:
                sense.set_pixel(1, 7-1, [255, 0, 0])
                # print(int(t)-23)
        for i in range(int(p/2) - 500):
            if i < 8:
                sense.set_pixel(3, 7-1, [0, 255, 0])
                # print(int(p/2)-500)
        for i in range(int(h) - 35):
            if i < 8:
                sense.set_pixel(5, 7-1, [0, 0, 255])
                # print(int(h)-35)

        time.sleep(10)
        sensor_data['temperature'] = f'{t:.2f}'
        sensor_data['pressure'] = f'{p:.2f}'
        sensor_data['humidity'] = f'{h:.2f}'
        time.sleep(10)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    threading.Thread(target=update_sensor_data, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)
