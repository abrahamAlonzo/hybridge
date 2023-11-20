
print("Dame el número 1:")
firstNumber = input()

print("Dame el número 2:")
secondNumber = input()
if int(firstNumber) > int(secondNumber):
  print("Recibí el número {firstNumber} y {secondNumber}. El número mayor es {firstNumber}.".format(firstNumber=firstNumber, secondNumber=secondNumber))
elif int(firstNumber) == int(secondNumber):
  print("Recibí el número {firstNumber} y {secondNumber}. Los números son iguales ".format(firstNumber=firstNumber, secondNumber=secondNumber))
else:
  print("Recibí el número {firstNumber} y {secondNumber}. El número mayor es {secondNumber}. ".format(firstNumber=firstNumber, secondNumber=secondNumber))