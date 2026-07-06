from pathlib import Path
from collections import Counter
from PIL import Image
import statistics

# ==========================================================
# CONFIGURACIÓN
# ==========================================================

DATASET_DIR = Path(r"flowers16")      # <-- Cambiar por la carpeta raíz

EXT = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

# ==========================================================
# RECORRIDO
# ==========================================================

classes = sorted([d for d in DATASET_DIR.iterdir() if d.is_dir()])

print("="*60)
print("Analizando dataset...")
print("="*60)

total_images = 0
widths = []
heights = []
modes = Counter()
formats = Counter()

class_info = []

for c in classes:

    files = [f for f in c.rglob("*") if f.suffix.lower() in EXT]

    total_images += len(files)

    for f in files:
        try:
            with Image.open(f) as img:
                w, h = img.size
                widths.append(w)
                heights.append(h)
                modes[img.mode] += 1
                formats[img.format] += 1
        except:
            pass

    class_info.append((c.name, len(files)))

# ==========================================================
# RESULTADOS
# ==========================================================

print()
print("Número de clases :", len(classes))
print("Total imágenes   :", total_images)
print()

print("Imágenes por clase")
print("------------------")

for name, n in class_info:
    print(f"{name:20} {n:5d}")

print()

print("Resoluciones")
print("------------------")
print("Ancho mínimo :", min(widths))
print("Ancho máximo :", max(widths))
print("Ancho medio  :", round(statistics.mean(widths),1))

print()

print("Alto mínimo  :", min(heights))
print("Alto máximo  :", max(heights))
print("Alto medio   :", round(statistics.mean(heights),1))

print()

print("Formatos")
print("------------------")
for k,v in formats.items():
    print(f"{k:6}: {v}")

print()

print("Modos de color")
print("------------------")
for k,v in modes.items():
    print(f"{k:6}: {v}")

# ==========================================================
# GENERAR MARKDOWN
# ==========================================================

with open("dataset_info.md","w",encoding="utf8") as f:

    f.write("# Estadísticas del dataset\n\n")

    f.write(f"- Número de clases: **{len(classes)}**\n")
    f.write(f"- Número de imágenes: **{total_images}**\n\n")

    f.write("## Imágenes por clase\n\n")

    f.write("| Clase | Imágenes |\n")
    f.write("|-------|----------:|\n")

    for name,n in class_info:
        f.write(f"| {name} | {n} |\n")

    f.write("\n")

    f.write("## Resoluciones\n\n")

    f.write(f"- Ancho mínimo: {min(widths)} px\n")
    f.write(f"- Ancho máximo: {max(widths)} px\n")
    f.write(f"- Ancho medio: {statistics.mean(widths):.1f} px\n\n")

    f.write(f"- Alto mínimo: {min(heights)} px\n")
    f.write(f"- Alto máximo: {max(heights)} px\n")
    f.write(f"- Alto medio: {statistics.mean(heights):.1f} px\n\n")

    f.write("## Formatos\n\n")
    for k,v in formats.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Modos de color\n\n")
    for k,v in modes.items():
        f.write(f"- {k}: {v}\n")

print("\nSe generó dataset_info.md")