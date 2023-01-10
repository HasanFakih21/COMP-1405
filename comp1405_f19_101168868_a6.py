#Hassan Fakih 101168868

#global constant list of list, where each list includes the corresponding symbol for the correct letter, and a float number for the "value" of the piece
identifier = [["k","♔","♚",0.0],["q","♕","♛",10.0],["r","♖","♜",5.0],["n","♘","♞",3.5],["b","♗","♝",3.0],["p","♙","♟",1.0]] #second item is black piece third is white piece

#gets the corresponding piece from the global constant based on whether the letter is capital or not
#@param character - it is a character that is sent to the function, one entered by the user when first defining the row
#@return corresponding piece from the identifier list
def findPiece(character):
	if ord(character)>=65 and ord(character)<=90: #checks whether the character is upper case
		character = chr(ord(character) + 32) #sets the new character to the lower case version
		for x in range(len(identifier)): #traverses the first item of each list in the identifier list 
			if identifier[x][0] == character: 
				return identifier[x][1] #returns the symbol based on the corresponding character 
	else:
		for x in range(len(identifier)):
			if identifier[x][0] == character:
				return identifier[x][2]

#prints a formatted board with the symbols onto the terminal
#@param chessboard - it's a list of a list of characters
#@return None
def printBoard(chessboard):
	print("")
	for x in range(len(chessboard)):
		print(8-x, end = " ") #prints numbers before each row, going from bottom to top, 1 to 8
		for i in range(len(chessboard[x])):
			if chessboard[x][i] == "-":
				print(".", end = " ") #prints a "." for a blank space on the board
			else:
				print(findPiece(chessboard[x][i]), end = " ") #calls the findPiece function to retrieve the corresponding piece and print it
		print("")
	print(" ","a b c d e f g h") #prints letters to help identify each coulmn on the board
	print("")

#gets each row as input to create the inital state of the chessboard
#@param None
#@return chessboard - a list of list of characters that defines the state of the board
def userInput():
	chessboard = [] #initializes the list
	for z in range(8): #runs 8 times as the size of a chessboard is 8x8
		validated = False #initializes the validated boolean value
		while not(validated): #runs atleast once
			print("Enter Row",z+1) #tells the user which row they're typing the list for
			rowString = input() #gets a string from the user
			validated = validate(rowString) #calls the validate function to make sure the user entered a valid roww
		rowlist = [] #initializes the second list which will be inserted into the chessboard list 8 times
		for x in range(len(rowString)): 
			rowlist.append(rowString[x]) #appends each character from the string into the rowlist so it becomes a proper list of characters
		chessboard.append(rowlist) #appends the entire list of characters or one row into the chessboard
	return chessboard

#makes sure the string entered by the user is valid input
#@param rowString - the string entered by the user that should be a row in the chessboard
#@return validated - determines whether the string is valid input or not
def validate(rowString):
	validated = False
	if len(rowString) != 8: #checks if there are 8 characters for the row
		print("Error, the row needs to be of size 8")
		return validated
	for x in range(len(rowString)):
		if rowString[x] not in "kqrnbpKQRNBP-": #checks if the characters entered are part of the ones defined by the program
			print("Error, the character",rowString[x],"is not defined") #tells the user which character they entered isn't defined
			return validated
	validated = True
	return validated

#calculates the score of the black side and white side then says which one is winning or if it's a tie
#@param chessboard - it's a list of a list of characters
#@return None
def calculateScore(chessboard):
	black_points = 0.0 #initiliazes the score of each side
	white_points = 0.0
	for x in range(len(chessboard)): #for each row
		for character in chessboard[x]: #for each character in the row
			if character!= "-": #if the character is not an empty space
				if ord(character)>=65 and ord(character)<=90: #if the character is uppercase which means it's a black piece
					character = chr(ord(character) + 32) #makes the character lower case so it can be identified through the indentifier list
					for z in range(len(identifier)): #looks for the corresponding value in the identifier list 
						if character == identifier[z][0]:
							black_points = black_points + identifier[z][3] #adds the points as defined
							break				
				else:
					for z in range(len(identifier)):
						if character == identifier[z][0]:
							white_points = white_points + identifier[z][3]
							break
	if black_points > white_points:
		print("Black is winning")
	elif white_points > black_points:
		print("White is winning")
	else:
		print("It's a tie")

#moves pieces from one spot to another spot on the board
#@param chessboard - it's a list of a list of characters
#@return chessboard - an updated list of a list of characters with new positions

def movePiece(chessboard):
	validated = False
	while not(validated):
		move_from = input("Which piece would you like to move? ")
		validated = validateLocation(move_from)	#calls the validateLocation function to check if the input by the user is valid
	temp = chessboard[8-int(move_from[1])][int(chr(ord(move_from[0])-49))] #sets a temporary variable to hold the character of the piece the user said they wanted to move
	if temp == "-": #checks if there even is a piece at that location
		print("There is no piece to move!")
		return chessboard #if there's no piece to move the user is told and the chessboard without any updates is returned back again
	validated = False
	while not(validated):
		move_to = input("Where would you like to move to? ")
		validated = validateLocation(move_to)

	chessboard[8-int(move_from[1])][int(chr(ord(move_from[0])-49))] = "-" #leaves a blank space of where the piece was moved away from
	chessboard[8-int(move_to[1])][int(chr(ord(move_to[0])-49))] = temp #sets the new location as the character that was moved

	return chessboard

#validates whether the location entered by the user is a valid one
#@param move - a string entered by the user that is supposed to specify a location on the chessboard
#@return False, True - returns a boolean value determining whether the string input is valid or not
def validateLocation(move):
	if len(move) != 2: #the location has to be of length two, for example "a5"
		print("Your location is invalid")
		return False
	if move[0] not in "abcdefgh": #the first part has to be one of the first 8 letters
		print("The first part of the location has to be one of the letters on the board!")
		return False
	if not(int(move[1])>0 and int(move[1])<=8): #the second part has to be a number from 1 to 8
		print("The second part of the location has to be a number from 1 to 8!")
		return False
	return True

#turns a string uppercase
#@param oldstring - the string that should be turned uppercase
#@return newstring - the string with everything uppercase
def uppercase(oldstring):
	newstring = ""
	for x in range(len(oldstring)):
		temp = ord(oldstring[x])
		if temp>=97 and temp<=122:
			temp = temp-32
		newstring = newstring+chr(temp)
	return newstring

#checks and validates a yes/no question response from the user
#@param None
#@return temp - if the input by the user implies a yes a Y is returned and if it's a no N or NO is returned
def respond():
	flag = True
	while flag:
		temp = uppercase(input("Y/N \n"))
		if temp == "YES":
			temp = "Y"
		if temp == "Y" or temp == "N" or temp == "NO":
			flag = False
		else:
			print("Please enter valid input")
	return temp

#main function
#@param None
#@return None					
def main():
	print("Would you like to read the instructions?")
	if respond() == "Y":
		print("\nYou will first be asked to enter each row you would like for the board,\nthere are 8 rows in a chess board.\nEach row should consist of either a k for king, q for queen, r for rook,\nn for knight, b for bishop, or a p for pawn\nA capital case character means it belongs to black\nwhile a lowercase character means it belongs to white\nIf you want an empty space on the board you type '-'\nAfter you type all the rows, a board is printed for you and\nthe you're told who is currently winning\nYou will then be asked if you would like to move a piece, if you answer yes,\nyou will then be asked which piece you would like to move,\nyou have to use a letter and a number on the board\nin the form of 'a3' to pick a location.\n")
	chessboard = userInput()
	printBoard(chessboard)
	calculateScore(chessboard)
	while True:
		while True:
			print("Would you like to move a piece?")
			if respond() == "Y":
				chessboard = movePiece(chessboard)
				printBoard(chessboard)
				calculateScore(chessboard)
			else:
				break
		print("Would you like to enter a new board?")
		if respond() == "Y":
			chessboard = userInput()
			printBoard(chessboard)
			calculateScore(chessboard)
		print("Would you like to end the program?")
		if respond() == "Y":
			break

main()

	
