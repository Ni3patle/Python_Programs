# Factorial :-

num = int(input("Enter Any Number : "))
fact = 1
for i in range(1,num+1):
  fact = fact * i
  
 print(f"Factorial of {num} :{fact}")
