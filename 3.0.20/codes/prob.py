from fractions import Fraction

# Box compositions (total = 5)
# B1: 2 red, 3 white
# B2: 3 red, 2 white

R1, W1 = 2, 3
R2, W2 = 3, 2

T1 = R1 + W1  # = 5
T2 = R2 + W2  # = 5

# Probability of selecting boxes
P_B1 = Fraction(4, 6)  # even + 5
P_B2 = Fraction(2, 6)

# Function for different colours (with replacement)
def prob_different(R, W, T):
    return 2 * Fraction(R, T) * Fraction(W, T)

# Compute probabilities
P_diff_B1 = prob_different(R1, W1, T1)
P_diff_B2 = prob_different(R2, W2, T2)

# Total probability
P_total = P_B1 * P_diff_B1 + P_B2 * P_diff_B2

# Output
print("P(different colours) =", P_total)
