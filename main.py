import random 
heads = 0
tails = 0
n = 10000 #number of times the coin will be fliped
for x in range(n):
    if random.choice([1,2]) == 1:
        heads = heads + 1 #if it was rolled head add 1 point to head 
    else:
        tails = tails + 1 # roll tail adds 1 point to tail
print(f"AFter flipping {n} coins we got heads: {heads} and prob of getting heads {heads/n}% and we ot {tails} and prob of getting tails {tails/n}%")
# prints the result
