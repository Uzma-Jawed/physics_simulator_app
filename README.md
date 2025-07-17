---

![banner](banner.png)

---

### ✨ Key Features

- 🔸 Simulate 1D and 2D (projectile) motion using kinematic equations
- 🔸 Compare two objects side-by-side
- 🔸 Watch real-time **1D motion animation**
- 🔸 Upload CSV to simulate multiple bodies at once
- 🔸 Clean, interactive **Streamlit web interface**
- 🔸 Includes history log for previous simulations

---

### 📂 File Structure

physics-motion-simulator/

├── app.py # Main Streamlit app

├── main.py

├── motion.py # Physics logic (Body class)

├── simulator.py # Simulation functions

├── utils.py # History handling

├── requirements.txt # Python dependencies

├── data/

│ └── history.json # Saved results

├── banner.png

└── README.md

---

### 📐 Physics Formulas Used

These are the core kinematic equations implemented in the simulator:

### ▶️ 1D Motion (Straight Line)

- **Final Velocity:**  
  \[ v = u + at \]

- **Distance Travelled:**  
  \[ s = ut + 1/2*at^2 \]

- **Velocity Squared:**  
  \[ v^2 = u^2 + 2as \]

---

### 🏹 2D Projectile Motion

Horizontal Distance (x). 

x = uₓ * t

Vertical Distance (y). 

y = uᵧ * t - (1/2) * g * t²


✨Concepts Used

🔸Python Classes & OOP

🔸Kinematics Equations

🔸NumPy & Matplotlib

🔸Streamlit for UI

🔸File handling (JSON, CSV)
___

✨Made by Uzma Jawed
---

### ▶️ Run It Locally

```bash
git clone https://github.com/Uzma-Jawed/physics-motion-simulator.git
cd physics-motion-simulator
pip install -r requirements.txt
streamlit run app.py
