#Mendel's First Law http://rosalind.info/problems/iprb/
file = open("rosalind_iprb.txt", "r")
k, m, n,  = (int(value) for value in file.read().split())
parents = k + m + n
children = (parents**2 - parents) / 2
child_AA = k * (m + n) + (k**2 - k) / 2
child_Aa = 3 * ((m**2 - m) / 2) / 4 + m * n / 2
result = (child_AA + child_Aa) / children
print(result)
