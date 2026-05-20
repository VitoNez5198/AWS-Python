Trabajo con tipos de datos compuestos
Información general sobre el laboratorio
Un tipo de datos compuesto es cualquier tipo de datos que comprende tipos de datos primitivos. Si le gusta la comida, puede imaginar un tipo de datos compuesto como si fuera turducken, un plato que consiste en pavo relleno con pato que, a su vez, está relleno con pollo. En este laboratorio, creará un tipo de datos que consiste en una cadena que está en un diccionario y que, a su vez, se encuentra en una lista.

En este laboratorio, deberá realizar lo siguiente:

utilizar tipos de datos numéricos
utilizar tipos de datos de texto (cadena o string)
utilizar el tipo de dato de diccionario
utilizar el tipo de dato de lista
utilizar un bucle for
utilizar la función print()
utilizar la instrucción if
utilizar la instrucción else
utilizar la instrucción import
Tiempo de finalización estimado
45 minutos

Acceso al IDE de AWS Cloud9
Para activar el entorno de su laboratorio, desplácese hasta la parte superior de estas instrucciones y seleccione Start Lab (Iniciar laboratorio).

Se abrirá el panel Start Lab (Iniciar laboratorio), donde se muestra el estado del laboratorio.

Espere hasta que aparezca el mensaje Lab status: ready (Estado del laboratorio: listo) y, a continuación, para cerrar el panel Start Lab (Iniciar laboratorio), haga clic en la X.

En la parte superior de estas instrucciones, elija AWS.

AWS Management Console se abrirá en una pestaña nueva del navegador. El sistema iniciará la sesión de forma automática.

Nota: Si no se abre una pestaña nueva del navegador, generalmente aparece un anuncio o un icono en la parte superior de este, el cual indica que el navegador no permite que se abran ventanas emergentes en el sitio. Haga clic en el anuncio o en el icono, y elija Allow pop ups (Permitir ventanas emergentes).

En AWS Management Console, elija Services (Servicios) > Cloud9. En el panel Your environments (Sus entornos), busque la tarjeta reStart-python-cloud9 y elija Open IDE (Abrir IDE).

Se abre el entorno de AWS Cloud9.

Nota: Si se abre una ventana emergente con el mensaje .c9/project.settings have been changed on disk (Se ha modificado la configuración de .c9/project. en el disco), elija Discard (Descartar) para ignorarlo. Del mismo modo, si una ventana de diálogo le pide que Show third-party content (Muestre contenido de terceros), elija No para rechazar la indicación.

Creación del archivo de ejercicio de Python
En la barra de menú, elija File > New From Template > Python File (Archivo > Nuevo a partir de plantilla > Archivo en Python).

Esta acción crea un archivo sin título.

Elimine el código de muestra que obtiene del archivo de plantilla.

Elija File > Save As... (Archivo > Guardar como...), proporcione un nombre adecuado para el archivo de ejercicio (por ejemplo, composite-data.py) y guárdelo en el directorio /home/ec2-user/environment.

Acceso a la sesión del terminal
En su IDE de AWS Cloud9, elija el icono + y seleccione New Terminal (Nuevo terminal).

Se abre una sesión de terminal.

Para ver el directorio en el que está trabajando actualmente, escriba pwd. Este comando lleva a /home/ec2-user/environment.

En este directorio, localice el archivo que creó en la sección anterior.

Creación de datos de un inventario de vehículos
Valores separados por comas (CSV) es un formato de archivo que se utiliza para almacenar datos tabulares, como los datos de una hoja de cálculo. Trabajará con el archivo CSV del siguiente bloque.

En la barra de menú, seleccione File > New File (Archivo > Archivo nuevo).
Esta acción crea un archivo sin título.

Elija File > Save As… (Archivo > Guardar como…) y guarde el archivo como car_fleet.csv.

Copie y pegue el siguiente bloque de texto en el archivo car_fleet.csv y guarde el archivo.

vin,make,model,year,range,topSpeed,zeroSixty,mileage
TMX20122,AnyCompany Motors, Coupe, 2012, 335, 155, 4.1, 50000
TM320163,AnyCompany Motors, Sedan, 2016, 240, 140, 5.2, 20000
TMX20121,AnyCompany Motors, SUV, 2012, 295, 155, 4.7, 100000
TMX20204,AnyCompany Motors, Truck, 2020, 300, 155, 3.5, 0
Sugerencia: Si se abre una ventana emergente con el mensaje Native Clipboard Unavailable (Portapapeles nativo no disponible), utilice el teclado, no el menú del navegador, para realizar acciones de copiar y pegar. Por ejemplo, en Windows, utilice CTRL+C y CTRL+V para copiar y pegar, respectivamente. En Mac, utilice Command+C y Command+V.

Creación de un programa de inventario de vehículos
Definición del diccionario
Leerá el archivo a través de un módulo denominado csv. Además, realizará una copia profunda de los datos para almacenarlos en la memoria mediante un módulo denominado copy.

En el panel de navegación del IDE, elija el archivo .py (haga doble clic sobre este) que creó en la sección anterior, Creación del archivo de ejercicios de Python.

Primero, importe los módulos que utilizará:

import csv
import copy
A continuación, defina el diccionario que funcionará como tipo compuesto para leer los datos tabulares:
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
Utilizará un bucle for para recorrer las claves y valores del diccionario.
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
Nota: La función items () pertenece al tipo de datos de diccionario. La función items() indica al bucle for que recorra la colección que pertenece al tipo de datos de diccionario.

Defina una lista vacía para almacenar el inventario de vehículos que leerá:
myInventoryList = []
Guarde el archivo.
Copia del archivo CSV en memoria
Leerá los datos del disco (disco duro) y realizará una copia en memoria (memoria de acceso aleatorio o RAM). En una computadora, se utiliza un disco duro para almacenar los datos a largo plazo, incluso cuando se apaga la alimentación. La sigla RAM hace referencia a la memoria temporal, que es más rápida, pero se borra cuando se apaga la alimentación de la computadora.

Se le presentará la instrucción de sintaxis with open, que mantiene un archivo abierto mientras lee datos. Cerrará automáticamente el archivo CSV cuando termine de ejecutarse el código dentro del bloque with.

También utilizará una nueva manera de formatear una cadena. En lugar de utilizar comillas dobles y .format para pasar las variables, puede utilizar comillas simples y escribir las variables entre los símbolos “{}”.

Por último, csv.reader() es una función existente en la biblioteca csv, que ya ha importado con la instrucción import csv.

Debería estar familiarizado con la mayor parte del resto del código.

Ahora, regrese al archivo en Python:

Escriba el siguiente código:
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
Aunque este código parece una gran cantidad de código para procesar, en su mayoría comprende instrucciones que vio en laboratorios anteriores. Contiene un bucle for con una instrucción if-else, seguido de una instrucción print() al final.

Sin embargo, la siguiente línea necesita una explicación adicional:

currentVehicle = copy.deepcopy(myVehicle)
De forma predeterminada, Python realiza una copia superficial de tipos de datos complejos. Una copia superficial hace referencia o apunta a la ubicación del almacenamiento de la variable de diccionario myVehicle. Sin esta línea, contaría solo con una única caja de almacenamiento y solo el último elemento de la lista se copiaría en memoria. Esta línea garantiza que se creen nuevas cajas de almacenamiento en memoria para almacenar los nuevos datos tabulares que se están leyendo.

Impresión del inventario de vehículos
Finalizará el script de Python mostrando el inventario de automóviles de la variable myInventoryList.

Regrese al script en Python y escriba el siguiente código:
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")
Guarde el archivo.

Elija el botón Run (Ejecutar) en la barra de menú para ejecutar el programa.

Confirme que el script se ejecuta de forma correcta y que la salida se muestra según lo previsto.

Revise una vez más el código que lee los datos tabulares del archivo CSV. Comprender esta sección del código es fundamental para este ejercicio.

¡Felicitaciones! Ha trabajado con tipos de datos compuestos en Python.

Finalizar laboratorio
 ¡Felicitaciones! Ha llegado al final del laboratorio.

Elige  End Lab (Finalizar laboratorio) en la parte superior de esta página y, a continuación, selecciona Yes (Sí) para confirmar que deseas finalizar el laboratorio.
Un panel muestra el mensaje DELETE has been initiated… You may close this message box now (Se ha iniciado la ELIMINACIÓN… Ya puedes cerrar este mensaje).

Aparece brevemente el mensaje Ended AWS Lab Successfully (El laboratorio de AWS finalizó correctamente), que indica que el laboratorio ha finalizado.​
Recursos adicionales
Para obtener más información sobre AWS Training and Certification, consulte https://aws.amazon.com/training/.

Sus comentarios son bienvenidos y valorados. Si desea compartir alguna sugerencia o corrección, proporcione los detalles en nuestro Formulario de contacto de AWS Training and Certification.

© 2022 Amazon Web Services, Inc. y sus empresas afiliadas. Todos los derechos reservados. Este contenido no puede reproducirse ni redistribuirse, total ni parcialmente, sin el permiso previo por escrito de Amazon Web Services, Inc. Queda prohibida la copia, el préstamo o la venta de carácter comercial.

 
 
< Rubric: 6 - Tipos de datos compuestos | Points: 0 >


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17