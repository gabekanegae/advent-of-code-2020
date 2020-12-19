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
        return "("+"".join([parseRule(c) for c in rule])+")"

####################################

rawInput = AOCUtils.loadInput(19)

for i in range(len(rawInput)):
    if rawInput[i] == "": rawInput[i] = "\n"

rawRules, rawMessages = "\n".join(rawInput).split("\n\n")

rawRules = rawRules.split("\n")
messages = rawMessages.split("\n")

baseRules = dict()
for rawRule in rawRules:
    ruleID, rule = rawRule.split(": ")
    rule = [c.replace("\"", "") for c in rule.split()]

    baseRules[ruleID] = rule

directRules = {ruleID: [buildDirectRule(baseRules, c) for c in rule] for ruleID, rule in baseRules.items()}

parsedRules = {ruleID: parseRule(rule) for ruleID, rule in directRules.items()}

p1 = sum(checkRule(parsedRules["0"], message) for message in messages)
print("Part 1: {}".format(p1))

modifiedRule = parsedRules["0"]
modifiedRule = modifiedRule.replace(parsedRules["42"], parsedRules["42"]+"!")
modifiedRule = modifiedRule.replace(parsedRules["42"]+"!"+parsedRules["31"], parsedRules["42"]+"X"+parsedRules["31"]+"X")
modifiedRule = modifiedRule.replace(parsedRules["42"]+"!", parsedRules["42"]+"+")

p2 = 0
for n in range(1, 10):
    p2 += sum(checkRule(modifiedRule.replace("X", "{"+str(n)+"}"), message) for message in messages)
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()