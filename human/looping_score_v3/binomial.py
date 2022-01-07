"""
binomial distribution
only when probability of each event

===USELESS===
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy import stats

## contacts called
# discrete outcomes
subed = pd.read_csv('subed_merge.txt', sep='\t', header=0) #don't work


n = 20
p = 0.05
# x = np.array(sorted([ int(f) for f in subed.iloc[:,0] ]))
x = np.arange(1, n+1)


## Construct PMF
binomial_pmf = binom.pmf(x, n, p)

print(binomial_pmf)

plt.plot(x, binomial_pmf, color='blue')
plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.show()

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(x, binomial_pmf, 'bo', ms=8, label='nbinom pmf')
ax.plot(x, binomial_pmf, 'bo', ms=8, label='nbinom pmf')
plt.ylabel("Probability", fontsize="18")
plt.xlabel("X - No. of Sales Call", fontsize="18")
plt.title("Negative Binomial Distribution - No. of Sales Call Vs Probability", fontsize="18")
ax.vlines(x, 0, binomial_pmf, colors='b', lw=5, alpha=0.5)

