import streamlit as st
from streamlit.components.v1 import html

st.set_page_config( 
   page_icon="🧊",
   layout="wide", 
)

# Combinando todos los estilos en un solo bloque
combined_style = """
<style>
    /* Hide the Streamlit header and menu */
    header {visibility: hidden;}
    
    /* Optionally, hide the footer */
    .streamlit-footer {display: none;}
    
    /* Hide your specific div class */
    .st-emotion-cache-uf99v8 {display: none;}
    
    /* Full width content */
    .st-emotion-cache-zy6yx3 {
        width: 100%;
        padding: 1rem 1rem 1rem;
        max-width: initial;
        min-width: auto;
    }
    
    /* Media query para la primera medida de pantalla */
    @media (min-width: calc(736px + 8rem)) {
        .st-emotion-cache-zy6yx3 {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    
    /* Media query para pantallas de 14 pulgadas (aproximadamente 1366px) */
    @media (min-width: 1366px) and (max-width: 1599px) {
        .st-emotion-cache-zy6yx3 {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }
    
    /* Media query para pantallas de 15 pulgadas (aproximadamente 1600px-1920px) */
    @media (min-width: 1600px) and (max-width: 1920px) {
        .st-emotion-cache-zy6yx3 {
            padding-left: 3rem;
            padding-right: 3rem;
        }
    }
</style>
"""

# Aplicar el estilo combinado
st.markdown(combined_style, unsafe_allow_html=True)


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
      width: 110vw; /* Ocupa todo el ancho del viewport */
      margin: 0;
      padding: 0;
    }
    iframe {
      width: 100vw; /* Ocupa todo el ancho del viewport */  
      height: 100vh; /* Ocupa todo el alto del viewport */
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
     
    ></iframe>
  </div>
</body>

</body>
</html>
"""

# Renderizar el HTML en Streamlit
html(html_code, height=800)
