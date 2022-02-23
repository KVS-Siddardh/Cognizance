a = int(input("enter the number:"))
initial= a
rev= 0
while(a>0):
  b= a%10
  rev= 10*rev+ b
  a= a//10
  
if rev == initial:
  print("it is a palindrome")
  
else:
  print("it is not a palindrome")