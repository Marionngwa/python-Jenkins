#write a script that will take two numbers and display the sum of the numbers
while True:
    try:
        num_1 = int(input("Please enter the first number: "))
        num_2 = int(input("Please enter the second number: "))
        
        total = num_1 + num_2
        print("The sum of the numbers is:", total)
        break  # Exit the loop if everything runs successfully
    except ValueError:  # Catch specific exceptions (like invalid input)
        print("Invalid input. Please enter valid numbers.")
