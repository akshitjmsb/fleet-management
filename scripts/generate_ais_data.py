import pandas as pd
import random
from datetime import datetime, UTC
import os

def generate_fake_vessel_data(num_vessels=10):
    vessel_data = []
    for i in range(num_vessels):
        vessel_data.append({
            "vessel_id": f"VSL-{1000+i}",
            "name": f"Vessel-{chr(65+i)}",
            "latitude": round(random.uniform(-90, 90), 6),
            "longitude": round(random.uniform(-180, 180), 6),
            "speed_knots": round(random.uniform(0, 30), 2),
            "timestamp": datetime.now(UTC).isoformat()
        })
    return pd.DataFrame(vessel_data)

if __name__ == "__main__":
    os.makedirs("storage", exist_ok=True)  # ✅ Ensure storage/ folder exists
    df = generate_fake_vessel_data()
    df.to_csv("storage/fake_ais_data.csv", index=False)
    print("✅ AIS data generated and saved to storage/fake_ais_data.csv")

