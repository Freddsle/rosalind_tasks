#Mortal Fibonacci Rabbits http://rosalind.info/problems/fibd/
with open("rosalind_fibd.txt", "r") as f:
    n, m = (int(value) for value in f.read().split())

#n, m = 6, 3
rabbits = [[0, 0, 0] for i in range(m)]
rabbits[0][1], rabbits[1][2] = 1, 1

for i in range(2, n):
    for j in range(m):
        rabbits[j][0], rabbits[j][1] = rabbits[j][1], rabbits[j][2]
        if j == 0:
            rabbits[0][2] = sum(rabbits[k][2] for k in range(1, m))
        else:
            rabbits[j][2] = rabbits[j-1][1]

stop_rab = sum(rabbits[i][2] for i in range(m))
print(stop_rab)
