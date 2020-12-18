###################################
# --- Day 18: Operation Order --- #
###################################

import AOCUtils

# Special int subclass for Part 1: for + and * to have the same precedence,
# replace all '*' with '-' but change __sub__ behavior to __mul__.
class int1(int):
    repl = {"*": "-"}

    def __add__(self, other): return int1(super().__add__(other))
    def __sub__(self, other): return int1(super().__mul__(other))

# Special int subclass for Part 2: for + to have a higher precedence than *,
# swap both '*' and '+' but swap their behaviors as well.
class int2(int):
    repl = {"*": "+", "+": "*"}

    def __add__(self, other): return int2(super().__mul__(other))
    def __mul__(self, other): return int2(super().__add__(other))

def splitTokens(expr):
    splitExpr = []
    i = 0
    j = 0
    while j < len(expr):
        if not expr[j].isdigit():
            splitExpr.append(expr[j])
            j += 1
        else:
            while j < len(expr) and expr[j].isdigit(): j += 1
            splitExpr.append(expr[i:j])

        i = j

    return splitExpr

def specialEval(expr, cls):
    expr = expr.replace(" ", "")

    # Replace operations according to cls
    replacedExpr = list(expr)
    for i in range(len(replacedExpr)):
        for old, new in cls.repl.items():
            if expr[i] == old: replacedExpr[i] = new
    expr = "".join(replacedExpr)

    # expr.split(), but keep digits together
    expr = splitTokens(expr)

    # Replace numbers with instances of cls
    for i in range(len(expr)):
        if expr[i].isdigit():
            expr[i] = "{}({})".format(cls.__name__, expr[i])

    return eval("".join(expr))

###################################

homework = AOCUtils.loadInput(18)

p1 = sum(specialEval(expr, int1) for expr in homework)
print("Part 1: {}".format(p1))

p2 = sum(specialEval(expr, int2) for expr in homework)
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()