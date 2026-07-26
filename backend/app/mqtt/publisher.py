import json
import random
import time

import paho.mqtt.client as mqtt

from app.mqtt.topics import (
    TEMPERATURE_TOPIC,
    PRESSURE_TOPIC,
    VIBRATION_TOPIC,
    HUMIDITY_TOPIC,
    MACHINE_STATUS_TOPIC,
)

BROKER = "localhost"
PORT = 1883

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.connect(BROKER, PORT)

print("Connected to MQTT Broker")

machine_states = [
    "Running",
    "Idle",
    "Maintenance",
    "Fault"
]

machines = [
    "CNC Machine",
    "Robot Arm",
    "Conveyor Belt"
]

while True:

    temperature = round(random.uniform(25, 45), 2)

    pressure = round(random.uniform(95, 110), 2)

    vibration = round(random.uniform(0.5, 6.5), 2)

    humidity = round(random.uniform(40, 75), 2)

    machine = random.choice(machines)

    status = random.choice(machine_states)

    machine_payload = {
        "machine": machine,
        "status": status
    }

    client.publish(TEMPERATURE_TOPIC, str(temperature))
    client.publish(PRESSURE_TOPIC, str(pressure))
    client.publish(VIBRATION_TOPIC, str(vibration))
    client.publish(HUMIDITY_TOPIC, str(humidity))
    client.publish(
        MACHINE_STATUS_TOPIC,
        json.dumps(machine_payload)
    )

    print("=" * 60)

    print(f"🌡 Temperature : {temperature} °C")
    print(f"📈 Pressure    : {pressure} kPa")
    print(f"📳 Vibration   : {vibration} mm/s")
    print(f"💧 Humidity    : {humidity} %")
    print(f"⚙ Machine     : {machine}")
    print(f"📍 Status      : {status}")

    time.sleep(3)