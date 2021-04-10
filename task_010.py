#Consensus and Profile http://rosalind.info/problems/cons/
with open("rosalind_cons.txt", "r") as f:
    line = f.read().strip('>').split('>')

data = {}

for i in line:
    name, seq = i.split('\n', 1)
    seq = seq.replace('\n', '')
    data[name] = seq
    ls = len(seq)

Profile = {'A': [0] * ls,
           'C': [0] * ls,
           'G': [0] * ls,
           'T': [0] * ls}

for seq in data:
    for i, c in enumerate(data[seq]):
        Profile[c][i] += 1

alphabet = ['A', 'C', 'G', 'T']
answer = ''

for i in range(len(Profile['A'])):
    l = (Profile['A'][i],Profile['C'][i],Profile['G'][i], Profile['T'][i])
    index = l.index(max(l))
    answer += alphabet[index]

with open("myfile.txt", "w") as f:
    print(answer, 
        '\nA: ', *Profile['A'], 
        '\nC: ', *Profile['C'], 
        '\nG: ', *Profile['G'], 
        '\nT: ', *Profile['T'], 
        file=f)
