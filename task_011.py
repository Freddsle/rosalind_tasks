#Mortal Fibonacci Rabbits http://rosalind.info/problems/fibd/
with open("rosalind_fibd.txt", "r") as f:
    n, m = (int(value) for value in f.read().split())

#n, m = 6, 3
rabbits = [[0]*n for i in range(m)]
rabbits[0][0], rabbits[1][1] = 1, 1

for i in range(2, n):
    for j in range(m):
        if j == 0:
            rabbits[j][i] = sum(rabbits[k][i-1] for k in range(1,m))
        else:
            rabbits[j][i] = rabbits[j-1][i-1]

stop_rab = sum(rabbits[i][n-1] for i in range(m))
print(stop_rab)

