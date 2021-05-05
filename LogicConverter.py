# ~ = not
# & = and
# | = or
# @ = for all
# \ = exists
# $ = implies
# _ = subset
# % = bidirectional
# # = not equal

# param: eq, string starting with a forall
# param: ud, string containing universe of discord
# returns: converted equation to prepositional logic
from typing import re


def forall(eq, ud):
    output = "("
    wrt = eq[1]
    for var in range(len(ud)):
        for char in eq[2:]:
            if char == wrt:
                output += ud[var]
            else:
                output += char
        if var != len(ud)-1:
            output += "&"
    output += ")"
    return output

# param: eq, string starting with an existential
# param: ud, string containing universe of discord
# returns: converted equation to prepositional logic
def exists(eq, ud):
    output = "("
    wrt = eq[1]
    for var in range(len(ud)):
        for char in eq[2:]:
            if char == wrt:
                output += ud[var]
            else:
                output += char
        if var != len(ud) - 1:
            output += "|"
    output += ")"
    return output

# param: input, string containing input to be checked if valid equation
# returns: True if input is valid first order logic, False otherwise
def inputChecker(input):
    special = "&|@\\$_%#"
    operations = "&|$_%#"
    nonchars = "&|@\\$_%#~()"
    parcount = 0
    for n in input:
        if n == "(":
            parcount += 1
        elif n == ")":
            parcount -= 1
    if parcount != 0:
        return False
    for x in range(len(input)-1):
        if input[x] in special:
            if input[x+1] in special or input[x+1] == ")":
                return False
            elif input[x] == "@" or input[x] == "\\":
                if input[x+1] == "(" or input[x+1] == "~":
                    return False
    if input[-1] in special or input[-1] == "(" or input[-1] == "~":
        return False
    if input[0] in operations or input[0] == ")":
        return False
    x = len(input)-1
    while x > 0:
        if input[x] in operations:
            if input[x-1] == "(":
                return False
        x -= 1
    x = 0
    while x < len(input):
        if not (input[x] in nonchars):
            if not (input[x+1] in nonchars):
                return False
        x += 1
    x = 0
    while x < len(input):
        if input[x] == "@" or input[x] == "\\":
            curVar = input[x+1]
            back = x
            while back >= 0:
                if input[back] == curVar:
                    return False
                back -= 1
            parse = x+2
            parcount = 0
            while input[parse] == "~":
                parse += 1
            while parse < len(input):
                if input[parse] == "(":
                    parcount += 1
                elif input[parse] == ")":
                    parcount += -1
                parse += 1
                if parcount == 0:
                    break
            while parse < len(input):
                if input[parse] == curVar:
                    return False
                parse += 1
        x += 1
    return True


# param: eq, string containing first order logic equation to be converted
# param: ud, string containing universe of discord
# returns: converted equation to prepositional logic
def converter(eq, ud):
    for n in range(len(eq)-2):
        if eq[n] == "~" and eq[n+1] == "@":
            eq = eq[:n] + "\\" + eq[n+2] + eq[n] + eq[n+3:]
    print(eq)
    x = len(eq)-1
    while x >= 0:
        if eq[x] == "@" or eq[x] == "\\":
            parCount = 0
            endIndex = x + 2
            if eq[endIndex] == "~":
                endIndex += 1
            for char in eq[endIndex: len(eq)]:
                if char == "(":
                    parCount += 1
                elif char == ")":
                    parCount -= 1
                endIndex += 1
                if parCount == 0:
                    break
            if eq[x] == "@":
                eq = eq.replace(eq[x: endIndex], forall(eq[x: endIndex], ud))
            elif eq[x] == "\\":
                eq = eq.replace(eq[x: endIndex], exists(eq[x: endIndex], ud))
        x -= 1
    return eq


def parDiv(expr):
    output = []
    parcount = 1
    start = 0
    end = 0
    for n in range(1, len(expr)):
        if expr[n] == "(":
            parcount += 1
            parDiv(expr[n+1:])
        if expr[n] == ")":
            parcount -= 1
            if parcount == 0:
                end = n
    output.append(expr[start:end+1])
    return output