#Mendel's First Law http://rosalind.info/problems/iprb/
with open("rosalind_iprb.txt", "r") as f:
    k, m, n,  = (int(value) for value in f.read().split())

children = (parents**2 - (k + m + n))) / 2
child_AA = k * (m + n) + (k**2 - k) / 2
child_Aa = 3 * ((m**2 - m) / 2) / 4 + m * n / 2
result = (child_AA + child_Aa) / children
print(result)
