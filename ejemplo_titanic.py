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
## Gráfico de Sobrevivientes agrupados por sexo
""")
# ===== Gráficos de sobrevivientes por sexo =====

# Filtrar sobrevivientes
df_survived = df[df["Survived"] == 1]

# Contar sobrevivientes por sexo
surv_male = len(df_survived[df_survived["Sex"] == "male"])
surv_female = len(df_survived[df_survived["Sex"] == "female"])

# Colores consistentes
colors = ["#4A90E2", "#E94E77"]   # azul para masculino, rosado para femenino

# === Gráfico de barras moderno ===
fig_bar, ax_bar = plt.subplots(figsize=(6,4))

ax_bar.bar(["Masculino", "Femenino"], [surv_male, surv_female], 
           color=colors, edgecolor="black")

ax_bar.set_title("Total de sobrevivientes por sexo", fontsize=14)
ax_bar.set_ylabel("Cantidad", fontsize=12)
ax_bar.grid(axis="y", linestyle="--", alpha=0.4)

st.pyplot(fig_bar)

# === Gráficos de anillos (donut charts) por sexo ===
fig_donut, axs = plt.subplots(1, 2, figsize=(10, 4))

# Total general de sobrevivientes
total_surv = surv_male + surv_female

# Donut masculino
axs[0].pie([surv_male, total_surv - surv_male],
           labels=["", ""],
           colors=[colors[0], "#DDDDDD"],
           autopct=lambda pct: f"{pct:.1f}%" if pct > 0 else "",
           startangle=90,
           wedgeprops={"width": 0.4})
axs[0].set_title("Porcentaje sobrevivientes (Masculino)")

# Donut femenino
axs[1].pie([surv_female, total_surv - surv_female],
           labels=["", ""],
           colors=[colors[1], "#DDDDDD"],
           autopct=lambda pct: f"{pct:.1f}%" if pct > 0 else "",
           startangle=90,
           wedgeprops={"width": 0.4})
axs[1].set_title("Porcentaje sobrevivientes (Femenino)")

st.pyplot(fig_donut)





st.write("""
## Muestra de datos cargados
""")
# Graficamos una tabla
st.table(df.head())
