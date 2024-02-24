list = [1, 2, 3, 4, 5, 6, 25, 35, 12, 13]
print(max(list))
list1 = ["karthik", "bala", "kishore", "chintu"]
# print(f"hello {list1[" "]}!")

names = ["karthik", "bala", "kishore", "chintu"]
for name in names:
    print("Hello,", name + "!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)
    if num % 2 == 0:
        print('num', num)


a = [1, 2, 3, 4, 5, 6, 25, 35, 12, 13]
sum(a)
print("total", sum(a))


# numbers = [1, 2, 3, 4, 5, 6, 25, 35, 12, 13]
# total = sum(numbers)
# print("The sum of all numbers in the list is:", total)
A = [1, 2, 3, 4, 5, 6, 25, 35, 12, 13, 10, 22, 3, 4, 52, 62, 25, 35, 1, 13]
unique = set(a)
print("unique",unique)

A = [1, 2, 3, 4, 5, 6, 25, 35, 12, 13]
B = [10, 22, 3, 4, 52, 62, 25, 35, 1, 13]
C = (set(A) & set(B))
print(C)

names = ["karthik", "bala", "kishore", "chintu"]
for name in names:
    print(name, len(name))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 23, 45, 3, 5, 2]
unique = set(numbers)
print(unique)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 23, 45, 3, 5, 2]
average_nums = sum(nums)/len(nums)
print(average_nums)
# 117/16 --7.3125

names = ["eshwar", "ishu", "arun", "karthik", "bala", "kishore", "chintu"]
for name in names:
    if name[0].lower() in 'aeiou':
        print(name)
print("-------------------------------------")
# LIST = ["radar","madam","eve","eee","chin","karthik"]
# for list in LIST:
#     if [list[::-1]]:
#         print(list)

# strings = ["radar", "level", "hello", "racecar", "python"]
# palindromes = [s for s in strings if s == s[::-1]]
# print(palindromes)

values = ["radar", "level", "hello", "racecar", "python"]
for value in values:
    if value == value[::-1]:
        print(value)
print("-------------------------------------")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for nums in numbers:
    square = nums *2
    print(square)
print('---------------------------------------')
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [11, 22, 33, 44, 55, 66, 7, 8]
concate = list1 + list2
print(concate)

print("----------------------------------------")

list1 = [1, 2, 3, -4, -5, 6, 7, -8]
for list in list1:
     if list >0:
         print(list)
print("---------------------------")

names = ["eshwar", "ishu", "arun", "karthik", "bala", "kishore", "chintu"]
for name in names:
    A = [len(name) > 5]
    if [len(name) > 5] is True:
        print("Hello,", name + "!")


strings = ["apple", "banana", "orange", "kiwi", "grape","kaju"]
for i in strings:
    if i.upper():
        print(i.upper())
if len(strings) > 3:
    print(len(strings) > 3)


# long_strings = [s for s in strings if len(s) >5]
# print(long_strings)


numbers = [1, 2, 3, 4, 5]
product = 1
for num in numbers:
    product *= num
print("Product of all numbers:", product)

print("---------------------------------")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 23, 45, 3, 5, 2]
# for nums in numbers:
#     sorted = nums()


numbers = [3, 2, 5, 4, 6, 1]
even_numbers = sorted([num for num in numbers if num % 2 == 0])
print(even_numbers)
print("---------------------------------")

names = ["eshwar", "ishu", "arun", "karthik", "bala", "kishore", "chintu"]
alphabetic = sorted(names)
print(alphabetic)


numbers = [1, 2, 3, 4, 5]
cumulative_sum = []
current_sum = 0
for num in numbers:
    current_sum += num
    cumulative_sum.append(current_sum)
print("Cumulative sum:", cumulative_sum)

print("----------------//////")

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    if i == 4:
        continue
    print(i)
print('1111111111111111')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 23, 45, 3, 5, 2]
nums = {"name": "karthik", "age": 23, "phno": 9515}
print(nums.keys())
print(nums.values())
print(nums.items())
nums.update({1:2})
print(nums)
print("1111111111111")



for i,j in nums.items():
    print({i,j})

# A = open('timezone.py', mode='a')
# A.write("karthik")
# A.close()

print("????????????????????????????????????????????????")
class add():
    def sum(self):
        a = 5
        print(a)

B = add()
B.sum()


'''
single inheritance
multi level inheritance
multiple inheritance
hirarechal inheritance
'''

class parent():
    def output(self):
        print(self.a, "I am a parent")

class child(parent):
    def outputchild(self):
        print("I am a child")

# c = child()
# c.output()       # Output from parent class method
# c.outputchild()  # Output from child class method

class grandparent():
    def output(self):
        print("I am a grandparent")
class parent(grandparent):
    def outputparent(self):
        print("I am a parent")

class child(parent):
    def outputchild(self):
        print("I am a child")

c = child()
c.output()
c.outputparent()  # Output from parent class method
c.outputchild()

class grandparent():
    def output(self):
        print("I am a grandparent")
class parent(grandparent):
    def outputparent(self):
        print("I am a parent")

class child(parent):
    def outputchild(self):
        print("I am a child")

c = child()
c.output()
c.outputparent()  # Output from parent class method
c.outputchild()


'''
swapping
'''


# Initial values
a = 5
b = 10

# Swapping using tuple unpacking
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1, 1, 23, 45, 3 ,0, 5, 2]

prime_numbers = [num for num in numbers if is_prime(num)]

print("Prime numbers in the list:", prime_numbers)


# i want element  in list
l = ['arun', 'bala', 'chintu', 'eshwar', 'ishu', 'karthik', 'kishore']
name ="kiran"
if name  in l:
    print(f"there is a {name}")
else:
    print(f"there is no name ")

# l = ['arun', 'bala', 'chintu', 'eshwar', 'ishu', 'karthik', 'kishore']
# name = "arun"
# if name in l:
#     print(f"there is a {name} in the list")
# else:
#     print("there is no arun")

# palidrome

s = ['arun', 'nun', 'radar', 'eshwar', 'ishu', 'karthik', 'kishore']

def is_palindrome(s):
    return s == s[::-1]

# Example usage
print(is_palindrome("RADAR"))  # Output: True
print(is_palindrome("NUN"))  # Output: False

names = []
numbers = []
dotnums = []
l = ["karthik","chintu",121211,"kiran",1.1323,"arun",12132435,121324351131,"kishore", 1.223, 2.009]

for i in l:
    if type(i) == str:
        names.append(i.upper())


    if type(i) == int:
        numbers.append(i)

    if type(i) == float:
        dotnums.append(i)

print(f"they are names {names}")
print(f"they are numbers {numbers}")
print(f"they are float {dotnums}")
print("-------------------------------------------------------------------")


a = "floccinaucinihilipilification"
p = len(a)
print(p)

# Importing the add function from timezone.py
from timezone import multiple, add


# Now you can call the add function directly
result = multiple(5, 6)
print(result)  # Output: 11
#
#
#
adding = add(2,3)
print(adding)

x = 5
y = 10

x, y = y, x

print("x =", x)
print("y =", y)

names = ("radar","chintu","nun")
for i in names:
    if i==i[::-1]:
        print(i,"is a polidorme")
    else:
        print(i ,"not is a polidorme")

