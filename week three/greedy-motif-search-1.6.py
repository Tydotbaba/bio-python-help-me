
'''
	Code Challenge: Implement GreedyMotifSearch with pseudocounts.

	Input: Integers k and t, followed by a collection of strings Dna.

	Output: A collection of strings BestMotifs resulting from applying 
			GreedyMotifSearch(Dna, k, t) with pseudocounts. 
			If at any step you find more than one Profile-most probable 
			k-mer in a given string, use the one occurring first.
'''

from collections import Counter 

motifs = [
	'TCGGGGGTTTTT',
	'CCGGTGACTTAC',
	'ACGGGGATTTTC',
	'TTGGGGACTTTT',
	'ATGGGGACTTCC',
	'TCGGGGACTTCC',
	'TCGGGGATTCAT',
	'TAGGGGATTCCT',
	'TAGGGGAACTAC',
	'TCGGGTATAACC'
]

def Score(motifs):
	''' Score(Motifs) is the number of unpopular 
		(lower case) letters in the motif matrix Motifs

		@args: 
			motifs -> a string matrix of nueclotides

		@returns:
			integer, number of unpopular nueclotides
	'''
	
	result = []
	for j in range(len(motifs[0])):
		# let j be the motifs column
		# get each row nueclotide in motifs column
		res = [string[j] for string in motifs]
		# Pass the res list to instance of Counter clas. 
		counter = Counter(res) 
		  
		# most_common() produces k frequently encountered 
		# input values and their respective counts. 
		# count the most frequent nueclotide. 
		most_occur = counter.most_common(1)
		# add most_occur to result
		result.append(len(res) - most_occur[0][-1])
	# return the sum of the result
	return sum(result)


# Score(motifs)


def Count(motifs):
	'''Count(motifs) construct the 4 × k count matrix  
		counting the number of occurrences of each nucleotide in each
		column of the motif matrix; the (i, j)-th element of Count(Motifs) 
		stores the number of times that nucleotide i appears in column j 
		of Motifs
	'''
	result = {
		'A': [],
		'C': [],
		'G': [],
		'T': [],
	}
	if len(motifs) == 0:
		return {}
	if len(motifs) == 1:
		return {
			'A': [1 + 1 if 'A' == i else 0 + 1 for i in motifs[0]],
			'C': [1 + 1 if 'C' == i else 0 + 1 for i in motifs[0]],
			'G': [1 + 1 if 'G' == i else 0 + 1 for i in motifs[0]],
			'T': [1 + 1 if 'T' == i else 0 + 1 for i in motifs[0]],
		}
	for j in range(len(motifs[0])):
		# let j be the motifs column
		# get each row nueclotide in motifs column
		res = [string[j] for string in motifs]
		result['A'].append(int(res.count('A')) + 1)
		result['C'].append(int(res.count('C')) + 1)
		result['G'].append(int(res.count('G')) + 1)
		result['T'].append(int(res.count('T')) + 1)
	# return the sum of the result
	# print(result)
	return result

motifs = [
	'GGCGT'
]
# print(Count(motifs))


def ProfileMatrix(motifs):
	motifCount = Count(motifs)
	t = len(motifs) + 4
	# print(motifCount['A'])
	result = {
		'A': [],
		'C': [],
		'G': [],
		'T': [],
	}
	result['A'].extend([value / t for value in motifCount['A']])
	result['C'].extend([value / t for value in motifCount['C']])
	result['G'].extend([value / t for value in motifCount['G']])
	result['T'].extend([value / t for value in motifCount['T']])

	# return the result
	# print(result)
	return result

# print(ProfileMatrix(motifs))






from functools import reduce

# Compute Pr(pattern | Profile)
def Pr(pattern, Profile):
	res = [Profile[genome][i] for i, genome in enumerate(pattern)]
	# print(res)
	return reduce(lambda x, y: x * y, res)


def ProfileMostProbableKmer(text, k, profile):
	# for each k-mer in test
	# find Pr(k-mer, Profile)
	# find the maximum k-mer with high probability in Profile
	res = [Pr(text[i : i + k], profile) for i in range(len(text) - k + 1)]
	# print([text[i : i + k] for i in range(len(text) - k + 1)], res, max(res), sep='\n')
	return text[res.index(max(res)): res.index(max(res)) + k]


def  GreedyMotifSearchWithPseudocounts(Dna, k, t):
	'''
		@args:
			Dna -> str, a Dna of a bacterial or plant
			k -> integer, represents a k-mer motif
			t -> integer, represents the number of strings in Dna
		@returns:
			A collection of strings BestMotifs

		BestMotifs ← motif matrix formed by first k-mers in each string from Dna
	'''
	# print(Dna)
	BestMotifs = [string[0:k] for string in Dna]
	# print(BestMotifs)
	# print(BestMotifs)
	for i in range(0, len(Dna[0]) - k + 1):
		motifs = []
		motifs.append(Dna[0][i:i+k])
		for j in range(1, t):
			profile = ProfileMatrix(motifs)
			# print('profile: ', profile, sep='\n')
			most_probable_motif = ProfileMostProbableKmer(
										text = Dna[j],
										k = k,
										profile = profile
									)
			motifs.append(most_probable_motif)

			# print('motifs: ', motifs, sep='\n')
		
		# print('Score(BestMotifs): ', Score(BestMotifs), sep='\n')
		# print('Score(motifs): ', Score(motifs), sep='\n')
		if Score(motifs) < Score(BestMotifs):
			BestMotifs = motifs.copy()
		# break
	print()
	print('BestMotifs: ', ' '.join(BestMotifs), sep='\n')


# code to parse input file for GreedyMotifSearchWithPseudocounts
def parseFile(f):
	res = []
	str_list = f.strip().split('\n')
	res.extend(str_list[0].split())
	res.extend(str_list[1:])
	# print(res)
	return res 

# change your code below this line for GreedyMotifSearchWithPseudocounts

# change your code below this line
# read the file
try:
	with open('./datasets/dataset_2_7.txt') as f:
		Text = f.read()
		[k, t, *Dna] = parseFile(Text)
		k, t = int(k), int(t)
except Exception as e:
	raise e
# change your code above this line for GreedyMotifSearchWithPseudocounts


GreedyMotifSearchWithPseudocounts(Dna, k, t)










'''
	Coded Graded Problem
	
	Implement GreedyMotifSearchWithPseudocounts() below along with 
	any subroutines that you need.
	Your function should include a pseudocount parameter that 
	is added to each element of the count matrix.
	(When your function is called, the pseudocount parameter 
	will be equal to 1.)
'''


from collections import Counter 


def Score(motifs):
	''' Score(Motifs) is the number of unpopular 
		(lower case) letters in the motif matrix Motifs

		@args: 
			motifs -> a string matrix of nueclotides

		@returns:
			integer, number of unpopular nueclotides
	'''
	
	result = []
	for j in range(len(motifs[0])):
		# let j be the motifs column
		# get each row nueclotide in motifs column
		res = [string[j] for string in motifs]
		# Pass the res list to instance of Counter clas. 
		counter = Counter(res) 
		  
		# most_common() produces k frequently encountered 
		# input values and their respective counts. 
		# count the most frequent nueclotide. 
		most_occur = counter.most_common(1)
		# add most_occur to result
		result.append(len(res) - most_occur[0][-1])
	# return the sum of the result
	return sum(result)


# Score(motifs)


def Count(motifs):
	'''Count(motifs) construct the 4 × k count matrix  
		counting the number of occurrences of each nucleotide in each
		column of the motif matrix; the (i, j)-th element of Count(Motifs) 
		stores the number of times that nucleotide i appears in column j 
		of Motifs
	'''
	result = {
		'A': [],
		'C': [],
		'G': [],
		'T': [],
	}
	if len(motifs) == 0:
		return {}
	if len(motifs) == 1:
		return {
			'A': [1 + 1 if 'A' == i else 0 + 1 for i in motifs[0]],
			'C': [1 + 1 if 'C' == i else 0 + 1 for i in motifs[0]],
			'G': [1 + 1 if 'G' == i else 0 + 1 for i in motifs[0]],
			'T': [1 + 1 if 'T' == i else 0 + 1 for i in motifs[0]],
		}
	for j in range(len(motifs[0])):
		# let j be the motifs column
		# get each row nueclotide in motifs column
		res = [string[j] for string in motifs]
		result['A'].append(int(res.count('A')) + 1)
		result['C'].append(int(res.count('C')) + 1)
		result['G'].append(int(res.count('G')) + 1)
		result['T'].append(int(res.count('T')) + 1)
	# return the sum of the result
	# print(result)
	return result

motifs = [
	'GGCGT'
]
# print(Count(motifs))


def ProfileMatrix(motifs):
	motifCount = Count(motifs)
	t = len(motifs) + 4
	# print(motifCount['A'])
	result = {
		'A': [],
		'C': [],
		'G': [],
		'T': [],
	}
	result['A'].extend([value / t for value in motifCount['A']])
	result['C'].extend([value / t for value in motifCount['C']])
	result['G'].extend([value / t for value in motifCount['G']])
	result['T'].extend([value / t for value in motifCount['T']])

	# return the result
	# print(result)
	return result

# print(ProfileMatrix(motifs))



from functools import reduce

# Compute Pr(pattern | Profile)
def Pr(pattern, Profile):
	res = [Profile[genome][i] for i, genome in enumerate(pattern)]
	# print(res)
	return reduce(lambda x, y: x * y, res)


def ProfileMostProbableKmer(text, k, profile):
	# for each k-mer in test
	# find Pr(k-mer, Profile)
	# find the maximum k-mer with high probability in Profile
	res = [Pr(text[i : i + k], profile) for i in range(len(text) - k + 1)]
	# print([text[i : i + k] for i in range(len(text) - k + 1)], res, max(res), sep='\n')
	return text[res.index(max(res)): res.index(max(res)) + k]


def  GreedyMotifSearchWithPseudocounts(Dna, k, t, pseudocount):
	'''
		@args:
			Dna -> str, a Dna of a bacterial or plant
			k -> integer, represents a k-mer motif
			t -> integer, represents the number of strings in Dna
		@returns:
			A collection of strings BestMotifs

		BestMotifs ← motif matrix formed by first k-mers in each string from Dna
	'''
	# print(Dna)
	BestMotifs = [string[0:k] for string in Dna]
	# print(BestMotifs)
	# print(BestMotifs)
	for i in range(0, len(Dna[0]) - k + 1):
		motifs = []
		motifs.append(Dna[0][i:i+k])
		for j in range(1, t):
			profile = ProfileMatrix(motifs)
			# print('profile: ', profile, sep='\n')
			most_probable_motif = ProfileMostProbableKmer(
										text = Dna[j],
										k = k,
										profile = profile
									)
			motifs.append(most_probable_motif)

			# print('motifs: ', motifs, sep='\n')
		
		# print('Score(BestMotifs): ', Score(BestMotifs), sep='\n')
		# print('Score(motifs): ', Score(motifs), sep='\n')
		if Score(motifs) < Score(BestMotifs):
			BestMotifs = motifs.copy()
		# break
	print()
	return BestMotifs