import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV "database_titanic.csv" en un DataFrame de pandas.
df = pd.read_csv("database_titanic.csv")

# Muestra un título y una descripción en la aplicación Streamlit.
st.write("""
# Mi primera aplicación interactiva.
## Gráficos usando la base de datos del Titanic
""")

# Usando la notación "with" para crear una barra lateral en la aplicación Streamlit.
with st.sidebar:
    # Título para la sección de opciones en la barra lateral.
    st.write("# Opciones")
    
    # Crea un control deslizante (slider) que permite al usuario seleccionar un número de bins
    # en el rango de 0 a 10, con un valor predeterminado de 2.
    div = st.slider('Número de bins:', 0, 10, 2)
    
    # Muestra el valor actual del slider en la barra lateral.
    st.write("Bins=", div)

# Desplegamos un histograma con los datos del eje X
fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df["Age"], bins=div)
ax[0].set_xlabel("Edad")
ax[0].set_ylabel("Frecuencia")
ax[0].set_title("Histograma de edades")

# Tomando datos para hombres y contando la cantidad
df_male = df[df["Sex"] == "male"]
cant_male = len(df_male)

# Tomando datos para mujeres y contando la cantidad
df_female = df[df["Sex"] == "female"]
cant_female = len(df_female)

ax[1].bar(["Masculino", "Femenino"], [cant_male, cant_female], color = "red")
ax[1].set_xlabel("Sexo")
ax[1].set_ylabel("Cantidad")
ax[1].set_title('Distribución de hombres y mujeres')

# Desplegamos el gráfico
st.pyplot(fig)







# Muestra un título y una descripción en la aplicación Streamlit.
st.write("""
## Gráfico de Sobrevivientes por Sexo
""")

# ====== Gráfico de anillo de sobrevivientes por sexo ======

# Filtrar y contar desde el DataFrame
surv_male = len(df[(df["Sex"] == "male") & (df["Survived"] == 1)])
total_male = len(df[df["Sex"] == "male"])
non_male = total_male - surv_male

surv_female = len(df[(df["Sex"] == "female") & (df["Survived"] == 1)])
total_female = len(df[df["Sex"] == "female"])
non_female = total_female - surv_female

# Colores consistentes (masculino, femenino)
colors = ["#4A90E2", "#BE1BC4"]
grey = "#DDDDDD"

# Figura con dos donuts lado a lado
fig, axs = plt.subplots(1, 2, figsize=(12, 0))

# Donut masculino
vals_m = [surv_male, non_male]
labels_m = [f"Sobrevivientes ({surv_male})", f"No sobrevivientes ({non_male})"]
axs[0].pie(
    vals_m,
    labels=labels_m,
    colors=[colors[0], grey],
    startangle=90,
    wedgeprops={"width": 0.45, "edgecolor": "white"}
)
axs[0].set_title("Hombres — Sobrevivientes (cantidad)")
# número grande en el centro del donut
axs[0].text(0, 0, str(surv_male), ha="center", va="center", fontsize=16, fontweight="bold")

# Donut femenino
vals_f = [surv_female, non_female]
labels_f = [f"Sobrevivientes ({surv_female})", f"No sobrevivientes ({non_female})"]
axs[1].pie(
    vals_f,
    labels=labels_f,
    colors=[colors[1], grey],
    startangle=90,
    wedgeprops={"width": 0.45, "edgecolor": "white"}
)
axs[1].set_title("Mujeres — Sobrevivientes (cantidad)")
axs[1].text(0, 0, str(surv_female), ha="center", va="center", fontsize=16, fontweight="bold")

# Asegurar aspecto igual para que los donuts sean circulares
for ax in axs:
    ax.axis("equal")

# Mostrar en Streamlit
st.pyplot(fig)




st.write("""
## Muestra de datos cargados
""")
# Graficamos una tabla
st.table(df.head())
