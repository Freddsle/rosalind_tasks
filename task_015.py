#Independent Alleles http://rosalind.info/problems/lia/
from math import factorial


def successes(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))

def probability(n, k, prob_one):
    return successes(n, k) * prob_one ** k * ((1 - prob_one) ** (n - k))


with open("rosalind_lia.txt", "r") as f:
    k, n_org = (int(value) for value in f.read().split())

#k, n_org = 2, 1
kids = 2 ** k 
prob_one = 0.25
result = 0

for i in range(n_org, kids+1):
    result += probability(kids, i, prob_one)

print(result)
