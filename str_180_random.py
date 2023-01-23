import random

f=random.randint(1, 10)
print(f)
s=float(random.randint(1, 11))
print(s)

def coin_flip():
    """Возвращает случайно выбранную строку 'heads' или 'tails' ."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"
print(coin_flip())

heads_tally = 0
tails_tally = 0
for trial in range(10_000):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1
print(heads_tally, tails_tally)
ratio = heads_tally / tails_tally
print(f"The ratio of heads to tails is {ratio}")