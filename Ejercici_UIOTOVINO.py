print("Asociación de ViniCultores")
tipo_uva = input("Ingrese que tipo de uva (A/B) ")
tamaño_uva = input("Ingrese el tamaño de la uva (1/2) ")
kilo= float(input("Ingrese el número de kilos producidos ")) 
valor_kilo = float(input("Ingrese el valor por kilo "))

if tipo_uva == "A" and tamaño_uva == "1" :
    precio_final = (valor_kilo*kilo) + .20
    print (f"El precio final por su uva es de {precio_final}")
elif tipo_uva == "A" and tamaño_uva == "2" :
    precio_final = (valor_kilo*kilo) + .30
    print (f"El precio final por su uva es de {precio_final}")
elif tipo_uva == "B" and tamaño_uva == "1" :
    precio_final = (valor_kilo*kilo) - .30
    print (f"El precio final por su uva es de {precio_final}")
elif tipo_uva == "B" and tamaño_uva == "2" :
    precio_final = (valor_kilo*kilo) - .50
    print (f"El precio final por su uva es de {precio_final}")
else:
    print ("Datos ingresados incorrectso, pruebe de nuevo")
