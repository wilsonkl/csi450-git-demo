import random
print("Hello World")

def random_coin_flip():
    if random.randint(1, 2) == 1:
        return "Heads"
    else:
        return "Tails"