import streamlit as st
from PIL import Image

st.title("myapp")

st.header("En este espacio comienzo a desarrollar mis apllicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Int.png')




texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
