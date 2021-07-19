
import math
import random


def shuffle_list():
    temp_list = [['7.7', '3.0', '6.1', '2.3'], ['6.3', '3.4', '5.6', '2.4'], ['6.4', '3.1', '5.5', '1.8'],
                 ['6.0', '3.0', '4.8', '1.8'], ['6.9', '3.1', '5.4', '2.1'], ['6.7', '3.1', '5.6', '2.4'],
                 ['6.9', '3.1', '5.1', '2.3'], ['5.8', '2.7', '5.1', '1.9'], ['6.8', '3.2', '5.9', '2.3'],
                 ['6.7', '3.3', '5.7', '2.5'], ['6.7', '3.0', '5.2', '2.3'], ['6.3', '2.5', '5.0', '1.9'],
                 ['6.5', '3.0', '5.2', '2.0'], ['6.2', '3.4', '5.4', '2.3'], ['5.9', '3.0', '5.1', '1.8']]
    print("temp list before", temp_list)
    random.shuffle(temp_list)
    print("temp_list after", temp_list)

#Prompt user to enter the sides of triangle
#Side_1= int(input("Enter the length of the first side: "))
#Side_2= int(input("Enter the length of the second side: "))
#Side_3= int(input("Enter the length of the third side: "))

#Calculate Perimeter
#Pr=Side_1+Side_2+Side_3

#Calculate Area
#P = Pr/2
#A = math.sqrt(P*(P-Side_1)*(P-Side_2)*(P-Side_3))

#Print Perimeter and area
#print("Perimeter :",Pr)
#print("Area :",A)
shuffle_list()
