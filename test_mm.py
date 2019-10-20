from itertools import combinations
import unittest						#Importing the unittest module for testing

#======================================================Functions===============================================================================

def Allteams(combi,m):
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


#------------------------------------------------Main Program-----------------------------------------------------------------------


#Inherting the testing capabilities of unittest.TestCase

class test_mm(unittest.TestCase):
	

	#Test to check whether all the teams are getting generated or not.

	def test_allteams(self):
		arr=[('bleh',85),('Aequitas',90),('Aks',87),('Iam',20)]
		arr=combinations(arr,2)
		
		
		result=Allteams(arr,2)
		check=[('bleh', 'Aequitas', 87.5), ('bleh', 'Aks', 86.0), ('bleh', 'Iam', 52.5), ('Aequitas', 'Aks', 88.5), ('Aequitas', 'Iam', 55.0), ('Aks', 'Iam', 53.5)]
		
		self.assertEqual(result,check)


	#Test to check whether all the valid teams are getting generated or not.
	def test_validmatch(self):
		teams=[('bleh', 'Aequitas', 87.5), ('bleh', 'Aks', 86.0), ('bleh', 'Iam', 52.5), ('Aequitas', 'Aks', 88.5), ('Aequitas', 'Iam', 55.0), ('Aks', 'Iam', 53.5)]
		check=[(('bleh', 'Aequitas', 87.5), ('Aks', 'Iam', 53.5)), (('bleh', 'Aks', 86.0), ('Aequitas', 'Iam', 55.0)), (('bleh', 'Iam', 52.5), ('Aequitas', 'Aks', 88.5))]

		result=Validmatch(teams,2)

		self.assertEqual(result,check)


if __name__=='__main__':
	unittest.main()
