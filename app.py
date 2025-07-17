# app.py

import streamlit as st
import pandas as pd
from motion import Body
from simulator import simulate_motion, simulate_projectile_motion
from utils import save_to_history, get_history
import matplotlib.pyplot as plt
import time
import streamlit.components.v1 as components
import io

st.set_page_config(page_title="Physics Motion Simulator", layout="centered")
st.markdown("<h1 style='text-align: center;'>🌠 Physics Motion Simulator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Simulate 1D motion using kinematic equations 📈</p>", unsafe_allow_html=True)

# Select Mode
motion_type = st.radio("Select Motion Type", ["1D Motion", "Projectile Motion (2D)"])
compare_mode = st.checkbox("✨ Compare Two Objects")

st.subheader("📁 Upload CSV for Batch Simulation")
csv_file = st.file_uploader("Upload a CSV file with columns: name, mass, initial_velocity, acceleration, time", type=["csv"])

if csv_file:
    df_csv = pd.read_csv(csv_file)
    summary_list = []

    for index, row in df_csv.iterrows():
        try:
            body = Body(
                name=row["name"],
                mass=float(row["mass"]),
                initial_velocity=float(row["initial_velocity"]),
                acceleration=float(row["acceleration"]),
                time=float(row["time"])
            )
            summary = body.get_summary()
            summary_list.append(summary)
        except Exception as e:
            st.error(f"⚠️ Error in row {index+1}: {e}")

    if summary_list:
        st.success(f"✅ Simulated {len(summary_list)} objects!")
        st.subheader("📊 Batch Summary Table")
        st.dataframe(pd.DataFrame(summary_list))

# Input Form
with st.form("motion_form"):
    st.subheader("🎯 Enter Object Parameters")

    if compare_mode:
        st.markdown("### 🧍 Object A")
        col1, col2 = st.columns(2)
        with col1:
            name_a = st.text_input("Name A", "Object A")
            mass_a = st.number_input("Mass A (kg)", value=1.0)
            u_a = st.number_input("Initial Velocity A (m/s)", value=5.0)
        with col2:
            a_a = st.number_input("Acceleration A (m/s²)", value=2.0)
            t_a = st.number_input("Time A (s)", value=5.0)

        st.markdown("### 🧍 Object B")
        col3, col4 = st.columns(2)
        with col3:
            name_b = st.text_input("Name B", "Object B")
            mass_b = st.number_input("Mass B (kg)", value=1.0)
            u_b = st.number_input("Initial Velocity B (m/s)", value=10.0)
        with col4:
            a_b = st.number_input("Acceleration B (m/s²)", value=1.0)
            t_b = st.number_input("Time B (s)", value=5.0)

    elif motion_type == "1D Motion":
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Object Name", "Ball")
            mass = st.number_input("Mass (kg)", min_value=0.1, value=1.0)
            u = st.number_input("Initial Velocity (m/s)", value=0.0)
        with col2:
            a = st.number_input("Acceleration (m/s²)", value=9.8)
            t = st.number_input("Time Duration (s)", min_value=0.1, value=5.0)

    elif motion_type == "Projectile Motion (2D)":
        u = st.number_input("Initial Speed (m/s)", value=10.0)
        angle = st.slider("Launch Angle (degrees)", 0, 90, 45)
        t = st.number_input("Time Duration (s)", min_value=0.1, value=5.0)

    submitted = st.form_submit_button("🌠 Run Simulation")

# Handle Simulation
if submitted:
    if compare_mode:
        body_a = Body(name_a, mass_a, u_a, a_a, t_a)
        body_b = Body(name_b, mass_b, u_b, a_b, t_b)

        results_a = simulate_motion(body_a)
        results_b = simulate_motion(body_b)

        df_a = pd.DataFrame({
            "Time (s)": results_a["time"],
            f"Velocity - {name_a} (m/s)": results_a["velocity"],
            f"Position - {name_a} (m)": results_a["position"]
        })

        df_b = pd.DataFrame({
            "Time (s)": results_b["time"],
            f"Velocity - {name_b} (m/s)": results_b["velocity"],
            f"Position - {name_b} (m)": results_b["position"]
        })

        df_compare = pd.merge(df_a, df_b, on="Time (s)", how="outer")

        st.subheader("📊 Comparison Table")
        st.dataframe(df_compare)

        st.subheader("📉 Velocity Comparison")
        st.line_chart(df_compare.set_index("Time (s)")[
            [f"Velocity - {name_a} (m/s)", f"Velocity - {name_b} (m/s)"]
        ])

        st.subheader("📏 Position Comparison")
        st.line_chart(df_compare.set_index("Time (s)")[
            [f"Position - {name_a} (m)", f"Position - {name_b} (m)"]
        ])

    elif motion_type == "1D Motion":
        body = Body(name, mass, u, a, t)
        summary = body.get_summary()
        save_to_history(summary)

        st.subheader("📊 Summary")
        st.json(summary)

        results = simulate_motion(body)
        df = pd.DataFrame({
            "Time (s)": results["time"],
            "Velocity (m/s)": results["velocity"],
            "Position (m)": results["position"]
        })

        st.subheader("📈 Motion Table")
        st.dataframe(df)
        st.subheader("📉 Velocity vs Time")
        st.line_chart(df.set_index("Time (s)")["Velocity (m/s)"])
        st.subheader("📏 Position vs Time")
        st.line_chart(df.set_index("Time (s)")["Position (m)"])

    # ✅ Show animation option for 1D motion
    if st.checkbox("🎞️ Show 1D Motion Animation"):
        st.subheader("🎬 Animation: Object Moving in 1D")

        fig, ax = plt.subplots()
        ax.set_xlim(0, max(df["Position (m)"]) + 5)
        ax.set_ylim(-1, 1)
        ax.set_xlabel("Position (m)")
        ax.set_title("1D Motion Animation")

        obj, = ax.plot([], [], "ro", markersize=12)

        frame = st.empty()

        for pos in df["Position (m)"]:
            obj.set_data(pos, 0)
            buf = io.BytesIO()
            fig.savefig(buf, format="png")
            frame.image(buf.getvalue(), use_column_width=True)
            time.sleep(0.1)


    elif motion_type == "Projectile Motion (2D)":
        results = simulate_projectile_motion(u, angle, t)
        df_proj = pd.DataFrame({
            "Time (s)": results["time"],
            "X Position (m)": results["x"],
            "Y Position (m)": results["y"]
        })

        st.subheader("🧮 Projectile Motion Table")
        st.dataframe(df_proj)
        st.subheader("📐 Trajectory: X vs Y")
        st.line_chart(df_proj.set_index("X Position (m)")["Y Position (m)"])

# View history
if st.checkbox("📂 View Simulation History"):
    st.subheader("📜 Previous Simulations")
    history = get_history()
    if history:
        st.dataframe(pd.DataFrame(history))
    else:
        st.info("No history yet.")