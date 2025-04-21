# Simulador de Vida Real Financiera - Versión Avanzada Estilo Juego con Propiedades

import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt

# Inicializar estado si no existe
if "estado" not in st.session_state:
    st.session_state.estado = {
        "juego_iniciado": False,
        "avatar_creado": False,
        "patrimonio": 0,
        "felicidad": 50,
        "estres": 30,
        "ahorros": random.randint(100000, 500000),
        "ingresos_pasivos": 0,
        "edad": 18,
        "activos": [],
        "trayectoria": "",
        "situacion": "",
        "historial": []
    }

estado = st.session_state.estado

st.title("🧠 Simulador de Vida Real Financiera - DON’T PATO")

if not estado["avatar_creado"]:
    st.subheader("🧍‍♂️ Crea tu personaje")
    nombre = st.text_input("Nombre")
    ciudad = st.selectbox("Ciudad", ["Antofagasta", "Santiago", "Concepción"])
    estilo_vida = st.radio("Estilo de vida", ["Austero", "Normal", "Me lo merezco"], key="estilo_vida")
    trayectoria = st.radio("¿Qué camino quieres seguir?", [
        "Estudiante universitario",
        "Trabajador asalariado",
        "Emprendedor",
        "Freelancer"
    ], key="trayectoria")

    if st.button("Iniciar Simulación", key="iniciar_simulacion"):
        estado["nombre"] = nombre
        estado["ciudad"] = ciudad
        estado["estilo_vida"] = estilo_vida
        estado["trayectoria"] = trayectoria

        if trayectoria == "Estudiante universitario":
            estado["patrimonio"] = -1000000
            estado["situacion"] = "Estás estudiando y tu ingreso mensual es $200.000 CLP."
        elif trayectoria == "Trabajador asalariado":
            estado["patrimonio"] = 500000
            estado["situacion"] = "Tienes un empleo formal y ganas $500.000 CLP al mes."
        elif trayectoria == "Emprendedor":
            estado["patrimonio"] = 300000
            estado["situacion"] = "Estás comenzando un negocio propio, tus ingresos son variables."
        elif trayectoria == "Freelancer":
            estado["patrimonio"] = 400000
            estado["situacion"] = "Trabajas por cuenta propia y tus ingresos mensuales rondan los $450.000 CLP."

        estado["avatar_creado"] = True
        st.rerun()

if estado["avatar_creado"]:
    st.success(f"¡Bienvenido/a {estado['nombre']}!")
    st.write(f"🌆 Ciudad: {estado['ciudad']} | 🧭 Estilo de vida: {estado['estilo_vida']} | 🎯 Trayectoria: {estado['trayectoria']}")
    st.info(f"📌 {estado['situacion']}")

    # Mostrar propiedades disponibles
    st.header("🏠 Compra de Propiedades")
    propiedades = {
        "Departamento en Santiago": {"precio": 20000000, "ingreso": 250000},
        "Auto de trabajo": {"precio": 6000000, "ingreso": 0},
        "Mini Market": {"precio": 10000000, "ingreso": 400000}
    }

    for nombre_prop, datos in propiedades.items():
        if nombre_prop not in estado['activos']:
            if st.button(f"Comprar {nombre_prop} - ${datos['precio']:,}"):
                if estado["patrimonio"] >= datos['precio']:
                    estado["patrimonio"] -= datos['precio']
                    estado["ingresos_pasivos"] += datos['ingreso']
                    estado["activos"].append(nombre_prop)
                    st.success(f"¡Compraste {nombre_prop}!")
                else:
                    st.error("No tienes suficiente patrimonio para comprar esta propiedad.")

    # Guardar historial para gráficas
    estado["historial"].append({
        "Patrimonio": estado["patrimonio"],
        "Felicidad": estado["felicidad"],
        "Estrés": estado["estres"]
    })

    # Mostrar métricas
    st.header("📊 Estado Actual")
    st.metric("💰 Patrimonio", f"${estado['patrimonio']:,.0f}")
    st.metric("😊 Felicidad", f"{estado['felicidad']}%")
    st.metric("😰 Estrés", f"{estado['estres']}%")
    st.metric("🏦 Ahorros", f"${estado['ahorros']:,.0f}")
    st.metric("📈 Ingresos Pasivos", f"${estado['ingresos_pasivos']:,.0f}")

    st.write(f"🎒 Activos actuales: {', '.join(estado['activos']) if estado['activos'] else 'Ninguno'}")

    # Mostrar gráficas de evolución
    if len(estado["historial"]) > 1:
        df_hist = pd.DataFrame(estado["historial"])
        st.subheader("📈 Evolución del Simulador")
        fig, ax = plt.subplots()
        df_hist.plot(ax=ax)
        st.pyplot(fig)

    if st.button("🔁 Reiniciar simulador", key="reiniciar"):
        del st.session_state.estado
        st.rerun()
