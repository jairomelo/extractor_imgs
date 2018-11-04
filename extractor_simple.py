import fitz, time

nombredelPDF = 'xxxxxx.pdf' # cambiar por el nombre del arhivo PDF

print("Se está convirtiendo el archivo " + nombredelPDF + " .")

# convertir pdf a imágenes con PyMuPDF (Fitz)
doc = fitz.open(nombredelPDF)
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