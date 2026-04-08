def factorial():
    factorial = 1
    i = 1
    n = int(input("Ingrese un número: "))
    while i <= n:
        factorial = factorial * i
        i = i + 1
    return factorial


def main():
    factorial_f = factorial()
    print(factorial_f)

if __name__=="__main__":
    main()
