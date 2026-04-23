# Sistema de Presupuesto de Construcción
#  Objetivo
# Desarrollar un programa en Python que calcule el costo total de un proyecto de construcción y determine si está dentro del presupuesto.
# ________________________________________
#  Enunciado
# Una constructora necesita un programa para estimar el costo de un proyecto en base a materiales y mano de obra.
# El programa debe:
# 1.	Solicitar al usuario: 
# o	Nombre del proyecto 
# o	Cantidad de metros cuadrados a construir 
# o	Costo por metro cuadrado 
# o	Cantidad de trabajadores 
# o	Pago por trabajador 
# 2.	Definir las siguientes constantes: 
# o	IVA = 0.19 
# o	PRESUPUESTO_MAXIMO = 50000000 (50 millones) 
# 3.	Validar que todos los datos numéricos: 
# o	Sean números válidos 
# o	Sean mayores que 0
# En caso de error, manejar la situación con try-except. 
# 4.	Calcular: 
# o	Costo de materiales = metros cuadrados × costo por metro 
# o	Costo de mano de obra = trabajadores × pago por trabajador 
# o	Costo neto = suma de ambos 
# o	IVA aplicado 
# o	Costo total del proyecto 
# 5.	Usar variables auxiliares para almacenar cálculos intermedios. 
# 6.	Determinar el estado del proyecto: 
# o	Si el costo total es menor o igual al presupuesto → Dentro del presupuesto 
# o	Si supera el presupuesto hasta en un 10% → Presupuesto ajustado 
# o	Si supera en más de un 10% → Fuera de presupuesto 
# 7.	Mostrar un resumen con: 
# o	Nombre del proyecto 
# o	Costo total (redondeado a 2 decimales) 
# o	Estado del proyecto 
# ________________________________________
#  Condiciones
# •	Debe utilizar try-except para evitar errores de entrada. 
# •	Debe usar if, elif y else. 
# •	Debe definir y utilizar constantes correctamente. 
# •	El programa no debe terminar abruptamente ante errores.

try:
    nombre_proyecto = input("Ingrese nombre del proyecto: \n")
    m2 = float(input("Cantidad de metros cuadrados a construir: \n"))
    costo_m2 = float(input("Ingrese el costo por metro cuadrado: \n"))
    cant_trabajadores = int(input("Ingrese la cantidad de trabajadores: \n"))
    pago_trabajador = float(input("Ingrese el pago por trabajador: \n$ "))
    IVA = 0.19
    PRESUPUESTO_MAX = 50000000
    if m2 > 0 and costo_m2 > 0 and cant_trabajadores > 0 and pago_trabajador > 0:
        costo_mat = m2 * costo_m2
        costo_m_obra = cant_trabajadores * pago_trabajador
        costo_neto = costo_mat + costo_m_obra
        iva = costo_neto * IVA
        costo_total = costo_neto + iva
    else:
        print("valor no puede ser 0 o menor")
    redondeo_costo = round(costo_total,2)
    if costo_total <= PRESUPUESTO_MAX:
        estado = "Dentro del presupuesto"
    presupuesto_ajustado = (PRESUPUESTO_MAX * .10) + PRESUPUESTO_MAX
    if costo_total > PRESUPUESTO_MAX and costo_total < presupuesto_ajustado:
        estado = "Presupuesto Ajustado"
    if costo_total > presupuesto_ajustado:
        estado = "Fuera de presupuesto"
    
    print(f"Nombre del Proyecto : {nombre_proyecto}")
    print(f"Costo total: {redondeo_costo} ")
    print(f"Estado del Proyecto: {estado}")
except:
    print("Algún valor no es correcto")