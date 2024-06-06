1) Crear una lista de elementos de tipo numérico. Luego, mediante un ciclo `for` iterar esta lista e imprimir en la consola cada uno de los valores.
---
2) Crear un diccionario con 4 atributos. Debe tener datos de tipo:
- Numérico
- String
- List (array) de números
- bool

Luego, imprimir cada atributo de éste diccionario por separado, en la consola.

---
3) Crear una lista de diccionarios. Cada diccionario debe tener los siguientes atributos:

- Nombre --> string

- Apellido --> string

- Edad --> numero

- Lenguajes --> lista de strings

Luego, mediante un `for` recorrer cada elemento de la lista e imprimir en la consola sus valores.

---
4) Crear una función llamada `obtenerMayor` que reciba dos números y devuelva el mayor de los dos.
Luego, invocar a esta función pasándole dos numeros y mostrar el resultado en la consola.
Invocarla nuevamente con otros números para probar el otro caso de prueba.

---
5) Crear una función llamada `eliminarRepetidos` que reciba una lista y devuelva los elementos de ésta lista pero sin elementos repetidos.

Por ejemplo

`eliminarRepetidos([1,2,3,3,4,6,7,4,8])`

Debe devolver

`[1,2,3,4,6,7,8]`

---  
6) Crear una función que se llame `convertirALista` y reciba un string.
El string que recibe debe ser una serie de palabras, numeros o frases separadas por una coma (,).
La función debe devolver una lista de elementos con la información contenida entre cada separador (,).
Por ejemplo, si recibe:

`'hola, hoy es Jueves, 6/6/2024,19hs'`

debe devolver:

`['hola', ' hoy es Jueves', ' 6/6/2024', '19hs']`