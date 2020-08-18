'''
Exercise Break: Compute Pr(TCGTGGATTTCC | Profile), 
where Profile is the matrix shown above.
'''
from collections import Counter 
from functools import reduce

Profile = {
	'A': [4/5, 0.0, 0.0, 1/5],
	'C': [0.0, 3/5, 1/5, 0.0],
	'G': [1/5, 1/5, 4/5, 0.0],
	'T': [0.0, 1/5, 0.0, 4/5],
}

pattern = 'TCGTGGATTTCC'

def Pr(pattern, Profile):
	res = [Profile[genome][i] for i, genome in enumerate(pattern)]
	# print(res)
	# return prod(res)
	return reduce(lambda x, y: x * y, res)


# print(Pr(pattern, Profile))




'''
	Profile-most Probable k-mer Problem: 
	Find a Profile-most probable k-mer in a string.

	Input: A string Text, an integer k, and a 4 × k matrix Profile.
	Output: A Profile-most probable k-mer in Text.
	Code Challenge: Solve the Profile-most Probable k-mer Problem.
'''



def ProfileMostProbableKmer(text, k, profile):
	# for each k-mer in test
	# find Pr(k-mer, Profile)
	# find the maximum k-mer with high probability in Profile
	res = [Pr(text[i : i + k], profile) for i in range(len(text) - k + 1)]
	# print(res)
	return text[res.index(max(res)): res.index(max(res)) + k]
	




def Motifs(profile, Dna):
	k = len(profile['A'])
	motifs = []
	for string in Dna:
		motifs.append(ProfileMostProbableKmer(string, k, profile))
	return motifs





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


def RandomNumber(N):
	'''generate random numbers from 1 - N and return it'''
	import random
	return random.randint(0, N)

def randomly_select_kmers(Dna, k):
	''' randomly select kmers in each string in Dna
		@args: Dna -> str, a dna of a bacterial of plant

		@returns:
			list,
	'''
	motifs = []
	for string in Dna:
		j = RandomNumber(len(Dna[0]) - k)
		motifs.append(string[j : j + k])
	return motifs
	


def GibbsSampler(Dna, k, t):
	initial_motifs = randomly_select_kmers(Dna, k)
	BestMotifs = randomly_select_kmers(Dna, k)
	while True:
		profile = ProfileMatrix(initial_motifs)
		motifs = Motifs(profile, Dna)
		if Score(motifs) < Score(BestMotifs):
			BestMotifs = motifs
			initial_motifs = motifs
		else:
			return BestMotifs


def Random(probabilities):
    summand=sum(probabilities)
    for i in range(len(probabilities)):
        probabilities[i]=probabilities[i]/(summand)
    random_number=random.random()
    counter=0
    for j in range(len(probabilities)):
        if random_number>=counter and random_number<(counter+probabilities[j]):
            return j
        else:
            counter+=probabilities[j]

# code to parse input file for DistanceBetweenPatternAndStrings
def parseFile(f):
	str_list = f.strip().split('\n')
	[k, t] = str_list[0].split()
	[*Dna] = str_list[1:]
	k, t = int(k), int(t)
	# print(k, t, Dna)
	return k, t, Dna

	 

# change your code above this line for DistanceBetweenPatternAndStrings

# change your code below this line
# read the file
try:
	with open('./datasets/dataset_2_7.txt') as f:
		Text = f.read()
		k, t, Dna = parseFile(Text)
		# print(Dna)
except Exception as e:
	raise e
# change your code below this line for DistanceBetweenPatternAndStrings


def run():
	lowest_bestscore = float('inf')
	lowest_motifs = []
	i = 0
	while True:
		bestmotifs = GibbsSampler(Dna, k, t)
		bestscore = Score(bestmotifs)
		if bestscore < lowest_bestscore:
			lowest_bestscore = bestscore
			lowest_motifs = bestmotifs
			i = 0
		else:
			i += 1
		if i > 900:
			break

	return '\n'.join(lowest_motifs)


print(run())
# print(Motifs(Profile, Dna))



'''
  coded graded Problem

'''

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






