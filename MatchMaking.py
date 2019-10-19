from itertools import combinations   					#Importing combinations module from the itertools package

arr=[('bleh',85),('Aequitas',90),('Aks',87),('Iam',20)] #Players List

m=2		#M vs M Match

combi=combinations(arr,m) #All combinations of team with m players

teams=[]  #Empty array list to store all the teams


# Creating all the teams and calculating average score of each team

for team in combi:
	names=[]
	avg=0
	for j in range(m):
		avg+=team[j][1]
		names.append(team[j][0])
	avg=avg/m
	avg = float("{0:.2f}".format(avg))  #Restricting the average to 2 decimal place and type casing it back to float
	names.append(avg)
	teams.append(tuple(names))			#Appending each team at the end of each iteration to the teams array list


validmatches=[]							#Empty array list to store all the valid m vs m matches


#Deciding whether a match is valid or not from all the possible m vs m combinations

for match in combinations(teams,2):
	flag=True
	for i in range(m):
		if(match[0][i] not in match[1]):
			continue
		else:
			flag=False
			break
	if(flag):
		validmatches.append(match)


#Sorting all the valid matches according to the quality of each match

matches=sorted(validmatches,key=lambda x:abs(int(x[0][m])-int(x[1][m])))

#Printing out all the valid matches
for i in matches:
	print(i)