#Pandas Data Structures: Series and Dataframe

"""Series Data Structure:
A Serles is a Pandas data structure that represents a one-dimensional array-like object containing an array of data (of any NumPy data type) and an associated array of data labels, called its Index.

Creating Series Objects: 
    <Series Object> = pandas.Series(data, index = idx)
    
    where idx is a valid Numpy datatype and data is the data part of the Series object, it can be one of the following :
        A Python sequence
        An ndarray
        Python dictionary
        A scalar value
"""
#1. Specify data as Python Sequence (list, tuple, string)
import pandas as pd 
s1 = pd.Series([4, 6, 8, 10]) #using list
print(s1)

s2 = pd.Series((41, 26, 18, 100)) #using tuple
print(s2)

s3 = pd.Series("So funny") #using string
print(s3)

#2. Specify data as an ndarrray
import numpy as np 
nda1 = np.arange(3, 12, 3.5)
s4 = pd.Series(nda1) #or pd.Series(np.aranage(3, 13, 3.5))
print(s4)

#3. Specify data a Python Dictionary
s5 = pd.Series({ 'Jan' :31, 'Feb' : 28, 'Mar':31})
print(s5)

#4. Specify data as a Scalar Value
s6 = pd.Series(data = 10, index = range(1, 6, 2))
print(s6)
s7 = pd.Series("Yet to start", index = ["Indore", "Bhopal", "Delhi"])
print(s7)


#Additional Functionality of Series Object
#1. Specifying/Adding NaN Values in a Series Object
s8 = pd.Series([6.5, np.nan, 2.34])
print(s8)

#2. Specify index as well as data with Series()
arr = [31, 28, 31, 30]
mon = ["Jan", "Feb", "Mar", "Apr"]
s9 = pd.Series(data = arr, index = mon) #OR pd.Series(arr, index = mon)
print(s9)

#3. Specify Data Type along with data and index
s10 = pd.Series(arr, index = mon, dtype = np.float64)
print(s10)

#4. Using Mathematical Function/Expression
a = np.arange(9, 13)
s11 = pd.Series(index = a, data = a*2)
print(s11)

l1 = [9, 10, 11, 12]
s12 = pd.Series(data = (2*l1))
print(s12)


"""When you store a NaN value in a series object, Pandas requires the data type to be of floating point type. Even if you specify an integer type, Pandas will promote it to a floating point type (automatically) because NaN is not supported by integer types."""

"""Indices need not be unique in Pandas Series Object. This will only cause an error if/when you perform an operation that requires unique indices."""
s12 = pd.Series (np.arange(2.75, 50, 9.75), index = ['a', 'b', 'a', 'a', 'b'])
print(s12)