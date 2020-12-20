####################################
# --- Day 19: Monster Messages --- #
####################################

import AOCUtils
import re

def checkRule(rule, line):
    return re.match("^"+rule+"$", line) is not None

def buildDirectRule(baseRules, rule):
    if rule in "ab|":
        return rule
    else:
        return [buildDirectRule(baseRules, t) for t in baseRules[rule]]

def parseRule(rule):
    if rule == ["a"] or rule == ["b"] or rule == "|":
        return rule[0]
    else:
        strRule = [parseRule(c) for c in rule]
        strRule = "".join(strRule)
        return "(?:" + strRule + ")"

####################################

rawInput = AOCUtils.loadInput(19)

rawRules, rawMessages = "\n".join(rawInput).split("\n\n")
rawRules = rawRules.split("\n")
messages = rawMessages.split("\n")

baseRules = dict()
for rawRule in rawRules:
    ruleID, rule = rawRule.split(": ")
    rule = [c.replace("\"", "") for c in rule.split()]

    baseRules[ruleID] = rule

# Get token references, building a direct recursive array of arrays down until terminal symbols
directRules = {ruleID: [buildDirectRule(baseRules, c) for c in rule] for ruleID, rule in baseRules.items()}

# Serialize the recursive arrays enclosing them in parentheses (resulting in a regex-ready pattern)
parsedRules = {ruleID: parseRule(rule) for ruleID, rule in directRules.items()}

p1 = sum(checkRule(parsedRules["0"], message) for message in messages)
print("Part 1: {}".format(p1))

# '8: 42 | 42 8' === '(42)+'
# '11: 42 31 | 42 11 31' === '(42){n}(31){n}', n >= 1

modifiedRule = parsedRules["0"]
modifiedRule = modifiedRule.replace(parsedRules["42"], parsedRules["42"]+"!")

# Replace all '(42)(31)' with '(42){n}(31){n}'
modifiedRule = modifiedRule.replace(parsedRules["42"]+"!"+parsedRules["31"], parsedRules["42"]+"X"+parsedRules["31"]+"X")

# Replace all '(42)' (without a following (31)) with '(42)+'
modifiedRule = modifiedRule.replace(parsedRules["42"]+"!", parsedRules["42"]+"+")

# Will check rule 11's n up until N, assuming it doesn't occur more than N times
N = 10

p2 = 0
for n in range(1, N):
    p2 += sum(checkRule(modifiedRule.replace("X", "{"+str(n)+"}"), message) for message in messages)
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()