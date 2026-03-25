import numpy as np

# number of simulations
N = 1_000_000

# simulate die rolls (1-6)
die = np.random.randint(1, 7, size=N)

# decide which box to use: True = B1, False = B2
use_B1 = (die % 2 == 0) | (die == 5)

# probabilities
# B1: P(R)=2/5, B2: P(R)=3/5
p_red = np.where(use_B1, 2/5, 3/5)

# draw two balls (with replacement)
draw1 = np.random.rand(N) < p_red
draw2 = np.random.rand(N) < p_red

# check if colors are different
different = draw1 != draw2

# estimate probability
prob = np.mean(different)

print("Estimated probability:", prob)
