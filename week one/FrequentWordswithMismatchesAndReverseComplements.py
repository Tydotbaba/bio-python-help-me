'''
	Find FrequentWordWithMismatchAndReverseCompliment
	using: https://www.chegg.com/homework-help/questions-and-answers/frequentwordswithmrc-algorithm-finding-frequent-k-mers-mismatches-reverse-complements-text-q27423715
'''

from count1 import ApproximatePatternMatching, ApproximatePatternCount, reverse

# def FrequentWordWithMismatchAndReverseCompliment(Text, k, d):
# 	frequencyPattern = []
# 	Count = []
# 	count_1 = 0
# 	count_2 = 0
# 	for i in range(len(Text) - k + 1):
# 		pattern = Text[i:i + k]
# 		count_1 = ApproximatePatternCount(Text, pattern, d) 
# 		pattern_rc = reverse(pattern)
# 		count_2 = ApproximatePatternCount(Text, pattern_rc, d)
# 		Count.append(count_1 + count_2)
# 	maxCount = max(Count)
# 	for j in range(len(Text) - k + 1):
# 		if Count[j] == maxCount:
# 			frequencyPattern.append(Text[j:j+k])
# 	return frequencyPattern



#Another try
# def reverse_list(pattern_list):
# 	res = []
# 	for pattern in pattern_list:
# 		res.append(reverse(pattern))
# 	return res

# def FrequentWordWithMismatchAndReverseCompliment(Text, k, d):
# 	frequencyPattern = []
# 	Count = []
# 	count_1 = 0
# 	count_2 = 0
# 	for i in range(len(Text) - k + 1):
# 		pattern = Text[i:i + k]
# 		# 1. Generate the "possible kmers"
# 		count_1 = ApproximatePatternMatching(Text, pattern, d)
# 		# 2. Generate the reverse complements of "possible kmers"
# 		count_2 = reverse_list(count_1)
# 		for j in range(len(count_1)):
# 			count1 = ApproximatePatternCount(Text, count_1[j], d)
# 			count2 = ApproximatePatternCount(Text, count_2[j], d)
# 			Count.append(count1 + count2)
# 	maxCount = max(Count)
# 	for j in range(len(Text) - k + 1):
# 		if Count[j] == maxCount:
# 			frequencyPattern.append(Text[j:j+k])
# 	return set(frequencyPattern)




# Another Try: Finally worked
import itertools
import time
from collections import defaultdict

def FrequentWordsWithMismatchesAndReverseComplements(Genome, k, d):
	# start = time.process_time()
	aprox_frq_words = []
	frequencies = defaultdict(lambda: 0)
	# all existent kmers with d mismatches of current kmer in genome
	for index in range(len(Genome) - k + 1):
		pattern = Genome[index : index + k]
		pattern_rc = reverse(pattern)
		curr_kmer_and_neighbors = PermuteMotifDistanceTimes(pattern, d)
		curr_kmer_and_neighbors += PermuteMotifDistanceTimes(pattern_rc, d)
		for kmer in curr_kmer_and_neighbors:
			frequencies[kmer] += 1 

	for kmer in frequencies:
		if frequencies[kmer] == max(frequencies.values()):
			aprox_frq_words.append(kmer)
	# end = time.process_time()
	# print("Time:", end - start)
	return aprox_frq_words


def PermuteMotifOnce(motif, alphabet={"A", "C", "G", "T"}):
	"""
	Gets all strings within hamming distance 1 of motif and returns it as a
	list.
	"""

	return list(set(itertools.chain.from_iterable([[
		motif[:pos] + nucleotide + motif[pos + 1:] for
		nucleotide in alphabet] for
		pos in range(len(motif))])))


def PermuteMotifDistanceTimes(motif, d):
	workingSet = {motif}
	for _ in range(d):
		workingSet = set(itertools.chain.from_iterable(map(PermuteMotifOnce, workingSet)))
	return list(workingSet)


# change your code below this line
text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
# pattern = 'AT'

# # change your code above this line

print(FrequentWordsWithMismatchesAndReverseComplements(text, k, d))

