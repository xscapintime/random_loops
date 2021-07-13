# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os, sys, glob, re
import numpy as np
import pandas as pd
import pyranges as pr


# %%
#files = os.listdir('../data/ctcf.rad21/')
#len(files)

path = '../data/random_loop/ctcf.rad21/'
file = glob.glob(os.path.join(path,'*.txt'))
d1 = [] 
d2 = []

for f in file:
    if  re.match('.*r1.*', f) != None:
        d1.append(pd.read_csv(f,comment='#',header=None))
    else: #re.match('.*r2.*', f) != None:
        d2.append(pd.read_csv(f,comment='#',header=None))
data_r1 = pd.concat(d1,axis=1)
data_r2 = pd.concat(d2,axis=1)

print(data_r1.head())
print(data_r2.head())


# %%
# lpfiles = []
# for f in files:
#     if os.path.splitext(f)[1] == '.txt':
#         #print(f)
#         lpfiles.append(f)
#print(lpfiles)


# %%
filename_r1 = []
filename_r2 = []
#rep = []

for f in file:
    #rep = os.path.split(f)[1].split('primed_')[1].split('.intral')[0]
    if  re.match('.*r1.*', f) != None:
        fn = os.path.split(f)[1].split('.hesc')[0].replace("_shuff", "")
        filename_r1.append(fn + '_r1')
    else:
        fn = os.path.split(f)[1].split('.hesc')[0].replace("_shuff", "")
        filename_r2.append(fn + '_r2')

print(filename_r1)
print(filename_r2)


# %%
data_r1.columns = filename_r1
data_r2.columns = filename_r2
print(data_r1.head())
print(data_r2.head())


# %%
## load bed files
bedpath = '../data/bed/ctcf.rad21/'
bedfile = glob.glob(os.path.join(bedpath,'*.bed'))
peaknum = []
for b in bedfile:
    bed = pr.read_bed(b)
    peaknum.append(len(bed))


# %%
print(peaknum)


# %%
## 5 shuffled bed
peaknum = np.repeat(peaknum, 5)
peaknum

# %% [markdown]
# ```python
# *Bad attempt*
# 
# CTCF_35846 = data.iloc[:,0:10] / peaknum[0]
# CTCF_36632 = data.iloc[:,10:20] / peaknum[1]
# CTCF_45230 = data.iloc[:,20:30] / peaknum[2]
# CTCF_46184 = data.iloc[:,30:40] / peaknum[3]
# CTCF_50988 = data.iloc[:,40:50] / peaknum[4]
# RAD21_45689 = data.iloc[:,50:60] / peaknum[5]
# RAD21_46164 = data.iloc[:,60:70] / peaknum[6]
# RAD21_91096 = data.iloc[:,70:80] / peaknum[7]
# RAD21_94415 = data.iloc[:,80:90] / peaknum[8]
# 
# CTCF_35846_r1 = CTCF_35846.iloc[:,CTCF_35846.columns.str.contains('r1')].mean(axis=1)
# CTCF_36632_r1 = CTCF_35846.iloc[:,CTCF_36632.columns.str.contains('r1')].mean(axis=1)
# CTCF_45230_r1 = CTCF_35846.iloc[:,CTCF_45230.columns.str.contains('r1')].mean(axis=1)
# CTCF_46184_r1 = CTCF_35846.iloc[:,CTCF_46184.columns.str.contains('r1')].mean(axis=1)
# CTCF_50988_r1 = CTCF_35846.iloc[:,CTCF_50988.columns.str.contains('r1')].mean(axis=1)
# RAD21_45689_r1 = CTCF_35846.iloc[:,RAD21_45689.columns.str.contains('r1')].mean(axis=1)
# RAD21_46164_r1 = CTCF_35846.iloc[:,RAD21_46164.columns.str.contains('r1')].mean(axis=1)
# RAD21_91096_r1 = CTCF_35846.iloc[:,RAD21_91096.columns.str.contains('r1')].mean(axis=1)
# RAD21_94415_r1 = CTCF_35846.iloc[:,RAD21_94415.columns.str.contains('r1')].mean(axis=1)
# CTCF_35846_r2 = CTCF_35846.iloc[:,CTCF_35846.columns.str.contains('r2')].mean(axis=1)
# CTCF_36632_r2 = CTCF_35846.iloc[:,CTCF_36632.columns.str.contains('r2')].mean(axis=1)
# CTCF_45230_r2 = CTCF_35846.iloc[:,CTCF_45230.columns.str.contains('r2')].mean(axis=1)
# CTCF_46184_r2 = CTCF_35846.iloc[:,CTCF_46184.columns.str.contains('r2')].mean(axis=1)
# CTCF_50988_r2 = CTCF_35846.iloc[:,CTCF_50988.columns.str.contains('r2')].mean(axis=1)
# RAD21_45689_r2 = CTCF_35846.iloc[:,RAD21_45689.columns.str.contains('r2')].mean(axis=1)
# RAD21_46164_r2 = CTCF_35846.iloc[:,RAD21_46164.columns.str.contains('r2')].mean(axis=1)
# RAD21_91096_r2 = CTCF_35846.iloc[:,RAD21_91096.columns.str.contains('r2')].mean(axis=1)
# RAD21_94415_r2 = CTCF_35846.iloc[:,RAD21_94415.columns.str.contains('r2')].mean(axis=1)
# 
# av = [CTCF_35846_r1, CTCF_35846_r2, CTCF_36632_r1, CTCF_36632_r2, CTCF_45230_r1, CTCF_45230_r2, CTCF_46184_r1, CTCF_46184_r2,
#       CTCF_50988_r1, CTCF_50988_r2, RAD21_45689_r1, RAD21_45689_r2, RAD21_46164_r1, RAD21_46164_r2, RAD21_91096_r1, RAD21_91096_r2,
#       RAD21_94415_r1, RAD21_94415_r2]
# avs = pd.concat(av,axis=1)
# avs
# 
# col_1 = []
# col_2 = []
# for n in name:
#     col_1.append(n + '_r1')
#     col_2.append(n + '_r2')
# cols = col_1 + col_2
# cols.sort()
# 
# avs.columns = cols
# avs.columns
# ```

# %%
len(peaknum)


# %%
data_r1.shape
data_r2.shape


# %%
back_r1 = data_r1.div(peaknum)
back_r2 = data_r2.div(peaknum)


# %%
print(back_r1.head())
print(back_r2.head())


# %%
m_r1 = []
#np.linspace(0, 40, 9)

for i in np.linspace(0, 40, 9, dtype=int):
    #print(i)
    #print(i, i+5)
    m_r1.append(back_r1.iloc[:,i:i+5].mean(axis=1))
mback_r1 = pd.concat(m_r1, axis=1)


# %%
m_r2 = []
#np.linspace(0, 40, 9)

for i in np.linspace(0, 40, 9, dtype=int):
    #print(i)
    #print(i, i+5)
    m_r2.append(back_r2.iloc[:,i:i+5].mean(axis=1))
mback_r2 = pd.concat(m_r2, axis=1)


# %%
sample = []
for f in file:
    sample.append(os.path.split(f)[1].split('_shuff')[0])
name = np.unique(sample)
print(name)


# %%
name = name.tolist()


# %%
type(name)


# %%
name1 = [name[i] + '_r1' for i in range(len(name))]
name2 = [name[i] + '_r2' for i in range(len(name))]


# %%
mback_r1.columns = name1
mback_r2.columns = name2


# %%
mback_r1.head()


# %%
mback_r2.head()


# %%
#back.to_csv("ctcf_rad21_meanback.txt", sep='\t', index=False)

mback_r1.to_csv("ctcf_rad21_meanback_r1.txt", sep='\t', index=False)
mback_r2.to_csv("ctcf_rad21_meanback_r2.txt", sep='\t', index=False)


