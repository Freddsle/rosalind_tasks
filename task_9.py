#Finding a Motif in DNA http://rosalind.info/problems/subs/
file = open("rosalind_subs.txt", "r")
s, t = file.read().split()
answer = list()
index = 0

while index != -1:
    answer.append(index)
    index = s.find(t, (index+1))
 
for value in answer[1:]:
    print(value+1, end=' ')