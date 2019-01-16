import fitz, os, time

rut = input('Ubicación del archivo: ')
pdf = input('Nombre del pdf (sin la extensión *.pdf): ') # A mejorar: detectar la terminación *.pdf

ruta = os.path.join(rut, '')

nom_pdf = "{}{}.pdf".format(ruta, pdf)

ruta_imgs = os.path.join('{}{}'.format(ruta, nom_pdf), '')

if not os.path.exists(pdf):
	os.makedirs(pdf)

doc = fitz.open(nom_pdf)
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("{}/{}-{}.png".format(pdf, i, xref))
            print("extraida la imagen {}-{}.png".format(i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("{}/{}-{}.png".format(pdf, i, xref))
            print("extraida la imagen {}-{}.png".format(i, xref))
            pix1 = None
        pix = None
doc.close()

print("Ha finalizado la extracción de las imágenes de su PDF")
wait = input("Presione ENTER para salir.")