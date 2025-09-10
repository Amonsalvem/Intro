import streamlit as st
from PIL import Image

# =========================
# CONFIGURACIÓN DE LA APP
# =========================
st.set_page_config(
    page_title="MyApp - Interfaces Multimodales",
    page_icon="✨",
    layout="wide"
)

# =========================
# PORTADA
# =========================
st.title("🌐 MyApp")
st.header("Espacio para desarrollar aplicaciones de interfaces multimodales")
st.write("Aquí combino **backend** y **frontend** fácilmente con Streamlit.")

# Mostrar imagen de portada
try:
    image = Image.open("Int.png")
    st.image(image, caption="Ejemplo de interfaz multimodal", use_container_width=True)
except FileNotFoundError:
    st.warning("⚠️ No se encontró la imagen `Int.png`. Asegúrate de subirla al mismo directorio.")

# =========================
# INPUT DE TEXTO
# =========================
st.subheader("✍️ Entrada de texto")
texto = st.text_input("Escribe algo:", "Este es mi texto")
st.write(f"El texto escrito es: **{texto}**")

# =========================
# COLUMNAS PARA MODALIDADES
# =========================
st.subheader("🔀 Columnas con opciones")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario.")
    if st.checkbox("Estoy de acuerdo"):
        st.success("✅ ¡Correcto!")

with col2:
    st.markdown("### Segunda columna")
    modo = st.radio(
        "¿Qué modalidad es la principal en tu interfaz?",
        ("Visual", "Auditiva", "Háptica")
    )
    if modo == "Visual":
        st.info("👀 La vista es fundamental para tu interfaz.")
    elif modo == "Auditiva":
        st.info("👂 La audición es fundamental para tu interfaz.")
    elif modo == "Háptica":
        st.info("✋ El tacto es fundamental para tu interfaz.")

# =========================
# BOTONES
# =========================
st.subheader("🔘 Uso de botones")
if st.button("Presiona el botón"):
    st.success("Gracias por presionar 🙌")
else:
    st.write("Aún no has presionado el botón.")

# =========================
# SELECTBOX
# =========================
st.subheader("🎛️ Selectbox de modalidades")
in_mod = st.selectbox(
    "Selecciona la modalidad:",
    ("Audio", "Visual", "Háptico")
)

if in_mod == "Audio":
    set_mod = "🔊 Reproducir audio"
elif in_mod == "Visual":
    set_mod = "🎥 Reproducir video"
elif in_mod == "Háptico":
    set_mod = "📳 Activar vibración"

st.write(f"La acción seleccionada es: **{set_mod}**")

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.subheader("⚙️ Configuración de la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar:",
        ("Visual", "Auditiva", "Háptica")
    )
    st.write(f"🔧 Modalidad configurada: **{mod_radio}**")
