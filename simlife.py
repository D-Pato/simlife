# Simulador de Vida Real Financiera - MVP en Streamlit

import streamlit as st
import random

# ------------------------------
# Inicialización del personaje
# ------------------------------
st.title("🧠 Simulador de Vida Real Financiera - DON’T PATO")

st.subheader("Crea tu personaje")
nombre = st.text_input("Nombre")
edad = st.slider("Edad", 18, 30, 24)
ciudad = st.selectbox("Ciudad", ["Antofagasta", "Santiago", "Concepción"])
estilo_vida = st.radio("Estilo de vida", ["Austero", "Normal", "Me lo merezco"])

if st.button("Iniciar Simulación"):
    patrimonio = 0
    felicidad = 50
    estres = 30
    ahorros = random.randint(100000, 500000)
    ingresos_pasivos = 0

    st.success(f"¡Bienvenido/a {nombre}!")
    st.write(f"Edad: {edad}, Ciudad: {ciudad}, Estilo de vida: {estilo_vida}")

    # ------------------------------
    # Primera decisión
    # ------------------------------
    st.header("🔀 Primera decisión")
    decision1 = st.radio("¿Qué quieres hacer ahora?", [
        "Estudiar una carrera",
        "Buscar trabajo",
        "Emprender con bajo capital"
    ])

    if decision1 == "Estudiar una carrera":
        patrimonio -= 3000000
        estres += 10
        felicidad += 5
    elif decision1 == "Buscar trabajo":
        patrimonio += 1000000
        estres += 20
        felicidad -= 5
    elif decision1 == "Emprender con bajo capital":
        resultado = random.choice(["éxito", "fracaso"])
        if resultado == "éxito":
            patrimonio += 2000000
            felicidad += 10
        else:
            patrimonio -= 500000
            estres += 10

    # ------------------------------
    # Evento aleatorio 1
    # ------------------------------
    evento = random.choice([
        ("Te enfermaste y tuviste que pagar $200.000 en salud", -200000, 10),
        ("Recibiste una herencia de $1.000.000", 1000000, -5),
        ("Perdiste dinero en una inversión arriesgada", -500000, 15)
    ])
    st.warning(f"⚠️ Evento aleatorio: {evento[0]}")
    patrimonio += evento[1]
    estres += evento[2]

    # ------------------------------
    # Segunda decisión
    # ------------------------------
    st.header("🔄 Segunda decisión")
    decision2 = st.radio("¿Cómo quieres manejar tus finanzas ahora?", [
        "Invertir en criptomonedas",
        "Ahorrar en un fondo seguro",
        "Gastar en un viaje para despejarte"
    ])

    if decision2 == "Invertir en criptomonedas":
        resultado = random.choice(["ganancia", "pérdida"])
        if resultado == "ganancia":
            patrimonio += 1000000
            ingresos_pasivos += 50000
            felicidad += 5
        else:
            patrimonio -= 700000
            estres += 10
    elif decision2 == "Ahorrar en un fondo seguro":
        patrimonio += 300000
        ingresos_pasivos += 20000
        felicidad += 3
    elif decision2 == "Gastar en un viaje para despejarte":
        patrimonio -= 500000
        felicidad += 15
        estres -= 10

    # ------------------------------
    # Evento aleatorio 2
    # ------------------------------
    evento2 = random.choice([
        ("Te ascendieron en el trabajo y ganas más", 800000, -5),
        ("Se rompió tu celular y tuviste que comprar otro", -300000, 5),
        ("Tu arriendo subió inesperadamente", -400000, 10)
    ])
    st.warning(f"⚠️ Evento aleatorio: {evento2[0]}")
    patrimonio += evento2[1]
    estres += evento2[2]

    # ------------------------------
    # Resultados finales
    # ------------------------------
    st.header("📊 Resultados Finales")
    st.metric("💰 Patrimonio", f"${patrimonio:,.0f}")
    st.metric("😊 Felicidad", f"{felicidad}%")
    st.metric("😰 Estrés", f"{estres}%")
    st.metric("🏦 Ahorros", f"${ahorros:,.0f}")
    st.metric("📈 Ingresos Pasivos", f"${ingresos_pasivos:,.0f}")

    st.info("🦆 Consejo de DON’T PATO: Las decisiones más sabias no siempre son las más populares. ¡Planea tu vida como si fuera un juego, pero juega en serio!")
