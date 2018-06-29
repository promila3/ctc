# Setting M in N from bits i to j
def setNinM(n, m, i, j):
    mask = 0
    for b in range(31, -1, -1):
        if (b < i ) or (b > j):
            mask = (mask << 1) + 1
            #print("Hi")
            #print(bin(mask))
        else :
            mask = mask << 1
        
    return ( n & mask ) | ( m << i)

n = 0b10000000000
m = 0b10011
i = 2
j = 6
print(n,m)
print(bin(setNinM(n,m,i,j)))
# Promila http://py3.codeskulptor.org/#user301_rVvJPcJKbU_0.py
