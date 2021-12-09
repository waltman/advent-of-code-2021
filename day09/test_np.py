import numpy as np

def neighbors(row, col):
    return [(row+1,col), (row-1,col), (row,col+1), (row,col-1)]

def n2(row, col):
    return [row+1,row-1,row,row],[col,col,col+1,col-1]

for r,c in neighbors(1,1):
    print(r,c)

print()

for x in zip(*n2(1,1)):
    print(x)

