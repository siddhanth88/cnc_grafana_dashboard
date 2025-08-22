import time
import random
import psycopg2
from datetime import datetime, timezone

try:
    conn = psycopg2.connect(
        dbname="cnc_metrics_v2",
        user="----",
        password="-----",
        host="localhost",
        port=5434
    )
    cur = conn.cursor()
    machines = ["haas_demo", "okuma_demo", "doosan_demo"]

    print("[INFO] Writing dummy CNC data to 'cnc_metrics_v2'...")
    while True:
        for machine in machines:
            spindle_speed = random.choice([random.randint(1000, 6000), 0])
            power_state = "ON" if spindle_speed > 0 else "OFF"
            try:
                cur.execute(
                    "INSERT INTO spindle_data (time, machine, spindle_speed, power_state) VALUES (%s, %s, %s, %s)",
                    (datetime.now(timezone.utc), machine, spindle_speed, power_state)
                )
                conn.commit()
                print(f"[{datetime.now().strftime('%H:%M:%S')}] {machine}: {power_state} — {spindle_speed} RPM")
            except Exception as db_err:
                print(f"[DB INSERT ERROR] {db_err}")
                conn.rollback()
        time.sleep(5)
except Exception as e:
    print(f"[DB ERROR] {e}")

