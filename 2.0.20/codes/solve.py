import numpy as np
import matplotlib.pyplot as plt

# Given values
p = 100
d = 60
Q = 300

# Derived values
t1 = Q / p
I_max = (Q/p)*(p - d)
t_end = t1 + I_max/d  # time when inventory hits zero

# Time axis (only until inventory becomes zero)
t = np.linspace(0, t_end, 200)

# Inventory function (no negative values)
inventory = np.piecewise(
    t,
    [t <= t1, t > t1],
    [lambda t: (p - d)*t,
     lambda t: I_max - d*(t - t1)]
)

# Plot
plt.figure()
plt.plot(t, inventory, linewidth=2)

# Mark key points
plt.scatter([0, t1, t_end], [0, I_max, 0], zorder=3)

# Annotate points
plt.text(0, 0, "(0,0)", fontsize=9, ha='left', va='bottom')
plt.text(t1, I_max, f"(3,120)", fontsize=9, ha='left', va='bottom')
plt.text(t_end, 0, f"(5,0)", fontsize=9, ha='right', va='top')

# Axes lines
plt.axhline(0)
plt.axvline(0)

# Labels
plt.xlabel("Time (days)")
plt.ylabel("Inventory (units)")
plt.title("Inventory vs Time (Non-negative EPQ Cycle)")

plt.xlim(0, t_end + 1)
plt.ylim(0, I_max + 20)

plt.grid()
plt.savefig("../figs/inventory.png")
plt.show()
