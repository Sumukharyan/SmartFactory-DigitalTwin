import random
import time

import paho.mqtt.client as mqtt

from app.mqtt.topics import TEMPERATURE_TOPIC

BROKER = "localhost"
PORT = 1883

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

client.connect(BROKER, PORT)

print("Connected to MQTT Broker")

while True:
    temperature = round(random.uniform(25.0, 45.0), 2)

    client.publish(TEMPERATURE_TOPIC, str(temperature))

    print(f"Published Temperature: {temperature} °C")

    time.sleep(2)