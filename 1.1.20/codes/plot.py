import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Time
t = np.linspace(0, 5, 1000)

# ---------------------------------
# 1. Effect of Kv (Ramp Tracking)
# ---------------------------------
plt.figure()

Kv_values = [10, 100, 1000]

for Kv in Kv_values:
    # Type-1 system: G(s) = Kv / s
    G = ctrl.TransferFunction([Kv], [1, 0])
    T = ctrl.feedback(G, 1)

    # Ramp input
    t_out, y = ctrl.forced_response(T, t, t)

    plt.plot(t_out, y, label=f"Kv={Kv}")

# Ideal ramp
plt.plot(t, t, '--', label="Ideal (Reference)")

plt.title("Effect of Kv on Ramp Tracking")
plt.xlabel("Time")
plt.ylabel("Output")
plt.legend()
plt.grid()
plt.savefig('../figs/Kv')

# ---------------------------------
# 2. Effect of ζ (Damping)
# ---------------------------------
plt.figure()

zeta_values = [0.2, 0.5, 1.0]
wn = 5  # fixed natural frequency

for zeta in zeta_values:
    num = [wn**2]
    den = [1, 2*zeta*wn, wn**2]
    sys = ctrl.TransferFunction(num, den)

    t_out, y = ctrl.step_response(sys, t)

    plt.plot(t_out, y, label=f"zeta={zeta}")

plt.title("Effect of Damping Ratio (ζ) on Step Response")
plt.xlabel("Time")
plt.ylabel("Output")
plt.legend()
plt.grid()
plt.savefig('../figs/zeta')
plt.show()
