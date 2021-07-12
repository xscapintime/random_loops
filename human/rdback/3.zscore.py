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
#import pyranges as pr


# %%
subed = pd.read_csv('ctcf_rad21_subed.txt', sep='\t')


# %%
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
zmat.head()


# %%
zmat.to_csv("ctcf_rad21_zmat.txt", sep='\t', index=False)
# index as row name in txt?
# better drop it


