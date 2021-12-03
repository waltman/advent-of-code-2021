import sys
import numpy as np
import operator
import copy

def calc_rating(report, op):
    a = copy.copy(report)
    col = 0
    while True:
        half = a.shape[0] / 2
        if op(sum(a[:,col]) half):
            pass

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
