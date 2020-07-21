# # Place your Neighbors() function here, along with any subroutines you need.
# # Neighbors() should return a list.
# def Neighbors(Pattern, d):
#     if d = 0
#             return {Pattern}
#         if |Pattern| = 1 
#             return {A, C, G, T}
#         Neighborhood ← an empty set
#         SuffixNeighbors ← Neighbors(Suffix(Pattern), d)
#         for each string Text from SuffixNeighbors
#             if HammingDistance(Suffix(Pattern), Text) < d
#                 for each nucleotide x
#                     add x • Text to Neighborhood
#             else
#                 add FirstSymbol(Pattern) • Text to Neighborhood
#         return Neighborhood
    
#     if d == 0:
#         return Pattern
#     if len(Pattern) == 1:
#         return ['A', 'C', 'G', 'T']
#     Neighborhood = set()
#     SuffixNeighbors = Neighbors(Suffix(Pattern), d)
#     for t in SuffixNeighbors:
#         if HammingDistance(Suffix(Pattern), t) < d:
#             for x in t:
#                 Neighborhood.add(x + t)
#         else:
#             Neighborhood.add(FirstSymbol(Pattern) + t)
#     return Neighborhood
            
# def FirstSymbol(Pattern):
    
# def Suffix(Pattern):
    
    

# Place your Neighbors() function here, along with any subroutines you need.
# Neighbors() should return a list.
# Place your Neighbors() function here, along with any subroutines you need.
# Neighbors() should return a list.

chars = "ACGT"

def Neighbors(pattern, d):
    l = sum([neighbors(pattern, d2) for d2 in range(d + 1)], [])
    l = set(l)
    # print(len(l))
    # res = str(l.pop())
    l = list(l)
    for i in l:
        # res += ' {}'.format(str(i))
        print('{} '.format(i))
    return l
    
def neighbors(pattern, d):
    assert(d <= len(pattern))

    if d == 0:
        return [pattern]

    r2 = Neighbors(pattern[1:], d-1)
    r = [c + r3 for r3 in r2 for c in chars if c != pattern[0]]

    if (d < len(pattern)):
        r2 = Neighbors(pattern[1:], d)
        r += [pattern[0] + r3 for r3 in r2]

    return r
    
Neighbors('ACGT', 3)