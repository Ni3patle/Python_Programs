# Sum of Digits of string:

str = input("Enter Any String Which Contains Digits : ")
sum = 0
for char in str:
  if char.isdigit():
    sum = sum + int(char)
print(f"Sum of Digits which are present in String : {sum} ")
