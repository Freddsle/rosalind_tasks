#Rabbits and Recurrence Relations http://rosalind.info/problems/fib/
with open("rosalind_fib.txt", "r") as f:
    n, k = (int(value) for value in f.read().split())

pairs_1, pairs_2 = 1, 1

for i in range(n-2):
    pairs_1, pairs_2 = pairs_2, pairs_1*k + pairs_2

print(pairs_2)