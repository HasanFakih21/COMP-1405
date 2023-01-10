#Hassan Fakih 101168868

#Introduction
print("*** GROCERY SHOPPING: THE GAME ***\n")
print("Many differnet types of people visit the grocery store. You may:\n1. Be a grandma dragging her grand son along\n2. Be a broke college student with a tight budget\n3. Be a single mother who brought a bunch of coupons\n")
typeofperson = int(input("What is your choice? "))

#Empty line
print()

#Different prompts for different type selected
if typeofperson == 1:
	print("Surely a grandma would not visit the store alone, what are the names of the other 4 grandmas going with you? ")
elif typeofperson == 2:
	print("College students travel in droves, what are the names of the other 4 students going with you?")
else:
	print("As single as single moms are they never travel in singles, what are the names of the 4 other single moms going with you?")

#Inputs for names of the rest of the 'party'
name1 = input("1. ")
name2 = input("2. ")
name3 = input("3. ")
name4 = input("4. ")

#Extra text
print()
print("At the store you decide to buy some groceries.\n")


toiletpaper = int(input("Toilet paper costs $0.84 a roll. How many rolls will you buy? ")) #Asks for input for toilet paper amount
if toiletpaper>99:
	print("What? Why? You do you I guess") #print extra text on condition
toiletpaper = toiletpaper*0.84 #gets the total cost of toilet paper rolls
total = toiletpaper #adds it to the overall total amount so far
print("Your bill so far is ${:.2f}\n".format(total)) #outputs total so far to two decimal spots

cigarettes = int(input("Cigarettes cost $6.28 a pack. How many packs will you get? ")) #asks for input for cigs
flag = cigarettes>19
if flag:
	print("Okay yikes. chill.") #extra text
cigarettes = cigarettes*6.28 #calculates cig total cost
total = total + cigarettes #calculates overall total cost
print("Your bill so far is ${:.2f}\n".format(total)) #output overall total 2 decimal spots

liquor = int(input("A bottle of liquor costs $22. How many bottles will you get? ")) #asks for inpur for liquor
if liquor> 19:
	if flag:
		print("DO YOU NEED HELP?!?!") #extra text
	else:
		print("Please tell me it's for a party") #extra text
liquor = liquor*22 #liq total cost
total = total + liquor #overall
print("Your bill so far is ${:.2f}\n".format(total)) #output overal 2 dec
	
print("You then decide you probably should get some food\n") #more text

fruits = int(input("Fruits cost $5 a kilogram. How many kilograms will you buy? ")) #aks for input for fruits
fruits = fruits*5 #fruits total costs
total = total + fruits #overall total
print("Your bill so far is ${:.2f}\n".format(total)) #output overall total 2 dec

bread = int(input("Each loaf of bread costs $0.62. How many loafs will you buy? ")) #input for bread
bread = bread*0.62 #bread total cost
total = total + bread #overall total
print("Your bill so far is ${:.2f}\n".format(total)) #output overall total 

print()
print("************************\n\tRoofmart\n************************\n1. Toilet Paper\t${:.2f}\n2. Cigarettes\t${:.2f}\n3. Liquor\t${:.2f}\n4. Fruits\t${:.2f}\n5. Bread\t${:.2f}\n************************\n".format(toiletpaper, cigarettes, liquor, fruits, bread)) #outputs bill with each item's total cost
print("Total Bill: ${:.2f}".format(total)) #outputs the overall cost of everything




