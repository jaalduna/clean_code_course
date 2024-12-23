"""test module"""

for i in range(0, 10):
    print(f"new line: {i}")


def test():
    return 42


def test2():
    return 4


test2()
print("hola mundo")

test() + test2()
