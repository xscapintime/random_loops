"""
predict read threshold using negative binomial regression

"""

import os, sys, glob
import pandas as pd
import numpy as np
import statistics as stats
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pyranges as pr
import matplotlib.pyplot as plt
import seaborn as sns
import pymc3 as pm
import bambi as bmb
import arviz as az


# real contact data
real_r1 = pd.read_csv('real_r1.txt', sep='\t', header=0)
real_r2 = pd.read_csv('real_r2.txt', sep='\t', header=0)

df = pd.concat([real_r1, real_r2], axis=1)
df['read'] = [i+1 for i in df.index]

dat = pd.melt(df, id_vars=['read'], var_name = 'tf', value_name='contacts')
# dat['contacts'] = dat['contacts'] + 1 #log(0)=inf

# count_data = pd.DataFrame({
#     'read':real_r1.index.tolist(),
#     'contacts': real_r1.iloc[:,0]
#     })


# peak number
path = '../data/'

bedfile = glob.glob(os.path.join(path,'bed/*.bed'))
bedfile += glob.glob(os.path.join(path,'encode_bed/*.bed.gz'))
bedfile += glob.glob(os.path.join(path,'bed/ctcf.rad21/*.bed'))

peaknum = []
for b in bedfile:
    bed = pr.read_bed(b)
    peaknum.append(len(bed))

peak = np.repeat(peaknum ,20).tolist() * 2


dat['peak'] = peak


## negative binomial regression
# variance vs mean
stats.variance(dat['contacts'])
stats.mean(dat['contacts'])

stats.variance(dat['contacts'])/stats.mean(dat['contacts'])



## bambi
# fml = "contacts ~ read"

fml = 'read ~ contacts' # to predict log of read

model = bmb.Model(fml, dat, family='negativebinomial')
trace = model.fit(draws=1000, tune=1000, cores=2, init='adapt_diag') # auto: Use "jitter+adapt_diag" and if this method fails it uses "adapt_diag".

summary = az.summary(trace)
summary.to_csv('read-bn_aztrace_summ.txt', sep='\t', header=True, index=True)

axes = az.plot_trace(trace)
fig = axes.ravel()[0].figure
fig.savefig('read-bn_aztrace.pdf')


# add peak as an independent variable
fml = 'read ~ contacts + peak' # to predict log of read

model = bmb.Model(fml, dat, family='negativebinomial')
trace = model.fit(draws=1000, tune=1000, cores=2, init='adapt_diag') # auto: Use "jitter+adapt_diag" and if this method fails it uses "adapt_diag".

summary = az.summary(trace)
summary.to_csv('read-pkct-bn_aztrace_summ.txt', sep='\t', header=True, index=True)

axes = az.plot_trace(trace)
fig = axes.ravel()[0].figure
fig.savefig('read-pkct-bn_aztrace.pdf')



## smf
# only contacts as independent variable
reg = smf.glm(formula = "read ~ contacts", data=dat, family=sm.families.NegativeBinomial()).fit()
summary = reg.summary()
summary.as_csv()

text_file = open('read-bn_smf_summ.csv', 'w')
n = text_file.write(summary.as_csv())
text_file.close()


# add peak as an independent variable
reg = smf.glm(formula = "read ~ contacts + peak", data=dat, family=sm.families.NegativeBinomial()).fit()
summary = reg.summary()
summary.as_csv()

text_file = open('read-pkct-bn_smf_summ.csv', 'w')
n = text_file.write(summary.as_csv())
text_file.close()


