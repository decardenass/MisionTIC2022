-- Consulta 1
SELECT ID_MaterialConstruccion AS ID, Nombre_Material AS NOMBRE,Precio_Unidad AS PRECIO 
	FROM MaterialConstruccion 
		WHERE Importado = 'Si'
			ORDER BY Nombre_Material;
-----------------------------------------------------------------------------------------		
-- Consulta 2
SELECT P.ID_Proyecto AS ID, P.Constructora, P.Ciudad, P.Clasificacion, T.Estrato AS Estrato, (L.Nombre||' '||L.Primer_Apellido||' '||L.Segundo_Apellido) AS LIDER
	FROM Proyecto P NATURAL JOIN Tipo T JOIN Lider L ON P.ID_Lider = L.ID_Lider
		WHERE P.Banco_Vinculado = 'Conavi'
			ORDER BY P.Fecha_Inicio DESC, P.Ciudad, P.Constructora;		
-----------------------------------------------------------------------------------------
-- Consulta 3
SELECT Ciudad, Clasificacion, COUNT(*) AS TOTAL, MIN(Fecha_Inicio) AS VIEJO, MAX(Fecha_Inicio) AS RECIENTE
	FROM Proyecto P GROUP BY Ciudad, Clasificacion
		HAVING Clasificacion <> 'Condominio' AND Clasificacion <> 'Casa Campestre';
-----------------------------------------------------------------------------------------
-- Consulta 4
SELECT P.ID_Proyecto AS ID_Proyecto, SUM(C.Cantidad*MC.Precio_Unidad) AS VALOR
	FROM Proyecto P NATURAL JOIN Compra C NATURAL JOIN MaterialConstruccion MC
		WHERE C.Pagado = 'No'
			GROUP BY P.ID_Proyecto
				HAVING VALOR>50000
					ORDER BY VALOR DESC;

-- Con subconsulta
SELECT Gasto.ID_Proyecto AS ID_Proyecto, Gasto.VALOR AS VALOR
	FROM (SELECT P.ID_Proyecto AS ID_Proyecto, SUM(C.Cantidad*MC.Precio_Unidad) AS VALOR
			FROM Proyecto P NATURAL JOIN Compra C NATURAL JOIN MaterialConstruccion MC
				WHERE C.Pagado = 'No'
					GROUP BY P.ID_Proyecto) AS Gasto
		WHERE Gasto.VALOR>50000
			ORDER BY Gasto.VALOR DESC;
-----------------------------------------------------------------------------------------
-- Consulta 5
-- Final
SELECT (L.Nombre||' '||L.Primer_Apellido||' '||L.Segundo_Apellido) AS LIDER, SUM(C.Cantidad*MC.Precio_Unidad) AS VALOR  
	FROM Proyecto P NATURAL JOIN Compra C NATURAL JOIN MaterialConstruccion MC JOIN Lider L ON P.ID_Lider = L.ID_Lider
		GROUP BY LIDER
			ORDER BY VALOR DESC
				LIMIT 10;