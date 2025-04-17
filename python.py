#in python everything is object datatype variable etc

# modules = libraries for python having different functions classes

# pip = used as package manager to download modules

# comments = non executable lines for better understanding 
# for example 
# print('hello world') #this will print hello world.
# two type 1st # second """ multiple line statement"""

'''escape sequance = used to escape some cases where INSERT 
in string is invalid.
for example 
  print('hey im 'yash' good to know it') #this is not valid
  print('hey im \'yash\' good to know it') #this is valid 
  **for new line = \n 
  print("hello 
        world") #invalid output - error
  print('hello \n world') #valid output - hello 
                                          world
   '''


# print statement and parameters 
# print method is use to return given statement
# for example 
# '''print('hello world') #output - hello world
# parameters in print statement 
# seperator -> seperate each object 
# print(1,2,3,4, sep="~") #output - 1~2~3~4
# end -> print given argument at the end 
# print('hello world',end=' this is me')

"""
variables = use to store datas of different datatypes in R.A.M
for example - 
a = 'hello world' # a is a container and hello world is data
= assignment operator is using to assign the data to the variable
#data could be different data types 
"""

#type method = use to get which type of data
# a23123 = None
# print(type(a23123)) 

"""datatpyes
integer = int(1, -2),float(2.2, -1.2),complex(8,2j)# j is imaginary part
boolean = consist true and false
string = group of characters ('hello world')
sequance data = list(mutuable) - ['hello'] and tuple(immutuable) - ("hello")
mapped data = dict(dctionary) key value pairs -{"name" : "John", "age" : 36}
""" 


# typecasting 
# converting one datatype to another datatype
# two typee - explicit and implicit\
# explicit - where user convert one datatype to another datatype
# a = int(8.3) #float converting into integer
# b = int("21") #string coverting into integer
# c = float(5) #integer converting into float
# print(a,b,c)
#implicit - where python convert lower datatype to higher datatype
# a = 4.3 
# b = 3
# print(a + b) # b converted into float for a for higher datatype

"""
input function - use to take input from user 
*the input will be always string untill it is typecasted
a = input('enter your name') #input = yash
print('my name is ',a) # my name is yash
"""

#strings - group of characters enclosed by qoutes
#print something like that -> he said 'he want to eat'
# done through two ways by escape sequance or single qoutes & double quotes
#by escape sequance
# print("he said \"he want to eat\"") -> he said "he want to eat"
#by single & double qoutes
# print("he said 'he want to eat'") -> he said 'he want to eat' 

# we can write string like this also
# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

#to print multiple line in single string
# -> we can use triple qoutes
# a = """ helllo im yash
# from jaipur 
# how are you"""
# print(a)

"""accessing strings character individually
two ways -
first - by index number which starts from 0 and ends with -1
second - by for loop
#first
access_string = 'hello my name is dash'
print(access_string[0])
print(access_string[10])
print(access_string[-1])

# second
access_string = 'hello my name is dash'
for char in access_string:
      print(char)
"""
# slicing string 
# to get a particular character in string
# a = 'hello'
# print(a[0:3]) -> hel
# print(a[:5])-> hello
# print(a[0:]) -> hello
# print(a[-5:-1])#negative index value -1 = last index   -> hello


""" 
operations in strings 

# exampleString = "hello world im here !!!!" 
# len() - use to identify length of string
print(len(exampleString))

# uppercase() -> upper case all the character
print(exampleString.upper())

#lower case -> lower case all the character
print(exampleString.lower())

# rstrip -- remove all the trailing charcter from the end
exampleString1 = 'hello world $$$$'
print(exampleString1.rstrip("$"))

# replace -- use to replace string to new string
print(exampleString.replace('here','new')) # here replaced by new

# split -- use to convert a string into list
splitstring = 'hello world'
splitstring2 = 'hello%world%im%new'
print(splitstring.split(' ')) #split and converted  by space 
print(splitstring2.split('%')) # split and converted by percent

# capatilize() -- use to convert only first character to capital and all other to lower
capatalizeString = 'hELlo Im NEw'
print(capatalizeString.capitalize())

# center -- use to align the string by given padding 
print(exampleString.center(100,"%"))

# count -- use to count  string or character how many time present in a string
print(exampleString.count("l")) 

exampleString = "hello world im here !!!!"
# endswith --use to check string ends with the given character
print(exampleString.endswith('!!!',15,-1))

# startswith -- use to check string starts with given character
print(exampleString.startswith('hello'))

# find -- use to find first character and return true if present else -1
print(exampleString.find('world'))
print(exampleString.find('use'))

# index -- similar to find but return error if the given character is not present
print(exampleString.index('hello'))
print(exampleString.index('use'))

exampleString = "hello world im here !!!!"
# isalnum -- use to check if string holds only a-z and 0-9
print(exampleString.isalnum()) #false

# isalpha -- use to check if string holds only a-z
print(exampleString.isalpha()) #false

# islower -- to check all the character is lower case
print(exampleString.islower()) #true

# isupper -- to check all the character is upper case
print(exampleString.isupper()) #false

# isprintable -- to check all the character is printable if holds \n \" then non printable
exampleString1 ="hello world"
exampleString2 ="hello \nworld"
print(exampleString1.isprintable()) #true
print(exampleString2.isprintable()) #false

# isspace -- use to check whitespace is present or not 
exampleString1 ="hello world"
exampleString2 =" " 
print(exampleString1.isspace()) #false
print(exampleString2.isspace()) #true

exampleString = "hello world im here !!!!"

# title -- convert all the fisrt character of string into capital
print(exampleString.title())

# istitle -- use to check the string is titled all not 
print(exampleString.istitle())

# swapcase -- convert lower case into upper and upper into lower
print(exampleString.swapcase())
"""

# if-else -- return if statement if true else return else statement if false
# askedNum = int(input("enter valid number: "))

# if(askedNum >= 0):
#   print(f"positve number {askedNum}")
# else:
#  print(f"negative number {askedNum}")

#**if-elif-else-case -- use to check multiple condition

# askedNum = int(input("enter number: "))

# if(askedNum > 10):
#   print(f"the value is greater then zero {askedNum}")
# elif(askedNum == 0):
#   print(f"the value is equal to zero")
# elif(askedNum > 10):
#   print(f"the value is less then ten{askedNum}")
# else:
#   print(f"the value is negative{askedNum}")

# **nested if else -- if inside a if statement 
# askedNum = int(input("enter a number: "))

# if(askedNum == 0):
#   print(f"it is equal to zero {askedNum}")

# elif(askedNum >=0 and askedNum <= 20):
#       if(askedNum >= 0 and askedNum <= 10):
#             print(f"it is between 0 and 10 ({askedNum})")
#       elif(askedNum >= 10 and askedNum <= 20):
#             print(f"the value is between 10 to 20 ({askedNum})")

# else''':
#   print(f"not a postive number")


# match case -- similar to if case and other language switch case 
# it is use to match variable with some cases
'''x = int(input('enter a value : '))
match x:
   case 0:
     print(f"the value of {x} is zero")
   case 2:
     print(f"the value of {x} is two") 
   case 4:
     print(f"the value of {x} is four")
   case _:
     print(f"the value of {x} is different")

# we can use if condition with match statement
x = int(input('enter a value : '))
match x:
  case 2 if x / 2 == 1: # 2/2 =1
      print(f"x{x} is divisible by 2 and reminder is zero")
  case 4 if x / 2 == 2: # 4/2 =2
    print(f"x{x} is divisible by 2 and reminder is two")
  case 6 if x / 2 == 3: # 6/2 =3
    print(f"x{x} is divisible by 2 and reminder is three")
  case _:
    print("default")'''

# loop -- use to perform a task for a particular time 
# for loop -- 
# while loop --
# for loop
# for loop to print number 
# it will print always n - 1 for example if you want 5 give the value till 6 
# for i in range(11): #range is argument till where we want the number 
#   print(i) 

# #  we can also give starting number,ending number and omitted number 
# omitted numbers are those number which will skip that much number 
# for eg- omitted number is 2 than it will skip 2 numbers (0,2,4,6...)
# for numbers in range(0,11,2):
#   print(numbers)

# we can perform task with list,tuple,dict,string
# # achieving each element in list
# listName = ['hello','world','coding','python']  
# for eachELement in listName:
#   print(eachELement)

# # to achieve each character for each and individual element
# listName = ['hello','world','coding','python']  
# for everyElem in listName:
#   print(everyElem)
#   for eachchar in everyElem:
#     print(eachchar)


# printing star (decending to acending)
# i = 5
# while(i > 0):
#   for j in range(i+0):
#     print("*",end='')
#   print("")
#   i -= 1
# i = 1
# while(i < 5):
#   for j in range(i+1):
#     print("*",end='')
#   print("")
#   i += 1

# printing star using while loop
#
 
# printing value until it match the user value 
# i = int(input('enter a number :'))
# while(i <= 21):
#   print(i)
#   i = int(input('enter a number :'))

# table using while and for 
# i = 1
# while (i <= 10):
#   i * 2
#   print(i)
#   i += 1
#  
# for j in range(1,11):
#     j *= 2
#     print(j)

"""
functions - functions are reusable code that has to created once and can be used many times
function in python can be denoted by (def) keyword

two type of functions -
1) user defined - created by using def kerword
2) inbuilt - which is already created only need to be used like (min(),max(),sum(),len())

for example - printing a table using function
# def table(a):                       # table is the name / a is the argument
#   for multiple in range(1,11):      # loop from 1 to 10
#     multiplication = a * multiple   #multipling argument by the loop 
#     print(f"{a} * {multiple} = {multiplication}")

# table(5)  # calling a function by its name / passing parameter  to the argument (5) 
# print('\n')
# table(10)

# calling a function - to use a function we have to call it by its name
for example -  
table(5)
* table is the function name 
* 5 is the parameter of the argument 

there are 4 type of argument 
1) default argument
2) required argument
3) variable length argument
4) keyword argument

1 -> default argument - where the argument is already given to the function 
   
def average(a=4,b=6):
 print(f"the average of two number is ",(a+b)/2)

average()
# ** the value of argument can be changed when calling the function 
average(a=6) 

2 -> required argument - is this there is no default argment and value .
      the parameter should be passed in order and the parameter should be equals to
      the argument

def average(a,b): # the a,b are required argument 
 print(f"the average of two number is ",(a+b)/2)

average(4,6) # a= 4, b= 6 # value passed in order to as per the argument 

3-> keyword argument: the parameter are passed by the argument name then the
    order of the argument doesn't matter.

def average(a,b):
 print(f"the average of two number is ",(a+b)/2)
 
average(b=10,a=8) # value passsed by key value pair so order doesnt matter

4-> variable length argument - this are use to take multiple parameter
      under single argument by using (*)

 # def average(*a):
#  sum = 0 
#  for multipleValue in a:
#   sum += multipleValue
#   avg = sum / len(a)
#  return avg

# result = average(1,2,3,4,5) 
# print(result)     
"""




# List :- lists are ordered collection of data types.
# lists are mutable.
# used to store multiple values under single variable
# for example - 
# numList = [1,2,3,4,5]
# alphaList = ["abc","def","ghi"]
# mixedList = [1,"abc",2,"def"]

# accessing list value :- two ways to access
# 1st- by indexed value 
# 2nd- by loop

# # 1st- by index value (positive indexing and negative indexing)
# numList = [1,2,3,4,5,6]
# # print(numList[0]) // positive indexing
# print(numList[-5]) // negative indexing

# # 2nd by loop 
# for values in numList:
#   print(values)


#to find out particular element in list 
# alphaList = ["yash","soni"]
# if "yash" in alphaList:
#   print('true')
# else:
#   print('false')

# to print values of a particular range 
# listValue = [1,2,3,4,5,6,7,8]

# // len(listvalue) - means total length of a list till the last value
# print(listValue[0 : len(listValue)]) // o index to last index  
# print(listValue[:]) // epmty values means 0 index to last index 
# print(listValuep[:len(listValue)]) // interpretor automatically place 0 in the start index
# print(listValue[-8:-1])// negative index
# print(listValue[0:-1]) // positive and negative index
# print(listValue[0:8:2]) // jumping index- use to jump from a particular index


# list comprehension - use to create new list from the iterables 
# old_list = ['yash','soni','raghav','jal','yant']
# new_list = [i for i in old_list if len(i) <= 4]
# print(new_list)

# string_list = 'yash','soni','raghav','jal','yant'
# another_list = [item for item in old_list]
# print(another_list)

# existing_list = ['yash','yirag','soni','raj','hello',]
# for i in existing_list:
#   a = []
#   if i[0] == 'y':
#    a.append(i)
#    print(a)

"""# methods in lists 

## adding methods
# 1 - Append() = add item at end of the list
# 2 - Insert() = add item at a specific index
# 3 - expend() = add items of another iterable(set,list,tuple) 
#                at the end of the original list 

# originalList = [1,2,3,4,5,6]
# print(originalList)

# originalList.insert(0,0)
# print(f"insert method {originalList}")

# originalList.append(7)
# print(f"append method {originalList}")

# fakeList = [8,9]
# originalList.extend(fakeList)
# print(f"expend method {originalList}")

## Removing method
# 1 - remove() = remove the first accurance of the item 
# 2 = pop() = remove the item by the index value and return it default is last value 
# 3 - clear() = remove all the item and empty the list 

# originalList = [1,2,3,4,5,6]
# originalList.remove(6)
# print(f"remove method {originalList}")

# originalList.pop(4)
# print(f"pop method {originalList}")

# originalList.clear()
# print(f"clear method {originalList}")

## sorting and reversing
# 1 - sort() = sort the item in ascending and descending order. 
#              default is ascending. For desending use list.sort(reverse = true)
# 2 - reverse() = reverse the whole list 

# originalList = [5,6,3,4,1,2]

# originalList.sort()
# print(f"ascending sort method {originalList}")
# originalList.sort(reverse=True)
# print(f"desending sort method {originalList}")

# originalList = [5,6,3,4,1,2]
# originalList.reverse()
# print(f"reverse method {originalList}")

## searhing and sorting 
1 - Index() = return the index of first occurance of the item.
2 - count() = return how mant time a item accurs 

# originalList = ['a','b','c','d','e']
# print(f"index method {originalList.index('b')}")

# originalList = ['a','b','c','d','e','b']
# print(f"count method {originalList.count('b')}")

## copying 
copy () - this method create a copy of original list to modify the copied list without impacting the original list 
# originalList = [1,2,3,4,5,6]
# copiedList = originalList.copy()

# copiedList[0] = 8
# print(f"original list {originalList}")
# print(f"copied list {copiedList}")

"""


# #tuple = tuple is similar to list but the difference is tuple is immutable 
#        # means it can not modified.
#        # it is enclosed by () round brackets and value are seperated by commas

# tupleExample = (1,2,3,4,5,6,'yash',True)

# # exception - if wanted to create a tuple with sinlge value use comma after value
# # for example 
# normalTuple = ('string') # it will consider as a int bcz of single value 
# print(type(normalTuple),normalTuple)

# originalTuple = ('string',) # now the tuple is created 
# print(type(originalTuple),originalTuple)

# # accessing value can be doned through two ways same as list 
# # 1- loops
# # 2- index value(negative, positive) 
# tup = (1,2,3,4)
# print(tup[0],tup[-2])

# a tuple cannot be modified directly but it can done through indirectly -
  #by converting a tuple into list 
  #perform operations 
  #convert the list into tuple again

# #for example -
# tup1 = (1,2,3,5)  #created a tuple
# tempList = list(tup1)  # converted a tuple into list 

# tempList.insert(3,4)  #performed list operation
# tempList.pop(4)
# print(tempList) 

# newTup = tuple(tempList) #converted a list into tuple again
# print(newTup)

# #concatenation of tuple 
# tup1 = ('yash',)
# tup2 = ('soni',) 
# tup3 = tup1 + tup2
# print(tup3)

#count - use to count total accurance of the value
# tup1 = (1,2,3,1,4,1,41,45,1)
# result = tup1.count(1)
# print(result)

#index = print the index of first accurance of the value
# tup1 = (1,23,4,5,6,7,1,51)
# result = tup1.index(23)
# print(result)
# result2 = tup1.index(1,3,len(tup1))
# print(result2)

# ** if the value is not found then it will through an valueError
# result = tup1.index(55)
# print(result)


# length() - give the length of tuple
# tup = (1,2,3,4)
# print(len(tup))

''' # F-string - f string is use to format a string 
    # it helps to add a variable ina string without concatenation
    # it introduced in version 3.6
    # also known as literal string interpolation

      
two ways to create a F-string
1st - by variable.format() -
txt = 'my name is {} and iam {} years old'
name = 'yash'
age = 22
print(txt.format(name,age))
# also can done through index of format()
txt1 = 'my name is {1} and iam {0} years old'
name1 = 'komal'
age1 = 20
print(txt1.format(age1,name1))


2nd- by f'string' -
name = 'yash'
age = 20
txt = (f'name is {name} and iam {age} years old')
print(txt)


price = 49.1234
value = (f'the amount is {price:.2f}') # the 2f will print 2 value after point
print(value)
'''
