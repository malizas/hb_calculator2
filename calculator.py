"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)


while True: 
    enter_input = input("enter your equation: ")

    input_list = enter_input.split(' ')

    if "q" in input_list:
        print("thanks for playing")
        break
    
    if len(input_list) <= 2:
        print("you need more inputs!")
        continue
        

    operator = input_list[0]
    num1 = input_list[1]

    if len(input_list) > 2:
        num2 = input_list[2]
    if len(input_list) > 3:
        num3 = input_list[3]

    if operator == "+":
        x = add(float(num1), float(num2))
    
    elif operator == "-":
        x = subtract(float(num1), float(num2))
    
    elif operator == "*":
        x = multiply(float(num1), float(num2))

    elif operator == "/":
        x = divide(float(num1), float(num2))
    
    elif operator == "square":
        x = square(float(num1))
    
    elif operator == "cube":
        x = cube(float(num1))
    
    elif operator == "pow":
        x = power(float(num1), float(num2))
    
    elif operator == "mod":
        x = mod(float(num1), float(num2))
    
    elif operator == "x+":
        x = add_mult(float(num1), float(num2), float(num3))
    
    elif operator == "c+":
        x = add_cubes(float(num1), float(num2))

    print(x)

        # create a while loop (done)
        # we need the user to input their equation (done)
        # tokenize/split up the input (done)
        # if the split input == "q", exit out of the loop (or program) (done)
        # if the split input == "+" then it will add (done)
        # if split input == "-" then it will subtract (and so on) (done)
