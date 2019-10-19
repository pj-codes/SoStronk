from itertools import combinations

arr=[('bleh',85),('Aequitas',90),('Aks',87),('Iam',20),('bill',50)]
m=2
combi=combinations(arr,m)
newarr=[]
for i in combi:
	avg=(i[0][1]+i[1][1])/m
	newarr.append((i[0][0],i[1][0],avg))
print(newarr)