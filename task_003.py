#Complementing a Strand of DNA http://rosalind.info/problems/revc/
with open("rosalind_revc.txt", "r") as f: 
    dna_text = f.read().strip('\n')

replacements = {"A": "T", 
                "G": "C", 
                "C": "G", 
                "T": "A"}
coml_dna = "".join([replacements[c] for c in reversed(dna_text)])
print(coml_dna)