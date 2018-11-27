import fitz, os, time

rut = input('Ubicación del archivo: ')
pdf = input('nombre del pdf \(sin la ext. pdf\): ')

ruta = os.path.join(rut, '')
ruta_imgs = os.path.join('{}{}'.format(ruta, pdf), '')

nom_pdf = "{}{}.pdf".format(ruta, pdf)

if not os.path.exists(pdf):
	os.makedirs(pdf)

doc = fitz.open(nom_pdf)
for i in range(len(doc)):
    for img in doc.getPageImageList(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n < 5:       # this is GRAY or RGB
            pix.writePNG("{}{}{}.png".format(ruta_imgs, i, xref))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.writePNG("{}{}{}.png".format(ruta_imgs, i, xref))
            pix1 = None
        pix = None
doc.close()

print("Ha finalizado la extracción de las imágenes de su PDF")
wait = input("Presione ENTER para salir.")