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
  <style>
    html, body {
      margin: 0;
      padding: 0;
      overflow: hidden;
      width: 100%;
      height: 100vh;
      background-color: #000;
    }
    
    
    iframe {
      width: 100%;
      height: 100vh; /* Altura extra para mostrar todo el contenido */
      border: none;
      transform-origin: top center;
      transform: scale(1);
    }
    
    @media screen and (max-width: 1366px) {
      /* Pantallas pequeñas (laptops de 14") */
      iframe {
        height: 100vh;
        transform: scale(1);
      }
    }
    
    @media screen and (min-width: 1921px) {
      /* Pantallas muy grandes (21" o más) */
      iframe {
        height: 105vh;
        transform: scale(0.95);
      }
    }
  </style>
</head>
<body>
  <div class="iframe-wrapper">
    <iframe 
      src="https://www.gexbot.com/"
      allowfullscreen
      id="gexbot-frame"
    ></iframe>
  </div>
  
  <script>
    // Función para ajustar manualmente el iframe según el tamaño de pantalla detectado
    function adjustIframe() {
      const iframe = document.getElementById('gexbot-frame');
      const screenWidth = window.innerWidth;
      const screenHeight = window.innerHeight;
      
      // Ajustamos la altura y escala según el ancho de pantalla
      if (screenWidth <= 1366) {
        // Pantallas pequeñas (14")
        iframe.style.height = "75vh";
        iframe.style.transform = "scale(0.9)";
      } 
      else if (screenWidth > 1366 && screenWidth <= 1920) {
        // Pantallas medianas
        iframe.style.height = "130vh";
        iframe.style.transform = "scale(0.9)";
      }
      else if (screenWidth > 1920) {
        // Pantallas grandes (21"+)
        iframe.style.height = "110vh";
        iframe.style.transform = "scale(1.1)";
      }
      
      console.log(`Pantalla: ${screenWidth}x${screenHeight}px - Ajustando iframe`);
    }
    
    // Ejecutar al cargar y cuando cambie el tamaño
    window.addEventListener('load', adjustIframe);
    window.addEventListener('resize', adjustIframe);
    
    // También podemos intentar ajustar periódicamente para asegurar la correcta visualización
    setInterval(adjustIframe, 2000);
  </script>
</body>
</html>
"""

# Renderizar el HTML en Streamlit - altura fija más alta para acomodar todo el contenido
html(html_code, height=1000, scrolling=False)
