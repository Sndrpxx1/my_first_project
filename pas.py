import random


def gen_pass(n):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""

    for i in range(n):
        password += random.choice(elements)

    return password


print(gen_pass(5))

print(gen_pass(12))

