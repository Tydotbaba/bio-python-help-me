'''
Exercise Break: Compute Pr(TCGTGGATTTCC | Profile), 
where Profile is the matrix shown above.
'''
from math import prod


Profile = {
	'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
	'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
	'G': [0.0, 0.0, 0.1, 0.1, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
	'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}

pattern = 'TCGTGGATTTCC'

def Pr(pattern, Profile):
	res = [Profile[genome][i] for i, genome in enumerate(pattern)]
	print(res)
	return prod(res)
	# return reduce(lambda x, y: x * y, res)


print(Pr(pattern, Profile))




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
	




# code to parse input file for DistanceBetweenPatternAndStrings
def parseFile(f):
	profile = {}
	str_list = f.strip().split('\n')
	text = str_list[0]
	k = int(str_list[1])
	profile['A'] = [float(value) for value in str_list[2].split(' ')]
	profile['C'] = [float(value) for value in str_list[3].split(' ')]
	profile['G'] = [float(value) for value in str_list[4].split(' ')]
	profile['T'] = [float(value) for value in str_list[5].split(' ')]
	return text, k, profile 

# change your code above this line for DistanceBetweenPatternAndStrings

# change your code below this line
# read the file
# try:
	# with open('./datasets/dataset_2_7.txt') as f:
	# 	Text = f.read()
	# 	text, k, profile = parseFile(Text)
		# print(text)
		# print(k)
		# print(profile)
# except Exception as e:
	# raise e
# change your code below this line for DistanceBetweenPatternAndStrings

# print(ProfileMostProbableKmer(text, k, profile))



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






