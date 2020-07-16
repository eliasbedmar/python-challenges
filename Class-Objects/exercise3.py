# Using the same file, add an instance attribute of is_hungry = True to the Dog class.
# Then add a method called eat() which changes the value of is_hungry to False when called.
# Figure out the best way to feed each dog and then output “My dogs are hungry" if all are hungry or “My dogs are not hungry.” if all are not hungry.
# The final output should look like this:

# I have 3 dogs.
# Tom is 6.
# Fletcher is 7.
# Larry is 9.
# And they're all mammals, of course.
# My dogs are not hungry.



# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    #Instance method
    def eat(self):
        self.is_hungry = False


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

my_Pets.dogs[0].is_hungry=False

print('I have {} dogs.'.format(len(dog_list)))
for dog in my_Pets.dogs:
    print('{} is {} years old and is a {}'.format(dog.name, dog.age, dog.species))
for dog in my_Pets.dogs:
    if dog.is_hungry == True:
        print('{} is hungry. I will feed him.'.format(dog.name))
        dog.eat()
        print('{} is now not hungry'.format(dog.name))
    else:
        print('{} is not hungry'.format(dog.name))


