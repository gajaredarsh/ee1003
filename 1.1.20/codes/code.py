import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# ---------------------------------
# STEP 1: Solve using CVXPY
# ---------------------------------
Kp = cp.Variable()
Kd = cp.Variable()
wn = cp.Variable()

Kv = 1000
zeta = 0.5

constraints = [
    10 * Kp == Kv,
    wn == 100,   # avoids non-convexity
    2 * zeta * wn == 10 + 100 * Kd
]

prob = cp.Problem(cp.Minimize(0), constraints)
prob.solve()

Kp_val = Kp.value
Kd_val = Kd.value

print("CVXPY Solution:")
print("Kp =", Kp_val)
print("Kd =", Kd_val)

# ---------------------------------
# STEP 2: Define function
# ---------------------------------
def closed_loop(Kp, Kd):
    num = [100*Kd, 100*Kp]
    den = [1, 10, 0]
    G = ctrl.TransferFunction(num, den)
    return ctrl.feedback(G, 1)

t = np.linspace(0, 1, 1000)

# ---------------------------------
# STEP 3: Vary Kd (damping effect)
# ---------------------------------
Kd_vals = np.linspace(0.1, 2, 5)

plt.figure()
for Kd_i in Kd_vals:
    T = closed_loop(Kp_val, Kd_i)
    t_out, y = ctrl.step_response(T, t)
    plt.plot(t_out, y, label=f"Kd={Kd_i:.2f}")

plt.title("Effect of Kd (Damping Variation)")
plt.xlabel("Time")
plt.ylabel("Output")
plt.legend()
plt.grid()

# ---------------------------------
# STEP 4: Vary Kp (speed effect)
# ---------------------------------
Kp_vals = np.linspace(20, 200, 5)

plt.figure()
for Kp_i in Kp_vals:
    T = closed_loop(Kp_i, Kd_val)
    t_out, y = ctrl.step_response(T, t)
    plt.plot(t_out, y, label=f"Kp={Kp_i:.0f}")

plt.title("Effect of Kp (Speed Variation)")
plt.xlabel("Time")
plt.ylabel("Output")
plt.legend()
plt.grid()

# ---------------------------------
# STEP 5: Optimal vs Deviations
# ---------------------------------
cases = [
    (Kp_val, Kd_val, "Optimal"),
    (Kp_val, 0.2, "Low Kd"),
    (50, Kd_val, "Low Kp"),
    (200, Kd_val, "High Kp")
]

plt.figure()
for Kp_i, Kd_i, label in cases:
    T = closed_loop(Kp_i, Kd_i)
    t_out, y = ctrl.step_response(T, t)
    plt.plot(t_out, y, label=label)

plt.title("Optimal vs Non-Optimal Designs")
plt.xlabel("Time")
plt.ylabel("Output")
plt.legend()
plt.grid()

plt.show()
