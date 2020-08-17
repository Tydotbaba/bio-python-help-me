import math

def HammingDistance(p, q):
		d = 0
		for i, j in zip(p, q):
			if i != j:
				d += 1
		return d
def DistanceBetweenPatternAndStrings(Pattern, Dna):
	k = len(Pattern)
	distance = 0
	for string in Dna:
		hammingDistance = math.inf
		patern_list = [string[i:i+k] for i in range(len(string) - k + 1)]
		for pattern_prim in patern_list:
			if hammingDistance > HammingDistance(Pattern, pattern_prim):
				hammingDistance = HammingDistance(Pattern, pattern_prim)
		distance += hammingDistance
	return distance


# code to parse input file for DistanceBetweenPatternAndStrings
def parseFile(f):
	# print(f)
	res = []
	str_list = f.strip().split('\n')
	res.append(str_list[0])
	res.extend(str_list[1].split(' '))
	# print(res)
	# print(str_list)

	# return parsed result
	return res

# change your code above this line for DistanceBetweenPatternAndStrings

# change your code below this line
# read the file
# try:
# 	with open('./datasets/dataset_2_7.txt') as f:
# 		Text = f.read()
# 		[pattern, *Dna] = parseFile(Text)
# except Exception as e:
# 	raise e
# change your code below this line for DistanceBetweenPatternAndStrings

# print(DistanceBetweenPatternAndStrings(pattern, Dna))



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


def MedianString(Dna, k):
	k = int(k)
	distance = math.inf
	Median = ''
	patterns = [NumberToPattern(i, k) for i in range(int(math.pow(4, k)))]
	# print(paterns)
	for k_mer in patterns:
		if distance > DistanceBetweenPatternAndStrings(k_mer, Dna):
			distance = DistanceBetweenPatternAndStrings(k_mer, Dna)
			Median = k_mer
	return Median


# Dna = [
# 	'AAATTGACGCAT',
# 	'GACGACCACGTT',
# 	'CGTCAGCGCCTG',
# 	'GCTGAGCACCGG',
# 	'AGTACGGGACAG'
# ]
# k = 3
# pattern = 'AAA'




# code to parse input file for MedianString
def parseFile(f):
	return f.strip().split('\n')
	

# change your code below this line for MedianString
# read the file
try:
	with open('./datasets/dataset_2_7.txt') as f:
		Text = f.read()
		[k, *Dna] = parseFile(Text)
except Exception as e:
	raise e
# change your code above this line for MedianString

print(MedianString(Dna, k))

