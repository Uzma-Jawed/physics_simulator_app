# motion.py

class Body:
    def __init__(self, name, mass, initial_velocity, acceleration, time):
        self.name = name
        self.mass = mass
        self.u = initial_velocity  # initial velocity
        self.a = acceleration      # acceleration
        self.t = time              # time

    def calculate_final_velocity(self):
        return self.u + self.a * self.t

    def calculate_distance(self):
        return self.u * self.t + 0.5 * self.a * (self.t ** 2)

    def calculate_velocity_squared(self):
        s = self.calculate_distance()
        return self.u ** 2 + 2 * self.a * s

    def get_summary(self):
        return {
            "Name": self.name,
            "Mass (kg)": self.mass,
            "Initial Velocity (m/s)": self.u,
            "Acceleration (m/s²)": self.a,
            "Time (s)": self.t,
            "Final Velocity (m/s)": round(self.calculate_final_velocity(), 2),
            "Distance Covered (m)": round(self.calculate_distance(), 2)
        }