#Complementing a Strand of DNA http://rosalind.info/problems/revc/
file = open("rosalind_revc.txt", "r")
dna_text = file.read().strip('/n')
replacements = {"A": "T", "G": "C", "C": "G", "T": "A"}
coml_dna = "".join([replacements.get(c, c) for c in dna_text])
print(coml_dna[::-1])