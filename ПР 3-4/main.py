import random


def cfg(name, rules):
    if isinstance(name, tuple):
        return cfg(random.choice(name), rules)
    if isinstance(name, list):
        return "".join([cfg(x, rules) for x in name])
    if name in rules:
        return cfg(rules[name], rules)
    else:
        return name


def test(rules, n):
    print("".join([cfg("S", rules) + "\n" for i in range(n)]))


g1 = {
    "S": ["D", (("D", ""), "S")],
    "D": ("0", "1"),
}

g2 = {
    "S": ["(", ("S", ""), ")"]
}

g3 = {
    "S": (["V", "R"], ["C", ("R", "")]),
    "V": ("x", "y"),
    "P": [" + ", "VC"],
    "M": [" - ", "VC"],
    "MUL": [" * ", "VC"],
    "D": [" / ", "VC"],
    "VC": ("V", "C"),
    "R": ("P", "M", "MUL", "D"),
    "C": ["(", ["V", "R"], ")"]
}

test(g3, 10)
