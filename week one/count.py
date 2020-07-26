'''
	Count the number of occurences of pattern in text.
	e.g: Count(ACAACTATGCATACTATCGGGAACTATCCT, ACTAT) => 3.
'''

# change your code below this line
# read the file
# try:
# 	with open('./datasets/dataset_2_7.txt') as f:
# 		Text = f.read()
# except Exception as e:
# 	raise e

# Pattern = 'GAGTATAGA'
# # change your code above this line


# test1: worked
# count = 0
# l = []
# def makeList(Text, Pattern):
# 	'''make a list of pattern occurences in text'''
# 	p = len(pattern)
# 	for i in range(len(text) - p + 1):
# 		l.append(text[i:i + p])

# def count(patternList, pattern):
# 	return patternList.count(pattern)

# makeList(text, pattern)
# res = count(l, pattern)
# print(res)




def PatternCount(Text, Pattern):
	count = 0
	p = len(Pattern)
	for i in range(len(Text) - p + 1):
		if Text[i:i + p] == Pattern:
			count += 1
	return count

# print(PatternCount(Text, Pattern))
	



# Another Question
# Frequent Words Problem: Find the most frequent k-mers in a string.
# Code Challenge: Solve the Frequent Words Problem.
# Input: A string Text and an integer k.
# Output: All most frequent k-mers in Text.

# Sample Input:
# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4
# Sample Output:
# CATG GCAT

def  FrequentWords(Text, k):
	FrequentPatterns = set()
	count = []
	for i in range(len(Text) - k + 1):
		pattern = Text[i:i + k]
		count.append(PatternCount(Text, pattern))
	maxi = max(count)
	for i in range(len(Text) - k + 1):
		if maxi == count[i]:
			FrequentPatterns.add(Text[i:i + k])
	return FrequentPatterns


# change your code below this line
# read the file
# try:
# 	with open('./datasets/dataset_2_7.txt') as f:
# 		Text = f.read()
# except Exception as e:
# 	raise e
Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 12
# # change your code above this line

# print(FrequentWords(Text, k))






# Reverse Complement Problem: Find the reverse complement of a DNA string.

# Input: A DNA string Pattern.
# Output: Patternrc , the reverse complement of Pattern.
# Code Challenge: Solve the Reverse Complement Problem.


# change your code below this line
# read the file
# try:
# 	with open('./datasets/dataset_2_7.txt') as f:
# 		pattern = f.read()
# except Exception as e:
# 	raise e
# Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'


def reverse(pattern):
	pattern_lenght = len(pattern)
	assert pattern_lenght > 0
	
	if pattern_lenght >= 1:
		res = ''
		for i in range(pattern_lenght):
			if pattern[i] == 'A':
				res += 'T'
			if pattern[i] == 'T':
				res += 'A'
			if pattern[i] == 'C':
				res += 'G'
			if pattern[i] == 'G':
				res += 'C'
		return res[::-1]

# print(reverse(pattern))




# Code Challenge: Solve the Pattern Matching Problem.

# Input: Two strings, Pattern and Genome.
# Output: A collection of space-separated integers specifying all 
# starting positions where Pattern appears as a substring of Genome.
# Visit the code-graded problem!

# Extra Dataset

# Debug Datasets

# Sample Input:

# ATAT
# GATATATGCATATACTT
# Sample Output:

# 1 3 9
# Exercise Break: Return a space-separated list of starting positions 
# (in increasing order) where CTTGATCAT appears as a substring in
# the Vibrio cholerae genome.

# change your code below this line
# text = 'GATATATGCATATACTT'
# read the file
# try:
# 	with open('./datasets/dataset_2_7.txt') as f:
# 		text = f.read()
# except Exception as e:
# 	raise e
# d = 0
# pattern = 'CTTGATCAT'

# # change your code above this line

# countd(text, pattern)
def ApproximatePatternCount(text, pattern, d):
	l = [] # initializing list of positions
	count = 0
	def HammingDistance(p, q):
		d = 0
		for i, j in zip(p, q):
			if i != j:
				d += 1
		return d

	def makeList(text, pattern):
		p = len(pattern)
		for i in range(len(text) - p + 1):
			l.append(text[i:i + p])

	makeList(text, pattern)
	#print(l)
	# print(HammingDistance(p, q))
	
	res = []
	for i, genome in enumerate(l):
		if HammingDistance(pattern, genome) <= d:
			count += 1
			res.append(str(i))

	# print(count)
	return ' '.join(res)



# print(ApproximatePatternCount(text, pattern, d))





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

index = 5437
k = 8
# print(NumberToPattern(index, k))





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

Text ='TGTGTGAATCCCGGGTCCGCTGTGTGACCCTTTTAAGGGCCTGTGCATCGATTCTAAATATCAAAGGCTGTGCTTGAATCCCATACATCGCCTGCCGATATAATTACGAGCGCAAACTTCCTGCCATGCGGCTGCTTACACTGTGCTTACCTACTCTATAGTCGCAATCAAGGACGTATATTCGTGATGCAGGCACTGGACATGCTCTGTCACAAGACTACGTGTTACGTTTACTGTACCGCGGCGACTACGATAATTAAAGCTGGCGGTACCGACCGGGCACCCGAACAATAAACACCAATGTCGTATATAAAGATTTTCAGGGCACGGTAAAGTGGCTTTCACTGAGACAATAGTATAACAGCTAGCCGTCGGCCTGAAATAAGCGCTGATAAATATCCCCGATTGCTCAACCGTTTGCAAGGGATTTTACAACTTCGAACAATTCGGGAGTCATACCATATCTCAAACTGATGGGGTACATCGGAGGTATTCTGAACGATGATCCACGCTTGGGGGCTGCGTTGGATTTGCTCTCAGCCAGTCCCCTTTTGTCACTCCTTTCACATCAGTAGAGAAGTTGTAGGATGGGGATGGTTTAAGCTGGGGAGTTATACACTATGCAACGCAGCTCACTCAGACTGTATCCAT'
k = 7
# print(ComputingFrequencies(Text, k))









# Code Challenge: Solve the Clump Finding Problem (restated below). 
# You will need to make sure that your algorithm is efficient 
# enough to handle a large dataset.
# Clump Finding Problem: Find patterns forming clumps in a string.
# link: https://stepik.org/lesson/3012/step/1?unit=8237
# Input: A string Genome, and integers k, L, and t.
# Output: All distinct k-mers forming (L, t)-clumps in Genome.
# Visit the code-graded problem!

# Extra Dataset

# Debug Datasets

# Sample Input:

# CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA
# 5 50 4
# Sample Output:

# CGACA GAAGA

import math
def ClumpFinding(Genome, k, L, t):
	FrequentPatterns = set()
	clump = []
	for i in range(int(math.pow(4,k))):
		clump.append(0)
	for i in range(len(Genome) - L + 1):
			text = Genome[i: i + L]
			frequencyArray = ComputingFrequencies(text, k)
			for i in range(int(math.pow(4,k))):
				if frequencyArray[i] >= t:
					clump[i] = 1
	for i in range(int(math.pow(4,k))):
		if clump[i] == 1:
			pattern = NumberToPattern(i, k)
			FrequentPatterns.add(pattern)
	return ' '.join(map(str, FrequentPatterns))


# change your code below this line
# Genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
# read the file
try:
	with open('./datasets/dataset_2_7.txt') as f:
		Genome = f.read()
except Exception as e:
	raise e
k = 8
L = 29
t = 4
# pattern = 'CTTGATCAT'

# # change your code above this line

print(ClumpFinding(Genome, k, L, t))
