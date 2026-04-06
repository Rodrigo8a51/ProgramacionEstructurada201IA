def factorial():
    n = int(input("Ingrese un número: "))

    factorial = 1
    i = 1
    while i <= n:
        factorial = factorial * i
        i = i + 1
    return factorial

def main():
    factorial_f = factorial()
    print(factorial_f)

if __name__=="__main__":
    main()
