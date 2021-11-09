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
# z-score matrix

zmat = pd.read_csv('zmat.txt', sep='\t')
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
# normed and subed loop number matrix

subed_r1 = pd.read_csv('subed_r1.txt', sep='\t')
subed_r2 = pd.read_csv('subed_r2.txt', sep='\t')


# %%
# merge subed matrix to one

subed = pd.concat([subed_r1, subed_r2], axis=1)
subed


# %%
# mean of loop number for each column
# exclude first two rows

loop_mean = subed.drop([0,1]).mean(axis=0)
print(loop_mean)
len(loop_mean)


# %%
# peak number

## load bed files
bedpath = '../data/bed/'
bedfile = glob.glob(os.path.join(bedpath,'*.bed'))

bedpath_ck = '../data/bed/ctcf.rad21/'
bedfile += glob.glob(os.path.join(bedpath_ck,'*.bed'))

peaknum = []
for b in bedfile:
    bed = pr.read_bed(b)
    peaknum.append(len(bed))


# %%
# print(peaknum)
len(peaknum)


# %%
#peaknum = np.repeat(peaknum, 2)
peaknum = peaknum + peaknum
peaknum


# %%
len(peaknum)
#type(peaknum)


# %%
## plot
# z-score vs peak number
plt.figure(figsize=(12,10))

plt.title("Z-score vs peak number") #title
plt.xlabel("Z-sore") #x label
plt.ylabel("Peak number") #y label

sns.regplot(x=zscore_mean, y=peaknum, fit_reg=True, marker="o", color="skyblue")
# for i in range(0, len(zscore_mean)):
     # plt.text(x=zscore_mean[i]+0.1, y=peaknum[i]-2500,
     #      s=zscore_mean.index[i], horizontalalignment='center',
     #      fontsize=8, color='black')

plt.savefig('tf_zvsp_rep.pdf')
plt.show()


# %%
## plot
# peak number vs z-score
plt.figure(figsize=(12,10))

plt.title("Peak number vs Z-score") #title
plt.xlabel("Peak number") #x label
plt.ylabel("Z-sore") #y label

plt.xlim((950, 160000))
#plt.ylim((-2, 2))

sns.regplot(x=peaknum, y=zscore_mean, fit_reg=True, marker="o", color="skyblue")
# for i in range(0, len(zscore_mean)):
#      plt.text(x=peaknum[i]-2000, y=zscore_mean[i]-0.2,
#           s=zscore_mean.index[i], fontsize=8, color='black')

plt.savefig('tf_pknum_zs_rep.pdf')
#plt.margins(0.1)
plt.show()


# %%
## plot
# peak number vs loop number
plt.figure(figsize=(12,10))

plt.title("Peak number vs Loop number") #title
plt.xlabel("Peak number") #x label
plt.ylabel("Loop number") #y label

plt.xlim((950, 160000))
#plt.ylim((-2, 2))

sns.regplot(x=peaknum, y=loop_mean, fit_reg=True, marker="o", color="skyblue")
# for i in range(0, len(loop_mean)):
#      plt.text(x=peaknum[i]-2000, y=loop_mean[i]-0.005,
#           s=loop_mean.index[i], fontsize=8, color='black')

plt.savefig('tf_pknum_lpnum_rep.pdf')
#plt.margins(0.1)
plt.show()


# %%
## test the correlation
# zscore vs peak number

print(scipy.stats.pearsonr(peaknum, zscore_mean))
print(scipy.stats.spearmanr(peaknum, zscore_mean))
print(scipy.stats.kendalltau(peaknum, zscore_mean))


# %%
# loop number vs zsocre 

print(scipy.stats.pearsonr(loop_mean, zscore_mean))
print(scipy.stats.spearmanr(loop_mean, zscore_mean))
print(scipy.stats.kendalltau(loop_mean, zscore_mean))


