import fitz, os, glob, time

# extraer el nombre del archivo pdf
pdfnomb = glob.glob("*.pdf")
cadena = str(pdfnomb)
encadenado = ''.join(cadena).replace('[\'','').replace('\']','')

# asegurar que el pdf exista
if os.path.exists(encadenado):
    print("Se están extrayendo las imágenes del archivo " + encadenado)
else:
    print("No existe ningún archivo para convertir")
    time.sleep(3)
    quit()

# convertir pdf a imágenes con PyMuPDF (Fitz)
doc = fitz.open(encadenado)
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("p%s-%s.png" % (i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("p%s-%s.png" % (i, xref))
            pix1 = None
        pix = None
doc.close() #cierra el archivo

print("Ha finalizado la extracción de las imágenes de su PDF")
wait = input("Presione ENTER para continuar.")