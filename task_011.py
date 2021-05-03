#Mortal Fibonacci Rabbits http://rosalind.info/problems/fibd/
with open("rosalind_fibd.txt", "r") as f:
    n, m = (int(value) for value in f.read().split())

#n, m = 6, 3

prev_step = [0 for i in range(m)]
current_step = [0 for i in range(m)]
prev_step[0], current_step[1] = 1, 1

for i in range(2, n):
    for j in range(m):
        prev_step[j] = current_step[j]
        if j == 0:
            current_step[0] = sum(current_step) - current_step[0]
        else:
            current_step[j] = prev_step[j-1]

print(sum(current_step))
