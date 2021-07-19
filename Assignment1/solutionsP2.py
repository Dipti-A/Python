#Defining variables
Depth = 2
Height = 1

#Prompt user to enter width of the plinth at highest level
Width_highest = int(input("Enter the width of the plinth at the highest level: "))

#Prompt user to enter width of the plinth at lowest level
Width_ground = int(input("Enter the width of the plinth at the ground level: "))

#Check if the highest plinth is smaller than the one at the base
if (Width_highest>Width_ground):
    print("Width at highest level should be less than width at lowest level. Try again...")
else:
    #Initializing volume
    Volume = 0

    #Calculate volume at each level
    for x in range(Width_highest, Width_ground+1):
        # Add the volumes calculated at each level
        Volume = Volume + (x*Depth*Height)

    #Combined volume of the plinths at all levels
    print ("Volume of the plinth:",Volume)
