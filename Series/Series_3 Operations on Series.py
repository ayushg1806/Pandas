#Operations on Series

#1. Modifying Elements of Series:
"""Series object's values can be modified but size cannot. Hence, Series objects are value-mutable but size-immutable objects.
        <SeriesObject>[<index>] = <new_data_value>
        <SeriesObject>[start : stop] = <new_data_value>
"""
import numpy as np 
import pandas as pd
a = np.arange(9, 14)
s3 = pd.Series(index = a, data = a*2)
s3[11] = 30 #modifying existing value
s3[2] = 25 #adding new value
print(s3)

s2 = pd.Series(data = [11, 14, 17, 20, 23])
s2[1:3] = 15
print(s2)

#Renaming Indexes
"""     <Object>.index = <new index array> """
s2.index = ["A", "B", "C", "D", "E"]
print(s2)


#2. head() and tail() Functions:
"""The head() function is used to fetch first n rows from a Pandas object and tall() function returns last N rows from a Pandas object. The syntax to use these functions is :
        <pandas object>.head([n])
        <pandas object>.tail([n])
If you do not provide any value for a, then head() and tail() will return first 5 and last 5 rows respectively of a Pandas object.
"""
a2 = np.arange(2.75, 56.1, 4.85)
s4 = pd.Series(data = a2)
print(s4.head())
print(s4.tail())
print(s4.head(7))


#3. Vector Operations on Series:
print(s3 + 2)
print(s3 * 3)
print(s4 > 15)


#4 Arithmetic Operations on Series:
"""When you perform arithmetic operations on two Series type objects, the data is aligned on the basis of matching indexes (this is called Data Alignment in Pandas objects) and then performed arithmetic; for non-overlapping indexes, the arithmetic operations result as a NaN (Not a Number)."""
s5 = s3 + s4
print(s5)

s6 = s4 / s3
print(s6)

s7 = s2 + s3
print(s7)


#5. Filtering Entries:
"""     <Series Object>[<Boolean expression on Series]"""
print(s3>20)
print(s3[s3>20])


#6. Sorting Series Values:
"""Sorting on the basis of Values
        <Series object>.sort_values([ascending = True | False])"""
s8 = pd.Series(data = [6700, 5600, 5000, 5200], index = ['A', 'B', 'C', 'D'])
print(s8.sort_values())
print(s8.sort_values(ascending = False))

"""Sorting on the basis of Indexes
        <Series object>.sort_indexes([ascending = True | False])"""
print(s8.sort_index())
print(s8.sort_index(ascending = False))


#7. Dropping Entries from an Axis
"""     <Series object>.drop(<index to be removed>)"""
s8 = s8.drop('C')
print(s8)