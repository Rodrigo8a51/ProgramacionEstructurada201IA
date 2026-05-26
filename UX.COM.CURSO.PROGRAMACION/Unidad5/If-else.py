def odd_even (number):
    if number % 2 == 1:
        return "Weird"
    else:
        if 2 <= number < 5:
            return "Not Weird"
        elif 6 <= number <= 20:
            return "Weird"
        else:
            return "Not Weird"

def main():
    n = int(input("Ingrese un número entero: "))
    result = odd_even(n)
    print(result)
    
    

if __name__ == "__main__":
    main()