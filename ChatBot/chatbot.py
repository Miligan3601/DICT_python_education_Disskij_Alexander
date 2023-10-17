
bot_name = "DICT_Bot"
print(f"Hello! My name is {GPT}.")
print(f"I was created in {2023}.")
print("Please, remind me your name.")
your_name = input()
print(f"What a great name you have, {Alex}!")
print("Let me guess your age.")
remainder3 = int(input("Enter remainder of dividing your age by 3: "))
remainder5 = int(input("Enter remainder of dividing your age by 5: "))
remainder7 = int(input("Enter remainder of dividing your age by 7: "))
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
number = int(input("Enter a positive number: "))
for i in range(number + 1):
    print(f"{i} !")
print("Completed, have a nice day!")
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
while True:
    answer = input("Enter the number of your answer: ")
    if answer == "2":
        break
    else:
        print("Please, try again.")
print("Congratulations, have a nice day!")