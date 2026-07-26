import paho.mqtt.client as mqtt

from app.database.session import SessionLocal
from app.mqtt.topics import TEMPERATURE_TOPIC
from app.services.mqtt_service import save_temperature

BROKER = "localhost"
PORT = 1883


def on_connect(client, userdata, flags, reason_code, properties=None):
    print("Connected to MQTT Broker")

    client.subscribe(TEMPERATURE_TOPIC)

    print(f"Subscribed to {TEMPERATURE_TOPIC}")


def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())

    print(f"Received Temperature: {temperature} °C")

    db = SessionLocal()

    try:
        save_temperature(db, temperature)
        print("Saved to PostgreSQL")
    finally:
        db.close()


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)

client.loop_forever()