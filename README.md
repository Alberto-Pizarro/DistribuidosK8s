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

El contexto del problema a resolver hace referencia a crear una prueba de concepto que aune lo trabajado y aprendido en clases de Sistemas Distribuidos junto con el tópico entregado. Específicamente este corresponde a crear una conexión entre múltiples _"pods"_ de Kubernetes, cada uno funcionando con una imagen de Docker y que entre los 3 se pueda simular el funcionamiento distribuido de una página web básica.

---

4. **Enfoque de solución**

Al momento de planear el desarrollo de la solución del problema anterior descrito, se decidió utilizar una plataforma como lo es [Google Cloud](https://cloud.google.com/) dado que se cuenta con múltiples tutoriales, inclusive algunos proveídos en la misma plataforma por parte de Google, además de los 300 dólares gratuitos que nos permite probar el funcionar de nuestra plataforma web simulada sin entrar en un desembolso monetario.

La solución cuenta con 3 partes principales:

* Un front-end basado en React (JavaScript)
* Un back-end diseñado con Spring (Java)
* Un programa en Python conectado a Spring que hace lo referente a la inteligencia de negocio

Las partes anterior mencionadas se encuenran funcionando dentro de _"pods"_ independientes dentro de la plataforma de Google Cloud

Respecto al programa escrito en Python, este consiste en una prueba de concepto simple utilizando el cálculo de números primos para obtener una muestra de performance aparente del sistema en cuestión.

---

5. **Desarrollo de la actividad**

Durante el desarrollo de la actividad, se presentaron un puñado de problemas. El principal fue intentar registrarse exitosamente en la plataforma de Google Cloud dado que era necesario una tarjeta de crédito y tarjetas virtuales como [MACH](https://www.somosmach.com/) del banco BCI no eran aceptadas por la plataforma.

Una vez solucionado dicho inconveniente el siguiente en presentarse fue establecer correctamente la conexión de los pods de la plataforma, dado que Kubernetes era una herramienta nunca antes utilizada fue un punto de conflicto y demora durante varias horas. Eso, sumado a los protocolos de seguridad, verificaciones y permisos de Google Cloud, demoraron el trabajo al menos un día completo.

No obstante lo anterior, una vez superados estos problemas el resto del trabajo fue desarrollado con mucha mayor facilidad de lo esperado, a pesar de ser un tema nuevo para nosotros.

Respecto al programa en Python que representa el núcleo de nuestra prueba de concepto, este se basa en un clásico problema: _**¿cómo obtener números primos de manera eficiente?**_. Para esto se procedió a implementar un clásico algoritmo, conocido desde la antiguedad: **La Criba de Erastótenes**

**Explicación de la Criba de Erastótenes**

Este algoritmo consiste en eliminar de un listado de números menores o iguales a N (esta es nuestra cota superior) todos los múltiplos del primer número (generalemente el 2) y luego avanzar al siguiente. Si se repite esto sucesivas veces hasta llegar (o superar) la raíz cuadrada de N, los números sin eliminar son los primos iguales o inferiores a este.

Ejemplo gráfico del algoritmo con N=120:

![Image](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif "Criba de Eratóstenes, extraído de: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes")

Para desarrollar este algoritmo se hizo del programa **PyCharm Community Version 2019.2** para Linux junto con el ambiente de desarrollo **Anaconda 4.7.12** y utilizando **Python 3.7**.
Para conectarse con la plaforma de Google Cloud se hizo uso de la herramienta [SDK](https://cloud.google.com/sdk/install) para utilizar la línea de comandos de Linux directamente.
Finalmente para escribir el presente Readme, se hizo uso de **Visual Studio Code** con el plugin de _"Instant Markdown"_ para ver directamente los cambios en el texto.
