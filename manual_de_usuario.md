# Manual de Usuario PetWorld Manager
## Lenguajes Formales y de Programación B-
### Primer Semestre 2024
```js
Universidad San Carlos de Guatemala
Facultad de Ingeniería
Nombre: Angely Lucrecia García Martínez
Carne: 202210483
```
---
## Descripción del Proyecto
PetWorld Manager es una aplicación diseñada para la gestión y cuidado de mascotas virtuales de una manera sencilla y divertida. Con esta herramienta, el usuario podrá crear, alimentar, jugar y monitorear el estado de tus mascotas, todo desde la comodidad de tu ordenador.
La aplicación permite realizar diversas acciones mediante comandos ingresados en un archivo con extensión .petmanager, lo que facilita su uso y personalización. Desde la creación de mascotas hasta el seguimiento de su estado general, PetWorld Manager brinda una experiencia completa de cuidado de mascotas en un entorno virtual con el fin de inculcar valores de cuidado y responsabilidad en la tenencia de mascotas.

## Objetivos
* Objetivo General
    * Proporcionar a los usuarios una guía detallada y comprensible sobre cómo utilizar todas las funciones y características de la aplicación. El manual está diseñado para facilitar el aprendizaje y la utilización eficiente de PetWorld Manager, permitiendo a los usuarios gestionar y cuidar a sus mascotas virtuales de manera efectiva.
* Objetivos Específicos
    * Proporcionar instrucciones paso a paso sobre cómo utilizar cada función de la aplicación, desde la creación de mascotas hasta la generación de informes y gráficos.
    * Detallar el propósito de cada comando utilizado en PetWorld Manager, incluyendo ejemplos prácticos para una comprensión clara.

## Desarrollo del Manual de Usuario
### Menú Principal
En esta sección, se mostrará la información de la programadora y se desplegará un menú con dos opciones, el usuario deberá ingresar el número según la acción que quiera realizar y presionar Enter para continuar.


![INVCLASS](https://i.ibb.co/5rWZSR2/image.png)

### Menú PetManager
En este menú, se mostrarán dos opciones a escoger como Cargar archivo y Salir. La primera opción pedirá al usuario ingresar el nombre del archivo que contiene los comandos de las mascotas y la segunda opción es "Salir" la cual finalizará la ejecución de la aplicación.

![INVCLASS](https://i.ibb.co/H7kB5D5/image.png)

Para poder cargar el archivo, ingresamos la opción 1 y luego el sistema pedirá que se ingrese el nombre del archivo a leer. Este debe tener el siguiente formato [nombre del archivo].petmanager; Es importante recalcar que este archivo debe de estar dentro de la carpeta de la aplicación para que el sistema pueda leerlo.

![INVCLASS](https://i.ibb.co/qrmzGqR/image.png)

## Archivo .petmanager
### Comandos a ejecutar
### Crear Gato
El comando Crear_Gato se utiliza en PetWorld Manager para agregar una nueva mascota de tipo gato al sistema. Este comando permite al usuario introducir el nombre de la mascota que desea crear, lo que da inicio a la existencia virtual de una nueva mascota.

El formato que deberá tener este comando es el siguiente:


**Crear_Gato:\<nombre\>**


Por ejemplo

Crear_Gato:Micifuz

![INVCLASS](https://i.ibb.co/bKgsR9z/image.png)


### Dar de Comer
El comando Dar_de_Comer se utiliza en PetWorld Manager para alimentar a una mascota gato y aumentar su nivel de energía. Este comando simula el momento en que un gato se alimenta de un ratón, el cual tiene cierto peso tomando en cuenta que cuando el gato come, su energía aumenta en 12 joules + el peso del ratón en gramos.

El formato de este comando debe ser:


**Dar_de_Comer:\<nombre\>,<peso\>**


Por ejemplo


Dar_de_Comer:Micifuz,140

![INVCLASS](https://i.ibb.co/HB7jm3p/image.png)

### Jugar
El comando Jugar se utiliza en PetWorld Manager para simular la interacción del usuario con una mascota gato, proporcionándole entretenimiento y actividad física. Este comando permite que la mascota realice una sesión de juego, durante la cual perderá energía gradualmente debido al esfuerzo físico. Se debe considerar que el tiempo siempre se cuenta en minutos y por cada minuto transcurrido, su energía disminuye en 0.1 Joules. El tiempo debe ser un valor de tipo entero.

El formato de este comando debe ser:


**Jugar:\<nombre\>,<tiempo\>**


Por ejemplo


Jugar:Micifuz,20

![INVCLASS](https://i.ibb.co/0F7v7yk/image.png)

### Resumen Mascota
El comando Resumen_Mascota en PetWorld Manager se utiliza para obtener información detallada sobre una mascota gato específica. Proporciona un resumen completo del estado actual de la mascota, incluyendo su nivel de energía y su estado de vida.

El formato de este comando debe ser:


**Resumen_Mascota:\<nombre\>**


Por ejemplo


Resumen_Mascota:Micifuz

![INVCLASS](https://i.ibb.co/hmyPNzd/image.png)

### Resumen Global
El comando Resumen_Global en PetWorld Manager se utiliza para obtener un resumen general del estado actual de todas las mascotas gato registradas en el sistema. Proporciona una visión global de la energía y el estado de vida de cada mascota.

El formato de este comando debe ser:


**Resumen_Global**

![INVCLASS](https://i.ibb.co/nBBTvzn/image.png)

## Estado del Gato
En el sistema PetWorld Manager, el estado de vida de un gato puede ser "vivo" o "muerto", y este estado se determina en función de su nivel de energía. Cuando se crea un nuevo gato, este tendrá una energía de 1 Joules. El estado vivo o muerto se actualiza dinámicamente según las acciones realizadas sobre la mascota, como alimentarla, jugar con ella o el paso del tiempo. 

* Determinación del Estado
    * Cuando la energía de un gato cae a cero o menos, se considera "muerto". Esto puede suceder si el nivel de energía disminuye debido a la falta de alimentación o el agotamiento por jugar.
    * Si la energía de un gato se mantiene por encima de cero, se considera "vivo".

* Actualización del Estado
    * Cada vez que se realiza una acción que afecta la energía del gato, como alimentarlo o jugar con él, el sistema verifica si la energía restante es suficiente para mantener al gato "vivo".
    * Si la energía cae a cero o menos, el estado del gato se cambia automáticamente a "muerto".
    * Si la energía se mantiene por encima de cero, el estado del gato permanece como "vivo".

* Implicaciones del Estado:
    * Un gato "vivo" puede seguir interactuando con el usuario, como jugar o recibir alimentación.
    * Un gato "muerto" no puede participar en ninguna actividad adicional y se considera fuera de juego en el sistema.

## Archivo .petmanager_result
Luego de que el sistema realice la lectura del archivo .petmanager, creará un archivo .petmanager_result en el cual se imprimen los comandos que pudo leer en el archivo ingresado. Imprimirá la fecha y hora en que ejecutó cada uno de los comandos, así como un mensaje que la mascota puede emitir según el tipo de comando que haya realizado.

![INVCLASS](https://i.ibb.co/tLMNTbh/image.png)

## Gráfico
El gráfico es generado por PetWorld Manager cuando el sistema lee el comando Resumen_Globa. Este gráfico proporciona una representación visual de las mascotas virtuales y su estado actual.
### Elementos del gráfico
* Nodos para Cada Mascota:
    * Cada mascota en el sistema se representa como un nodo en el gráfico.
    * El nombre de la mascota se muestra en el centro del nodo.

* Detalles de la Mascota:
    * La información importante sobre cada mascota se muestra en nodos secundarios conectados al nodo principal de la mascota.
    * Hay tres nodos secundarios:
        * Nodo de Energía: Muestra el nivel de energía actual de la mascota.
        * Nodo de Tipo: Indica el tipo de mascota, en este caso, "Gato".
        * Nodo de Estado: Muestra si la mascota está "Viva" o "Muerta".

* Funcionalidad del Gráfico:
    * El gráfico proporciona una visión general rápida del estado actual de todas las mascotas en el sistema.
    * Permite a los usuarios identificar fácilmente qué mascotas están vivas y cuáles están muertas, así como su nivel de energía actual.
    * Facilita el seguimiento del bienestar y la salud de las mascotas a lo largo del tiempo, lo que ayuda a tomar decisiones informadas sobre su cuidado y gestión.

![INVCLASS](https://i.ibb.co/yy4LDM1/image.png)