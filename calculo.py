#Cálculo de la distancia mínima requerida para trabajar en altura según Compañía Minera Zaldivar 
#Basado en la actual normativa Nch. 1258 y Guía del ISP - SPDC


anclaje = input('Ingrese la altura del anclaje: ')
largoCola = input('Ingrese el largo de la cola: ')
largoAmortiguador = input('Ingrese el largo del amortiguador de impacto: ')
estaturaTrabajador = input('Ingrese su estatura: ')
margenSeguridad = input('Ingrese el margen de seguridad segun Nch 1258: ')


alturaAnclaje = float(anclaje)
primerNumero = float(largoCola)
segundoNumero = float(largoAmortiguador)
tercerNumero = float(estaturaTrabajador)
margenSeguridad = float(margenSeguridad)

resultado = (alturaAnclaje - primerNumero - segundoNumero - tercerNumero - margenSeguridad)

print(resultado)

if resultado > 0: print('Su altura de trabajo es segura')
else:
    print('¡Advertencia! su altura no es segura para trabajar')
