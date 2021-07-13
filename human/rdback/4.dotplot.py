# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""

Dotplot to reveal the relationship.

"""


# %%
import os, sys, glob
import numpy as np
import pandas as pd
import pyranges as pr
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats


# %%
zmat = pd.read_csv('ctcf_rad21_zmat.txt', sep='\t')
zmat.head()


# %%
zmat.shape


# %%
# mean of zscore for each column
# exclude first two rows

zscore_mean = zmat.drop([0,1]).mean(axis=0)
print(zscore_mean)
len(zscore_mean)


# %%
# peak number

## load bed files
bedpath = '../data/bed/ctcf.rad21/'
bedfile = glob.glob(os.path.join(bedpath,'*.bed'))
peaknum = []
for b in bedfile:
    bed = pr.read_bed(b)
    peaknum.append(len(bed))


# %%
print(peaknum)
len(peaknum)


# %%
#peaknum = np.repeat(peaknum, 2)
peaknum = peaknum + peaknum
peaknum


# %%
len(peaknum)
#type(peaknum)


# %%
min(peaknum)


# %%
zscore_mean


# %%
## plot
plt.figure(figsize=(8,6))

plt.title("Z-score vs peak number") #title
plt.xlabel("Z-sore") #x label
plt.ylabel("Peak number") #y label

sns.regplot(x=zscore_mean, y=peaknum, fit_reg=True, marker="o", color="skyblue")
for i in range(0, len(zscore_mean)):
     plt.text(x=zscore_mean[i]+0.1, y=peaknum[i]-2500,
          s=zscore_mean.index[i], horizontalalignment='center',
          fontsize=8, color='black')

plt.savefig('ctcf_rad21_zvsp.pdf')
plt.show()


# %%
## plot
plt.figure(figsize=(8,6))

plt.title("Peak number vs Z-score") #title
plt.ylabel("Z-sore") #x label
plt.xlabel("Peak number") #y label

plt.xlim((50000, 160000))
#plt.ylim((-2, 2))

sns.regplot(x=peaknum, y=zscore_mean, fit_reg=True, marker="o", color="skyblue")
for i in range(0, len(zscore_mean)):
     plt.text(x=peaknum[i]-2000, y=zscore_mean[i]-0.2,
          s=zscore_mean.index[i], fontsize=8, color='black')

plt.savefig('ctcf_rad21_pknum_zs.pdf')
#plt.margins(0.1)
plt.show()


# %%
## test the correlation 
scipy.stats.pearsonr(zscore_mean, peaknum)


# %%
scipy.stats.spearmanr(zscore_mean, peaknum)


# %%
scipy.stats.kendalltau(zscore_mean, peaknum)


