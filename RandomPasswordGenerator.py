import random

latter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','m','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%']

a_latter = int(input("Enter the number of latters:"))
a_number = int(input("Enter the number of numbers:"))
a_symbol  = int(input("Enter the number of symbols:"))
password = ""

for char in range(1, a_latter + 1):
  password += random.choice(latter)

for char in range(1, a_number + 1):
  password += random.choice(number)

for char in range(1, a_symbol + 1):
  password +=  random.choice(symbol)

random.shuffle(password)
print(password)

