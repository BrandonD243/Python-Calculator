#PYTHON CALCULATOR
on = True

while on == True: #ENTIRE LOOP
    while True:
        operator = input("Enter an operator(+ - * /): ")
    
        if operator != "+" and operator != "-" and operator != "*" and operator != "/":
            print(f"{operator} is not a valid operator")
        else:
            break
    while True:
        nums = list(map(float, (input("Enter the numbers you want to calculate: ")).split()))
        if len(nums) < 2:
            print("You must enter at least 2 numbers.")
        else:
            break

    result = nums[0]

    if operator  == "+":
        for n in range(1, len(nums)):
            result += nums[n]
        print(f"The result is: {result}")

    elif operator  == "-":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        for n in range (1, len(nums)):
            result -= nums[n]
        print(f"The result is: {result}")

    elif operator  == "*":
        for n in range (1, len(nums)):
            result *= nums[n]
        print(f"The result is: {result}")

    elif operator  == "/":
        for n in range (1, len(nums)):
            result /= nums[n]
        print(f"The result is: {result}")
    
    while True:
        again = input("Would you like to perform another calculation? (Y/N) ")
        if again == "Y":
            break
        elif again == "N":
            on = False
            break
        else:
            print("Either enter 'Y' for Yes or 'N' for No")