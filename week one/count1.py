'''
	Count1 from Hamming distance
	HammingDistance(Pattern, pattern') <= d
'''

# change your code below this line
# text = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC'
# d = 3
# pattern = 'ATTCTGGA'
# # change your code above this line

# count = 0
# def HammingDistance(p, q):
#     d = 0
#     for i, j in zip(p, q):
#         if i != j:
#             d += 1
#     return d

# l = []

# def makeList(text, pattern):
# 	p = len(pattern)
# 	for i in range(len(text) - p):
# 		l.append(text[i:i + p])

# makeList(text, pattern)
# # print(l)
# # print(HammingDistance(p, q))


# for genome in l:
# 	if HammingDistance(pattern, genome) <= d:
# 		count += 1

# print(count)




# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(text, pattern, d):
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
			res.append(genome)

	#print(count)
	return res




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
			res.append(i)

	# print(count)
	return res



# change your code below this line
text = 'AAGCAAAGGTGGG'
d = 1
pattern = 'AT'

# # change your code above this line


print(ApproximatePatternCount(text, pattern, d))



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

# print(reverse('TTA'))
