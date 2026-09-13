import paho.mqtt.client as mqtt
import json

broker_host = "localhost"
broker_port = 1883
topic = "enterprise/iot/telemetry"

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected to broker with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"Received Telemetry -> Device: {payload['device_id']} | Temp: {payload['temperature']}°C | Humidity: {payload['humidity']}%")
    except Exception as e:
        print(f"Failed to parse message: {e}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "sensor_subscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_host, broker_port, 60)

print("Starting sensor subscriber... Press Ctrl+C to stop.")
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Subscriber stopped.")
    client.disconnect()
