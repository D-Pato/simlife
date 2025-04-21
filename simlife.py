# Simulador de Vida Real Financiera - MVP en Streamlit

import streamlit as st
import random

# Inicializar estado si no existe
if "juego_iniciado" not in st.session_state:
    st.session_state.juego_iniciado = False
    st.session_state.patrimonio = 0
    st.session_state.felicidad = 50
    st.session_state.estres = 30
    st.session_state.ahorros = random.randint(100000, 500000)
    st.session_state.ingresos_pasivos = 0
    st.session_state.avatar_creado = False

st.title("🧠 Simulador de Vida Real Financiera - DON’T PATO")

if not st.session_state.avatar_creado:
    st.subheader("Crea tu personaje")
    nombre = st.text_input("Nombre")
    edad = st.slider("Edad", 18, 30, 24)
    ciudad = st.selectbox("Ciudad", ["Antofagasta", "Santiago", "Concepción"])
    estilo_vida = st.radio("Estilo de vida", ["Austero", "Normal", "Me lo merezco"])

    if st.button("Iniciar Simulación"):
        st.session_state.nombre = nombre
        st.session_state.edad = edad
        st.session_state.ciudad = ciudad
        st.session_state.estilo_vida = estilo_vida
        st.session_state.avatar_creado = True
        st.session_state.juego_iniciado = True
        st.rerun()

if st.session_state.avatar_creado:
    st.success(f"¡Bienvenido/a {st.session_state.nombre}!")
    st.write(f"Edad: {st.session_state.edad}, Ciudad: {st.session_state.ciudad}, Estilo de vida: {st.session_state.estilo_vida}")

    if "decision1" not in st.session_state:
        st.header("🔀 Primera decisión")
        decision1 = st.radio("¿Qué quieres hacer ahora?", [
            "Estudiar una carrera",
            "Buscar trabajo",
            "Emprender con bajo capital"], key="d1")

        if st.button("Confirmar decisión 1"):
            if decision1 == "Estudiar una carrera":
                st.session_state.patrimonio -= 3000000
                st.session_state.estres += 10
                st.session_state.felicidad += 5
            elif decision1 == "Buscar trabajo":
                st.session_state.patrimonio += 1000000
                st.session_state.estres += 20
                st.session_state.felicidad -= 5
            elif decision1 == "Emprender con bajo capital":
                resultado = random.choice(["éxito", "fracaso"])
                if resultado == "éxito":
                    st.session_state.patrimonio += 2000000
                    st.session_state.felicidad += 10
                else:
                    st.session_state.patrimonio -= 500000
                    st.session_state.estres += 10

            evento = random.choice([
                ("Te enfermaste y tuviste que pagar $200.000 en salud", -200000, 10),
                ("Recibiste una herencia de $1.000.000", 1000000, -5),
                ("Perdiste dinero en una inversión arriesgada", -500000, 15)
            ])
            st.session_state.patrimonio += evento[1]
            st.session_state.estres += evento[2]
            st.session_state.evento1 = evento[0]
            st.session_state.decision1 = decision1
            st.rerun()

    elif "decision2" not in st.session_state:
        st.header("🔀 Primera decisión tomada")
        st.write(f"Decisión: {st.session_state.decision1}")
        st.warning(f"⚠️ Evento aleatorio: {st.session_state.evento1}")

        st.header("🔄 Segunda decisión")
        decision2 = st.radio("¿Cómo quieres manejar tus finanzas ahora?", [
            "Invertir en criptomonedas",
            "Ahorrar en un fondo seguro",
            "Gastar en un viaje para despejarte"], key="d2")

        if st.button("Confirmar decisión 2"):
            if decision2 == "Invertir en criptomonedas":
                resultado = random.choice(["ganancia", "pérdida"])
                if resultado == "ganancia":
                    st.session_state.patrimonio += 1000000
                    st.session_state.ingresos_pasivos += 50000
                    st.session_state.felicidad += 5
                else:
                    st.session_state.patrimonio -= 700000
                    st.session_state.estres += 10
            elif decision2 == "Ahorrar en un fondo seguro":
                st.session_state.patrimonio += 300000
                st.session_state.ingresos_pasivos += 20000
                st.session_state.felicidad += 3
            elif decision2 == "Gastar en un viaje para despejarte":
                st.session_state.patrimonio -= 500000
                st.session_state.felicidad += 15
                st.session_state.estres -= 10

            evento2 = random.choice([
                ("Te ascendieron en el trabajo y ganas más", 800000, -5),
                ("Se rompió tu celular y tuviste que comprar otro", -300000, 5),
                ("Tu arriendo subió inesperadamente", -400000, 10)
            ])
            st.session_state.patrimonio += evento2[1]
            st.session_state.estres += evento2[2]
            st.session_state.evento2 = evento2[0]
            st.session_state.decision2 = decision2
            st.rerun()

    else:
        st.header("🔄 Segunda decisión tomada")
        st.write(f"Decisión: {st.session_state.decision2}")
        st.warning(f"⚠️ Evento aleatorio: {st.session_state.evento2}")

        st.header("📊 Resultados Finales")
        st.metric("💰 Patrimonio", f"${st.session_state.patrimonio:,.0f}")
        st.metric("😊 Felicidad", f"{st.session_state.felicidad}%")
        st.metric("😰 Estrés", f"{st.session_state.estres}%")
        st.metric("🏦 Ahorros", f"${st.session_state.ahorros:,.0f}")
        st.metric("📈 Ingresos Pasivos", f"${st.session_state.ingresos_pasivos:,.0f}")

        st.info("🦆 Consejo de DON’T PATO: Las decisiones más sabias no siempre son las más populares. ¡Planea tu vida como si fuera un juego, pero juega en serio!")

        if st.button("🔁 Reiniciar simulador"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
