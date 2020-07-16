# Create a Pets class that holds instances of dogs; this class is completely separate from the Dog class.
# In other words, the Dog class does not inherit from the Pets class.
# Then assign three dog instances to an instance of the Pets class.
# Start with the following code below. Save the file as pets_class.py. Your output should look like this:
# #
# # I have 3 dogs.
# # Tom is 6.
# # Fletcher is 7.
# # Larry is 9.
# # And they're all mammals, of course.

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


#Pets class holding instances of dogs
class Pets:
    dogs = []

    def __init__(self,dogInstances):
        self.dogs=dogInstances


#Instances of 3 dogs:
dog1=RussellTerrier('Tom', 6)
dog2=Bulldog('Fletcher', 7)
dog3=Dog('Larry', 9)

#Instance of Pets, holding dog instances
dog_list=dog1,dog2,dog3
my_Pets=Pets(dog_list)

print('I have {} dogs.'.format(len(dog_list)))
for dog in my_Pets.dogs:
    print('{} is {} years old and is a {}'.format(dog.name, dog.age, dog.species))
