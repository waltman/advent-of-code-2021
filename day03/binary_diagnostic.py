import sys
import numpy as np
import operator
import copy

def calc_rating(report, op, tie):
    a = copy.copy(report)
    col = 0
    while a.shape[0] > 1:
        # are we looking for 0s or 1s?
        half = a.shape[0] / 2
        if op((cnt := sum(a[:,col])), half):
            common = 1
        elif cnt == half:
            common = tie
        else:
            common = 0

        # find the rows in col with that value
        rows = [a[row][col] == common for row in range(a.shape[0])]

        # make a new a
        a = a[rows][:]
        col += 1

    # convert the remaining row to binary
    s = ''.join([str(val) for val in a[0][:]])
    return int(s, 2)

with open(sys.argv[1]) as f:
    report = np.array([[int(c) for c in line.rstrip()] for line in f.readlines()])

gamma = ""
eps = ""
half = report.shape[0] / 2
for i in range(report.shape[1]):
    if sum(report[:,i]) > half:
        gamma += "1"
        eps += "0"
    else:
        gamma += "0"
        eps += "1"

print('Part 1:', int(gamma,2) * int(eps,2))

oxygen_rating = calc_rating(report, operator.gt, 1)
co2_rating = calc_rating(report, operator.lt, 0)
print('Part 2:', oxygen_rating * co2_rating)
