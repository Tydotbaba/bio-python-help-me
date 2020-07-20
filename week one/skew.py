# text = ''
# l = [0] 
# g, c = 0,0

# for genome in text:
# 	# if genome == 'G':
# 	# 	g += 1
# 	# elif genome == 'C':
# 	# 	c += 1 
# 	g = 
# 	l.append(g -c)

# # print(l)
# # show result
# print('Showing the skewi(genome)')
# # for i in l:
# # 	print(i, end=' ')

# m = max(l)
# m = l.index(m)
# print('\nThe point where skew attains a maximum: {}'.format(m))

# # finding the points at which skew attains a minimum
# # the minimum is found when there is a sharp rise in the difference
# # between 'G' and 'C'
# p_minimum = ''
# min_value = 0
# i = 0
# cycle = 0
# while i < len(l) - 1:
# 	if l[i] == 0:
# 		min_value = 0
# 		cycle = 0
# 	elif l[i] > min_value:
# 		min_value = l[i]
# 		cycle = 1
# 	elif l[i] < min_value:
# 		if l[i + 1] > l[i]:
# 			if l[i] < cycle:
# 				cycle = -1
# 		min_value = l[i]
# 	if cycle == -1:
# 		p_minimum += ' {}'.format(str(i))

# 	i += 1
# print('The point where skew attains a minimum: {}'.format(p_minimum))






# Place your MinimumSkew() function here along with any subroutines you need.
# MinimumSkew() should return a list.
# def MinimumSkew(Genome):
# 	l = [0] 
# 	g, c = 0,0

# 	for genome in Genome:
# 		if genome == 'G':
# 			g += 1
# 		elif genome == 'C':
# 			c += 1 
# 		l.append(g -c)

# 	# print(l)
# 	# show result
# 	# print('Showing the skewi(genome)')
# 	# for i in l:
# 	# 	print(i, end=' ')

# 	# m = max(l)
# 	# m = l.index(m)
# 	#print('\nThe point where skew attains a maximum: {}'.format(m))

# 	# finding the points at which skew attains a minimum
# 	# the minimum is found when there is a sharp rise in the difference
# 	# between 'G' and 'C'
# 	p_minimum = ''
# 	min_value = 0
# 	i = 0
# 	cycle = 0
# 	skew_list = []
# 	while i < len(l) - 1:
# 		if l[i] == 0:
# 			min_value = 0
# 			cycle = 0
# 		elif l[i] > min_value:
# 			min_value = l[i]
# 			cycle = 1
# 		elif l[i] < min_value:
# 			if l[i + 1] > l[i]:
# 				if l[i] < cycle:
# 					cycle = -1
# 			min_value = l[i]
# 		if cycle == -1:
# 			p_minimum += ' {}'.format(str(i))
# 			skew_list.append(str(i))

# 		i += 1
# 	#print('The point where skew attains a minimum: {}'.format(p_minimum))
# 	return skew_list



def MinimumSkew(sequence):
	c = 0
	g = 0
	min_skew = 0
	skew_list = []
	index = 0
	for i in sequence:
		index += 1
		if i == 'C':
			c += 1
		if i == 'G':
			g += 1
		skew = g-c
		if skew < min_skew:
			skew_list = [index]
			min_skew = skew
		if skew == min_skew and index not in skew_list:
			skew_list.append(index)	
	return skew_list

# change your code below this line
sequence = ''
# change your code above this line

MinimumSkew(sequence)