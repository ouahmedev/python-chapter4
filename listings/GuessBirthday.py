
day = 0
answer = eval(input("Is your birthday in Set1?\n" +
                    " 1  3  5  7\n" +
                    " 9 11 13 15\n" +
                    "17 19 21 23\n" +
                    "25 27 29 31\n" +
                    "Enter 0 for No and 1 for Yes: "))
if answer == 1:
    day += 1

answer = eval(input("\nIs your birthday in Set2?\n" + 
                    " 2  3  6  7\n" +
                    "10 11 13 15\n" +
                    "18 19 22 23\n" +
                    "26 27 30 31\n" +
                    "Enter 0 for No and 1 for Yes: "))
if answer == 1:
    day += 2

answer = eval(input("\nIs your birthday in Set2?\n" + 
                    " 4  5  6  7\n" +
                    "12 13 14 15\n" +
                    "12 21 22 23\n" +
                    "28 29 30 31\n" +
                    "Enter 0 for No and 1 for Yes: "))
if answer == 1:
    day += 4
    
answer = eval(input("\nIs your birthday in Set2?\n" + 
                    " 8  9 10 11\n" +
                    "12 13 14 15\n" +
                    "24 25 26 27\n" +
                    "28 29 30 31\n" +
                    "Enter 0 for No and 1 for Yes: "))
if answer == 1:
    day += 8
    
answer = eval(input("\nIs your birthday in Set2?\n" + 
                    "16 17 18 19\n" +
                    "20 21 22 23\n" +
                    "24 25 26 27\n" +
                    "28 29 30 31\n" +
                    "Enter 0 for No and 1 for Yes: "))   
if answer == 1:
    day += 16
    
# Display the birthday
print("Your birthday is", day)               