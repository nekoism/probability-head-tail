import random 
heads = 0
tails = 0
n = 10000
for x in range(n):
    if random.choice([1,2]) == 1:
        heads = heads + 1
    else:
        tails = tails + 1
print(f"AFter flipping {n} coins we got heads: {heads} and prob of getting heads {heads/n}% and we ot {tails} and prob of getting tails {tails/n}%")
