import dis


def foo(x):
    while x:
        x -= 1
    return x + 1


print(dis.dis(foo))
