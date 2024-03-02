# Manual Técnico PetWorld Manager
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
El proyecto PetWorld Manager es una aplicación de gestión de mascotas virtuales desarrollada para brindar a los usuarios una experiencia interactiva y divertida al cuidar de sus propias mascotas en un entorno digital. Esta aplicación permite a los usuarios crear, alimentar, jugar y monitorear el estado de sus mascotas virtuales a través de una interfaz de línea de comandos.

## Objetivo
El manual técnico proporciona una guía detallada para desarrolladores, administradores de sistemas y otros usuarios técnicos sobre cómo instalar, configurar y utilizar el PetWorld Manager. Contiene información sobre la estructura del código, las dependencias del proyecto, las instrucciones de implementación, y la explicación de los diferentes componentes y su funcionamiento.

El manual técnico está diseñado para ofrecer una referencia completa para aquellos que deseen comprender el funcionamiento interno del sistema, realizar personalizaciones o contribuir al desarrollo continuo del proyecto.

## Características Principales
* Creación de Mascotas: Los usuarios pueden crear nuevas mascotas proporcionando un nombre único para cada una.

* Alimentación: Las mascotas pueden ser alimentadas utilizando el comando "Dar_de_Comer", lo que aumenta su nivel de energía.

* Juego: Los usuarios pueden interactuar con sus mascotas jugando con ellas, lo que afecta su nivel de energía.

* Resumen Individual de Mascotas: Se proporciona un resumen detallado de cada mascota, que incluye su nombre, nivel de energía y estado (vivo o muerto).

* Resumen Global: Se genera un resumen global que muestra el estado actual de todas las mascotas en el sistema.

* Generación de Gráficos: Se genera un gráfico visual que representa el estado de todas las mascotas y sus detalles asociados.

## Tecnologías utilizadas
* Python: El proyecto está desarrollado principalmente en Python, aprovechando las bibliotecas nativas para implementar la funcionalidad requerida.

* Graphviz: Se utiliza la biblioteca Graphviz para generar gráficos visuales que representan las mascotas y su estado.

## Requisitos del sistema
* Python instalado en el sistema.
* Sistema operativo compatible con Python.

## Instalación
Debido a que es una aplicación que se ejecuta en consola, se debe clonar o descargar el repositorio del proyecto desde [Github](https://github.com/angelygm03/LFP_S1_2024_Practica_202210483.git) para luego abrir el proyecto en el IDE de su preferencia (se recomienda Visual Studio Code) y correr la aplicación.

## Estructura del Proyecto
El proyecto sigue una estructura de directorios típica de Python
* PetWorld Manager
    * main.py: Script principal para ejecutar la aplicación.
        * pet_manager.py: Contiene la implementación de la clase PetManager, que gestiona todas las funcionalidades del proyecto.
            * mascotas.petmanager_result: Archivo de salida que almacena los resultados de las operaciones realizadas por el usuario.
                * [nombre del archivo].petmanager: Archivo de entrada que almacena los comandos a ejecutar
                * image.png: Archivo de imagen que contiene los gráficos generados por el comando Resumen Global

## Bibliotecas utilizadas
* graphviz: Para la generación de gráficos visuales, en este proyecto se utiliza Graphviz para generar un diagrama que visualiza la información de cada mascota, incluyendo su nombre, energía y estado (vivo o muerto).

![INVCLASS](https://i.ibb.co/KLtcw80/image.png)


* Otras bibliotecas nativas de Python como:
    * os: permite limpiar la pantalla en la consola

    ![INVCLASS](https://i.ibb.co/9qG8B2d/image.png)

    * re: se utiliza para buscar patrones específicos en cada línea del archivo, como los separadores de comandos (:) y parámetros (: y ,). Esto permite dividir correctamente cada línea en partes que representan los comandos y sus argumentos.

    ![INVCLASS](https://i.ibb.co/V3pT8fB/image.png)

    * datetime: esta biblioteca es utilizada para obtener la fecha y la hora actuales cuando se realiza ciertas operaciones, como registrar eventos en el archivo .petmanager_result.

    ![INVCLASS](https://i.ibb.co/h7FXYDz/image.png)

## Uso del código
El archivo main.py contiene el script principal que debe ejecutarse para iniciar la aplicación. El sistema pide que se ingresen distintas opciones para que el usario elija la que desea por medio de inputs proporcionados por el script. Los detalles sobre cómo utilizar cada comando están documentados dentro del manual de usuario.
![INVCLASS](https://i.ibb.co/hZ4m7RQ/image.png)

## Métodos utilizados
### Ejecutar comando
Este método toma un comando como entrada y ejecuta la acción correspondiente según la instrucción en el comando. Las instrucciones posibles incluyen Crear_Gato, Dar_de_Comer, Jugar, Resumen_Mascota y Resumen_Global.

![INVCLASS](https://i.ibb.co/NN9m056/image.png)

### Crear Gato
Este método crea un nuevo gato con el nombre especificado y lo agrega al diccionario mascotas con una energía inicial de 1 y vivo. También escribe un mensaje en el archivo de resultados mascotas.petmanager_result.

![INVCLASS](https://i.ibb.co/D7wyN5X/image.png)

### Dar de comer
Este método aumenta la energía del gato especificado en función del peso proporcionado. Si la energía del gato cae a cero o menos, el gato se marca como muerto y se escribe un mensaje correspondiente en el archivo de resultados.

![INVCLASS](https://i.ibb.co/LkhtMxw/image.png)

### Jugar
Este método reduce la energía del gato especificado en función del tiempo de juego. Si la energía del gato cae a cero o menos, el gato se marca como muerto y se escribe un mensaje correspondiente en el archivo de resultados.

![INVCLASS](https://i.ibb.co/mq9S2Dk/image.png)

### Resumen Mascota
Este método genera un resumen del estado actual de la mascota especificada (nombre, energía y estado) y lo escribe en el archivo de resultados.

![INVCLASS](https://i.ibb.co/5YdFPz3/image.png)

### Resumen Global
Este método genera un resumen global de todas las mascotas (nombre, energía y estado) y lo escribe en el archivo de resultados. También genera un gráfico visual de las mascotas utilizando la biblioteca graphviz.

![INVCLASS](https://i.ibb.co/Fk10VJY/image.png)


## Manejo de Errores
### Instalación de Bibliotecas
La correcta instalación de las bibliotecas requeridas es crucial para el funcionamiento adecuado de PetWorld Manager. A continuación, se detalla cómo manejar posibles errores relacionados con la instalación y la importación de estas bibliotecas:

#### Error de Importación de Graphviz
Si al ejecutar PetWorld Manager se encuentra con un error relacionado con la importación de la biblioteca graphviz, es probable que esta biblioteca no esté instalada en su entorno. Esto puede suceder si la biblioteca no se ha instalado previamente utilizando el administrador de paquetes pip. 


Se debe ejecutar el siguiente comando en su terminal para instalar la biblioteca graphviz:


**pip install graphviz**

#### Manejo de Excepciones
PetWorld Manager está diseñado para manejar posibles errores de importación de bibliotecas de manera que el programa continúe ejecutándose sin interrupciones graves. Si no se puede importar graphviz, algunas funcionalidades que dependen de esta biblioteca pueden estar deshabilitadas, pero el resto del programa seguirá funcionando normalmente.






