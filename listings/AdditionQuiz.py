
import random
# Generate two integer numbers between 0 and 9
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Prompt the user to answer the question
answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

# Display the result
print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)

