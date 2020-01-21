# Sistemas Distribuidos - Laboratorio 2 - Pruebas de concepto  

## Descripción del laboratorio realizado

1. **Tema escogido**

Docker e integración con Kubernetes

---

2. **Autores**

* Sebastián Pasutti
* Alberto Pizarro Riffo

---

3. **Descripcíon de problema a resolver**

El contexto del problema a resolver hace referencia a crear una prueba de concepto que aúne lo trabajado y aprendido en clases de Sistemas Distribuidos junto con el tópico entregado. Específicamente este corresponde a crear una conexión entre múltiples _"pods"_ de Kubernetes, cada uno funcionando con una imagen de Docker y que entre los 3 se pueda simular el funcionamiento distribuido de una página web básica.

---

4. **Enfoque de solución**

Al momento de planear el desarrollo de la solución del problema anterior descrito, se decidió utilizar una plataforma como lo es [Google Cloud](https://cloud.google.com/) dado que se cuenta con múltiples tutoriales, inclusive algunos proveídos en la misma plataforma por parte de Google, además de los 300 dólares gratuitos que nos permite probar el funcionar de nuestra plataforma web simulada sin entrar en un desembolso monetario.

La solución cuenta con 3 partes principales:

* Un front-end basado en React (JavaScript)
* Un back-end diseñado con Spring (Java)
* Un programa en Python conectado a Spring que hace lo referente a la inteligencia de negocio

Las partes anterior mencionadas se encuentran funcionando dentro de _"pods"_ independientes dentro de la plataforma de Google Cloud

Respecto al programa escrito en Python, este consiste en una prueba de concepto simple utilizando el cálculo de números primos para obtener una muestra de desempeño aparente del sistema en cuestión.

---

5. **Desarrollo de la actividad**


Respecto a lo que es el uso de las tecnologías usadas para desarrollar la idea (NGINX, React, Spring, Python), no se presentaron dificultades mayores pues habían sido utilizadas en cursos anteriores en más de una ocasión.

Respecto al desarrollo de la actividad, se presentaron un puñado de problemas. El primero de estos fue intentar registrarse exitosamente en la plataforma de Google Cloud dado que era necesario una tarjeta de crédito y tarjetas virtuales como [MACH](https://www.somosmach.com/) del banco BCI no eran aceptadas por la plataforma.

Una vez solucionado el inconveniente respecto a lo que registrarse trataba, el siguiente en presentarse fue establecer correctamente la conexión de los pods, dado que Kubernetes era una herramienta nunca antes utilizada fue un punto de conflicto y demora durante varias horas. Una vez establecida de manera exitosa la conexión entre los pods, la dificultad que apareció fue como replicar aquello que funcionaba de manera local en el ambiente entregado por Google Cloud Plataform. Eso, sumado a los protocolos de seguridad, verificaciones y permisos de Google Cloud, demoraron el trabajo al menos un día y medio.

No obstante lo anterior, una vez superados estos problemas el resto del trabajo fue desarrollado con mucha mayor facilidad de lo esperado, a pesar de ser un tema nuevo para nosotros.

Respecto al programa en Python que representa el núcleo de nuestra prueba de concepto, este se basa en un clásico problema: _**¿cómo obtener números primos de manera eficiente?**_. Para esto se procedió a implementar un clásico algoritmo, conocido desde la antigüedad: **La Criba de Erastótenes**

**Explicación de la Criba de Erastótenes**

Este algoritmo consiste en eliminar de un listado de números menores o iguales a N (esta es nuestra cota superior) todos los múltiplos del primer número (generalmente el 2) y luego avanzar al siguiente. Si se repite esto sucesivas veces hasta llegar (o superar) la raíz cuadrada de N, los números sin eliminar son los primos iguales o inferiores a este.

Ejemplo gráfico del algoritmo con N=120:

![Image](/Imagenes/Criba.gif "Criba de Eratóstenes, extraído de: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes")

Para desarrollar este algoritmo se hizo del programa **PyCharm Community Version 2019.2** para Linux junto con el ambiente de desarrollo **Anaconda 4.7.12** y utilizando **Python 3.7**.
Para conectarse con la plataforma de Google Cloud se hizo uso de la herramienta [SDK](https://cloud.google.com/sdk/install) para utilizar la línea de comandos de Linux directamente.
Finalmente para escribir el presente Readme, se hizo uso de **Visual Studio Code** con el plugin de _"Instant Markdown"_ para ver directamente los cambios en el texto. 

---

6. **Resultados**

Los resultados se determinan como exitosos dado que se ha conseguido levantar correctamente las imágenes de Docker en la plataforma de Google Cloud. Utilizando Kubernetes se crearon _pods_ que mantienen en su interior dichas imágenes formando la estructura de la plataforma levantada, descrita en el punto anterior.

![Image](/Imagenes/k8-primos-diagrama.png "Diagrama de despliegue de la plataforma en GCP utilizando Kubernetes")

Al momento de utilizar la plataforma, esta se ve como una página simple con un pequeño campo para ingresar el número con el que se va a trabajar. En el siguiente ejemplo se muestra utilizando un N=4000:

![Image](/Imagenes/Localhost1.jpg "Ejemplo de funcionamiento con N=4000 de manera local")

Como se puede ver, el funcionamiento de la plataforma es bastante rápido por lo eficiente del algoritmo (a pesar de no ser un código óptimo ni el mejor algoritmo en lo que a eficiencia se trata).

A continuación mostramos el despliegue de la plataforma dentro del sistema de Google Cloud, los comandos, el estado de los pods, etc.
![Image](/Imagenes/1.png "Ejemplo de despliegue de la plataforma - parte 1")
![Image](/Imagenes/2.png "Ejemplo de despliegue de la plataforma - parte 2")
![Image](/Imagenes/3.png "Ejemplo de despliegue de la plataforma - parte 3")
![Image](/Imagenes/4.png "Ejemplo de despliegue de la plataforma - parte 4")

La siguiente imagen muestra las imágenes de Docker dentro del "container registry" de Google Cloud Plataform
![Image](/Imagenes/5.png "Imágenes de Docker dentro del repositorio de Google")

---

7. **Link de acceso a versión productiva del Software**

La versión productiva del software se puede encontrar haciendo click en el siguiente [LINK](http://34.95.209.27:80)

---

8. **Pasos para desplegar desde cero**

Para desplegar localmente las imágenes se deben contar con Docker instalado y ejecutar los siguientes comandos:

* **Para desplegar el código de Python:** `docker run -d -p 5050:5000 remnant12/kubernetes-dist-api-bench-final`

* **Para desplegar lo que es Backend:** `docker run -d -p 8080:8080 -e K8_PYTHON_API_URL='http://<IP del container anterior>:5000' remnant12/kubernetes-dist-back-final` 

* **Para desplegar lo que es Frontend** `docker run -d -p 80:80 remnant12/kubernetes-dist-front-final-2`


Las imágenes en el repositorio de Google se encuentran en las siguientes direcciones:

* [Código en Python](gcr.io/kubernetes-test-77617/remnant12/kubernetes-dist-api-bench-final)

* [Back-End](gcr.io/kubernetes-test-77617/remnant12/kubernetes-dist-back-final)

* [Front-End](gcr.io/kubernetes-test-77617/remnant12/kubernetes-dist-front-final-2)
