import math

def main():
    while True:
        try:
            v1 = int(input())
        except ValueError as e:
            v1 = 0
        operator = input()
        if not (operator in ["!", "x"]):
            try:
                v2 = int(input())
            except ValueError as e:
                v2 = 0
        if operator == "+":
            print(v1 + v2)
        elif operator == "-":
            print(v1 - v2)
        elif operator == "*":
            print(v1 * v2)
        elif operator == "/":
            print((v1 // v2) if (v2 != 0) else "Err")
        elif operator == "%":
            print((v1 % v2) if (v2 != 0) else "Err")
        elif operator == "!":
            print(math.factorial(v1) if (v1 >= 0) else "Err")
        else:
            print(v1)
            break

main()