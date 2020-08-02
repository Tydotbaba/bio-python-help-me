# place your ClumpFinding() function here along with any subroutines you need.
#def ClumpFinding(genome, k, L, t):
import math

def ComputingFrequencies(Text, k):
	FrequencyArray = []
	for i in range(int(math.pow(4, k))):
		FrequencyArray.append(0)
	for i in range(len(Text) - k + 1):
		patern = Text[i:i+k]
		j = PatternToNumber(patern)
		FrequencyArray[j] += 1
	# return ' '.join(map(str, FrequencyArray))
	return FrequencyArray



# # convert patern to number in the neigbours array
def PatternToNumber(patern):
	'''
		convert patern to number given patern of k-mer
		e.g: PatternToNumber('AAAA') -> 0
		@args: i -> str, represents patern of each k-mer in 
				lexicographic order
		@returns: int, the index of patern in its Neighborhoods
	'''
	k =  len(patern)
	if k == 0: 
		return 0
	symbol = patern[-1]
	prefix = patern[:-1]

	return 4 * PatternToNumber(prefix) + symbolToNumber(symbol)

def symbolToNumber(neuclotide):
	return {
	        	'A': 0,
		        'C': 1,
		        'G': 2,
		        'T': 3
		    }.get(neuclotide, 0) 

patern = 'ATGCAA'
# print(PatternToNumber(patern))






# convert patern to number in the neigbours array
def NumberToPattern(index, k):
	'''
		convert patern to number given patern of k-mer
		e.g: PatternToNumber('AAAA') -> 0
		@args: index -> str, represents index a k-mer in 
				lexicographic order
		@args: k -> str, represents  of each k-mer in 
				lexicographic order
		@returns: int, the index of patern in its Neighborhoods
	'''
	if k == 1: 
		return NumberToSymbol(index)
	prefixIndex = index // 4
	r = index % 4
	symbol = NumberToSymbol(r)
	# print(symbol)
	return NumberToPattern(prefixIndex, k-1) + symbol
	

def NumberToSymbol(index):
	return {
	        	0: 'A',
		        1: 'C',
		        2: 'G',
		        3: 'T'
		    }.get(index) 

def ClumpFinding(Genome, k, L, t):
	FrequentPatterns = set()
	clump = [0 for i in range(int(math.pow(4,k)))]
	text = Genome[0:L]
	frequencyArray = ComputingFrequencies(text, k)
	for i in range(int(math.pow(4,k))):
		if frequencyArray[i] >= t:
			clump[i] = 1
	for i in range(1, len(Genome) - L + 1):
		FirstPattern = Genome[i - 1:i - 1 + k]
		index = PatternToNumber(FirstPattern)
		frequencyArray[index] -= 1
		LastPattern = Genome[i + L - k: i + L] 
		index = PatternToNumber(LastPattern)
		frequencyArray[index] += 1
		if frequencyArray[index] >= t:
			clump[index] = 1
	for i in range(int(math.pow(4,k))):
		if clump[i] == 1:
			pattern = NumberToPattern(i, k)
			FrequentPatterns.add(pattern)
	return FrequentPatterns




# place your ClumpFinding() function here along with any subroutines you need.

import math
import time

motif_dict = {}

def ClumpFinding(genome,k,L,t):
    motif_len = k # for better readability
    list = []
    n = 1
    for i in range(len(genome)-motif_len ):
        motif = genome[i:i+motif_len]
        if motif not in motif_dict:
            motif_dict[motif] = [1,i] 
        else:
            motif_dict[motif][0] += 1 # accumulate the count
            motif_dict[motif].append(i) # append() to the list the index of all founded motif
    print(motif_dict)
    for motif in motif_dict:
        # look for motif repeated t times with an index distance of L
        if motif_dict[motif][0] >= t and motif not in list:
            for n in range(len(motif_dict[motif])-t):
                if motif_dict[motif][n+t-1] - motif_dict[motif][n] <= L:
                    if motif not in list:
                        list.append(motif)
    return list




# my submission
# place your ClumpFinding() function here along with any subroutines you need.
#def ClumpFinding(genome, k, L, t):
import math

def ComputingFrequencies(Text, k):
	FrequencyArray = []
	for i in range(int(math.pow(4, k))):
		FrequencyArray.append(0)
	for i in range(len(Text) - k + 1):
		patern = Text[i:i+k]
		j = PatternToNumber(patern)
		FrequencyArray[j] += 1
	# return ' '.join(map(str, FrequencyArray))
	return FrequencyArray



# # convert patern to number in the neigbours array
def PatternToNumber(patern):
	'''
		convert patern to number given patern of k-mer
		e.g: PatternToNumber('AAAA') -> 0
		@args: i -> str, represents patern of each k-mer in 
				lexicographic order
		@returns: int, the index of patern in its Neighborhoods
	'''
	k =  len(patern)
	if k == 0: 
		return 0
	symbol = patern[-1]
	prefix = patern[:-1]

	return 4 * PatternToNumber(prefix) + symbolToNumber(symbol)

def symbolToNumber(neuclotide):
	return {
	        	'A': 0,
		        'C': 1,
		        'G': 2,
		        'T': 3
		    }.get(neuclotide, 0) 

# patern = 'ATGCAA'
# print(PatternToNumber(patern))






# convert patern to number in the neigbours array
def NumberToPattern(index, k):
	'''
		convert patern to number given patern of k-mer
		e.g: PatternToNumber('AAAA') -> 0
		@args: index -> str, represents index a k-mer in 
				lexicographic order
		@args: k -> str, represents  of each k-mer in 
				lexicographic order
		@returns: int, the index of patern in its Neighborhoods
	'''
	if k == 1: 
		return NumberToSymbol(index)
	prefixIndex = index // 4
	r = index % 4
	symbol = NumberToSymbol(r)
	# print(symbol)
	return NumberToPattern(prefixIndex, k-1) + symbol
	

def NumberToSymbol(index):
	return {
	        	0: 'A',
		        1: 'C',
		        2: 'G',
		        3: 'T'
		    }.get(index) 

def ClumpFinding(Genome, k, L, t):
	FrequentPatterns = set()
	clump = [0 for i in range(int(math.pow(4,k)))]
	text = Genome[0:L]
	frequencyArray = ComputingFrequencies(text, k)
	for i in range(int(math.pow(4,k))):
		if frequencyArray[i] >= t:
			clump[i] = 1
	for i in range(1, len(Genome) - L + 1):
		FirstPattern = Genome[i - 1:i - 1 + k]
		index = PatternToNumber(FirstPattern)
		frequencyArray[index] -= 1
		LastPattern = Genome[i + L - k: i+ L] 
		index = PatternToNumber(LastPattern)
		frequencyArray[index] += 1
		if frequencyArray[index] >= t:
			clump[index] = 1
	for i in range(int(math.pow(4,k))):
		if clump[i] == 1:
			pattern = NumberToPattern(i, k)
			FrequentPatterns.add(pattern)
	return FrequentPatterns

# change your code below this line
# read the file
Genome = 'CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
# try:
# 	with open('./datasets/dataset_2_7.txt') as f:
# 		Genome = f.read()
# except Exception as e:
# 	raise e
k = 3
L = 25
t = 3

# change your code above this line	

print(ClumpFinding(Genome, k, L, t))