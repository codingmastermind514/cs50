def main():
    # prompt the user for an expression in the format x y z where x and z are int and y is an operation
    expression = input("Expression: ").split(" ")

    # identify x, y, z from split list
    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])

    # result is currently 0
    result = 0

    # checking y is which operation
    match y:
        case '+':
            result = x+z
        case '-':
            result = x-z
        case '*':
            result = x*z
        case '/':
            result = x/z

    # floating the result
    new = float(result)

    # rounding to 1 decimal place
    print(round(new,1))

main()
