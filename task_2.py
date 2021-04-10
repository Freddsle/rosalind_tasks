#Transcribing DNA into RNA http://rosalind.info/problems/rna/
file = open("rosalind_rna.txt", "r")
dna_text = file.read().strip('/n')
rna_text = str()

for letter in dna_text:
    if letter == 'T':
        rna_text += 'U'
    else:
        rna_text += letter

print(rna_text)

# other way -  s.replace("T", "U")
