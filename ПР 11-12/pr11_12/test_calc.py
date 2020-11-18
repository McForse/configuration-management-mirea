import sys
import inspect
import random
import calc


def coverage(f):
    lines = set()
    def trace(frame, event, arg):
        lines.add((event, frame.f_lineno))
        return trace
    sys.settrace(trace)
    f()
    sys.settrace(None)
    return lines


def print_coverage(module, trace):
    lines = [y for x, y in trace]
    source = inspect.getsource(module).splitlines()
    for i, x in enumerate(source):
        print(("|" if i + 1 in lines else " ") + x)


def test_calc(s):
    try:
        return calc.calc(s)
    except:
        pass


def gen():
    o = ['+', '-', '*', '/', '(', ')']
    return str(random.randint(1, 100)) + " " + " ".join([random.choice(o) + " " + str(random.randint(1, 100)) for _ in range(20)])


def tests():
    for _ in range(100):
        test_calc(gen())


c = coverage(tests)
print_coverage(calc, c)
print(len(c))
#print(gen())