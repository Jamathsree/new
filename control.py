# # if statement  & if else
# lastBall = 1
# if (lastBall==6):
#     print("Won t he match")
# else:
#     print("Lost the match")
# #  write a program to check even or odd
# a = int(input("Enter the number"))
# if (a%2==0):
#     print("Even number")
# else:
#     print("Odd number")
#
# # nested if : if inside another if
# # write a program to check whether a num i divided by both 2 and 4
# number = int(input("enter the number"))
# if (number%2==0):
#     if(number%4==0):
#         print("congrats divided by 2 and 4")
#     else:
#         print("sorry")
# else:
#     print("sorry")
#
# # if-elif ladder
# # program for btech admissions
# rank = int(input("Enter your Rank:"))
# if rank<=1000:
#     print("you got college1")
# elif rank>1000 and rank<=10000:
#     print("you got college2")
# elif rank>10000 and rank<=40000:
#     print("you got college 3")
# else:
#     print("you got no college")
#
# # for loop
# numberList = [1,2,3,4,5,30]
# for i in numberList:
#     print(i * 5)
# name = "Jamath"
# for Char in name:
#     print(Char)
#
# for i in range(10):
#     print(i)
# name = input('Enter your name:')
# # print(name[-2:])
# lastTwoChar = name[-2:]
# for i in range(1,11):
#     print(lastTwoChar*i)
# find vowels and constant
# name = input("Enter your name:")
# vowelsList= ['a','e','i','o','u']
# for char in name:
#     if char in vowelsList:
#         print(char)
#     else:
#         print(char, 'its is constant')
# write a program  100 to 1
# for item in range(100,0,-1):
#     print(item)
# write a program last 2 char from your name and repeat it frm 1 to 10
# name = input("Enter the name:")
# lastName = name[-2:]
# for char in range(1,11):
#     print(lastName*char)

# name = input("Enter the name:")
# vowellist = ['a','e','i','o','u']
# for char in name:
#     if char in vowellist:
#         print(char,'vowel')
# # to control loop we have 3 loop 1. break 2. continue
# name = input("Enter the name:")
# vowellist = ['a','e','i','o','u']
# for char in name:
#     if char in vowellist:
#         print(char, 'vowel')
#         continue
number = {1:'oone',2:'two',3:'three'}
for element in number:
    print(element)
    break
    print(number[element])

# marks = [50,67,40,90,30,98]
# sum = 0
# for mark in marks:
#     sum = sum + mark
#     print(sum)
i = 1
while i<=10:
    print(i)
    i = i+1
