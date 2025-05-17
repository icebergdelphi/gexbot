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

    /* Media query para pantallas de 15 pulgadas (aproximadamente 1600px-1920px) /
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
      overflow: hidden; / Evita barras de desplazamiento /
      height: 100%;
    }
    .iframe-container {
      width: 105vw; / Ocupa todo el ancho del viewport /
      margin: 0;
      padding: 0;
      height: 100%;
    }
    iframe {
      width: 100vw; / Ocupa todo el ancho del viewport /
      height: 100vh; / Altura dinámicamente ajustada al viewport /
      border: none; / Elimina el borde /
      display: block; / Asegura que no haya espacios extra */
    }

    /* Ajustes responsivos para diferentes tamaños de pantalla /
    @media (max-height: 768px) {
      iframe {
        height: 80vh; / Para pantallas pequeñas 100 /
      }
    }
    @media (min-height: 769px) and (max-height: 900px) {
      iframe {
        height: 93vh; / Para pantallas medianas 90/
      }
    }
    @media (min-height: 901px) {
      iframe {
        height: 95vh; / Para pantallas grandes */
      }
    }
  </style>
</head>
<body>
  <div class="iframe-container">
    <iframe 
      src="https://www.gexbot.com/"    
          allowfullscreen
    ></iframe>
  </div>
  <script>
    // Script para ajustar dinámicamente la altura del iframe
    function adjustIframeHeight() {
      const iframe = document.querySelector('iframe');
      const viewportHeight = window.innerHeight;
      iframe.style.height = viewportHeight + 'px';
    }

    // Ajustar al cargar y cuando cambie el tamaño de la ventana
    window.addEventListener('load', adjustIframeHeight);
    window.addEventListener('resize', adjustIframeHeight);
  </script>
</body>
</html>
"""
# Renderizar el HTML en Streamlit - usar un valor que se ajuste a la mayoría de pantallas
# Podemos ajustar este valor según las necesidades específicas
html(html_code, height=760, scrolling=False)
