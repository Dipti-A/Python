from math import pi
import sys

class Circle():
    def __init__(self, radius):
        self.radius= radius

    def surface(self):
        return pi * self.radius * self.radius

#Inherited from superclass Circle
class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def volume(self):
        #Invoke inherited surface from superclass
        return super().surface() * self.height

    def surface(self):
        return ((2*super().surface())+(2*pi*self.radius*self.height))

#Inherit from class Cylinder
class Cone(Cylinder):
    def __init__(self,radius, height):
        super().__init__(radius, height)

    def volume(self):
        return super().volume()/3

try:
    cylinder=Cylinder(4,9)
    print ('The surface of the cylinder : ',cylinder.surface())
    print ('The volume of the cylinder : ',cylinder.volume())
    cone = Cone(4,9)
    print ('The volume of the cone : ',cone.volume())

except NameError:
    print("\nName error occured.. Try again!")
except TypeError:
    print("\nType mismatch occured.. Try again!")
except ValueError:
    print("\nValue error occurred.. Try again! ")
except IndexError:
    print("\nIndex error occurred.. Try again!")
except SyntaxError:
    print("\nSyntax error ocurred.. Try again!")
except AttributeError:
    print("\nAttribute error occured. Try again")
except ArithmeticError:
    print("\nArithmetic error ocurred.. Try again!")
except Exception:
    e = sys.exc_info()[0]
    print("Error encountered : ", e)
    print("Try again...")