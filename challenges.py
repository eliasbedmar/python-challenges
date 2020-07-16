# Dump of exercises from Hacker rank challenges, varying in difficulty



n=5

for i in range(0,n):
    print(i**2)



def check_leap(year):
    is_leap=False
    if year%4==0:
        is_leap=True
    if year%100==0:
        is_leap=False
    if year%400==0:
        is_leap=True
    return is_leap


print(check_leap(1999))
print(check_leap(1234))

print(check_leap(2000))
print(check_leap(2400))



def print_range(n):
    string =""
    for i in range(1,n+1):
        string=string+str(i)
    print (string)


print_range(7)


import numpy
a=numpy.array(input().split(" "), float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))

x = 1
y = 1
z = 1
n = 2

coordinates = [[i, j, k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n]
coordinates.sort()

print(coordinates)


input = '5 3 2 6 6'

input = map(int, input.split(' '))

input = list(input)

print(input)

#using sets
score_set=set(input)
sorted(score_set)

print(score_set)

print(max(score_set))

score_set.remove(max(score_set))

print(score_set)

print(max(score_set))



name_list = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
score_list = [37.21, 37.21, 37.2, 41.0, 39.0]

joint_list = [[name, score] for name,score in zip(name_list,score_list)]

#Take second element
def takeSecond(item):
    return item[1]

joint_list.sort(key=takeSecond, reverse = False)

print(joint_list)

if takeSecond(joint_list[1]) == takeSecond(joint_list[0]):
    i = 1
    while i <= len(joint_list):
        if takeSecond(joint_list[i+1]) != takeSecond(joint_list[i]):
            print(joint_list[i+1])
            if takeSecond(joint_list[i + 2]) == takeSecond(joint_list[i+1]):
                print(joint_list[i+2])
            if takeSecond(joint_list[i + 3]) == takeSecond(joint_list[i+2]):
                print(joint_list[i + 3])


else:
    print(joint_list[1])
    i = 2
    while i <= len(joint_list):
        if takeSecond(joint_list[i+1]) == takeSecond(joint_list[i]):
            print(takeSecond(joint_list[i+1]))
            i+1






if __name__ == '__main__':
    from statistics import mean
    n = int(input())
    data = {}


    def process_input(raw_input):

        inputs = input().split(' ')
        inputs.reverse()
        name = inputs.pop()
        mark_list = list(map(float, inputs))

        return name, mark_list

    for i in range(n):
        name, mark_list = process_input(i)
        data.update({name: mark_list})

    def retrieve_average_mark(query_name, dict):
        mark_list = dict[query_name]
        res = mean(mark_list)
        output = "{:.2f}".format(res)
        print(output)

    retrieve_average_mark(input(), data)
##################################################

from statistics import mean

raw_input = [
    'Krishna 67 68 69',
    'Arjun 70 98 63',
    'Malika 52 56 60'
    ]

def process_input(raw_input):

    inputs = raw_input.split(' ')
    inputs.reverse()
    name = inputs.pop()
    mark_list = list(map(float, inputs))

    return name, mark_list


data = {}

for i in raw_input:
    name, mark_list = process_input(i)
    data.update({name: mark_list})

print(data)


def retrieve_average_mark(student, dict):
    res = mean(data[student])
    output = "{:.2f}".format(res)
    print(output)

# retrieve_average_mark(input('Say name of student'),data)
retrieve_average_mark('Krishna',data)
#########################################

class Marks:

    def __init__(self, raw_input):

        self.data = {}

        for student in raw_input:
            input = student.split()
            input.reverse()
            name = input.pop()
            mark_list = list(map(float, input))

            self.data.update({name: mark_list})

        print(self.data)


    def retrieve_mark(self,input_request):
        from statistics import mean

        res = mean(self.data[input_request])
        output = "{:.2f}".format(res)
        print(output)

raw_input = [
    'Krishna 67 68 69',
    'Arjun 70 98 63',
    'Malika 52 56 60'
    ]

marks_Obj = Marks(raw_input)

for student in ['Krishna','Arjun','Malika']:
    marks_Obj.retrieve_mark(student)



import math


N = 12

raw_input = ['operation X Y', 'operation Y Z', 'Operation']


list = []
for i in range(int(raw_input())):
    s = raw_input().split()

    for i in range(1, len(s)):
        s[i] = int(s[i])



if __name__ == '__main__':
    N = int(input())

    instructions = []

    for i in range(N):
        inst = input()
        instructions.append(inst)

    # instructions = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print', 'remove 6', 'append 9', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']


    list = []

    for i in instructions:

        if i == 'print':
            print(list)

        elif i == 'sort':
            list.sort()

        elif i == 'pop':
            list.pop()

        elif i == 'reverse':
            list.reverse()

        else:

            i_list = i.split(' ')


            if i_list[0] == 'remove':
                elem = int(i_list[1])
                list.remove(elem)

            elif i[0] == 'append':
                elem = int(i_list[-1])
                list.append(elem)

            else:
                index = int(i_list[1])
                elem = int(i_list[-1])
                list.insert(index, elem)


if __name__ == '__main__':

    N = int(input)

    tuple_const = input()

    tuple_const = tuple_const.split()

    tuple_const = map(int, tuple_const)

    t = tuple(tuple_const)

    print(hash(t))


if __name__ == '__main__':
    input_msg = input()

    def swap_case(input):
        return input.swapcase()

    swap_case(input_msg)


def split_and_join(line):
    split = line.split(" ")
    return "-".join(split)

if __name__ == '__main__':
    line = 'this is a string'
    result = split_and_join(line)
    print(result)

sockMerchant. n = no socks in pile. ar = colours of each sock

Input - n, then n space separated integers describing ar[i]
Output - number of total matching pairs.


n = '9'

n = int(n)

raw_input = '10 20 20 10 10 30 50 10 20'

arr = raw_input.split(" ")

arr = list(map(int, arr)

print(arr)

































