from itertools import combinations

arr=[('bleh',85),('Aequitas',90),('Aks',87),('Iam',20)]
m=2
combi=combinations(arr,m)
newarr=[]
for i in combi:
	avg=(i[0][1]+i[1][1])/m
	newarr.append((i[0][0],i[1][0],avg))

validmatches = list(match for match in combinations(newarr, 2) if (match[0][0] not in match[1] and match[0][1] not in match[1]))

matches=sorted(validmatches,key=lambda x:abs(x[0][2]-x[1][2]))
for i in matches:
	print(i)