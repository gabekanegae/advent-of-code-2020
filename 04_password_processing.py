######################################
# --- Day 4: Passport Processing --- #
######################################

import AOCUtils

checks1 = [
    lambda pp: all(field in pp for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
]
def isValid1(passport):
    return all(check(passport) for check in checks1)

checks2 = [
    lambda pp: 1920 <= int(pp["byr"]) <= 2002,
    lambda pp: 2010 <= int(pp["iyr"]) <= 2020,
    lambda pp: 2020 <= int(pp["eyr"]) <= 2030,
    lambda pp: (pp["hgt"][-2:] == "cm" and 150 <= int(pp["hgt"][:-2]) <= 193) or \
               (pp["hgt"][-2:] == "in" and 59 <= int(pp["hgt"][:-2]) <= 76),
    lambda pp: pp["hcl"][0] == "#" and all(c in "0123456789abcdef" for c in pp["hcl"][1:]),
    lambda pp: pp["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    lambda pp: len(pp["pid"]) == 9 and all(c in "0123456789" for c in pp["pid"])
]
def isValid2(passport):
    return isValid1(passport) and all(check(passport) for check in checks2)

######################################

rawInput = AOCUtils.loadInput(4)

for i in range(len(rawInput)):
    if rawInput[i] == "": rawInput[i] = "\n"

rawPassports = " ".join(rawInput).split(" \n ")

passports = []
for rawPassport in rawPassports:
    passport = dict()
    for kvp in rawPassport.split():
        k, v = kvp.split(":")
        passport[k] = v

    passports.append(passport)

p1 = sum(isValid1(passport) for passport in passports)
print("Part 1: {}".format(p1))

p2 = sum(isValid2(passport) for passport in passports)
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()