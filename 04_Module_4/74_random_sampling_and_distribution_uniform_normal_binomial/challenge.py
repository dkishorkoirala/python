import numpy as np

fair_heads = np.random.binomial(1, 0.5, 1000).sum()
print("Fair coin heads count:", fair_heads)

# Biased coin (p=0.7)
biased_heads = np.random.binomial(1, 0.7, 1000).sum()
print("Biased coin heads count:", biased_heads)
