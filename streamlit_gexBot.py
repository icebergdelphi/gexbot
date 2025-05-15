import streamlit as st
from streamlit.components.v1 import html

# HTML personalizado con el iframe ajustado
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GexBot Embed</title>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      margin: 0;
      padding: 0;
      overflow: hidden; /* Evita barras de desplazamiento */
    }
    .iframe-container {
      width: 100vw; /* Ocupa todo el ancho del viewport */
      margin: 0;
      padding: 0;
    }
    iframe {
      width: 110vw; /* Ocupa todo el ancho del viewport */
      height: 110vh; /* Ocupa todo el alto del viewport */
      border: none; /* Elimina el borde */
      display: block; /* Asegura que no haya espacios extra */
    }
  </style>
</head>
<body>
  <div class="iframe-container">
    <iframe 
      src="https://www.gexbot.com/"
      title="Contenido externo"
      allowfullscreen
    ></iframe>
  </div>
</body>
</html>
"""

# Renderizar el HTML en Streamlit
html(html_code, height=1150)
