import numpy as np
import matplotlib.pyplot as plt

def simulate_system(K, N=30):
    n = np.arange(N)

    # Input
    x = np.zeros(N)
    x[0] = 1

    # Output
    y = np.zeros(N)

    for i in range(N):
        x1 = x[i-1] if i-1 >= 0 else 0
        x2 = x[i-2] if i-2 >= 0 else 0
        y1 = y[i-1] if i-1 >= 0 else 0
        y2 = y[i-2] if i-2 >= 0 else 0

        y[i] = x1 + x2 + K*y1 + K*y2

    return n, x, y


def plot_system(K):

    n, x, y = simulate_system(K)

    # impulse response
    g = np.zeros_like(n)
    if len(n) > 1:
        g[1] = 1
    if len(n) > 2:
        g[2] = 1

    # Input plot
    plt.figure()
    plt.stem(n, x)
    plt.title("Input (Impulse)")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid()
    plt.savefig("../figs/input.png")
    plt.close()

    # Impulse response plot
    plt.figure()
    plt.stem(n, g)
    plt.title("Impulse Response g[n]")
    plt.xlabel("n")
    plt.ylabel("g[n]")
    plt.grid()
    plt.savefig("../figs/impulse.png")
    plt.close()

    # Output plot
    plt.figure()
    plt.stem(n, y)
    plt.title(f"Output y[n] (K={K})")
    plt.xlabel("n")
    plt.ylabel("y[n]")
    plt.grid()
    plt.savefig("../figs/output1.png")
    plt.close()


# Run
plot_system(0.7)
