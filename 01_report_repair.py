################################
# --- Day 1: Report Repair --- #
################################

import AOCUtils

def twoSum(counts, target):
    for i, ct in counts.items():
        if target-i in counts:
            return i * (target-i)

def threeSum(counts, target):
    for i in counts:
        twoSumResult = twoSum(counts, target-i)
        if twoSumResult is not None:
            return i * twoSumResult

################################

report = AOCUtils.loadInput(1)

target = 2020

reportCounts = dict()
for i in report:
    if i not in reportCounts:
        reportCounts[i] = 0
    reportCounts[i] += 1

print("Part 1: {}".format(twoSum(reportCounts, target)))

print("Part 2: {}".format(threeSum(reportCounts, target)))

AOCUtils.printTimeTaken()
