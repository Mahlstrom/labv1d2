import time
import random
import redis
from pymongo import MongoClient

def main():
    r = redis.Redis(host='redis', port=6379)
    mongo = MongoClient('mongo', 27017)
    db = mongo['iot']
    events = db['sensor_events']

    print("Simulerar sensor-data. Tryck Ctrl+C för att stoppa.")
    while True:
        data = {
            "device_id": "sensor1",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "temperature": round(random.uniform(20, 25), 2),
            "gps": {"lat": 59.3, "lon": 18.1},
            "vibration": round(random.uniform(0, 0.05), 3)
        }
        # Spara senaste temperatur i Redis
        r.set("sensor1:temperature", data["temperature"])
        # Spara hela eventet i MongoDB
        events.insert_one(data)
        print(f"Skickat data: {data}")
        time.sleep(5)

if __name__ == "__main__":
    main()
