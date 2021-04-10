#Counting Point Mutations http://rosalind.info/problems/hamm/
file = open("rosalind_hamm.txt", "r")
s, t = file.read().split()
dH = 0
for i in range(len(s)):
    if s[i] != t[i]:
        dH += 1
print(dH)