from pdf2image import convert_from_path
import pytesseract

# Convertir PDF → lista de imágenes
pages = convert_from_path("test.pdf")

# Procesar cada página
texto_total = ""
for page in pages:
    texto = pytesseract.image_to_string(page, lang="spa")
    texto_total += texto + "\n"

print(texto_total)
