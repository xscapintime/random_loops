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
subed_r1 = pd.read_csv('subed_r1.txt', sep='\t')
subed_r2 = pd.read_csv('subed_r2.txt', sep='\t')


# %%
subed_r1.head()
subed_r2.head()


# %%
# calculate the z-score for each row
# z-score for each rep
# then concat together seems more resonable

rowmean_r1 = subed_r1.mean(axis=1)
rowmean_r2 = subed_r2.mean(axis=1)

rowsd_r1 = subed_r1.std(axis=1)
rowsd_r2 = subed_r2.std(axis=1)


# %%
zmat_r1 = subed_r1.sub(rowmean_r1, axis=0).div(rowsd_r1, axis=0)
zmat_r2 = subed_r2.sub(rowmean_r2, axis=0).div(rowsd_r2, axis=0)

# %%
# merge two reps together
zmat = pd.concat([zmat_r1, zmat_r2], axis=1)


# %%
zmat.to_csv("zmat.txt", sep='\t', index=False)


