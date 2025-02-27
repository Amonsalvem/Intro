import streamlit as st
from PIL import Image

st.title("myapp")

st.header("En este espacio comienzo a desarrollar mis apllicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Int.png')
st.image(image)



texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)


col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')
with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principaL en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'auditiva':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write('El tacto es fundamental para tu interfaz')
    
st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
  st.write('Gracias por presionar')
else:
  st.write('no has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
  set_mod = "Reproducir audio"
elif in_mod == "Visual":
  set_mod = "Reproducir video"
elif in_mod == "Háptico":
  set_mod = "Activar vibración"
st.write("La acción es: " ,set_mod)


with st.sidebar:
  st.subeheader("Configuta la modalidad")
  mod_radio = st.radio(
      "Escoge la modadlidad de usar",
      ("Visual", "Auditiva", "Háptica")




