# Fibonacci Series :-

num = int(input("Enter Any Number : "))
n1 = 0
n2 = 1
count = 0

print("Fibonacci Series for Given Number :")

while(count < num):
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1