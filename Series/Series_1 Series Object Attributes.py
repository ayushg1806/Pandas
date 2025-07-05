""" Series Object Attributes:
<Series object>.index : The index (axis labels) of the Series.
<Series object>.values : Return Series as ndarray or ndarray-like depending on the dtype
<Series object>.dtype : return the dtype object of the underlying data
<Series object>.shape : return a tuple of the shape of the underlying data
<Series object>.nbytes : return the number of bytes in the underlying data
<Series object>.ndim : return the number of dimensions of the underlying data
<Series object>.size : return the number of elements in the underlying data
<Series object>.itemsize : return the size of the dtype of the item of the underlying data
<Series object>.hasnans : return True if there are any NaN values ; otherwise return False
<Series object>.empty : retum True if the Series object is empty, false otherwise
"""
import pandas as pd
lst = [31, 28, 30, 31]
mon = ["Jan", "Feb", "Mar", "Apr"]
s1 = pd.Series(data = mon, index = lst)
print(s1)

print(s1.index)
print(s1.values)
print(s1.dtype)
print(s1.shape)
print(s1.size)
print(s1.hasnans)
print(s1.empty)