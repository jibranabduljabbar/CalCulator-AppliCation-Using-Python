num1 = int(input("Enter Your Num1: "))
operator = input("Enter Your Operator: ")
num2 = int(input("Enter Your Num2: "))
 
if operator == "+" : 
    print("Answer Is: ", num1 + num2)
elif operator == "-" : 
    print("Answer Is: ", num1 - num2)
elif operator == "*" : 
    print("Answer Is: ", num1 * num2)
elif operator == "/" : 
    print("Answer Is: ", num1 / num2)
elif operator == "%" : 
    print("Answer Is: ", num1 % num2)
else :
      print("Make a Mistake!")