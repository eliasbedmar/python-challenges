class Dog:

    #Class attribute
    species = 'mammal'

    #Initialiser/Instance constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age


def get_biggest_number(*args):
    list_ages=[]
    for arg in args:
        print(arg.age)
        list_ages.append(arg.age)
    print(list_ages)
    return max(list_ages)

def main():
    dog1=Dog('Poncho',12)
    dog2=Dog('Monty',13)
    dog3=Dog('Shawn',15)
    max_number = get_biggest_number(dog1,dog2,dog3)
    print('Max age is: ', max_number)


if __name__=='__main__':
    main()
