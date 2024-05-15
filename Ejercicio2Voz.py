import webbrowser

print("Bienvendio, Usuario")
dia=input("Ingrese un día de la semana ")

match (dia) :
    case "Lunes" :
        print ("Hoy debes, hacer ejercicio")
    case "Martes" :
        print ("Hoy debes, hacer las compras")
    case "Miércoles" :
        print ("Hoy debes, ver películas")
        print ("Deseas que te recomiende un canal???")
        tipoWeb = input("Dime Si o No")
        if tipoWeb == " Si " :
            webbrowser.open_new_tab("www.disneyplus.com")
    case "Jueves" :
        print ("Hoy debes, hacer los deberes")
    case "Viernes" :
        print ("Hoy debes, jugar fútbol")
    case _:
        print ("No existe actividad para ese día")