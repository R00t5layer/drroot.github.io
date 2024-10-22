import os

def generate_html(directory):
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tools Directory</title>
</head>
<body>
    <h1>Tools Directory</h1>
    <ul>
"""

    # Recorrer el directorio y subdirectorios
    for root, dirs, files in os.walk(directory):
        # Obtener la ruta relativa de las carpetas
        rel_path = os.path.relpath(root, directory)
        if rel_path == ".":
            rel_path = ""

        for file in files:
            file_path = os.path.join(rel_path, file)
            html_content += f'        <li><a href="Tools/{file_path}">{file_path}</a></li>\n'

    html_content += """    </ul>
</body>
</html>"""

    return html_content


if __name__ == "__main__":
    # Cambia 'Tools' al nombre del directorio donde están los archivos
    directory = "Tools"

    # Generar el contenido HTML
    html_output = generate_html(directory)

    # Guardar el archivo HTML
    with open("tools.html", "w", encoding="utf-8") as f:
        f.write(html_output)

    print("Archivo HTML generado como tools.html")
