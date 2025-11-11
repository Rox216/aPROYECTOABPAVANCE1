import pytesseract
from PIL import Image

# Ruta a la imagen (ajústala según donde la guardes)
image_path = "fa35138b-8d47-48e5-b827-be5bae2def7e.png"

# Abrir la imagen
img = Image.open(image_path)

# Usar OCR para extraer texto
text = pytesseract.image_to_string(img)

# Guardar el resultado en un archivo de texto
with open("codigo_extraido.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Texto extraído y guardado en codigo_extraido.txt")
