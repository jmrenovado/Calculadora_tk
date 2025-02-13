Agregar funcionalidad básica de calculadora con tamaños de botones adaptativos

- Implementar una calculadora básica usando tkinter.
- Configurar la ventana principal con un título y color de fondo.
- Agregar un widget de entrada para mostrar la ecuación y el resultado.
- Definir funciones para presionar botones, presionar igual, limpiar y salir.
- Configurar filas y columnas de la cuadrícula para que se expandan proporcionalmente.
- Agregar botones para dígitos (0-9), punto decimal y operaciones básicas (+, -, *, /).
- Asegurar que los botones se adapten al tamaño de la ventana de la aplicación.
- Establecer fuentes y colores de los botones para una mejor interfaz de usuario.

  Resumen Detallado: Este commit introduce una aplicación de calculadora básica construida usando la biblioteca tkinter. Las características principales incluyen:

Configuración de la Ventana Principal:

La ventana principal se titula "Calculadora" y tiene un color de fondo #333333.
El tamaño de la ventana se establece en 386x168.
Widget de Entrada:

Se agrega un widget de entrada en la parte superior para mostrar la ecuación actual y el resultado.
El widget de entrada utiliza la fuente Arial con un tamaño de 18.
Funciones:

press(num): Agrega el número o operador presionado a la ecuación actual.
equalpress(): Evalúa la ecuación actual y muestra el resultado. Maneja SyntaxError y ZeroDivisionError.
clear(): Limpia la ecuación actual.
exit_app(): Sale de la aplicación.
Configuración de la Cuadrícula:

Las filas y columnas de la cuadrícula se configuran para que se expandan proporcionalmente con el tamaño de la ventana.
Botones:

Se agregan botones para dígitos (0-9), punto decimal y operaciones básicas (+, -, *, /).
Cada botón se configura con una fuente específica, color de primer plano y color de fondo.
Los botones se colocan en la cuadrícula con la opción sticky='nswe' para asegurar que se expandan para llenar el espacio disponible.
