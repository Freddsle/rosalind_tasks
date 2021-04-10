#Counting Point Mutations http://rosalind.info/problems/hamm/
with open("rosalind_hamm.txt", "r") as f:
    s, t = f.read().split()

dH = sum(1 for x, y in zip(s, t) if x != y)
print(dH)