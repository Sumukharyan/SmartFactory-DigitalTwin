import json
import random
import time

import paho.mqtt.client as mqtt

from app.mqtt.topics import FACTORY_TOPIC

BROKER = "localhost"
PORT = 1883

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.connect(BROKER, PORT)

print("Connected to MQTT Broker")

machines = [
    "CNC Machine",
    "Robot Arm",
    "Conveyor Belt",
    "Assembly Robot",
    "Packaging Unit"
]

machine_states = [
    "Running",
    "Idle",
    "Maintenance",
    "Fault"
]

while True:

    payload = {

        "machine": random.choice(machines),

        "temperature": round(random.uniform(25, 45), 2),

        "pressure": round(random.uniform(95, 110), 2),

        "humidity": round(random.uniform(40, 75), 2),

        "vibration": round(random.uniform(0.5, 6.5), 2),

        "status": random.choice(machine_states)

    }

    client.publish(
        FACTORY_TOPIC,
        json.dumps(payload)
    )

    print("=" * 60)

    print(json.dumps(payload, indent=4))

    time.sleep(3)