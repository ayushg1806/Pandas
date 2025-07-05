#Accessing Series and its Elements
import pandas as pd
lst = [31, 28, 30, 31]
mon = ["Jan", "Feb", "Mar", "Apr"]
s1 = pd.Series(data = mon, index = lst)
print(s1)

s2 = pd.Series(data = [11, 14, 17, 20, 23])
print(s2)

#1. Accessing Individual Elements
"""     <Series Object Name>[<valid index>]"""
print(s1[31])
print(s2[2])

#2. Extracting Slices from Series
"""Slicing takes place position wise and not the index wise in a Series.
Position    Index   Data
0           9       18
1           10      20 
2           11      22
3           12      24
4           13      26
"""
import numpy as np 
import pandas as pd
a = np.arange(9, 14)
s3 = pd.Series(index = a, data = a*2)
print(s3)

print(s3[2:5])
print(s3[::2])
print(s3[::-1])