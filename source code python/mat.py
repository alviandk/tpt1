#import numpy
from numpy import matrix
from numpy import linalg
a=matrix([[1,2,3],[2,3,1],[3,2,1]]) #matrix a
b=matrix([[4,2,1],[5,4,3],[8,9,1]])
print a
print a.T
print a*b
print b.I
print linalg.solve(a,b)
