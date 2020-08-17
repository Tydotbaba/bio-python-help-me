'''
    Finding Hamming distance
    
'''

# change your code below this line
p = 'GGGCCGTTGGT'
q = 'GGACCGTTGAC'
# change your code above this line

def HammingDistance(p, q):
    d = 0
    for i, j in zip(p, q):
        if i != j:
            d += 1
    return d

print(HammingDistance(p, q))
