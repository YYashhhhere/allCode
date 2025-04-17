# small calculator

# firstValue = int(input('print here your number '))
# secondValue = int(input('print here another number '))
# print("the additon of values are ", firstValue + secondValue)
# print("the substraction of values are ", firstValue - secondValue)
# print("the multiplication of values are ", firstValue * secondValue)
# print("the divsion of values are ", firstValue / secondValue)
# print("the modulus of values are ", firstValue % secondValue)
# print("the floor division of values are ", firstValue // secondValue)
# print("the exponentiation of values are ", firstValue ** secondValue)



# calculator from using user input 
# first value
# firstValue = int(input('enter your first number '))
# # second value
# secondValue = int(input('enter your second number '))
# #asking for operation to perform
# print('choose an operator\n 1 = +,\n 2 = -,\n 3 = %,\n 4 = *,\n 5 = /,\n 6 = //,\n 7 = **,')
# # now asking from user to choose the number given  before
# result = int(input('choose your operator '))

# # if..elif statement for example if 1 then add the values
# if result == 1 :
#  print(firstValue + secondValue)
# elif result == 2:
#  print(firstValue - secondValue)
# elif result == 3:
#  print(firstValue % secondValue)
# elif result == 4:
#  print(firstValue * secondValue)
# elif result == 5:
#  print(firstValue / secondValue)
# elif result == 6:
#  print(firstValue // secondValue)
# elif result == 7:
#  print(firstValue ** secondValue)


 
# # exercise 2 # slicing a string till 180 character if it is more then it
# randomString = """lf you want to access the last character of a string in Python without knowing its length, you can use negative indexing, a feature that allows direct access to elements starting from the end of a sequence. In Python, the index -1 represents the last character of a string, -2 is the second-to-last,
#  and so on. This eliminates the need to calculate the length using the len() function"""
# print(len(randomString)) #385
# slicedString = randomString[0:180] #cutted string into 180 charcacter
# print(slicedString)


# exercise which print message according to the time

# import time
# currentTime = int(time.strftime('%H%M%S'))
# print(type(currentTime),currentTime)

# if(currentTime >= 500000 and currentTime <= 120000):
#   print('good morning sir')
# elif(currentTime >= 120000 and currentTime <= 1600000):
#   print('good afternoon sir')
# elif(currentTime >= 160000 and currentTime <= 200000):
#   print('good evening sir')
# else:
#   print('good night sir') 

# matching time with match statement
# import time
# currTime = int(time.strftime("%H"))
# print(currTime)

# match currTime:
#   case hour if hour >= 5 and hour <=12:
#     print("good morning") 
#   case hour if hour >= 12 and hour <=16:
#     print("good afternoon")
#   case hour if hour >= 16 and hour <=19:
#     print("good evening")
#   case _:
#     print("good night")    


# to print a table using for loop
# askedValue = int(input('enter the number : '))
# for number in range(1,11):
#   print(number * askedValue)

# *
# **
# ***
# ****
# *****
# starloop = 5
# for number in range(starloop + 1): #outer loop 
#   for innerNUmber in range(0,number + 1): #inner loop
#     print("*",end="")
#   print('')

# # printing table of given number
# askkedValue = int(input('given number is : '))
# for multiple in range(1,11):
#   print(f"{askkedValue} * {multiple} = {multiple * askkedValue}")


""" printing table using functions """
# def table_of_N(Given_number):
#   for multiple in range(1,11):
#     multiplication = multiple * Given_number
#     print(f"{Given_number} * {multiple} = {multiplication}")

# table_of_N(6)    


""" printing average of multiple numbers """

# def average(*numbers):
#   sum = 0
#   for i in numbers:
#     sum += i 
#   print(sum / len(numbers))

# average(4,6,11)    

"""                calculator using function          """


# def calculation():
#   num1 = int(input('enter first value: '))
#   num2 = int(input('enter second value: '))
#   print("1 = + , 2 = - " ,"\n3 = *, 4 = /, " ,"\n5 = %,6 = **, " ,"\n7 = //.",sep='~')  
#   operation_value = input('what operation should be performed: ')
#   if(operation_value == '+'):
#     return num1 + num2 
#   elif(operation_value == '-'):
#     return num1 - num2 
#   elif(operation_value == '*'):
#     return num1 * num2
#   elif(operation_value == '/'):
#     return num1 / num2
#   elif(operation_value == '**'):
#     return num1 ** num2
#   elif(operation_value == '%'):
#     return num1 % num2
#   elif(operation_value == '//'):
#     return num1 // num2


# result = calculation()  
# print(result)

'''using variable length argument '''
# def calculator(operation,*args):
#   if operation == 'add':
#     return sum(args)
#   elif operation == 'substract':
#     result = args[0]
#     for num in args[1:]:
#       result -= num    
#     return result
#   elif operation == 'multiple':
#     result = 1
#     for num in args[0:]:
#       result *= num
#     return result

#   elif operation == 'divide':
#     result = args[0]
#     for num in args[1:]:
#       result /= num  
#     return result


# operation = input('enter the operation: ').strip().lower()
# askedvalue = input('enter value: ').split(',')

# numbers = [int(num) for num in askedvalue]
# result = calculator(operation,*numbers)
# print(result)


"""   getting percent as per the subjects    """
# total_marks = 0
# total_sub = int(input('total value: '))

# for i in range(1,total_sub + 1):
#     mark = int(input(f"Enter the marks {i}: "))
#     total_marks += mark


# percentage = total_marks / total_sub


# print(f"The total marks are: {total_marks}")
# print(f"The percentage are: {int(percentage)}")


"""    leap year or not    """
# askedYear = int(input("Enter the year to check if it is a leap year or not: "))

# if askedYear % 4 == 0:
#     if askedYear % 100 == 0:
#         if askedYear % 400 == 0:
#             print('It is a leap year')
#         else:
#             print('It is not a leap year')
#     else:
#         print('It is a leap year')
# else:
#     print('It is not a leap year')


"""     largest amonst the three     """

# a = float(input('Enter three numbers :'))
# b = float(input('Enter three numbers :'))
# c = float(input('Enter three numbers :'))
# print(a,b,c)


# if a > b: 
#   if a > c: 
#     print("a is largest then both")
#   else:
#     print('c is largest then both')
# else:
#   if b > c:
#     print('b is largest then both')
#   else:
#     print('c is largest then both')      

'''   check if it is vowel or consonent    '''
# userValue  = input('enter the value : ')
# if(userValue == 'a' or userValue == 'e' or userValue == 'i' or userValue == 'o' or userValue == 'u'):
#   print(f'{userValue} is a vowel')
# else:
#     print(f'{userValue} is consonent')


""" sum of digit of a number   """
"""1st - using for loop"""
# userInput = input('enter values you want to add - ')
# emptyDigit = 0

# for num in userInput:
#   emptyDigit += int(num)
#   print(num,end=' ')

# print(f"\nthe sum of given digit is - {emptyDigit}")

"""     2nd - using while loop   """

# userInput1 = int(input('enter values - ')) #asking user input
# emptyDigit2 = 0                   #variable with empty integer
# while userInput1 > 0:             #check the user input is greater then 0
#   emptyDigit2 += userInput1 % 10  #taking the last value of the input and putting in empty variable 
#   userInput1 //= 10               #removing the last value from the user input    
#                                   #loop work till the last value is removed
# print(emptyDigit2)                #printing the values 


"""   asked value untill user type exit   """
# while True:
#   askedValue = input('enter values(type exit to exit) -')
#   if(askedValue == "exit"):
#     print('you exited the loop')
#     break



"""   factorial of n  """
"""1st - while loop"""
# num = int(input('enter a number - '))
# result = 1

# if (num < 0):
#   print('negative number')
# else:
#   while num > 1:
#    result *= num
#    num -= 1
# print(result) 



"""2nd for loop"""
# num1 = int(input('enter a number - '))
# result2 = 1
# if(num1 < 0):
#   print('negative number')
# else:
#   for i in range(1,num1 + 1):
#    result2 *= i
# print(result2)

# n = int(input('enter the value '))
# first = 0
# second = 1
# for i in range(n):
#   fibonacci = first + second 
#   first = second
#   second = fibonacci
#   print(fibonacci)  

""" kon banega crorepati """
# 1st  - list of questions  
# 2nd - list of options 
# 3rd -  list of answers
# 4th - list of questions place a question then compare the answers and choose the correct one 

questions = ['1. What is the correct way to define a tuple with one element?',
             '2. Are tuples mutable in Python?',
             '3. Which of the following is used to define a function in Python?',
             '4. What is the output of: print(2 ** 3)?',
             '5. What does the input() function do?']

options = [['A. t = (5)','B. t = [5]','C. t = (5,)','D. t = (5,5)'],
           ['A. NO','B. Yes','C. Depends on the version','D. If it contain lists'],
           ['A. function','B. define','C. def','D. func'],
           ['A. 6','B. 8','C. 4','D. 10'],
           ['A. shows output','B. Exits the program','C. Converts strings to integers','D. Reads a line from the user ']]

answers = ['C','A','C','B','D']

price = [1000,5000,10000,15000,20000]
money = 0
print('\nWelcome to the game 😊')
print('Your game has started')

for i in range(0,len(questions)):
  print(f'\nquestion for {price[i]} rs✨')
  print(questions[i])

  for j in options[i]:
    print(j)

  askValue = input('choose option between A-D💭- ').upper()

  if(askValue == answers[i]):
    print(f'\nYour answer is correct 🎉')
    money += price[i]
    print(f'You won {price[i]} rs')
    print(f'Your total amount is {money} rs')
  else:
    print('\nOps!😬, Your answer is incorrect, your game is over')
    print(f'\nthe correct answer was {answers[i]}')
    print(f'Your final amount is {money} rs')
    break



