# put your student name and identification here


modifiable = "ABEKLOSZ"
modified = ["4","8","3","|<","1","0","5","2"]
phrase1 = "BY THE WAY"
phrase2 = "ON MY WAY"
phrase3 = "GOOD LUCK"
phrase4 = "NO WAY"
word1 = "PLEASE"
word2 = "SORRY"
word3 = "AND"
word4 = "WHAT"

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

def uppercase(oldstring):
	newstring = ""
	for x in range(len(oldstring)):
		temp = ord(oldstring[x])
		if temp>=97 and temp<=122:
			temp = temp-32
		newstring = newstring+chr(temp)
	return newstring

def removePunc(oldstring):
	newstring = ""
	for x in range(len(oldstring)):
		temp = ord(oldstring[x])
		if (temp>=97 and temp<=122) or (temp>=65 and temp<=90) or (temp>=48 and temp<=57) or temp == 32:
			newstring = newstring+chr(temp)
	return newstring

def phrase(oldstring):

	if phrase1 in oldstring:
		place = search(oldstring, phrase1)		
		newstring = oldstring[0:place] + "BTW" + oldstring[place+len(phrase1):len(oldstring)]
		return phrase(newstring)
	elif phrase2 in oldstring:
		place = search(oldstring, phrase2)	
		newstring = oldstring[0:place] + "OMW" + oldstring[place+len(phrase2):len(oldstring)]
		return phrase(newstring)
	elif phrase3 in oldstring:
		place = search(oldstring, phrase3)			
		newstring = oldstring[0:place] + "GL" + oldstring[place+len(phrase3):len(oldstring)]
		return phrase(newstring)
	elif phrase4 in oldstring:
		place = search(oldstring, phrase4)		
		newstring = oldstring[0:place] + "NOWAI" + oldstring[place+len(phrase4):len(oldstring)]
		return phrase(newstring)
	else:
		return oldstring

def word(oldstring):

	if word1 in oldstring:
		place = search(oldstring, word1)		
		newstring = oldstring[0:place] + "PLZ" + oldstring[place+len(word1):len(oldstring)]
		return word(newstring)
	elif word2 in oldstring:
		place = search(oldstring, word2)	
		newstring = oldstring[0:place] + "SRY" + oldstring[place+len(word2):len(oldstring)]
		return word(newstring)
	elif word3 in oldstring:
		place = search(oldstring, word3)			
		newstring = oldstring[0:place] + "ND" + oldstring[place+len(word3):len(oldstring)]
		return word(newstring)
	elif word4 in oldstring:
		place = search(oldstring, word4)		
		newstring = oldstring[0:place] + "WUT" + oldstring[place+len(word4):len(oldstring)]
		return word(newstring)
	else:
		return oldstring

def letter(oldstring, letters):
	letters = uppercase(letters)
	for x in range(len(letters)):
		if letters[x] not in modifiable:
			print("This program can not translate the letter", letters[x])
	return letter_replace(oldstring, letters)
	

def letter_replace(oldstring, letters):
	for x in range(len(letters)):
		flag = True
		if letters[x] in oldstring:
			if letters[x] in modifiable:
				y = 0
				while letters[x] != modifiable[y]:
					y+=1
				place = search(oldstring, modifiable[y])
				newstring = oldstring[0:place] + modified[y] + oldstring[place+1:len(oldstring)]
				return letter_replace(newstring, letters)
			else:
				flag = False
		else:
			flag = False
	if flag == False:
		return oldstring
	

def search(full_string, string_to_search):
	flag = False
	for y in range(len(full_string)):
		if full_string[y] == string_to_search[0]:
			flag = True
			for z in range(len(string_to_search)):
				if full_string[y+z] != string_to_search[z]:
					flag = False
					break
		if flag == True:
			place = y
			return place		

def main():
	while True:
		to_translate = input("Type the string you want to translate: ")
		to_translate = uppercase(to_translate)
		to_translate = removePunc(to_translate)
		print(to_translate)
		print("Do you want to replace phrases?")
		if respond() == "Y":
			to_translate = phrase(to_translate)
			print(to_translate)
		print("Do you want to replace words?")
		if respond() == "Y":
			to_translate = word(to_translate)
			print(to_translate)	
		print("Do you want to replace letters?")
		if respond() == "Y":
			replace = input("What letters would you like to replace? ")
			to_translate = letter(to_translate, replace)
			print(to_translate)			
		print("\nFinal Translation:",to_translate,"\n")
		print("Would you like to translate another string?")
		if respond() != "Y":
			break
			
	
if __name__ == '__main__':
	main()
