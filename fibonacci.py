
terms = int(input("How many terms? "))

num1, num2 = 0, 1
total = 0

if terms <= 0:
   print("The entered number is a negative integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,)
   print(num1)
else:
   print("Fibonacci sequence:")
   while total< terms:
       print(num1)
       nth = num1 + num2
       num1 = num2
       num2 = nth
       total+=1