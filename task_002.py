#Transcribing DNA into RNA http://rosalind.info/problems/rna/
with open("rosalind_rna.txt", "r") as f:
    dna_text = f.read().strip('/n')

rna_text = ''

for letter in dna_text:
    if letter == 'T':
        rna_text += 'U'
    else:
        rna_text += letter

print(rna_text)

# other way -  s.replace("T", "U")
