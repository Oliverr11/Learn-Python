# result = True and False
# print(result) #false

# result = True or False
# print(result) #true 

# result = not True
# print(result) #false     

# result = (5==5)
# print(result) #true 

# result = (5!=5)
# print(result) #false


# name = input("Enter Your Name : ")
# print("Welcome "+name+" to Python programming!")

# print(type(name))


# firstName = input("Enter Your First Name : ")
# secondName = input("Enter Your Second Name:")
# print("Welcome " + firstName + secondName + " to Python Programming!")

# myMentality = "John Wick " *3    
# print(myMentality)


# name = "Taing Sengkim"
# age = "18"

# print("\nHello, my name is {}. I'm {} years old!".format(name,age))

# greeting = f"\nHello , my name is {name}. I'am {age} years old!"
# print(greeting)

# age = input("Enter your age : ")

# if(int(age) >= 18):
#     print("You are allowed to watch this this movie")
# else:
#     print("Your are not allowrd to watch this movie!")

# import random
# num = random.randint(1,10)
# guesingNumber= input("Enter your guessing number : ")

# while guesingNumber.isdigit() and int(num) !=  int(guesingNumber):
#     guesingNumber = input("Wrong! Try again: ")
    
# if guesingNumber.isdigit():
#  print("Congrats! The number is " + guesingNumber) 
# else :
#  print("Please Enter Valid Number!") 

# print("Hello this is my first python class!")
# i=0
# while i <= 50 :
#     i+=1
#     print(i)

# for i in range(40,50):
#     print(i)


# first_name = "Taing"
# last_name = "Sengkim"
# print(f"{first_name} {last_name}")

# value_a = "50"
# value_b = "100"
# print(value_a + value_b)

# num1= 50
# num2= 100
# print(num2 + num1)

# message = "HELLO"
# print("\n"+message[0:2])
# print(message)
# print(message[2])
# print(message[:3])
# print(message[-5])

# a = 99
# b = 10
# print(a/b) 
# print(type(a/b)) #Flaot Division (/)

# print(a//b) 
# print(type(a//b)) #Integer Division (//)

# age = 25
# if age < 25:
#     print("age greater than 25")
# elif age == 25:
#     print("age equal 25")
# else:
#     print("age lower than 25")

# id = input("Enter Id : ")
# name = input("Enter name : ")
# age = input("Enter Age : ")
# print(f"ID : {id}\nName : {name}\nAge : {age}")

#input value A , input value B
#print (+,-,*,/,//)
# numA = float(input("Enter A : "))
# numB = float(input("Enter B : "))
# print(f"{numA} + {numB} = {numA + numB}")
# print(f"{numA} - {numB} = {numA - numB}")
# print(f"{numA} * {numB} = {numA * numB}")
# print(f"{numA} / {numB} = {numA / numB}")
# print(f"{numA} // {numB} = {numA // numB}")


# colors = input("Input color index (1-5) : ")
# match colors:
#     case "1" :
#         print("You're Choosing Blue")
#     case "2" :
#         print("You're Choosing Red")
#     case "3" :
#         print("You're Choosing Green")
#     case "4" :
#         print("You're Choosing Yellow")
#     case "5" :
#         print("You're Choosing Black")
#     case _:
#         print("Invalid index.")

# score = int(input("Input Score : "))
# match score:
#     case 12 | 11:
#         print(f"Great Score : {score}")
#     case 10| 9 | 8 :
#         print(f"Passed : {score}")
#     case _:
#         print(f"Failed : {score}")

# names = ["makara","both","rak","dara"] #list
# #for loop (iterator)
# for name in names:
#     print(name)
    
#1-100 (10,20,30...,100)
#for
# for num in range(0,100):
#     if num % 10 == 0:
#         print(num)
#while
# num =0 
# while num < 100 :
#     num+=1
#     if num % 10 != 0 :
#         print(num)
        
numbers = [] #list
print(type(numbers))

values = () #tuple
print(type(values))

students = {} #dict
print(type(students))

names = set() #set
print(type(names))


#mutable and immutable

print("============")

#immutable
age = 25
print(id(age))
age = age + 5 
print(id(age))

print("============")

#mutable
print(numbers)
print(id(numbers))
numbers.append(100)
print(numbers)
print(id(numbers))

numbers.append(200)
numbers.append(300)
print(numbers)
print(id(numbers))

print("============")

for num in numbers : 
    print(num)
    
print(numbers[0:2])