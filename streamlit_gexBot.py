import streamlit as st
from streamlit.components.v1 import html

# IMPORTANTE: st.set_page_config debe ser el primer comando de Streamlit
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
        padding: 0rem 1rem 0rem;
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
            padding-left: 2rem;
            padding-right: 2rem;
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

# HTML personalizado con el iframe ajustado y escala auto-adaptativa
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GexBot Embed</title>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.2/css/bootstrap.min.css" rel="stylesheet">
  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      width: 100%;
      height: 100%;
    }
    
    .iframe-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      transform-origin: top left;
      transition: transform 0.3s ease;
    }
    
    iframe {
      width: 100vw;
      height: 100vh;
      border: none;
      display: block;
    }
  </style>
</head>
<body>
  <div id="iframe-container" class="iframe-container">
    <iframe 
      src="https://www.gexbot.com/"
      allowfullscreen
    ></iframe>
  </div>
  
  <script>
    // Función para ajustar la escala según el tamaño de la pantalla
    function adjustScale() {
      const container = document.getElementById('iframe-container');
      const screenWidth = window.innerWidth;
      const screenHeight = window.innerHeight;
      
      // Detectar tamaño de pantalla y aplicar escala adecuada
      let scale = 1; // Escala predeterminada (100%)
      
      // Para pantallas pequeñas (14 pulgadas o similar)
      if (screenWidth <= 1366) {
        scale = 0.75; // Escala al 75%
      } 
      // Para pantallas medianas (15-17 pulgadas)
      else if (screenWidth > 1366 && screenWidth <= 1920) {
        scale = 0.9; // Escala al 90%
      }
      // Para pantallas grandes (21 pulgadas o más)
      else if (screenWidth > 1920) {
        scale = 1.2; // Escala al 120%
      }
      
      // Aplicar transformación de escala al contenedor
      container.style.transform = `scale(${scale})`;
      
      // Ajustar el contenedor para ocupar el espacio correcto después del escalado
      container.style.width = `${100 / scale}%`;
      container.style.height = `${100 / scale}%`;
      
      console.log(`Pantalla detectada: ${screenWidth}px de ancho. Aplicando escala: ${scale * 100}%`);
    }
    
    // Ejecutar al cargar y cuando cambie el tamaño de la ventana
    window.addEventListener('load', adjustScale);
    window.addEventListener('resize', adjustScale);
  </script>
</body>
</html>
"""

# Renderizar el HTML en Streamlit con altura flexible
html(html_code, height=800, scrolling=False)
