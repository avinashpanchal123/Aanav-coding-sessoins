

# THIS CODE IS FOR MAKING A COFFEE 

# makeCoffee =>
#     1. take half cup of water
#     2. boil in
#     3. add one spoon of coffee
#     4. add half spoon of sugar
#     5. add half cup of milk
# makeCoffee()   




num1 = input("Enter Number 1: ")
num2 = input("Enter Number 2: ")
operator = input("Enter the operator : ")


num1 = int(num1)
num2 = int(num2)



if( operator == "+"):
  print(num1+num2)
elif( operator == "-"):
  print(num1-num2)
elif( operator == "*"):
  print(num1*num2)
else: 
  print(num1/num2)
