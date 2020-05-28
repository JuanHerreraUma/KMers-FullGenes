# Kmers-FullGenes
### Juan Antonio Herrera Conde

# Objetivos

En este segundo proyecto, vamos a codificar un programa cuya función será contar los kmers de una secuencia de nucleótidos, hallando así la frecuencia relativa de cada uno de ellos. El programa mostrará al usuario una interfaz para que pueda elegir el tamaño “k” del kmer. Para los ejemplos, hallaré los dipéptidos de la secuencia. Vamos a resolver el problema usando el genoma completo del “Homo Sapiens” que se nos dio en clase, así nos enfrentamos a un problema real. A la hora de hacer pruebas durante su codificación, usé el gen número 20 de los cromosomas humanos, ya que el tiempo de computación del genoma completo es demasiado arduo de computar en cuanto a lo que a tiempo se refiere. En esta memoria, sí usaré el ejemplo del genoma completo, hallando la frecuencia relativa de todos los kmers de tamaño 2. Para saber el número total de posibles dipéptidos que tendremos, usaremos la fórmula de 4𝑘, en la que k es el tamaño del kmer. Si elevamos cuatro al cuadrado, obtenemos dieciséis posibilidades, que equivalen al número de posibles kmers que tendremos.

# Secciones del programa

Todas las secciones del código se muestran en el mismo fichero de Python, ya que no es necesario crear diferentes clases y ahorramos memoria y tiempo de implementación sin importar unas en otras. Principalmente, el código se divide en tres partes diferenciadas. En la primera, leeremos el formato fasta del genoma completo, para quedarnos sólo con los nucleótidos, y poder leer su longitud total. La segunda parte del programa será una definición de un método para archivar la frecuencia relativa del conjunto de los 16 posibles kmers que encontremos. En la tercera parte, invocaremos a la interfaz para que el usuario pueda introducir manualmente el tamaño del kmer (en este caso, serán dipéptidos). Invocaremos al método llamado a la secuencia fasta ya leída, y ordenaremos los resultados en una lista.

## Primera parte - Lectura Fasta

En mi caso, he usado el fasta del genoma completo del Homo Sapiens. Este programa es válido para cualquier fasta, siempre que se introduzca su nombre en la función open. Codificaremos unas líneas de código para leer el formato fasta. Abriremos el archivo del genoma del Homo Sapiens y lo leeremos con la función x.read(). Le diremos al programa que lea desde el carácter 113, que es la línea que equivale a la descripción del genoma, y no nos interesa, sólo buscamos los nucleótidos. A continuación, reemplazaremos todos los gaps por espacios, y asociaremos este código a la variable “lectura”. A continuación, imprimiremos la longitud de la secuencia de nucleótidos completa.

## Segunda parte - Definición del Método

Definiriremos un método para contener las frecuencias relativas de los dipéptidos. En primer lugar, crearemos un diccionario, al que llamaremos KFreq. A continuación, usando un bucle for, recorreremos todos los dipéptidos del genoma, estableciendo el tamaño a partir del atributo k. Recorreremos todos los kmers de tamaño dos. Si encontramos uno nuevo, lo albergamos en el diccionario, y si ya lo teníamos en este, añadiremos su frecuencia relativa.

## Tercera parte - Interfaz

En esta parte del código, crearemos el parámetro n para que el usuario pueda decidir el tamaño de los kmers que busque el método previamente mencionado. Introduciremos todos los kmers en una lista, para lograr una impresión por pantalla más limpia.
