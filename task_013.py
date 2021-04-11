#Calculating Expected Offspring http://rosalind.info/problems/iev/

with open("rosalind_iev.txt", "r") as f:
    AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = (int(value) for value in f.read().split())

answer = 2 * (AA_AA + AA_Aa + AA_aa) + 1.5 * Aa_Aa + Aa_aa
print(answer) 

