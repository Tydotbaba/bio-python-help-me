text = 'CATGGGCATCGGCCATACGCC' 
l = [0] 
g, c = 0,0

for genome in text:
	if genome == 'G':
		g += 1
	elif genome == 'C':
		c += 1 
	l.append(g -c)

print(l)
m = max(l)
print(l.index(m))