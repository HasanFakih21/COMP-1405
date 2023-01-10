#Hassan Fakih 101168868

import pygame
pygame.init()

#Function that merges the two images
def Copy(x_ghost_position_on_background, y_ghost_position_on_background):
	global backup_screen 
	screen.blit(background, [0,0]) #this resets the display so things like the hovering coordinates when using the mouse are gone when creating the image
	(width_ghost, height_ghost) = ghost.get_rect().size #gets the size of the original ghost image	
	for row in range(height_ghost): #loops for the rows in the image
		for column in range(width_ghost): #loops for the columns 
			(r, g, b, _) = ghost.get_at( (column, row) ) #gets color for every pixel in the ghost original image
			if not((r == 0) and (g == 255) and (b ==0)): #if pixel is not green
				final_cords = Allign(width_ghost,height_ghost,column,row, x_ghost_position_on_background, y_ghost_position_on_background) #calls the allign function to get the final cords
				if (final_cords[0]>0 and final_cords[1]>0) and (final_cords[0]<width_background and final_cords[1]<height_background): #makes sure no error happens if pixel is out of bounds
					final_colors = Transparency(r, g, b, final_cords) #calls transparency function to make pixels look transparent 
					screen.set_at(final_cords, final_colors) #sets the color of the pixel at the final cord and at the calculated color for transparency effect
	backup_screen = screen.copy() #backup screen used to make sure cords while using the mouse only display one at a time

#function that calculates the points for where the ghost image should be relative to the center point provided by the user on the background
def Allign(width_ghost,height_ghost,column,row, x_ghost_position_on_background, y_ghost_position_on_background):
	midpoint_of_x = width_ghost//2 #calculates the halfway cord for x in the original ghost image
	midpoint_of_y = height_ghost//2 #calculates the halfway cord for y in the original ghost image
	diff_x = column - midpoint_of_x #finds the difference between the current position pixel on the original ghost image with the midway point for the x value
	diff_y = row - midpoint_of_y #finds the difference between the current position pixel on the original ghost image with the midway point for the y value
	final_x = x_ghost_position_on_background + diff_x #adds the difference between the midpoint of the ghost image with where the x point specified by the user on the background image
	final_y = y_ghost_position_on_background + diff_y #adds the difference between the midpoint of the ghost image with where the x point specified by the user on the background image
	return(final_x, final_y)

#function that checks if the left mouse button was clicked
def Cursor():
	if pygame.mouse.get_pressed()[0] == True: #if the left click on the mouse was pressed
		screen.blit(background, [0,0]) #resets the display to the background (so only one ghost appears at a time)
		(x_ghost_position_on_background, y_ghost_position_on_background) = pygame.mouse.get_pos() #finds the x and y value for where the user clicked on the background image
		Copy(x_ghost_position_on_background, y_ghost_position_on_background) #calls the copy function and sends the previous x and y values
	DisplayCords() #calls the display cords function

#function that displays the cords while the mouse is hovering over the display
def DisplayCords():
	screen.blit(backup_screen, [0,0]) #this makes sure that the ghost stays on the display while moving the cursor
	pygame.event.get()
	(x_hover, y_hover) = pygame.mouse.get_pos() #gets the x,y position of where the cursor is
	cords_string = "("+str(x_hover)+" , "+str(y_hover)+")" #converts the position into a string in the (x,y) format
	surface = font.render(cords_string, True, (255,255,255)) #new surface created for the text, font color white
	screen.blit(surface, [x_hover+15,y_hover+15]) #copies the text onto the display on the same x,y cord it's hovering over

#function for if the user wants to type the cords instead
def FindCenter(): 
	x_ghost_position_on_background = int(input("Please enter the X coordinate you want the ghost to be centered on in the background ")) #takes the x value from the user
	y_ghost_position_on_background = int(input("Please enter the Y coordinate you want the ghost to be centered on in the background ")) #takes the y value from the user
	if (x_ghost_position_on_background>0 and y_ghost_position_on_background) and (x_ghost_position_on_background<width_background and y_ghost_position_on_background<height_background): #validates input
		Copy(x_ghost_position_on_background, y_ghost_position_on_background) #calls the copy function
	else:
		print("Please enter valid input! Size of background is ","(",width_background,",",height_background,")") #error message and it also shows the width and height so the user knows what to enter
		FindCenter() #the function calls itself again if the input isn't valid

#function that makes the pixel transparent relative to the background
def Transparency(r,g,b, final_cords):
	(r_background, g_background, b_background, _) = background.get_at(final_cords) #gets the background color of the pixel of the background the final image of the ghost will be on
	final_r = (r_background + r)//2 #average between the background color and the ghost's color
	final_g = (g_background + g)//2
	final_b = (b_background + b)//2
	return(final_r,final_g,final_b) #returns the final values

#function to validate yes/no input
def Respond():
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

#function that shows the instructions
def Instructions():
	print("Would you like some instructions before proceeding?")
	if Respond() == "Y":
		print("This program takes two images and merges them\nIt requires a background image and a main image which is infront of a green screen\nYou will be asked for the file name of the background image first and then the one for the main image\nPlease also include the file extension of the images you would like to use\nAfter selecting the images you will be asked if you want to use the cursor to select the point which your main image will be centered around in the background\nIf you say yes, just hover over the display window and click on any point\nIf you already have specific coordinates in mind and you say no you will then be asked to provide the two coordinates\nYou can exit the window by clicking on the exit button on the top right\nAnd that's all!")
		input("\nPress enter to proceed")


Instructions() #calls the instructions function

	
background = pygame.image.load(input("What is your background image? ")) #asks the user for the name of the background image and loads it
ghost = pygame.image.load(input("What is your main image? ")) #asks the user for the name of the ghost image and loads it

(width_background, height_background) = background.get_rect().size #gets the height and width of the background image
screen = pygame.display.set_mode( (width_background, height_background) ) #sets the display with the size equal to the background image
screen.blit(background, [0,0]) #copies the background image to the display
pygame.display.update() #updates display

font = pygame.font.SysFont(None,25) #creates a font object with a font size of 25

backup_screen = screen.copy() #creates a copy of the display as backup


use_cursor = False #initializes the use cursor variable as false
print("Would you like to use the cursor?")
if Respond() == "Y":
	use_cursor = True #sets it to true if user responds with a yes to the question
else:
	FindCenter() #if not then the findcenter function is called
	


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.display.quit()
			pygame.quit()
	if use_cursor == True:
		Cursor() #the cursor function is called here within the infinite loop if the user responds yes to using the cursor
	pygame.display.update()



	
	

	
				

























		
