# f = open('dataset_2_7 (2).txt')

# for line in f:
# 	print(line)

# ACGTTGCATGTCGCATGATGCATGAGAGCT
# 4

# ACGT 1
# CGTT 1
# GTTG 1
# TTGC 1
# CATG 2


text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
# patern. k -> integer
k = 4
# create an empty dictionary
d = {}

l_text = len(text)
print(l_text)
# iterate ove ther text
# for i in text:
i = 0
for i in text:
    print(i, end='  ')
    l_text = l_text - 1