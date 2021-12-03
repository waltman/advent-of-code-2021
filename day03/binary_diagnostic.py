import sys
import numpy as np
import operator

def calc_rating(report, op, tie):
    arr = report.copy()
    col = 0
    while arr.shape[0] > 1:
        # are we looking for 0s or 1s?
        half = arr.shape[0] / 2
        if op((cnt := sum(arr[:,col])), half):
            common = 1
        elif cnt == half:
            common = tie
        else:
            common = 0

        # make a new arr with only the rows in col that have that value
        arr = arr[np.where(arr[:,col] == common)]
        col += 1

    # convert the remaining row to binary
    s = ''.join([str(val) for val in arr[0][:]])
    return int(s, 2)

with open(sys.argv[1]) as f:
    report = np.array([[int(c) for c in line.rstrip()] for line in f])

gamma = ""
eps = ""
half = report.shape[0] / 2
for col in range(report.shape[1]):
    if sum(report[:,col]) > half:
        gamma += "1"
        eps += "0"
    else:
        gamma += "0"
        eps += "1"

print('Part 1:', int(gamma,2) * int(eps,2))

oxygen_rating = calc_rating(report, operator.gt, 1)
co2_rating = calc_rating(report, operator.lt, 0)
print('Part 2:', oxygen_rating * co2_rating)
