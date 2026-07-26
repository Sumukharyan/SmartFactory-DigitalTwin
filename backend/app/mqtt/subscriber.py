import json

import paho.mqtt.client as mqtt

from app.database.session import SessionLocal

from app.services.machine_service import update_machine_status
from app.services.mqtt_service import save_sensor

from app.mqtt.topics import (
    TEMPERATURE_TOPIC,
    PRESSURE_TOPIC,
    VIBRATION_TOPIC,
    HUMIDITY_TOPIC,
    MACHINE_STATUS_TOPIC,
)

BROKER = "localhost"
PORT = 1883


def on_connect(client, userdata, flags, reason_code, properties=None):

    print("Connected to MQTT Broker")

    client.subscribe(TEMPERATURE_TOPIC)
    client.subscribe(PRESSURE_TOPIC)
    client.subscribe(VIBRATION_TOPIC)
    client.subscribe(HUMIDITY_TOPIC)
    client.subscribe(MACHINE_STATUS_TOPIC)

    print("Subscribed to all factory topics")


def on_message(client, userdata, msg):

    topic = msg.topic

    payload = msg.payload.decode()

    db = SessionLocal()

    try:

        if topic == TEMPERATURE_TOPIC:

            save_sensor(
                db,
                "Temperature",
                float(payload),
                "°C"
            )

            print(f"🌡 Temperature : {payload} °C")

        elif topic == PRESSURE_TOPIC:

            save_sensor(
                db,
                "Pressure",
                float(payload),
                "kPa"
            )

            print(f"📈 Pressure : {payload} kPa")

        elif topic == VIBRATION_TOPIC:

            save_sensor(
                db,
                "Vibration",
                float(payload),
                "mm/s"
            )

            print(f"📳 Vibration : {payload} mm/s")

        elif topic == HUMIDITY_TOPIC:

            save_sensor(
                db,
                "Humidity",
                float(payload),
                "%"
            )

            print(f"💧 Humidity : {payload} %")

        elif topic == MACHINE_STATUS_TOPIC:

            machine_data = json.loads(payload)

            update_machine_status(
                db,
                machine_data["machine"],
                machine_data["status"]
            )

            print()
            print("⚙ Machine Update")
            print(f"Machine : {machine_data['machine']}")
            print(f"Status  : {machine_data['status']}")

    except Exception as e:

        print(f"Error: {e}")

    finally:

        db.close()


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect

client.on_message = on_message

client.connect(BROKER, PORT)

client.loop_forever()