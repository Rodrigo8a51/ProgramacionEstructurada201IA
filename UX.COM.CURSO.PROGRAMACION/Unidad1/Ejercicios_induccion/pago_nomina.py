#
numero_horas = float(input("Ingrese el numero de horas trabajadas: "))
tarifa_horas = float(input("Ingrese la tarifa por horas: "))
nombre_empleados = (input("Ingrese el nombre del empleado: "))

# Las horas superiores a 35 se pagan extra
if numero_horas > 35:
    horas_extra = numero_horas -35
    pago_bruto = (35 * tarifa_horas) + (horas_extra * tarifa_horas * 1.5)
else:
    pago_bruto = numero_horas * tarifa_horas

# Calcular Impuestos
if pago_bruto <= 2000:
    impuesto = 0
elif pago_bruto <= 2000:
    impuesto = (pago_bruto - 2000) * 0.20
else:
    impuesto = (pago_bruto - 2200) * 0.30 + 220 * 0.20

pago_neto = pago_bruto - impuesto

#Mostrar resultados
print(f"Empleado:{nombre_empleados}")
print(f"Pago Bruto: ${pago_bruto}")
print(f"Impuesto: ${impuesto}")
print(f"Pago Neto: ${pago_neto}")