# def CDT(usuario,capital,tiempo):
#     if tiempo > 2:
#         porcentaje_interes = 0.03  #3%
#         valor_interes = (capital * porcentaje_interes * tiempo)/12
#         valor_total = valor_interes + capital

#     else:
#         porcentaje_a_perder = 0.02 #2%
#         valor_a_perder = capital * porcentaje_a_perder
#         valor_total = capital - valor_a_perder
         
#     mensaje = "Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total)
    
#     return mensaje


# usuario = input("Ingrese su nombre de usuario: ")
# capital = int(input("Ingrese la cantidad de dinero con la cual desea abrir el CDT: "))
# tiempo = int(input("Ingrese el número de meses que desea mantener el CDT: "))

# print(CDT(usuario,capital,tiempo))



def CDT(usuario,capital,tiempo):
    if tiempo > 2:
        porcentaje_interes = 0.03  #3%
        valor_interes = (capital * porcentaje_interes * tiempo)/12
        valor_total = valor_interes + capital

    else:
        porcentaje_a_perder = 0.02 #2%
        valor_a_perder = capital * porcentaje_a_perder
        valor_total = capital - valor_a_perder
         
    mensaje = "Para el usuario " + usuario + " La cantidad de dinero a recibir, según el monto inicial " + str(capital) + " para un tiempo de " + str(tiempo) + " meses es: " + str(valor_total)
    
    return mensaje


#print(CDT("AB1012",1000000,3))
#print(CDT("ER6633",650000,2))



