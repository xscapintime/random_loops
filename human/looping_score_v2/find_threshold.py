"""
Find read thresholds from 4 nearest value to Z-score

"""

# %%
import os, sys, glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%
zmat = pd.read_csv('zmat.txt', sep='\t')

# %%
col_med = zmat.median()
col_mean = zmat.mean()

# %%
### not working well
# class Solution(object):
# def findClosestElements(arr, k, x): #delete `self`
#     """
#     :type arr: List[int]
#     :type k: int
#     :type x: int
#     :rtype: List[int]
#     """
#     n=len(arr)
#     l,r=0,n-k#返回列表元素时不会超出范围
#     while l<r:
#         mid=l+(r-l)//2
#         if x-arr[mid]>arr[mid+k]-x:#如果左边差距大，则缩小左边距离
#             l=mid+1
#         else:#右边与目标值差距大，则缩小右边范围
#             r=mid
#     return arr[l:l+k].index.tolist() # I want index
# 作者：yang-wang-xing-kong-54k
# 链接：https://leetcode-cn.com/problems/find-k-closest-elements/solution/python-zhao-dao-kge-zui-jie-jin-de-yuan-su-by-ya-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# %%
import heapq

all_idx = []
for i,m in enumerate(col_med):
    abs_diff = [abs(m - z) for z in zmat.iloc[:,i]]
    min_number = heapq.nsmallest(4, abs_diff) 

    min_index = []
    for t in min_number:
        index = abs_diff.index(t)
        min_index.append(index)
        abs_diff[index] = 0 # in case of duplicated value

    all_idx.append(min_index)


# all_idx_df = pd.DataFrame(all_idx)

# %%
fig = pd.DataFrame(all_idx).plot.hist(grid=False, bins=20, rwidth=0.9, color='#607c8e').get_figure()
fig.savefig('near-med_hist.pdf')
fig.savefig('near-med_hist.png')


# %%
# so frequence
for j in range(0, zmat.shape[0]):
    print(j, len(np.array(all_idx)[np.array(all_idx) == j]))


# %%
"""
if it's mean
"""

# %%
import heapq

all_idx = []
for i,m in enumerate(col_mean):
    abs_diff = [abs(m - z) for z in zmat.iloc[:,i]]
    min_number = heapq.nsmallest(4, abs_diff) 

    min_index = []
    for t in min_number:
        index = abs_diff.index(t)
        min_index.append(index)
        abs_diff[index] = 0 # in case of duplicated value

    all_idx.append(min_index)


# all_idx_df = pd.DataFrame(all_idx)

# %%
fig = pd.DataFrame(all_idx).plot.hist(grid=False, bins=20, rwidth=0.9, color='#607c8e').get_figure()
fig.savefig('near-mean_hist.pdf')
fig.savefig('near-mean_hist.png')


# %%
# so frequence
for j in range(0, zmat.shape[0]):
    print(j, len(np.array(all_idx)[np.array(all_idx) == j]))

# %%
# So 9-12 is the thresholds to choose. (index 8-11)
# export a threshold-selected table
zmat.iloc[8:12,].to_csv("zmat_thresholds.txt", sep='\t', index=False)