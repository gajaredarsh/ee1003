import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

Kp = 100
Kd = 0.9

num = [100*Kd, 100*Kp]
den = [1, 10, 0]

G = ctrl.TransferFunction(num, den)

# Use proper function
omega, mag, phase = ctrl.frequency_response(G)

# Plot manually
plt.figure()

plt.semilogx(omega, 20 * np.log10(abs(mag)))
plt.title("Bode Plot - Magnitude")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.savefig('../figs/bodem.png')

plt.figure()
plt.semilogx(omega, np.degrees(phase))
plt.title("Phase")
plt.ylabel("Phase (deg)")
plt.xlabel("Frequency (rad/s)")
plt.grid()

plt.savefig('../figs/bodef.png')
