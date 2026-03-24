import matplotlib.pyplot as plt
import numpy as np

# ── Solve the problem ──────────────────────────────────────────
p, d, Q = 10, 4, 100          # example values (p > d)

t_p   = Q / p                 # production phase duration
I_max = (p - d) * t_p         # maximum cycle inventory  = Q(p-d)/p
T     = t_p + I_max / d       # total cycle time

print(f"  Parameters : p={p}, d={d}, Q={Q}")
print("  I_max = Q(p-d)/p = ", I_max)

# ── Plot ───────────────────────────────────────────────────────
t1   = np.linspace(0,   t_p, 300)
t2   = np.linspace(t_p, T,   300)
inv1 = (p - d) * t1
inv2 = I_max - d * (t2 - t_p)

fig, ax = plt.subplots(figsize=(5, 3))

ax.plot(t1, inv1, 'k-', linewidth=1.8)
ax.plot(t2, inv2, 'k-', linewidth=1.8)
ax.plot([t_p, t_p], [0, I_max], 'k--', linewidth=0.8)
ax.plot([0,   t_p], [I_max, I_max], 'k--', linewidth=0.8)

ax.set_xlabel(r'Time', fontsize=10)
ax.set_ylabel(r'Inventory', fontsize=10)
ax.set_xlim(0, T * 1.05)
ax.set_ylim(0, I_max * 1.25)
ax.set_xticks([0, t_p, T])
ax.set_xticklabels([r'$0$', r'$t_p$', r'$T$'], fontsize=9)
ax.set_yticks([0, I_max])
ax.set_yticklabels([r'$0$', r'$I_{\max}$'], fontsize=9)
ax.text(t_p * 0.28, I_max * 0.32, r'slope $= p - d$', fontsize=8)
ax.text(t_p * 1.12, I_max * 0.58, r'slope $= -d$',    fontsize=8)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('../figs/inventory.png')
