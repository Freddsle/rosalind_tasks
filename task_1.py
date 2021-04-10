#Counting DNA Nucleotides http://rosalind.info/problems/dna/
file = open("dna.txt", "r")
dna_text = file.read()
letters = dict(zip(list(dna_text),[list(dna_text).count(i) for i in list(dna_text)]))
print(letters['A'],' ',letters['C'], ' ', letters['G'], ' ', letters['T'])
