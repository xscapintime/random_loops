# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""

Get z-score of each row

"""


# %%
import os, sys, glob
import numpy as np
import pandas as pd
import pyranges as pr


# %%
subed_r1 = pd.read_csv('ctcf_rad21_subed_r1.txt', sep='\t')
subed_r2 = pd.read_csv('ctcf_rad21_subed_r2.txt', sep='\t')


# %%
subed_r1.head()
subed_r2.head()


# %%
# merge two reps together

subed = pd.concat([subed_r1, subed_r2], axis=1)
subed.head()


# %%
# calculate the z-score for each row

rowmean = subed.mean(axis=1)
rowsd = subed.std(axis=1)


# %%
print(rowmean.head())
print(rowsd.head())


# %%
zmat = subed.sub(rowmean, axis=0).div(rowsd, axis=0)
zmat


# %%
zmat.to_csv("ctcf_rad21_zmat.txt", sep='\t', index=False)


