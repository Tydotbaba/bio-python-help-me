'''

    The algorithm:
    
    
    1. create variables that are needed
    2. # split the text into 4-mers
    3. # get the most frequent word
'''

# create a variable to hold the text
text = 'AGTTTGTCTACATCAATAAGTTTGTCTAAAATGTTCCATCAATAAAATGTTCTACCAGATAGTTTGTCTACATCAATATACCAGATAAATGTTCTCTTCAAGAGAGTTTGTCTATCTTCAAGAGAAATGTTCAAATGTTCTACCAGATAAATGTTCAGTTTGTCTACATCAATAAGTTTGTCTATCTTCAAGAGTACCAGATTCTTCAAGAGAGTTTGTCTATACCAGATTACCAGATAGTTTGTCTATACCAGATTACCAGATTACCAGATCATCAATATACCAGATCATCAATATACCAGATAGTTTGTCTAAAATGTTCCATCAATATCTTCAAGAGTCTTCAAGAGCATCAATAAAATGTTCAAATGTTCCATCAATATCTTCAAGAGTCTTCAAGAGTCTTCAAGAGCATCAATAAGTTTGTCTAAGTTTGTCTATACCAGATTCTTCAAGAGTCTTCAAGAGCATCAATAAAATGTTCAGTTTGTCTACATCAA'

# patern. k -> integer
k = 14

# create an empty dictionary
d = {}

def findMaximum(text, k):
    # get the lenght of the text
    l_text = int(len(text))

    # split the text into 4-mers
    # print(l_text)
    # iterate ove ther text to find k-mers, then add it to the dictionary
    # for i in text:
    count = int(0)
    for i in text:
        t = text[count:count + k]
        if t in d.keys():
            d[t] += 1
        else:
            d[t] = 1

        if (l_text - count) == k:
            break
        count += 1
    # get the most frequent word
    # get the most frequent word in the dictionary
    values = d.values()
    maxcount = max(values)
    for key, value in d.items():
        if maxcount == value:    
            print(key, end=' ')

findMaximum(text, k)





