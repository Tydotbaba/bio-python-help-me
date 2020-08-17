
def Entropy(Motifs):
    profile = {}
    # check that all motifs are the same length
    ListLength = len(Motifs)
    L1 = len(Motifs[1]) # length of the first motif
    print('There are {} motifs of length {}'.format(ListLength, L1))
    for i in range(len(Motifs)):
        if len(Motifs[i]) != L1:
            ShortMotif = Motifs[i]
            ShortMotifLen = len(ShortMotif)
            print('Oops, Motif {} is {} nucleotides instead of {}!'.format(ShortMotif, ShortMotifLen, L1))
            break
        
    # fill all positions with frequency of 0
    for nucleotide in 'ACGT':
        values = [0] * L1
        profile[nucleotide] = values
        
    # iterate through each position in the motif matrix, counting nucleotide frequencies
    TotalEntropy = 0
    for key, values in profile.items():
        for Motif in Motifs:
            for i in range(len(Motif)):
                if Motif[i] == key:
                    profile[key][i] += 1
        
        # convert nucleotide frequencies to probabilities
        for i in range(len(values)):
            profile[key][i] = profile[key][i] / float(ListLength)
        
        # calculate total entropy (Sum of (Prob_value * log2 Prob_n))
        import math
        for value in values:
            if value > 0:
                TotalEntropy += abs(value * math.log(value, 2))
            else: continue
            
    return(TotalEntropy)


Motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]

# print(Entropy(Motifs))



import math


profile = {
        'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
        'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
        'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}


total_enthropy = 0.0
for key, values in profile.items():
    for value in values:
        if value > 0:
            total_enthropy += abs(value * math.log(value, 2))
        else:
            continue
print(total_enthropy)