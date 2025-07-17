# simulator.py
import numpy as np

def simulate_motion(body, time_step=0.1):
    total_time = body.t
    times = np.arange(0, total_time + time_step, time_step)
    velocities = body.u + body.a * times
    positions = body.u * times + 0.5 * body.a * (times ** 2)

    return {
        "time": times,
        "velocity": velocities,
        "position": positions
    }

def simulate_projectile_motion(initial_velocity, angle_deg, total_time, time_step=0.1, g=9.8):
    angle_rad = np.radians(angle_deg)
    u_x = initial_velocity * np.cos(angle_rad)
    u_y = initial_velocity * np.sin(angle_rad)

    times = np.arange(0, total_time + time_step, time_step)
    x_positions = u_x * times
    y_positions = u_y * times - 0.5 * g * times**2

    return {
        "time": times,
        "x": x_positions,
        "y": y_positions
    }