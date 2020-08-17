'''
N = 500, L = 1000, k = 9.

Then, the combination of a 9-mer is 
(4 * 4 * 4 * 4 * 4 * 4 * 4 * 4 *4) = 4^9, 
and how each nucleotide has a 1/4 of probability of appearing,
then every 9-mer has a (1/4)^9 of probability of appearing.

In a space of 1000 nucleotides, 
there are (L - k + 1) different 9-mer.

So the probability to getting a specific 9-mer is: 
N * (L - k + 1) * (1/4)^9 = 1.89208984375

'''








'''

Code Challenge: Implement MotifEnumeration (reproduced below).

Input: Integers k and d, followed by a collection of strings Dna.
Output: All (k, d)-motifs in Dna.

Sample Input:

3 1
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT
Sample Output:

ATA ATT GTT TTT
'''

chars = "ACGT"

def Neighbors(pattern, d):
	l = sum([neighbors(pattern, d2) for d2 in range(d + 1)], [])
	l = set(l)    
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

def findNeigbours(pattern, d):
	l = Neighbors(pattern, d)
	return sorted(list(l))
	# for i in l:
	#     # res += ' {}'.format(str(i))
	#     print(i, end=' ')

# findNeigbours('AT', 2)
# print(findNeigbours('AT', 1))



def  MotifEnumeration(Dna, k, d):
	k = int(k)
	d = int(d)
	# print(k)
	# print(d)
	# print(Dna)
	kmer_list = [set() for _ in Dna] # Creating a list of sets length len(Dna)
	for pos, pattern in enumerate(Dna):
		for k_pos in range(len(pattern) - k + 1):
			# Generate neighbors for all kmers in all strings and
			# add them to a set() in a kmer_list
			kmer_list[pos].update(findNeigbours(pattern[k_pos:k_pos + k], d))

	patterns = kmer_list[0]
	for k_set in kmer_list:
		# Use 'AND' on a Python set() to ONLY get kmers from all sets
		# that are in all sets we generated above
		patterns &= k_set
	return ' '.join(patterns)



# code to parse input file
def parseFile(f):
	# print(f)
	res = []
	str_list = f.strip().split(' ')
	res.append(str_list[0])
	str_list = str_list[1].split('\n')
	res.extend(str_list)
	print(res)
	# print(str_list)

	# return parsed result
	return res
# change your code below this line
# read the file
try:
	with open('./datasets/dataset_2_7.txt') as f:
		Text = f.read()
		[k, d, *Dna] = parseFile(Text)
except Exception as e:
	raise e

# Dna = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
# k = 3
# d = 1
# # change your code above this line
# print()
print(MotifEnumeration(Dna, k, d))