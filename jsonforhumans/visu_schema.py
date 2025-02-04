import os

# Percorso in cui salvare il file HTML
output_dir = "_readthedocs/html/_static"
output_path = os.path.join(output_dir, "generated.html")

# Crea la directory se non esiste
os.makedirs(output_dir, exist_ok=True)

# Contenuto HTML da generare
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

# Scrive il file HTML
with open(output_path, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"File HTML generato con successo: {output_path}")
