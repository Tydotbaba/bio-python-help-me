import math

# neuclotides
chars = "ACGT"

def Neighbors(pattern, d):
    ''' Helper function for neighors function'''
    l = sum([neighbors(pattern, d2) for d2 in range(d + 1)], [])
    l = set(l)    
    return l
    
def neighbors(pattern, d):
    ''' Helper function for Neighbors'''
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
    '''This function helps to find the neighors of a word patern with d mismatches'''
    l = Neighbors(pattern, d)
    return list(l)
    # for i in l:
    #     # res += ' {}'.format(str(i))
    #     print(i, end=' ')

# test findNeigbours
# findNeigbours('AT', 2)
# print(sorted(findNeigbours('AAAA', 4)))



def PatternToNumber(patern):
    '''
        convert patern to number given patern of k-mer
        e.g: PatternToNumber('AAAA') -> 0
        @args: i -> str, represents patern of each k-mer in 
                lexicographic order
        @returns: int, the index of patern in its Neighborhoods
    '''
    neigbours = sorted(findNeigbours(patern, k))
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
    neigbours = sorted(findNeigbours(patern, k))
    return neigbours[i]

# test NumberToPattern function
# print(NumberToPattern(0, 4))


def ComputingFrequenciesWithMismatches(Text, k, d):
    '''
        ComputingFrequenciesWithMismatches: function to find the frequency of words with at most d mismatches in Text
        Args: Text -> str, a genome that contains a string of necluetides 
        @Args: k -> int, the number of k-mers in each word 
        @Args: d -> int, the maximum number of mismatches in necluotides 
        @returns: FrequencyArray -> object, the frequency array of k-mers with at least d mismatches in Text
    '''
    FrequencyArray = []
    for i in range(int(math.pow(4, k))):
      FrequencyArray.append(0)
    
    # print(FrequencyArray)
    for i in range(len(Text) - k + 1):
        ptn = Text[i:i + k]
        neigbours = sorted(findNeigbours(ptn, d))
        # print('neigbours -> ', i)
        
        for ApproximatePattern in neigbours:
            # print(ApproximatePattern)
            j = PatternToNumber(ApproximatePattern)
            FrequencyArray[j] += 1
            # print(ApproximatePattern, end=' ')

    return FrequencyArray

# test ComputingFrequenciesWithMismatches
# m = max(ComputingFrequenciesWithMismatches(Text, k, d)
# print(m)

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
    # check for k and d
    assert k <= 12, 'k must be less than 12'
    assert d <= 3, 'd must be less than 3'

    # get the FrequencyArray in Text 
    FrequencyArray = ComputingFrequenciesWithMismatches(Text, k, d)

    # get the maximum count of the most frequent word
    m = max(FrequencyArray)
    
    # lastly, get the most frequent word
    most_common = [NumberToPattern(i, k) for i, value in enumerate(FrequencyArray) if value == m]

    # return the most_common word
    return most_common



# change your code below this line
Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
# pattern = 'AG'
# # change your code above this line

# timeit(print(FrequentWordsWithMismatches(Text, k, d)))
print([NumberToPattern(i, k) for i in ComputingFrequenciesWithMismatches(Text, k, d)])
print(FrequentWordsWithMismatches(Text, k, d))
# 3. build the frequency array with up to d mismatches 