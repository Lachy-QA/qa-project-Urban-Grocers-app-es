# Proyecto Urban Grocers  
# El objetivo del Proyecto fue automatizar pruebas desde una lista de comprobación. 
# Para esto se utilizó apidoc como fuente de documentoación. 
# En el proyecto se trabajó con 4 archivos ".py". 
En "configuration.py" se escribieron las variables generales, 
en "data.py" se escribieron los bodies en formato json, 
en "sender_stand_request" se escribieron las solicitudes 
y en "create_kit_name_kit_test" se escribieron las validaciones (tanto positiva como negativa) y los test cases. 
# Durante la realización de la Lista de Comprobación se realizaron varias referencias entre archivos y librerías. 
Las solicitudes se realizaron con la librería request previamente instalada. 
Estas fueron la creación de un nuevo usuario y la de un kit para este, donde se verificó el campo "name" 
Las referencias se realizaron a través del comando "import". 
# La ejecución de las pruebas constó de lso siguientes pasos: 
i) Iniciar el servidor (o reiniciar) 
ii) Actualizar la url en "configuration.py" 
iii) Hacer clic en el triángulo verde a la izquierda de cada prueba (una a una) en "create_kit_name_kit_test.py" 
iv) En "create_kit_name_kit_test.py", seleccionar Current File 
v) Hacer clic correr
Cada vez que se requería de una acción se generó una función meduiante "def" y se utilizó el comando "retur" para que me devuelva el resultado de la función. 
A todas las pruebas se añadió el prefijo "test"
# Los resultados muestran que las pruebas de validación negativa fallaron. 
