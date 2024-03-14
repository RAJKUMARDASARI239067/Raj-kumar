# ! Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not


  # length= int(input())
  # breadth= int(input())
  # if lenght==breadth:
  #   print("its a square")
  # else:
  #    print("its not square")  


#  ! Eg: 4

# python program to check the wheather the
# given integer is a multiple of both 5 and 7

'''
 n=int(input("enter the the number")
 if n%5==0 and n%7==0:
    print("yes")
 else:
     print("no")

'''
'''
# Eg: 5
  write a program to accept the cost price of a bike and display the
  road tax to be paid
  according to the following criteria:

      Cost price (in Rs)                                         Tax
                                                                15 % + discount 6%
                                                                5%
      > 100000
      >50000 and <= 10000
      <= 50000

 price = int(input("enter the price:"))
 amoun= 0
 if price>=100000:
     dicount = price*(6/100)
     value = price-discount
     amount=value*(15/100)
     print(value+amount)

  else:
      tax = price*(5/100)
      total = price+tax
  print("The on road cost of bike is:",total)



# !------> if elif
# Eg:1
a = 7
b = 9
c = 3


 if a>b and a>c:
     print("A is greater")
  elif b>a and b>c:
      print("B is greater")
  elif c>a and c>b:
      print("c is greater")


# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - c
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

  mark = int(input("Enter mark:"))
  if mark>=80 and mark<=100:
      print("A")
  elif mark>=60 and mark<80:
      print("B")
  elif mark>=50 and mark<60:
      print("C")
  elif mark >=40 and mark<50:
      print("D")
  else:
      print("Fail")


# ! Eg:6
# ? Accept the age of 4 peaple and display the oldest one.

# ! ---> short hand if else
# Eg:1
  a = 9
  b = 60
# if a>b:
#     print("A")
# else:
#     print("B")
#? ---> using short hand if else
# * Rules
# 1.) statements inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else
# 3.) Always it have to end with else

# print("A") if a>b else print ("B")


# ! code to check the given char  is vowel or consonent
  char = input("Enter the char:")
# if char == ("a") or char == 'e' or char =='i' or char =='o' or char =='u':
#     print("is a vowel")
# else:
#     print("its consonent")

# ? or

# str1 = "aeiouAEIOU"
# if char in str1:
      print("vowel")
#  else:
#      print("consonent")

# ! shorthand if else
#  char = inpu("Enter the char:")
#  str1 = "aeiouAEIOU"
#  print("vowels") if char in str1 else print("consonenet")


# ! ---> elif ladder using shart hand if else
# Eg:1
# ? Find greter among 3 variables using short hand i else
   a = 8
   b = 5
   c = 9

   print("A is grater") if a>b and a>c else print("B is grater")
#  if b>a and b>c else print("C is greter")



# ! -------------> looping


# looping can be implemented  using
# for loop
# while  loop

# -----> for loop
# ?  for loop is used for itration,if we know the number of items  the loop haveto run
# ? It is used to iterate the iterables eg(string, list, tuple, ect....)


# todo -->  syntax for loop

# ! for syntax in c
#  for(i=0;<10;i++){
#      printf("hello");
#}

# ! for syntax in python
#  for userdefined_variable in range(start,end,step): default step value is 1
#      statement
#      statement
#      statement

# ? Eg:1
# To print the value from 1 to 10 using for loop

  for i in range(0,10): #(n, n-1)
      # print(i)
    print("hello")

#  ? Eg:2
   for val in range(1, 15, 2):
#       print(val)

#  for val in range(1, 15, 3):
#       print(val)


# ! Eg:3
#  to decrement the value


  for val in range(10,0,-1):
      print(val)
      

  for val in range(10,0,-2):
      print(val)
      
                   
 for val in range(10,0,1):
      print(val) # no output
'''

# ? Eg:4
# ! print the output of 7th multiplication table from 21 to 43


# for val in range(1,10+1):
# print( '7','x', val,'=',val*7)----> method :1


#------> method:2
#ans="7 x {} = {}"
#print(ans.formate(val,val*7))


# ---> method:3
#print(f"7 x {val}={val*7}")


# ? Eg:5
# break  ----> used to terminate the loop

  for val i  range(1, 10):
      if val ==6:
          break
        print(val)


# Eg:6

# for val i  range(1, 10):
       print(val)
      if val ==6:  
        break



# Eg:7

# for val i  range(1, 10):
       
# if val ==6:
        print(val)  
        break

# ! continue
# Eg:1
  for val in range(1,10):
   if val ==6:
       continue
    print(val)





















      
     
