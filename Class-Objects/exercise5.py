class Triangle:

    #Class attribute
    number_of_sides = 3

    #Instance constructor method
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    # Method - check_angles
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False


#Instances
my_triangle=Triangle(30,60,90)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

