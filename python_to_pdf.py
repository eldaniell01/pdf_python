from jinja2 import Environment, FileSystemLoader
import os
from weasyprint import HTML
from datetime import datetime

# Ruta al directorio que contiene la plantilla HTML
template_dir = ('')

# Ruta al archivo HTML de la plantilla
html_file = 'plantilla.html'

# Ruta al archivo PDF de salida
pdf_file = 'salida.pdf'

# Datos a pasar a la plantilla
datos = {
    'my_name': 'daniel',
    'item1': 'tv',
    'today': datetime.now()
}

# Cargar la plantilla HTML
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('plantilla.html')

# Reemplazar los marcadores de posición con los datos
html_content = template.render(datos)

# Generar el PDF
HTML(string=html_content).write_pdf(pdf_file)

print(f'El archivo PDF se ha creado con éxito en "{pdf_file}"')

