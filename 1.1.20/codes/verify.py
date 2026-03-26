import numpy as np
import control as ctrl

# -----------------------------
# Given solution
# -----------------------------
Kp = 100
Kd = 0.9

# -----------------------------
# Define open-loop system
# G(s) = 100(Kp + Kd s) / (s(s+10))
# -----------------------------
num = [100*Kd, 100*Kp]
den = [1, 10, 0]

G = ctrl.TransferFunction(num, den)

# -----------------------------
# 1. Verify Kv
# Kv = lim s->0 [sG(s)]
# -----------------------------
Kv = ctrl.dcgain(ctrl.TransferFunction([1, 0], [1]) * G)

print("Computed Kv =", Kv)

# -----------------------------
# 2. Closed-loop system
# -----------------------------
T = ctrl.feedback(G, 1)

# -----------------------------
# 3. Extract poles
# -----------------------------
poles = ctrl.poles(T)
print("Closed-loop poles:", poles)

# -----------------------------
# 4. Compute damping ratio
# -----------------------------
dominant_pole = poles[0]  # complex pole

zeta = -np.real(dominant_pole) / np.abs(dominant_pole)

print("Computed damping ratio =", zeta)

# -----------------------------
# 5. Natural frequency
# -----------------------------
wn = np.abs(dominant_pole)
print("Natural frequency =", wn)
