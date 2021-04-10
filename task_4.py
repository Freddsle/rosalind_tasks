#Rabbits and Recurrence Relations http://rosalind.info/problems/fib/
file = open("rosalind_fib.txt", "r")
n, k = file.read().split()
pairs_1, pairs_2 = 1, 1

for i in range(int(n)-2):
    pairs_1, pairs_2 = pairs_2, pairs_1*int(k) + pairs_2

print(pairs_2)