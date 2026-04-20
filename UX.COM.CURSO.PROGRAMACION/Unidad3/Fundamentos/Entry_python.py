def pregunta_1():
    print(2**3**2)

def pregunta_2():
    x = 10 / 2
    """
    Type nos dice si es float / int (TIPO DE DATO)
    """
    print(type(x)) 


def pregunta_3():
    x = 1
    x=x
    print(x==x)

def pregunta_4():
    """
    El doble division nos da el numero entero no decimal
    """
    print(1 // 2 * 3)

def pregunta_5():
    """
    Primero se evalua la multiplicacion y de ahi suma
    """
    y = 2 + 3 * 5
    print(y)

def pregunta_6():
    """
    Concatenacion de cadenas
    """
    a='1'
    b='2'
    print(a+b)

def pregunta_7():
    """
    Devuelve el residuo de la division (En este caso 2)
    """
    z = 11 % 3
    print(z)

def pregunta_8():
    """
    El doble division nos da el numero entero no decimal
    """
    x = 5
    y = 2
    print(x // y)

def pregunta_9():
    v = 10
    v += 5 * 2
    print(v)

def pregunta_10():
    """
    bool("")Es False porque es una cadena vacia
    bool(" ")Es True porque es una cadena con un caracter 
    """
    print(bool(""),bool(" "),bool(0),bool(0.0))


def main():
    pregunta_1()
    pregunta_2()
    pregunta_3()
    pregunta_4()
    pregunta_5()
    pregunta_6()
    pregunta_7()
    pregunta_8()
    pregunta_9()
    pregunta_10()

if __name__=="__main__":
    main()