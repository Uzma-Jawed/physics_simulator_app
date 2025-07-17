# main.py

from motion import Body
from simulator import simulate_motion
from utils import save_to_history
import pandas as pd

# Create a test object
obj = Body("Test Object", 1.0, 5.0, 2.0, 4)

# Get summary and print
summary = obj.get_summary()
print("=== Summary ===")
print(summary)

# Save to history
save_to_history(summary)

# Simulate motion
results = simulate_motion(obj)

# Create and show DataFrame
df = pd.DataFrame({
    "Time (s)": results["time"],
    "Velocity (m/s)": results["velocity"],
    "Position (m)": results["position"]
})

print("\n=== Motion Table ===")
print(df.head())