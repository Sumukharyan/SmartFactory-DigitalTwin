import json

import paho.mqtt.client as mqtt

from app.database.session import SessionLocal

from app.services.machine_service import update_machine_status
from app.services.mqtt_service import save_sensor

from app.mqtt.topics import FACTORY_TOPIC


BROKER = "localhost"
PORT = 1883


def on_connect(client, userdata, flags, reason_code, properties=None):

    print("Connected to MQTT Broker")

    client.subscribe(FACTORY_TOPIC)

    print("Subscribed to factory/data")


def on_message(client, userdata, msg):

    db = SessionLocal()

    try:

        sensor_data = json.loads(msg.payload.decode())

        update_machine_status(
            db,
            sensor_data["machine"],
            sensor_data["status"]
        )

        save_sensor(
            db,
            sensor_data
        )

        print("=" * 60)

        print(f"Machine      : {sensor_data['machine']}")
        print(f"Temperature  : {sensor_data['temperature']} °C")
        print(f"Pressure     : {sensor_data['pressure']} kPa")
        print(f"Humidity     : {sensor_data['humidity']} %")
        print(f"Vibration    : {sensor_data['vibration']} mm/s")
        print(f"Status       : {sensor_data['status']}")

    except Exception as e:

        print(f"Error : {e}")

    finally:

        db.close()


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect

client.on_message = on_message

client.connect(BROKER, PORT)

client.loop_forever()