# Write your FrequentWordsWithMismatches() function here, along with any subroutines you need.
# Your function should return a list.


# test1 

# from collections import OrderedDict
# from operator import itemgetter

# def FrequentWordsWithMismatches(sequence, motif_length, max_mismatches, most_common=False):
# #def kmers_finder_with_mismatches(sequence, motif_length, max_mismatches, most_common=False):
#   '''(str, int, int) -> sorted(list)
#   Find the most frequent k-mers with mismatches in a string.
#   Input: A sequence and a pair of integers: motif_length (<=12) and max_mismatch (<= 3).
#   Output: An OrderedDict containing all k-mers with up to d mismatches in string.
#   If most_common: return only the most represented kmer(s).
#   Sample Input:   ACGTTGCATGTCGCATGATGCATGAGAGCT 4 1
#   Sample Output:  OrderedDict([('ATGC', 5), ('ATGT', 5), ('GATG', 5),...])
#   '''
    

#   #check passed variables
#   if not motif_length <= 12 and motif_length >= 1:
#       raise ValueError("motif_length must be between 0 and 12. {} was passed.".format(motif_length))
#   if not max_mismatches <= 3 and max_mismatches >= 1:
#       raise ValueError("max_mismatch must be between 0 and 3. {} was passed.".format(max_mismatches))

#   #build a dict of motifs/kmers
#   motif_dict = {}
#   for i in range(len(sequence) - motif_length +1):
#       motif = sequence[i:i+motif_length]
#       if motif not in motif_dict:
#           motif_dict[motif] = 1
#       else:
#           motif_dict[motif] += 1

#   #check for mismatches
#   motif_dict_with_mismatches = {}
#   for kmer in motif_dict:
#       motif_dict_with_mismatches.update({kmer:[]})
            
#       for other_kmer in motif_dict:
#           mismatches = 0
#           for i in range(len(kmer)):
#               if kmer[i] != other_kmer[i]:
#                   mismatches += 1
#           if mismatches <= max_mismatches:
#               motif_dict_with_mismatches[kmer].append([other_kmer,motif_dict[other_kmer]])

#   #count occurrences of motifs
#   tmp = {}
#   for item in motif_dict_with_mismatches:
#       count = 0
#       for motif in motif_dict_with_mismatches[item]:
#           count += motif[-1]
#       tmp.update({item:count})

#   result = OrderedDict(sorted(tmp.items(), key=itemgetter(1), reverse=True))
    
#   #find the most common/s
#   if most_common:
#       commons = OrderedDict()
#       _max = result.items()[0][1]
#       for item in result:
#           if result[item] == _max:
#               commons.update({item:result[item]})
#           else:
#               return commons

#   # return result

#   # used for stepik
#   res = []
#   for key in a:
#       if a[key] == m:
#           res.append(a[key])



##Test
# sequence = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
# motif_length = 4
# max_mismatches = 1
# a = FrequentWordsWithMismatches(sequence, motif_length, max_mismatches, most_common=False)
# m = max(a.values())
# res = []
# for key in a:
#     if a[key] == m:
#       print(key, a[key])




# test2

# import collections
# kmer = 4
# in_genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT";
# in_mistake = 1;
# out_result = [];
# mismatch_list = []

# def hamming_distance(s1, s2):
#   # Return the Hamming distance between equal-length sequences
#   if len(s1) != len(s2):
#       raise ValueError("Undefined for sequences of unequal length")
#   else:
#       return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# for i in range(len(in_genome)-kmer + 1):
#   v = in_genome[i:i + kmer]
#   out_result.append(v)

# for i in range(len(out_result)):
#   for j in range(i + 1, len(out_result)):
#       if hamming_distance(out_result[i], out_result[j]) <= in_mistake:
#           mismatch_list.extend([out_result[i], out_result[j]])

# #  Here is some code that counts the occurrences in mismatch_list, 
# # sorts the results by frequency (not used, but you 
# # may want it later), 
# # and then prints all those that match the assumed frequency of 4.
# mismatch_count = collections.Counter(mismatch_list)
# sorted_match = sorted(list(mismatch_count), key=lambda pair: pair[1], reverse=True)
# for item, value in mismatch_count.items():
#     if value == 4:
#         print(item)

# print(mismatch_count)
# print(mismatch_list)
# create a result dict
# mismatch_res = {}

# # create a set out of list
# mismatch_set = set(mismatch_list)
# for match in mismatch_set:
#   # print(match)
#   mismatch_res[match] = mismatch_list.count(match)

# print(mismatch_res)












# aLGORITHM 
# from .d-neigbours import findNeigbours

# def FrequentWordsWithMismatches(Text, k, d)
#         FrequentPatterns = set()
#         Neighborhoods = list()
#         for i in range(len(Text) − len(k) + 1):
#             Neighborhoods.append(findNeigbours(Text(i, k), d)
#         NeighborhoodArray = []
#         for i in Neighborhoods:
#           for patern in i:
#               NeighborhoodArray.append(patern)
#         for i ← 0 to |Neighborhoods| − 1
#             Pattern ← NeighborhoodArray(i) 
#             Index(i) ← PatternToNumber(Pattern)
#             Count(i) ← 1
#         SortedIndex ← Sort(Index)
#         for i ← 0 to |Neighborhoods| − 2 
#             if SortedIndex(i) = SortedIndex(i + 1)
#                 Count(i + 1) ← Count(i) + 1
#        maxCount ← maximum value in array Count
#        for i ← 0 to |Neighborhoods| − 1
#            if Count(i) = maxCount
#                Pattern ← NumberToPattern(SortedIndex(i), k)
#                add Pattern to FrequentPatterns
#        return FrequentPatterns



# Test3: tested working, only test #8 failed.
import d_neigbours, math 
from count1 import ApproximatePatternCount


# create variables to work with
Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
# patern = 'ACGT'
k = 4
d = 1
# 1. build an array of k-mers Neighborhoods
# neigbours = d_neigbours.findNeigbours(patern, d)
# print(neigbours)


# convert patern to number in the neigbours array
def PatternToNumber(patern):
    '''
        convert patern to number given patern of k-mer
        e.g: PatternToNumber('AAAA') -> 0
        @args: i -> str, represents patern of each k-mer in 
                lexicographic order
        @returns: int, the index of patern in its Neighborhoods
    '''
    neigbours = sorted(d_neigbours.findNeigbours(patern, k))
    return neigbours.index(patern)

    

def NumberToPattern(i, k):
    '''
        convert number back to patern given i and k-mer
        e.g: NumberToPattern(0, 4) -> 'AAAA'
        @args: i -> int, represents index of each k-mer in in 
                lexicographic order
        @args: k -> int, represents the number of DNA k-mers
        @returns: str, the patern of k-mers at index i in its Neighborhoods 
    '''
    patern = 'A' * k 
    neigbours = sorted(d_neigbours.findNeigbours(patern, k))
    return neigbours[i]

# test NumberToPattern function
# print(NumberToPattern(0, 4))

# 2. create an index array of k-mers (k raised to power k)
def ComputingFrequenciesWithMismatches(Text, k, d):
    FrequencyArray = []
    for i in range(int(math.pow(4, k))):
      FrequencyArray.append(0)
    
    # print(FrequencyArray)
    for i in range(len(Text) - k + 1):
        ptn = Text[i:i + k]
        neigbours = sorted(d_neigbours.findNeigbours(ptn, d))
        # print('neigbours -> ', i)
        
        for ApproximatePattern in neigbours:
            # print(ApproximatePattern)
            j = PatternToNumber(ApproximatePattern)
            FrequencyArray[j] += 1
            # print(ApproximatePattern, end=' ')

    return FrequencyArray


# now get the frequent words with mismatches
def FrequentWordsWithMismatches(Text, k, d):
    '''
        Frequent Words with Mismatches Problem: Find the most 
            frequent k-mers with mismatches in a string.
        Input: A string Text as well as integers k and d. 
            (You may assume k ≤ 12 and d ≤ 3.)
        Output: All most frequent k-mers with up to d mismatches 
            in Text.
    '''

    # get the FrequencyArray in Text 
    FrequencyArray = ComputingFrequenciesWithMismatches(Text, k, d)

    # get the maximum count of the most frequent word
    m = max(FrequencyArray)

    # lastly, get the most frequent word
    most_common = [NumberToPattern(i, k) for i, value in enumerate(FrequencyArray) if value == m]

    # return the most_common word
    return most_common

# m = (ComputingFrequenciesWithMismatches(Text, k, d).count(5))
#print(FrequentWordsWithMismatches(Text, k, d))
# print(m)
# 3. build the frequency array with up to d mismatches 






# test4 worked excellently
import itertools
import time
from collections import defaultdict

def FrequentWordsWithMismatches(Genome, k, d):
    start = time.process_time()
    aprox_frq_words = []
    frequencies = defaultdict(lambda: 0)
    # all existent kmers with d mismatches of current kmer in genome
    for index in range(len(Genome) - k + 1):
        curr_kmer_and_neighbors = PermuteMotifDistanceTimes(Genome[index : index + k], d)
        for kmer in curr_kmer_and_neighbors:
            frequencies[kmer] += 1 

    for kmer in frequencies:
        if frequencies[kmer] == max(frequencies.values()):
            aprox_frq_words.append(kmer)
    end = time.process_time()
    print("Time:", end - start)
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


# create variables to work with
Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
# patern = 'ACGT'
k = 4
d = 1

print(FrequentWordsWithMismatches(Text, k, d))