import paho.mqtt.client as mqtt
import time
import json
import random

broker_host = "localhost"
broker_port = 1883
topic = "enterprise/iot/telemetry"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "sensor_simulator")
client.connect(broker_host, broker_port, 60)

print("Starting sensor publisher... Press Ctrl+C to stop.")
try:
    while True:
        payload = {
            "device_id": "sensor-edge-01",
            "temperature": round(random.uniform(20.0, 35.0), 2),
            "humidity": round(random.uniform(40.0, 80.0), 2),
            "timestamp": int(time.time())
        }
        client.publish(topic, json.dumps(payload))
        print(f"Published: {payload}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Publisher stopped.")
    client.disconnect()
