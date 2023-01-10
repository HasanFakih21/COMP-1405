#Hassan Fakih 101168868

# Subgenre Super-Heroes:
#	A = Marvel Studios, B = Solo Movie, C = Female Protagonist, D = Jason Mamoa, E = Zack Snyder, F = Magic, G = Shrink

#	"Wonder Woman" = B, C
#	"Justice League" = E
#	"Aquaman" = B, D
#	"Shazam" = B
#	"Suicide Squad" = 
#	"Captain Marvel" = A, B, C
#	"Black Panther" = A, B
#	"Avengers: Endgame" = A
#	"Doctor Strange" = A, B, F
#	"Ant-Man" = A, B

# Subgenre Sci-Fi Action/Adventure:
#	A = Before 2010, B = Space, C = Robots, D = Christopher Nolan, E = Hugh Jackman, F = Second Highest Grossing, G = Michael Bay

#	"Star Wars: The Force Awakens" = B
#	"Interstellar" = B, D
#	"Chappie" = C, E
#	"Mad Max: Fury Road" = 
#	"Pacific Rim" = C
#	"Avatar" = A, F
#	"Star Trek" = A, B
#	"Transformers" = A, C, G
#	"RoboCop" = A, C
#	"The Matrix" = A


#Function that validates the user's input and turns any indication of a "yes" to "Y"
def respond():
	flag = True
	while flag:
		temp = input("Y/N \n").upper()
		if temp == "YES":
			temp = "Y"
		if temp == "Y" or temp == "N" or temp == "NO":
			flag = False
		else:
			print("Please enter valid input")
	return temp

#Function that asks series of questions to find film in sci fi action/adventure subgenre
def scifiaction():
	print("Was your film released before 2010?")
	if respond() == "Y":
		print("Does your film include robots?")
		if respond() == "Y":
			print("Was your film directed by Michael Bay?")
			if respond() == "Y":
				print('"Transformers" is your film')
			else:
				print('"RoboCop" is your film')
		else:
			print("Is your film set in space?")
			if respond() == "Y":
				print('"Star Trek" is your film')
			else:
				print("Is your film the second highest grossing film of all time?")
				if respond() == "Y":
					print('"Avatar" is your film')
				else:
					print('"The Matrix" is your film')
	else:
		print("Is the film set in space?")
		if respond() == "Y":
			print("Was your film directed by Christopher Nolan?")
			if respond() == "Y":
				print('"Interstellar" is your film')
			else:
				print('"Star Wars: The Force Awakens" is your film')
		else:
			print("Does your film include robots?")
			if respond() == "Y":
				print("Does Hugh Jackman play a role in your film?")
				if respond() == "Y":
					print('"Chappie" is your film')
				else:
					print('"Pacific Rim" is your film')
			else:
				print('"Mad Max: Fury Road" is your film')

#Function that asks series of questions to find film in superheroes subgenre
def superhero():
	print("Is the film produced by Marvel Studios?")
	if respond() == "Y":
		print("Is it a solo film?")
		if respond() == "Y":
			print("Is the protagonist female?")
			if respond() == "Y":
				print('"Captain Marvel" is the film')
			else:
				print("Does the protagonist use magic?")
				if respond() == "Y":
					print('"Doctor Strange" is the film')
				else:
					print("Can the protagonist shrink?")
					if respond() == "Y":
						print('"Ant-Man" is your film')
					else:
						print('"Black Panther" is your film')
		else:
			print('"Avengers: Endgame" is the film')		
	else:
		print("Is it a solo film?")
		
		if respond() == "Y":
			print("Is the protagonist female?")
			if respond() == "Y":
				print('"Wonder Woman" is the film')
			else:
				print("Is Jason Momoa in the film?")
				if respond() == "Y":
					print('"Aquaman" is the film')
				else:
					print('"Shazam" is the film')
		else:
			print("Was the film directed by Zack Snyder?")
			if respond() == "Y":
				print('"Justice League" is the film')
			else:
				print('"Suicide Squad" is the film')

#function that returns an indicator for which subgenre was picked and returns a 2 if none of the two available were picked
def validate(genre):
	if genre == "SCI-FI ACTION" or genre == "SCI-FI ADVENTURE" or genre == "SCI-FI ACTION/ADVENTURE":
		return 0
	elif genre == "SUPER-HEROES" or genre == "SUPERHERO" or genre == "SUPERHEROES":
		return 1
	else:
		return 2

#asks about instructions
print("Would you like to read the instructions?")
if respond() == "Y":
	print("You will first be asked what the subgenre of the movie you're looking for is\n(either Sci-Fi Action/Adventure or Super-Heroes)\nAfterwards, you will be asked a series of yes/no questions\nYou may respond with either yes or no, or with y or n\nOnce you've answered enough questions, the title of your movie will appear!\n\n")

#sets terminate variable 
terminate = False

#loops until terminate is true and ends if a non valid subgenre was input
while (not terminate):

	identifier = validate(input("What is the subgenre of your movie?\n").upper())
	if identifier == 0:
		scifiaction()
	elif identifier == 1:
		superhero()
	else:
		break
	print ("Would you like to terminate the program?")
	if respond() == "Y":
		terminate = True

print("\nThe program has ended")

	





























		
