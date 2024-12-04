# **Movimiento-de-robots-con-lenguaje-natural**

Este proyecto permite controlar un robot en **CoppeliaSim** utilizando comandos de texto en lenguaje natural. El sistema interpreta direcciones como **"left"**, **"right"**, **"back"**, **"forward"** y sus sinónimos utilizando la librería **NLTK**, y luego mueve el robot en la simulación en función de las direcciones detectadas.

## **Características:**

- **Procesamiento de Texto Natural**: Detecta direcciones como **"left"**, **"right"**, **"backward"**, **"forward"** y sus sinónimos a partir de un texto de entrada.
- **Integración con CoppeliaSim**: Mueve el robot en la simulación de **CoppeliaSim** según las direcciones encontradas en el texto.
- **Soporte de Sinónimos**: Incluye sinónimos como **['ahead', 'onward', 'onwards', 'forwards', 'forrader']** para **"forward"**.
- **Direcciones base**: Las direcciones son normalizadas a las formas base **"left"**, **"right"**, **"back"** y **"forward"** para facilitar el movimiento del robot.

## **Requisitos:**

- **CoppeliaSim**: Debes tener instalado y configurado CoppeliaSim con soporte para la API remota.
- **Python 3.x**: Este proyecto requiere Python 3.x para ejecutar el código.
- **Dependencias de Python**: Asegúrate de tener las siguientes bibliotecas instaladas:
  - `nltk`
  - `zmqRemoteApi`
  - `re` (viene preinstalado con Python)
