# Pequeños programas para extraer imágenes de archivos PDF

La intención de estos *scripts* consiste en ayudar a las tareas de extracción de imágenes desde un PDF sin requerir la instalación de software. Los escribí específicamente para extraer las imágenes de archivos PDF muy grandes y poder luego subirlas al servidor de Transkribus. En un futuro espero poder ajustar el proceso poder extraer las imágenes de todos los archivos PDF dentro de varios directorios y subdirectorios.

Estos programas aprovechan el módulo [PyMuPDF](https://pypi.org/project/PyMuPDF/) y son básicamente una ligera adaptación de los ejemplos disponibles en <https://github.com/rk700/PyMuPDF/tree/master/examples>. 

# Descripción

Este repositorio contiene tres archivos de Python (dentro del directorio `extractores`) que contienen el mismo *script* para extraer imágenes aunque con pequeñas diferencias:

- `extractor_simple.py` requiere ser editado para indicarle el archivo PDF a procesar.
- `extractor_singleFile.py` sólo requiere ejecutarse para procesar un archivo PDF.\*
- `extractor_delPDF.py` funciona igual que `extractor_singleFile.py` pero elimina el archivo PDF después de extraer las imágenes.\*

# Utilización

1. Descargue o clone el repositorio con git `git clone https://github.com/jairomelo/extractor_imgs.git`
2. Escoja uno de los scripts según la tarea que quiera realizar y cópielo en el directorio donde se encuentre el archivo PDF del que quiere extraer las imágenes.
3. Ejecute el programa.
4. Las imágenes se guardarán automáticamente en el mismo directorio donde se ejecuta el programa.

# Advertencias

- Por el momento, estos *scripts* sólo analizan un archivo PDF a la vez.
- \* Si el directorio contiene muchos archivos PDF deberá utilizar `extractor_simple.py` e indicar el archivo del que quiere extraer imágenes en la línea 3 `nombredelPDF = 'xxxxxx.pdf'`
- \* Si el directorio tiene un sólo archivo PDF puede ejecutar cualquiera de los programas.

- La calidad de las imágenes dependerá del archivo de origen.
- Si no se retiraron los fondos de las páginas el programa los extraerá.
- De los archivos PDF a los que no se les ha aplicado OCR se extraerán cada una de las páginas.

# Tareas futuras

- Conseguir que el script se ejecute en todos los archivos PDF de un directorio.
- Conseguir que el script se ejecute en todos los archivos PDF de varios directorios y subdirectorios.
- Permitir escoger una lista de archivos PDF dentro de uno o varios directorios para extraer las imágenes.
- Permitir escoger el directorio de destino de las imágenes extraidas.

# Objetivo final

- Lograr extraer las imágenes de varios archivos PDF dentro de colecciones históricas de periódicos e impresos para hacer análisis de información gráfica.

# Soporte

Este repositorio es básicamente un ejercicio de aprendizaje y práctica personal, por lo que no puedo garantizar el soporte de las aplicaciones. 

# Licencia

GNU General Public License v3.0