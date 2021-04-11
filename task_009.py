#Finding a Motif in DNA http://rosalind.info/problems/subs/
with open("rosalind_subs.txt", "r") as f:
    s, t = f.read().split()

answer = []
index = s.find(t)

while index != -1:
    answer.append(index)
    index = s.find(t, (index+1))
        
for value in answer:
    print(value+1, end=' ')