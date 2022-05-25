def cliente(informacion):
    atracciones = {
        "X-Treme": {
            "atraccion": "X-Treme",
            "valor_boleta": 20000,
            "edad_ingreso": list(range(18,101)),
            "primer_ingreso": True,
            "descuento": 5
        },
        "Carros chocones": {
            "atraccion": "Carros chocones",
            "valor_boleta": 5000,
            "edad_ingreso": list(range(15,19)),
            "primer_ingreso": True,
            "descuento": 7
        },
        "Sillas voladoras": {
            "atraccion": "Sillas voladoras",
            "valor_boleta": 10000,
            "edad_ingreso": list(range(7,16)),
            "primer_ingreso": True,
            "descuento": 5
        }
    }

 
    if informacion["edad"] > 18:    # Ingresar a la atraccion "X-Treme"
        apto = True
        atraccion = atracciones["X-Treme"]["atraccion"]        
        if informacion["primer_ingreso"]==True:
            total_boleta = atracciones["X-Treme"]["valor_boleta"]*(1-(atracciones["X-Treme"]["descuento"]/100))
        else:
            total_boleta = atracciones["X-Treme"]["valor_boleta"]

    elif informacion["edad"] <= 18 and informacion["edad"] >= 15:   # Ingresar a la atraccion "Carros chocones"      
        apto = True
        atraccion = atracciones["Carros chocones"]["atraccion"]
        if informacion["primer_ingreso"]==True:
            total_boleta = atracciones["Carros chocones"]["valor_boleta"]*(1-(atracciones["Carros chocones"]["descuento"]/100))
        else:
            total_boleta = atracciones["Carros chocones"]["valor_boleta"]

    elif informacion["edad"] < 15 and informacion["edad"] >= 7:     # Ingresar a la atraccion "Sillas voladoras"
        apto = True
        atraccion = atracciones["Sillas voladoras"]["atraccion"]
        if informacion["primer_ingreso"]==True:
            total_boleta = atracciones["Sillas voladoras"]["valor_boleta"]*(1-(atracciones["Sillas voladoras"]["descuento"]/100))
        else:
            total_boleta = atracciones["Sillas voladoras"]["valor_boleta"]
        
    else:   # No ingresar a ninguna atracción , respuesta "N/A"
        apto = False
        atraccion = "N/A"
        total_boleta = "N/A"

   
    info_retorno = {
        "nombre": informacion["nombre"],
        "edad": informacion["edad"],
        "atraccion": atraccion,
        "apto": apto,
        "primer_ingreso": informacion["primer_ingreso"],
        "total_boleta": total_boleta
    }

    return info_retorno




info_cliente = {
    "id_cliente": 1,
    "nombre": "Tatiana Suarez",
    "edad": 15,
    "primer_ingreso": True
}

print(cliente(info_cliente))
