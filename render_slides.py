"""
Renderiza todas las presentaciones RevealJS del directorio slides/
y las deja en docs/

Uso:
    python render_slides.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent

print("Renderizando presentaciones...")
result = subprocess.run(
    ["quarto", "render", "slides/"],
    cwd=ROOT,
)

if result.returncode == 0:
    print("Presentaciones renderizadas correctamente en docs/")
else:
    print("Error al renderizar las presentaciones.")
    sys.exit(1)
