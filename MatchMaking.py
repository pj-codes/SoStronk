from itertools import combinations   					#Importing combinations module from the itertools package


#======================================================Functions===============================================================================


def Allteams(players,m):
	teams=[]  								#Empty array list to store all the teams

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

	return teams	


#=====================================================End of Function===============================================================================

def Validmatch(teams,m):
	
	validmatches=[]							#Empty array list to store all the valid m vs m matches


#Deciding whether a match is valid or not from all the possible m vs m combinations

	for match in combinations(teams,2):
		flag=True
		for i in range(m):
			if(match[0][i] not in match[1]):  #If both teams have different players, continue else break out and start again.
				continue
			else:
				flag=False
				break
		if(flag):
			validmatches.append(match)
	return validmatches


#=====================================================End of Function===============================================================================


#Sorting all the valid matches according to the quality of each match

def Qualitymatch(validmatches,m):
	return sorted(validmatches,key=lambda x:abs(int(x[0][m])-int(x[1][m])))

#=====================================================End of Function===============================================================================


def Printmatches(matches):

#Printing out all the valid matches
	for match in matches:
		count=1
		for team in match:
			print(team,end=" ")
			if(count):
				print("vs",end=" ")
			count-=1
		print()

#=====================================================End of Function===============================================================================

#Function to take input from the for number of players on each side.
def numplayer():
	while(True):
		try:
			print("Enter number of players on each side.")
			M=int(input())
			break
		except ValueError:
			print("Enter correct integer number.")
			continue
	return M

#=====================================================End of Function===============================================================================

#Function to take input of all the players and their score from the user.
def players_score():
	players=[]
	names=[]
	i=1
	while(True):
		while(True):
			print(f"Enter name of player {i} and score(<=100) seperated by space or type 'e' to finish.")
			name_score=input()
			if(name_score=='e'):
				break
			else:
				try:
					name,score=name_score.split(" ")
					if name in names:
						print('Name already exist, pick a different name.')
						print()
						continue
					elif(int(score)>100):
						print('Not a valid score.')
						print()
						continue
					else:
						names.append(name)
					players.append((name,int(score)))
					i+=1
				except:
					print("Enter the data correctly.")
					continue
		
		#Number of players cannot be less than 2*M.
		if(len(players)<2*M):
			left=2*M-len(players)
			print(f"Number of players insufficient for matchmaking. Enter {left} more data and then finish.")
			print()
			continue
		else:
			break
	return players


#------------------------------------------------Main Program-----------------------------------------------------------------------

#Taking input from the user

# M= Number of players on each side.
M=numplayer()


#Getting list of players along with their score
players=players_score() 


print()


#All combinations of team with M players

combi=combinations(players,M) 


#Getting all the teams with their average score
teams=Allteams(combi,M)

#Getting all the valid M vs M matches
validmatches=Validmatch(teams,M)

#Getting all the matches sorted by quality of each match
matches=Qualitymatch(validmatches,M)

#Printing all the matches sorted by quality

print("All the different possible matches sorted by quality: ")
print()
Printmatches(matches)

