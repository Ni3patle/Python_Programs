# Find Number is Prime Or Not :

num = int(input("Enter Any Number :"))

if num > 1:
    for i in range(2,num):
        if (num % i == 0) :
            print("Number is Not Prime")
            break
    else:
        print("Number is Prime")
else:
    print("Number is not Prime")