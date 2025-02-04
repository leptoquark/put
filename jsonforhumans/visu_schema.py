html_content = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagina Generata</title>
</head>
<body>
    <h1>Questa è una pagina HTML generata da Python</h1>
    <p>Ecco il contenuto che vuoi visualizzare nella documentazione.</p>
</body>
</html>
"""

# Salva il file nella cartella della documentazione (es. _static/)
output_path = "docs/_static/generated.html"
with open(output_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"File HTML generato con successo: {output_path}")