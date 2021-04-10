#Consensus and Profile http://rosalind.info/problems/cons/
with open("rosalind_cons.txt", "r") as f:
    line = f.read().strip('>').split('>')

data = {}

for i in line:
    name, seq = i.split('\n', 1)
    seq = seq.replace('\n', '')
    data[name] = seq
    ls = len(seq)

A, C, G, T = [0] * ls, [0] * ls, [0] * ls, [0] * ls

for seq in data:
    for i in range(len(data[seq])):
        if data[seq][i] == 'A':
            A[i] = A[i]+1
            C[i], G[i], T[i] = C[i]+0, G[i]+0, T[i]+0
        elif data[seq][i] == 'T':
            T[i] += 1
            C[i], G[i], A[i] = C[i]+0, G[i]+0, A[i]+0
        elif data[seq][i] == 'C':
            C[i] += 1
            A[i], G[i], T[i] = A[i]+0, G[i]+0, T[i]+0
        elif data[seq][i] == 'G':
            G[i] += 1
            C[i], A[i], T[i] = C[i]+0, A[i]+0, T[i]+0

alphabet = ['A', 'C', 'G', 'T']
answer = ''
for i in range(len(A)):
    l = (A[i],C[i],G[i],T[i])
    index = l.index(max(l))
    answer += alphabet[index]

with open("myfile.txt", "w") as f:
    print(answer, 
        '\nA: ', *A, 
        '\nC: ', *C, 
        '\nG: ', *G, 
        '\nT: ', *T, 
        file=f)