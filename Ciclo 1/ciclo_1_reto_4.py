def ordenes(rutinaContable):
    ordenTotal = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2] , x[1:])) , rutinaContable))
    a = list(map(lambda x: x[0], ordenTotal))
    b = list(map(lambda x: round(sum(x[1:]) , 2) , ordenTotal))
    lista_zip = list(map(list,list(zip(a, b))))
    lista_final = list(map(lambda x: x if x[1]>= 600000 else [x[0] , x[1]+25000]  , lista_zip))
    print("------------------------ Inicio Registro diario ---------------------------------")
    for i in range(len(lista_final)):
        mensaje = "" + "La factura {numero} tiene un total en pesos de {cantidad:,.2f}".format(numero = lista_final[i][0] , cantidad = lista_final[i][1])
        print(mensaje)
    print("-------------------------- Fin Registro diario ----------------------------------")